import csv
import io
import math
from typing import AsyncIterator, Dict, Iterable, Iterator, List, Optional, Union

from apify_client import ApifyClientAsync
from apify_client.clients import DatasetClientAsync, DatasetCollectionClientAsync
from apify_shared.models import ListPage
from apify_shared.types import JSONSerializable
from apify_shared.utils import ignore_docs, json_dumps

from .._memory_storage import MemoryStorageClient
from .._memory_storage.resource_clients import DatasetClient, DatasetCollectionClient
from .._utils import _wrap_internal
from ..config import Configuration
from ..consts import MAX_PAYLOAD_SIZE_BYTES
from .base_storage import BaseStorage
from .key_value_store import KeyValueStore

# 0.01%
SAFETY_BUFFER_PERCENT = 0.01 / 100
EFFECTIVE_LIMIT_BYTES = MAX_PAYLOAD_SIZE_BYTES - math.ceil(MAX_PAYLOAD_SIZE_BYTES * SAFETY_BUFFER_PERCENT)


def _check_and_serialize(item: JSONSerializable, index: Optional[int] = None) -> str:
    """Accept a JSON serializable object as an input, validate its serializability and its serialized size against `EFFECTIVE_LIMIT_BYTES`."""
    s = ' ' if index is None else f' at index {index} '

    try:
        payload = json_dumps(item)
    except Exception as e:
        raise ValueError(f'Data item{s}is not serializable to JSON.') from e

    length_bytes = len(payload.encode('utf-8'))
    if length_bytes > EFFECTIVE_LIMIT_BYTES:
        raise ValueError(f'Data item{s}is too large (size: {length_bytes} bytes, limit: {EFFECTIVE_LIMIT_BYTES} bytes)')

    return payload


def _chunk_by_size(items: Iterable[str]) -> Iterator[str]:
    """Take an array of JSONs, produce iterator of chunked JSON arrays respecting `EFFECTIVE_LIMIT_BYTES`.

    Takes an array of JSONs (payloads) as input and produces an iterator of JSON strings
    where each string is a JSON array of payloads with a maximum size of `EFFECTIVE_LIMIT_BYTES` per one
    JSON array. Fits as many payloads as possible into a single JSON array and then moves
    on to the next, preserving item order.

    The function assumes that none of the items is larger than `EFFECTIVE_LIMIT_BYTES` and does not validate.
    """
    last_chunk_bytes = 2  # Add 2 bytes for [] wrapper.
    current_chunk = []

    for payload in items:
        length_bytes = len(payload.encode('utf-8'))

        if last_chunk_bytes + length_bytes <= EFFECTIVE_LIMIT_BYTES:
            current_chunk.append(payload)
            last_chunk_bytes += length_bytes + 1  # Add 1 byte for ',' separator.
        else:
            yield f'[{",".join(current_chunk)}]'
            current_chunk = [payload]
            last_chunk_bytes = length_bytes + 2  # Add 2 bytes for [] wrapper.

    yield f'[{",".join(current_chunk)}]'


class Dataset(BaseStorage):
    """The `Dataset` class represents a store for structured data where each object stored has the same attributes.

    You can imagine it as a table, where each object is a row and its attributes are columns.
    Dataset is an append-only storage - you can only add new records to it but you cannot modify or remove existing records.
    Typically it is used to store crawling results.

    Do not instantiate this class directly, use the `Actor.open_dataset()` function instead.

    `Dataset` stores its data either on local disk or in the Apify cloud,
    depending on whether the `APIFY_LOCAL_STORAGE_DIR` or `APIFY_TOKEN` environment variables are set.

    If the `APIFY_LOCAL_STORAGE_DIR` environment variable is set, the data is stored in
    the local directory in the following files:
    ```
    {APIFY_LOCAL_STORAGE_DIR}/datasets/{DATASET_ID}/{INDEX}.json
    ```
    Note that `{DATASET_ID}` is the name or ID of the dataset. The default dataset has ID: `default`,
    unless you override it by setting the `APIFY_DEFAULT_DATASET_ID` environment variable.
    Each dataset item is stored as a separate JSON file, where `{INDEX}` is a zero-based index of the item in the dataset.

    If the `APIFY_TOKEN` environment variable is set but `APIFY_LOCAL_STORAGE_DIR` is not, the data is stored in the
    [Apify Dataset](https://docs.apify.com/storage/dataset) cloud storage.
    """

    _id: str
    _name: Optional[str]
    _dataset_client: Union[DatasetClientAsync, DatasetClient]

    @ignore_docs
    def __init__(self, id: str, name: Optional[str], client: Union[ApifyClientAsync, MemoryStorageClient], config: Configuration) -> None:
        """Create a `Dataset` instance.

        Do not use the constructor directly, use the `Actor.open_dataset()` function instead.

        Args:
            id (str): ID of the dataset.
            name (str, optional): Name of the dataset.
            client (ApifyClientAsync or MemoryStorageClient): The storage client which should be used.
            config (Configuration): The configuration which should be used.
        """
        super().__init__(id=id, name=name, client=client, config=config)

        self.get_data = _wrap_internal(self._get_data_internal, self.get_data)  # type: ignore
        self.push_data = _wrap_internal(self._push_data_internal, self.push_data)  # type: ignore
        self.export_to_json = _wrap_internal(self._export_to_json_internal, self.export_to_json)  # type: ignore
        self.export_to_csv = _wrap_internal(self._export_to_csv_internal, self.export_to_csv)  # type: ignore

        self._dataset_client = client.dataset(self._id)

    @classmethod
    def _get_human_friendly_label(cls) -> str:
        return 'Dataset'

    @classmethod
    def _get_default_id(cls, config: Configuration) -> str:
        return config.default_dataset_id

    @classmethod
    def _get_single_storage_client(cls, id: str, client: Union[ApifyClientAsync, MemoryStorageClient]) -> Union[DatasetClientAsync, DatasetClient]:
        return client.dataset(id)

    @classmethod
    def _get_storage_collection_client(
        cls,
        client: Union[ApifyClientAsync, MemoryStorageClient],
    ) -> Union[DatasetCollectionClientAsync, DatasetCollectionClient]:
        return client.datasets()

    @classmethod
    async def push_data(cls, data: JSONSerializable) -> None:
        """Store an object or an array of objects to the dataset.

        The size of the data is limited by the receiving API and therefore `push_data()` will only
        allow objects whose JSON representation is smaller than 9MB. When an array is passed,
        none of the included objects may be larger than 9MB, but the array itself may be of any size.

        Args:
            data (JSONSerializable): dict or array of dicts containing data to be stored in the default dataset.
                The JSON representation of each item must be smaller than 9MB.
        """
        dataset = await cls.open()
        return await dataset.push_data(data)

    async def _push_data_internal(self, data: JSONSerializable) -> None:
        # Handle singular items
        if not isinstance(data, list):
            payload = _check_and_serialize(data)
            return await self._dataset_client.push_items(payload)

        # Handle lists
        payloads_generator = (_check_and_serialize(item, index) for index, item in enumerate(data))

        # Invoke client in series to preserve the order of data
        for chunk in _chunk_by_size(payloads_generator):
            await self._dataset_client.push_items(chunk)

    @classmethod
    async def get_data(
        cls,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        clean: Optional[bool] = None,
        desc: Optional[bool] = None,
        fields: Optional[List[str]] = None,
        omit: Optional[List[str]] = None,
        unwind: Optional[str] = None,
        skip_empty: Optional[bool] = None,
        skip_hidden: Optional[bool] = None,
        flatten: Optional[List[str]] = None,
        view: Optional[str] = None,
    ) -> ListPage:
        """Get items from the dataset.

        Args:
            offset (int, optional): Number of items that should be skipped at the start. The default value is 0
            limit (int, optional): Maximum number of items to return. By default there is no limit.
            desc (bool, optional): By default, results are returned in the same order as they were stored.
                To reverse the order, set this parameter to True.
            clean (bool, optional): If True, returns only non-empty items and skips hidden fields (i.e. fields starting with the # character).
                The clean parameter is just a shortcut for skip_hidden=True and skip_empty=True parameters.
                Note that since some objects might be skipped from the output, that the result might contain less items than the limit value.
            fields (list of str, optional): A list of fields which should be picked from the items,
                only these fields will remain in the resulting record objects.
                Note that the fields in the outputted items are sorted the same way as they are specified in the fields parameter.
                You can use this feature to effectively fix the output format.
            omit (list of str, optional): A list of fields which should be omitted from the items.
            unwind (str, optional): Name of a field which should be unwound.
                If the field is an array then every element of the array will become a separate record and merged with parent object.
                If the unwound field is an object then it is merged with the parent object.
                If the unwound field is missing or its value is neither an array nor an object and therefore cannot be merged with a parent object,
                then the item gets preserved as it is. Note that the unwound items ignore the desc parameter.
            skip_empty (bool, optional): If True, then empty items are skipped from the output.
                Note that if used, the results might contain less items than the limit value.
            skip_hidden (bool, optional): If True, then hidden fields are skipped from the output, i.e. fields starting with the # character.
            flatten (list of str, optional): A list of fields that should be flattened
            view (str, optional): Name of the dataset view to be used

        Returns:
            ListPage: A page of the list of dataset items according to the specified filters.
        """
        dataset = await cls.open()
        return await dataset.get_data(
            offset=offset,
            limit=limit,
            desc=desc,
            clean=clean,
            fields=fields,
            omit=omit,
            unwind=unwind,
            skip_empty=skip_empty,
            skip_hidden=skip_hidden,
            flatten=flatten,
            view=view,
        )

    async def _get_data_internal(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        clean: Optional[bool] = None,
        desc: Optional[bool] = None,
        fields: Optional[List[str]] = None,
        omit: Optional[List[str]] = None,
        unwind: Optional[str] = None,
        skip_empty: Optional[bool] = None,
        skip_hidden: Optional[bool] = None,
        flatten: Optional[List[str]] = None,
        view: Optional[str] = None,
    ) -> ListPage:
        # try {
        #     return await this.client.listItems(options);
        # } catch (e) {
        #     const error = e as Error;
        #     if (error.message.includes('Cannot create a string longer than')) {
        #         throw new Error('dataset.getData(): The response is too large for parsing. You can fix this by lowering the "limit" option.');
        #     }
        #     throw e;
        # }
        # TODO: Simulate the above error in Python and handle accordingly...
        return await self._dataset_client.list_items(
            offset=offset,
            limit=limit,
            desc=desc,
            clean=clean,
            fields=fields,
            omit=omit,
            unwind=unwind,
            skip_empty=skip_empty,
            skip_hidden=skip_hidden,
            flatten=flatten,
            view=view,
        )

    async def export_to(
        self,
        key: str,
        *,
        to_key_value_store_id: Optional[str] = None,
        to_key_value_store_name: Optional[str] = None,
        content_type: Optional[str] = None,
    ) -> None:
        """Save the entirety of the dataset's contents into one file within a key-value store.

        Args:
            key (str): The key to save the data under.
            to_key_value_store_id (str, optional): The id of the key-value store in which the result will be saved.
            to_key_value_store_name (str, optional): The name of the key-value store in which the result will be saved.
                You must specify only one of `to_key_value_store_id` and `to_key_value_store_name` arguments.
                If you omit both, it uses the default key-value store.
            content_type (str, optional): Either 'text/csv' or 'application/json'. Defaults to JSON.
        """
        key_value_store = await KeyValueStore.open(id=to_key_value_store_id, name=to_key_value_store_name)
        items: List[Dict] = []
        limit = 1000
        offset = 0
        while True:
            list_items = await self._dataset_client.list_items(limit=limit, offset=offset)
            items.extend(list_items.items)
            if list_items.total <= offset + list_items.count:
                break
            offset += list_items.count

        if len(items) == 0:
            raise ValueError('Cannot export an empty dataset')

        if content_type == 'text/csv':
            output = io.StringIO()
            writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL)
            writer.writerows([items[0].keys(), *[item.values() for item in items]])
            value = output.getvalue()
            return await key_value_store.set_value(key, value, content_type)

        if content_type == 'application/json':
            return await key_value_store.set_value(key, items)

        raise ValueError(f'Unsupported content type: {content_type}')

    @classmethod
    async def export_to_json(
        cls,
        key: str,
        *,
        from_dataset_id: Optional[str] = None,
        from_dataset_name: Optional[str] = None,
        to_key_value_store_id: Optional[str] = None,
        to_key_value_store_name: Optional[str] = None,
    ) -> None:
        """Save the entirety of the dataset's contents into one JSON file within a key-value store.

        Args:
            key (str): The key to save the data under.
            from_dataset_id (str, optional): The ID of the dataset in case of calling the class method. Uses default dataset if omitted.
            from_dataset_name (str, optional): The name of the dataset in case of calling the class method. Uses default dataset if omitted.
                You must specify only one of `from_dataset_id` and `from_dataset_name` arguments.
                If you omit both, it uses the default dataset.
            to_key_value_store_id (str, optional): The id of the key-value store in which the result will be saved.
            to_key_value_store_name (str, optional): The name of the key-value store in which the result will be saved.
                You must specify only one of `to_key_value_store_id` and `to_key_value_store_name` arguments.
                If you omit both, it uses the default key-value store.
        """
        dataset = await cls.open(id=from_dataset_id, name=from_dataset_name)
        await dataset.export_to_json(key, to_key_value_store_id=to_key_value_store_id, to_key_value_store_name=to_key_value_store_name)

    async def _export_to_json_internal(
        self,
        key: str,
        *,
        from_dataset_id: Optional[str] = None,  # noqa: U100
        from_dataset_name: Optional[str] = None,  # noqa: U100
        to_key_value_store_id: Optional[str] = None,
        to_key_value_store_name: Optional[str] = None,
    ) -> None:
        await self.export_to(
            key,
            to_key_value_store_id=to_key_value_store_id,
            to_key_value_store_name=to_key_value_store_name,
            content_type='application/json',
        )

    @classmethod
    async def export_to_csv(
        cls,
        key: str,
        *,
        from_dataset_id: Optional[str] = None,
        from_dataset_name: Optional[str] = None,
        to_key_value_store_id: Optional[str] = None,
        to_key_value_store_name: Optional[str] = None,
    ) -> None:
        """Save the entirety of the dataset's contents into one CSV file within a key-value store.

        Args:
            key (str): The key to save the data under.
            from_dataset_id (str, optional): The ID of the dataset in case of calling the class method. Uses default dataset if omitted.
            from_dataset_name (str, optional): The name of the dataset in case of calling the class method. Uses default dataset if omitted.
                You must specify only one of `from_dataset_id` and `from_dataset_name` arguments.
                If you omit both, it uses the default dataset.
            to_key_value_store_id (str, optional): The id of the key-value store in which the result will be saved.
            to_key_value_store_name (str, optional): The name of the key-value store in which the result will be saved.
                You must specify only one of `to_key_value_store_id` and `to_key_value_store_name` arguments.
                If you omit both, it uses the default key-value store.
        """
        dataset = await cls.open(id=from_dataset_id, name=from_dataset_name)
        await dataset.export_to_csv(key, to_key_value_store_id=to_key_value_store_id, to_key_value_store_name=to_key_value_store_name)

    async def _export_to_csv_internal(
        self,
        key: str,
        *,
        from_dataset_id: Optional[str] = None,  # noqa: U100
        from_dataset_name: Optional[str] = None,  # noqa: U100
        to_key_value_store_id: Optional[str] = None,
        to_key_value_store_name: Optional[str] = None,
    ) -> None:
        await self.export_to(
            key,
            to_key_value_store_id=to_key_value_store_id,
            to_key_value_store_name=to_key_value_store_name,
            content_type='text/csv',
        )

    async def get_info(self) -> Optional[Dict]:
        """Get an object containing general information about the dataset.

        Returns:
            dict: Object returned by calling the GET dataset API endpoint.
        """
        return await self._dataset_client.get()

    def iterate_items(
        self,
        *,
        offset: int = 0,
        limit: Optional[int] = None,
        clean: Optional[bool] = None,
        desc: Optional[bool] = None,
        fields: Optional[List[str]] = None,
        omit: Optional[List[str]] = None,
        unwind: Optional[str] = None,
        skip_empty: Optional[bool] = None,
        skip_hidden: Optional[bool] = None,
    ) -> AsyncIterator[Dict]:
        """Iterate over the items in the dataset.

        Args:
            offset (int, optional): Number of items that should be skipped at the start. The default value is 0
            limit (int, optional): Maximum number of items to return. By default there is no limit.
            desc (bool, optional): By default, results are returned in the same order as they were stored.
                To reverse the order, set this parameter to True.
            clean (bool, optional): If True, returns only non-empty items and skips hidden fields (i.e. fields starting with the # character).
                The clean parameter is just a shortcut for skip_hidden=True and skip_empty=True parameters.
                Note that since some objects might be skipped from the output, that the result might contain less items than the limit value.
            fields (list of str, optional): A list of fields which should be picked from the items,
                only these fields will remain in the resulting record objects.
                Note that the fields in the outputted items are sorted the same way as they are specified in the fields parameter.
                You can use this feature to effectively fix the output format.
            omit (list of str, optional): A list of fields which should be omitted from the items.
            unwind (str, optional): Name of a field which should be unwound.
                If the field is an array then every element of the array will become a separate record and merged with parent object.
                If the unwound field is an object then it is merged with the parent object.
                If the unwound field is missing or its value is neither an array nor an object and therefore cannot be merged with a parent object,
                then the item gets preserved as it is. Note that the unwound items ignore the desc parameter.
            skip_empty (bool, optional): If True, then empty items are skipped from the output.
                Note that if used, the results might contain less items than the limit value.
            skip_hidden (bool, optional): If True, then hidden fields are skipped from the output, i.e. fields starting with the # character.

        Yields:
            dict: An item from the dataset
        """
        return self._dataset_client.iterate_items(
            offset=offset,
            limit=limit,
            clean=clean,
            desc=desc,
            fields=fields,
            omit=omit,
            unwind=unwind,
            skip_empty=skip_empty,
            skip_hidden=skip_hidden,
        )

    async def drop(self) -> None:
        """Remove the dataset either from the Apify cloud storage or from the local directory."""
        await self._dataset_client.delete()
        self._remove_from_cache()

    @classmethod
    async def open(
        cls,
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
        force_cloud: bool = False,
        config: Optional[Configuration] = None,
    ) -> 'Dataset':
        """Open a dataset.

        Datasets are used to store structured data where each object stored has the same attributes,
        such as online store products or real estate offers.
        The actual data is stored either on the local filesystem or in the Apify cloud.

        Args:
            id (str, optional): ID of the dataset to be opened.
                If neither `id` nor `name` are provided, the method returns the default dataset associated with the actor run.
                If the dataset with the given ID does not exist, it raises an error.
            name (str, optional): Name of the dataset to be opened.
                If neither `id` nor `name` are provided, the method returns the default dataset associated with the actor run.
                If the dataset with the given name does not exist, it is created.
            force_cloud (bool, optional): If set to True, it will open a dataset on the Apify Platform even when running the actor locally.
                Defaults to False.
            config (Configuration, optional): A `Configuration` instance, uses global configuration if omitted.

        Returns:
            Dataset: An instance of the `Dataset` class for the given ID or name.
        """
        return await super().open(id=id, name=name, force_cloud=force_cloud, config=config)

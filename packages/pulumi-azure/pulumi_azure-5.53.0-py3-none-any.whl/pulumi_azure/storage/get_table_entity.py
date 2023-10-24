# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetTableEntityResult',
    'AwaitableGetTableEntityResult',
    'get_table_entity',
    'get_table_entity_output',
]

@pulumi.output_type
class GetTableEntityResult:
    """
    A collection of values returned by getTableEntity.
    """
    def __init__(__self__, entity=None, id=None, partition_key=None, row_key=None, storage_account_name=None, table_name=None):
        if entity and not isinstance(entity, dict):
            raise TypeError("Expected argument 'entity' to be a dict")
        pulumi.set(__self__, "entity", entity)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if partition_key and not isinstance(partition_key, str):
            raise TypeError("Expected argument 'partition_key' to be a str")
        pulumi.set(__self__, "partition_key", partition_key)
        if row_key and not isinstance(row_key, str):
            raise TypeError("Expected argument 'row_key' to be a str")
        pulumi.set(__self__, "row_key", row_key)
        if storage_account_name and not isinstance(storage_account_name, str):
            raise TypeError("Expected argument 'storage_account_name' to be a str")
        pulumi.set(__self__, "storage_account_name", storage_account_name)
        if table_name and not isinstance(table_name, str):
            raise TypeError("Expected argument 'table_name' to be a str")
        pulumi.set(__self__, "table_name", table_name)

    @property
    @pulumi.getter
    def entity(self) -> Mapping[str, str]:
        """
        A map of key/value pairs that describe the entity to be stored in the storage table.
        """
        return pulumi.get(self, "entity")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> str:
        return pulumi.get(self, "partition_key")

    @property
    @pulumi.getter(name="rowKey")
    def row_key(self) -> str:
        return pulumi.get(self, "row_key")

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> str:
        return pulumi.get(self, "storage_account_name")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> str:
        return pulumi.get(self, "table_name")


class AwaitableGetTableEntityResult(GetTableEntityResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTableEntityResult(
            entity=self.entity,
            id=self.id,
            partition_key=self.partition_key,
            row_key=self.row_key,
            storage_account_name=self.storage_account_name,
            table_name=self.table_name)


def get_table_entity(partition_key: Optional[str] = None,
                     row_key: Optional[str] = None,
                     storage_account_name: Optional[str] = None,
                     table_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTableEntityResult:
    """
    Use this data source to access information about an existing Storage Table Entity.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.storage.get_table_entity(partition_key="example-partition-key",
        row_key="example-row-key",
        storage_account_name="example-storage-account-name",
        table_name="example-table-name")
    ```


    :param str partition_key: The key for the partition where the entity will be retrieved.
    :param str row_key: The key for the row where the entity will be retrieved.
    :param str storage_account_name: The name of the Storage Account where the Table exists.
    :param str table_name: The name of the Table.
    """
    __args__ = dict()
    __args__['partitionKey'] = partition_key
    __args__['rowKey'] = row_key
    __args__['storageAccountName'] = storage_account_name
    __args__['tableName'] = table_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:storage/getTableEntity:getTableEntity', __args__, opts=opts, typ=GetTableEntityResult).value

    return AwaitableGetTableEntityResult(
        entity=pulumi.get(__ret__, 'entity'),
        id=pulumi.get(__ret__, 'id'),
        partition_key=pulumi.get(__ret__, 'partition_key'),
        row_key=pulumi.get(__ret__, 'row_key'),
        storage_account_name=pulumi.get(__ret__, 'storage_account_name'),
        table_name=pulumi.get(__ret__, 'table_name'))


@_utilities.lift_output_func(get_table_entity)
def get_table_entity_output(partition_key: Optional[pulumi.Input[str]] = None,
                            row_key: Optional[pulumi.Input[str]] = None,
                            storage_account_name: Optional[pulumi.Input[str]] = None,
                            table_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTableEntityResult]:
    """
    Use this data source to access information about an existing Storage Table Entity.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.storage.get_table_entity(partition_key="example-partition-key",
        row_key="example-row-key",
        storage_account_name="example-storage-account-name",
        table_name="example-table-name")
    ```


    :param str partition_key: The key for the partition where the entity will be retrieved.
    :param str row_key: The key for the row where the entity will be retrieved.
    :param str storage_account_name: The name of the Storage Account where the Table exists.
    :param str table_name: The name of the Table.
    """
    ...

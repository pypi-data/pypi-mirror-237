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
    'GetDatabaseResult',
    'AwaitableGetDatabaseResult',
    'get_database',
    'get_database_output',
]

@pulumi.output_type
class GetDatabaseResult:
    """
    A collection of values returned by getDatabase.
    """
    def __init__(__self__, cluster_name=None, hot_cache_period=None, id=None, location=None, name=None, resource_group_name=None, size=None, soft_delete_period=None):
        if cluster_name and not isinstance(cluster_name, str):
            raise TypeError("Expected argument 'cluster_name' to be a str")
        pulumi.set(__self__, "cluster_name", cluster_name)
        if hot_cache_period and not isinstance(hot_cache_period, str):
            raise TypeError("Expected argument 'hot_cache_period' to be a str")
        pulumi.set(__self__, "hot_cache_period", hot_cache_period)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if size and not isinstance(size, float):
            raise TypeError("Expected argument 'size' to be a float")
        pulumi.set(__self__, "size", size)
        if soft_delete_period and not isinstance(soft_delete_period, str):
            raise TypeError("Expected argument 'soft_delete_period' to be a str")
        pulumi.set(__self__, "soft_delete_period", soft_delete_period)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> str:
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="hotCachePeriod")
    def hot_cache_period(self) -> str:
        """
        The time the data that should be kept in cache for fast queries as ISO 8601 timespan.
        """
        return pulumi.get(self, "hot_cache_period")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The Azure Region in which the managed Kusto Database exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def size(self) -> float:
        """
        The size of the database in bytes.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="softDeletePeriod")
    def soft_delete_period(self) -> str:
        """
        The time the data should be kept before it stops being accessible to queries as ISO 8601 timespan.
        """
        return pulumi.get(self, "soft_delete_period")


class AwaitableGetDatabaseResult(GetDatabaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseResult(
            cluster_name=self.cluster_name,
            hot_cache_period=self.hot_cache_period,
            id=self.id,
            location=self.location,
            name=self.name,
            resource_group_name=self.resource_group_name,
            size=self.size,
            soft_delete_period=self.soft_delete_period)


def get_database(cluster_name: Optional[str] = None,
                 name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseResult:
    """
    Use this data source to access information about an existing Kusto Database

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.kusto.get_database(cluster_name="test_cluster",
        name="my-kusto-database",
        resource_group_name="test_resource_group")
    ```


    :param str cluster_name: The name of the Kusto Cluster this database is added to.
    :param str name: The name of the Kusto Database.
    :param str resource_group_name: The Resource Group where the Kusto Database exists.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:kusto/getDatabase:getDatabase', __args__, opts=opts, typ=GetDatabaseResult).value

    return AwaitableGetDatabaseResult(
        cluster_name=pulumi.get(__ret__, 'cluster_name'),
        hot_cache_period=pulumi.get(__ret__, 'hot_cache_period'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        size=pulumi.get(__ret__, 'size'),
        soft_delete_period=pulumi.get(__ret__, 'soft_delete_period'))


@_utilities.lift_output_func(get_database)
def get_database_output(cluster_name: Optional[pulumi.Input[str]] = None,
                        name: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseResult]:
    """
    Use this data source to access information about an existing Kusto Database

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.kusto.get_database(cluster_name="test_cluster",
        name="my-kusto-database",
        resource_group_name="test_resource_group")
    ```


    :param str cluster_name: The name of the Kusto Cluster this database is added to.
    :param str name: The name of the Kusto Database.
    :param str resource_group_name: The Resource Group where the Kusto Database exists.
    """
    ...

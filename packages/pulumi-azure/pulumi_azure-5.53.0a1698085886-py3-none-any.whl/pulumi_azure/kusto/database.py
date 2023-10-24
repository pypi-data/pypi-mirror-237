# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DatabaseArgs', 'Database']

@pulumi.input_type
class DatabaseArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 hot_cache_period: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 soft_delete_period: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Database resource.
        :param pulumi.Input[str] cluster_name: Specifies the name of the Kusto Cluster this database will be added to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] hot_cache_period: The time the data that should be kept in cache for fast queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        :param pulumi.Input[str] location: The location where the Kusto Database should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Kusto Database to create. Changing this forces a new resource to be created.
        :param pulumi.Input[str] soft_delete_period: The time the data should be kept before it stops being accessible to queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        """
        DatabaseArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cluster_name=cluster_name,
            resource_group_name=resource_group_name,
            hot_cache_period=hot_cache_period,
            location=location,
            name=name,
            soft_delete_period=soft_delete_period,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cluster_name: pulumi.Input[str],
             resource_group_name: pulumi.Input[str],
             hot_cache_period: Optional[pulumi.Input[str]] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             soft_delete_period: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'clusterName' in kwargs:
            cluster_name = kwargs['clusterName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'hotCachePeriod' in kwargs:
            hot_cache_period = kwargs['hotCachePeriod']
        if 'softDeletePeriod' in kwargs:
            soft_delete_period = kwargs['softDeletePeriod']

        _setter("cluster_name", cluster_name)
        _setter("resource_group_name", resource_group_name)
        if hot_cache_period is not None:
            _setter("hot_cache_period", hot_cache_period)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if soft_delete_period is not None:
            _setter("soft_delete_period", soft_delete_period)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        Specifies the name of the Kusto Cluster this database will be added to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="hotCachePeriod")
    def hot_cache_period(self) -> Optional[pulumi.Input[str]]:
        """
        The time the data that should be kept in cache for fast queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        """
        return pulumi.get(self, "hot_cache_period")

    @hot_cache_period.setter
    def hot_cache_period(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hot_cache_period", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location where the Kusto Database should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Kusto Database to create. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="softDeletePeriod")
    def soft_delete_period(self) -> Optional[pulumi.Input[str]]:
        """
        The time the data should be kept before it stops being accessible to queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        """
        return pulumi.get(self, "soft_delete_period")

    @soft_delete_period.setter
    def soft_delete_period(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "soft_delete_period", value)


@pulumi.input_type
class _DatabaseState:
    def __init__(__self__, *,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 hot_cache_period: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[float]] = None,
                 soft_delete_period: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Database resources.
        :param pulumi.Input[str] cluster_name: Specifies the name of the Kusto Cluster this database will be added to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] hot_cache_period: The time the data that should be kept in cache for fast queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        :param pulumi.Input[str] location: The location where the Kusto Database should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Kusto Database to create. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[float] size: The size of the database in bytes.
        :param pulumi.Input[str] soft_delete_period: The time the data should be kept before it stops being accessible to queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        """
        _DatabaseState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cluster_name=cluster_name,
            hot_cache_period=hot_cache_period,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            size=size,
            soft_delete_period=soft_delete_period,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cluster_name: Optional[pulumi.Input[str]] = None,
             hot_cache_period: Optional[pulumi.Input[str]] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             size: Optional[pulumi.Input[float]] = None,
             soft_delete_period: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'clusterName' in kwargs:
            cluster_name = kwargs['clusterName']
        if 'hotCachePeriod' in kwargs:
            hot_cache_period = kwargs['hotCachePeriod']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'softDeletePeriod' in kwargs:
            soft_delete_period = kwargs['softDeletePeriod']

        if cluster_name is not None:
            _setter("cluster_name", cluster_name)
        if hot_cache_period is not None:
            _setter("hot_cache_period", hot_cache_period)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if size is not None:
            _setter("size", size)
        if soft_delete_period is not None:
            _setter("soft_delete_period", soft_delete_period)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Kusto Cluster this database will be added to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="hotCachePeriod")
    def hot_cache_period(self) -> Optional[pulumi.Input[str]]:
        """
        The time the data that should be kept in cache for fast queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        """
        return pulumi.get(self, "hot_cache_period")

    @hot_cache_period.setter
    def hot_cache_period(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hot_cache_period", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location where the Kusto Database should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Kusto Database to create. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[float]]:
        """
        The size of the database in bytes.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="softDeletePeriod")
    def soft_delete_period(self) -> Optional[pulumi.Input[str]]:
        """
        The time the data should be kept before it stops being accessible to queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        """
        return pulumi.get(self, "soft_delete_period")

    @soft_delete_period.setter
    def soft_delete_period(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "soft_delete_period", value)


class Database(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 hot_cache_period: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 soft_delete_period: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Kusto (also known as Azure Data Explorer) Database

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example", location="West Europe")
        cluster = azure.kusto.Cluster("cluster",
            location=example.location,
            resource_group_name=example.name,
            sku=azure.kusto.ClusterSkuArgs(
                name="Standard_D13_v2",
                capacity=2,
            ))
        database = azure.kusto.Database("database",
            resource_group_name=example.name,
            location=example.location,
            cluster_name=cluster.name,
            hot_cache_period="P7D",
            soft_delete_period="P31D")
        ```

        ## Import

        Kusto Clusters can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:kusto/database:Database example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Kusto/clusters/cluster1/databases/database1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: Specifies the name of the Kusto Cluster this database will be added to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] hot_cache_period: The time the data that should be kept in cache for fast queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        :param pulumi.Input[str] location: The location where the Kusto Database should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Kusto Database to create. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] soft_delete_period: The time the data should be kept before it stops being accessible to queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatabaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Kusto (also known as Azure Data Explorer) Database

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example", location="West Europe")
        cluster = azure.kusto.Cluster("cluster",
            location=example.location,
            resource_group_name=example.name,
            sku=azure.kusto.ClusterSkuArgs(
                name="Standard_D13_v2",
                capacity=2,
            ))
        database = azure.kusto.Database("database",
            resource_group_name=example.name,
            location=example.location,
            cluster_name=cluster.name,
            hot_cache_period="P7D",
            soft_delete_period="P31D")
        ```

        ## Import

        Kusto Clusters can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:kusto/database:Database example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Kusto/clusters/cluster1/databases/database1
        ```

        :param str resource_name: The name of the resource.
        :param DatabaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatabaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DatabaseArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 hot_cache_period: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 soft_delete_period: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatabaseArgs.__new__(DatabaseArgs)

            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["hot_cache_period"] = hot_cache_period
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["soft_delete_period"] = soft_delete_period
            __props__.__dict__["size"] = None
        super(Database, __self__).__init__(
            'azure:kusto/database:Database',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_name: Optional[pulumi.Input[str]] = None,
            hot_cache_period: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[float]] = None,
            soft_delete_period: Optional[pulumi.Input[str]] = None) -> 'Database':
        """
        Get an existing Database resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: Specifies the name of the Kusto Cluster this database will be added to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] hot_cache_period: The time the data that should be kept in cache for fast queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        :param pulumi.Input[str] location: The location where the Kusto Database should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Kusto Database to create. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[float] size: The size of the database in bytes.
        :param pulumi.Input[str] soft_delete_period: The time the data should be kept before it stops being accessible to queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DatabaseState.__new__(_DatabaseState)

        __props__.__dict__["cluster_name"] = cluster_name
        __props__.__dict__["hot_cache_period"] = hot_cache_period
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["size"] = size
        __props__.__dict__["soft_delete_period"] = soft_delete_period
        return Database(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Kusto Cluster this database will be added to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="hotCachePeriod")
    def hot_cache_period(self) -> pulumi.Output[Optional[str]]:
        """
        The time the data that should be kept in cache for fast queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        """
        return pulumi.get(self, "hot_cache_period")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location where the Kusto Database should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Kusto Database to create. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[float]:
        """
        The size of the database in bytes.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="softDeletePeriod")
    def soft_delete_period(self) -> pulumi.Output[Optional[str]]:
        """
        The time the data should be kept before it stops being accessible to queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        """
        return pulumi.get(self, "soft_delete_period")


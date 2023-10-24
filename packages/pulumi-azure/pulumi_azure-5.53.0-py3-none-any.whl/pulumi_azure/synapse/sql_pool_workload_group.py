# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SqlPoolWorkloadGroupArgs', 'SqlPoolWorkloadGroup']

@pulumi.input_type
class SqlPoolWorkloadGroupArgs:
    def __init__(__self__, *,
                 max_resource_percent: pulumi.Input[int],
                 min_resource_percent: pulumi.Input[int],
                 sql_pool_id: pulumi.Input[str],
                 importance: Optional[pulumi.Input[str]] = None,
                 max_resource_percent_per_request: Optional[pulumi.Input[float]] = None,
                 min_resource_percent_per_request: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 query_execution_timeout_in_seconds: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a SqlPoolWorkloadGroup resource.
        :param pulumi.Input[int] max_resource_percent: The workload group cap percentage resource.
        :param pulumi.Input[int] min_resource_percent: The workload group minimum percentage resource.
        :param pulumi.Input[str] sql_pool_id: The ID of the Synapse SQL Pool. Changing this forces a new Synapse SQL Pool Workload Group to be created.
        :param pulumi.Input[str] importance: The workload group importance level. Defaults to `normal`.
        :param pulumi.Input[float] max_resource_percent_per_request: The workload group request maximum grant percentage. Defaults to `3`.
        :param pulumi.Input[float] min_resource_percent_per_request: The workload group request minimum grant percentage.
        :param pulumi.Input[str] name: The name which should be used for this Synapse SQL Pool Workload Group. Changing this forces a new Synapse SQL Pool Workload Group to be created.
        :param pulumi.Input[int] query_execution_timeout_in_seconds: The workload group query execution timeout.
        """
        SqlPoolWorkloadGroupArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            max_resource_percent=max_resource_percent,
            min_resource_percent=min_resource_percent,
            sql_pool_id=sql_pool_id,
            importance=importance,
            max_resource_percent_per_request=max_resource_percent_per_request,
            min_resource_percent_per_request=min_resource_percent_per_request,
            name=name,
            query_execution_timeout_in_seconds=query_execution_timeout_in_seconds,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             max_resource_percent: pulumi.Input[int],
             min_resource_percent: pulumi.Input[int],
             sql_pool_id: pulumi.Input[str],
             importance: Optional[pulumi.Input[str]] = None,
             max_resource_percent_per_request: Optional[pulumi.Input[float]] = None,
             min_resource_percent_per_request: Optional[pulumi.Input[float]] = None,
             name: Optional[pulumi.Input[str]] = None,
             query_execution_timeout_in_seconds: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'maxResourcePercent' in kwargs:
            max_resource_percent = kwargs['maxResourcePercent']
        if 'minResourcePercent' in kwargs:
            min_resource_percent = kwargs['minResourcePercent']
        if 'sqlPoolId' in kwargs:
            sql_pool_id = kwargs['sqlPoolId']
        if 'maxResourcePercentPerRequest' in kwargs:
            max_resource_percent_per_request = kwargs['maxResourcePercentPerRequest']
        if 'minResourcePercentPerRequest' in kwargs:
            min_resource_percent_per_request = kwargs['minResourcePercentPerRequest']
        if 'queryExecutionTimeoutInSeconds' in kwargs:
            query_execution_timeout_in_seconds = kwargs['queryExecutionTimeoutInSeconds']

        _setter("max_resource_percent", max_resource_percent)
        _setter("min_resource_percent", min_resource_percent)
        _setter("sql_pool_id", sql_pool_id)
        if importance is not None:
            _setter("importance", importance)
        if max_resource_percent_per_request is not None:
            _setter("max_resource_percent_per_request", max_resource_percent_per_request)
        if min_resource_percent_per_request is not None:
            _setter("min_resource_percent_per_request", min_resource_percent_per_request)
        if name is not None:
            _setter("name", name)
        if query_execution_timeout_in_seconds is not None:
            _setter("query_execution_timeout_in_seconds", query_execution_timeout_in_seconds)

    @property
    @pulumi.getter(name="maxResourcePercent")
    def max_resource_percent(self) -> pulumi.Input[int]:
        """
        The workload group cap percentage resource.
        """
        return pulumi.get(self, "max_resource_percent")

    @max_resource_percent.setter
    def max_resource_percent(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_resource_percent", value)

    @property
    @pulumi.getter(name="minResourcePercent")
    def min_resource_percent(self) -> pulumi.Input[int]:
        """
        The workload group minimum percentage resource.
        """
        return pulumi.get(self, "min_resource_percent")

    @min_resource_percent.setter
    def min_resource_percent(self, value: pulumi.Input[int]):
        pulumi.set(self, "min_resource_percent", value)

    @property
    @pulumi.getter(name="sqlPoolId")
    def sql_pool_id(self) -> pulumi.Input[str]:
        """
        The ID of the Synapse SQL Pool. Changing this forces a new Synapse SQL Pool Workload Group to be created.
        """
        return pulumi.get(self, "sql_pool_id")

    @sql_pool_id.setter
    def sql_pool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "sql_pool_id", value)

    @property
    @pulumi.getter
    def importance(self) -> Optional[pulumi.Input[str]]:
        """
        The workload group importance level. Defaults to `normal`.
        """
        return pulumi.get(self, "importance")

    @importance.setter
    def importance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "importance", value)

    @property
    @pulumi.getter(name="maxResourcePercentPerRequest")
    def max_resource_percent_per_request(self) -> Optional[pulumi.Input[float]]:
        """
        The workload group request maximum grant percentage. Defaults to `3`.
        """
        return pulumi.get(self, "max_resource_percent_per_request")

    @max_resource_percent_per_request.setter
    def max_resource_percent_per_request(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "max_resource_percent_per_request", value)

    @property
    @pulumi.getter(name="minResourcePercentPerRequest")
    def min_resource_percent_per_request(self) -> Optional[pulumi.Input[float]]:
        """
        The workload group request minimum grant percentage.
        """
        return pulumi.get(self, "min_resource_percent_per_request")

    @min_resource_percent_per_request.setter
    def min_resource_percent_per_request(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "min_resource_percent_per_request", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Synapse SQL Pool Workload Group. Changing this forces a new Synapse SQL Pool Workload Group to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="queryExecutionTimeoutInSeconds")
    def query_execution_timeout_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        The workload group query execution timeout.
        """
        return pulumi.get(self, "query_execution_timeout_in_seconds")

    @query_execution_timeout_in_seconds.setter
    def query_execution_timeout_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "query_execution_timeout_in_seconds", value)


@pulumi.input_type
class _SqlPoolWorkloadGroupState:
    def __init__(__self__, *,
                 importance: Optional[pulumi.Input[str]] = None,
                 max_resource_percent: Optional[pulumi.Input[int]] = None,
                 max_resource_percent_per_request: Optional[pulumi.Input[float]] = None,
                 min_resource_percent: Optional[pulumi.Input[int]] = None,
                 min_resource_percent_per_request: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 query_execution_timeout_in_seconds: Optional[pulumi.Input[int]] = None,
                 sql_pool_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SqlPoolWorkloadGroup resources.
        :param pulumi.Input[str] importance: The workload group importance level. Defaults to `normal`.
        :param pulumi.Input[int] max_resource_percent: The workload group cap percentage resource.
        :param pulumi.Input[float] max_resource_percent_per_request: The workload group request maximum grant percentage. Defaults to `3`.
        :param pulumi.Input[int] min_resource_percent: The workload group minimum percentage resource.
        :param pulumi.Input[float] min_resource_percent_per_request: The workload group request minimum grant percentage.
        :param pulumi.Input[str] name: The name which should be used for this Synapse SQL Pool Workload Group. Changing this forces a new Synapse SQL Pool Workload Group to be created.
        :param pulumi.Input[int] query_execution_timeout_in_seconds: The workload group query execution timeout.
        :param pulumi.Input[str] sql_pool_id: The ID of the Synapse SQL Pool. Changing this forces a new Synapse SQL Pool Workload Group to be created.
        """
        _SqlPoolWorkloadGroupState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            importance=importance,
            max_resource_percent=max_resource_percent,
            max_resource_percent_per_request=max_resource_percent_per_request,
            min_resource_percent=min_resource_percent,
            min_resource_percent_per_request=min_resource_percent_per_request,
            name=name,
            query_execution_timeout_in_seconds=query_execution_timeout_in_seconds,
            sql_pool_id=sql_pool_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             importance: Optional[pulumi.Input[str]] = None,
             max_resource_percent: Optional[pulumi.Input[int]] = None,
             max_resource_percent_per_request: Optional[pulumi.Input[float]] = None,
             min_resource_percent: Optional[pulumi.Input[int]] = None,
             min_resource_percent_per_request: Optional[pulumi.Input[float]] = None,
             name: Optional[pulumi.Input[str]] = None,
             query_execution_timeout_in_seconds: Optional[pulumi.Input[int]] = None,
             sql_pool_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'maxResourcePercent' in kwargs:
            max_resource_percent = kwargs['maxResourcePercent']
        if 'maxResourcePercentPerRequest' in kwargs:
            max_resource_percent_per_request = kwargs['maxResourcePercentPerRequest']
        if 'minResourcePercent' in kwargs:
            min_resource_percent = kwargs['minResourcePercent']
        if 'minResourcePercentPerRequest' in kwargs:
            min_resource_percent_per_request = kwargs['minResourcePercentPerRequest']
        if 'queryExecutionTimeoutInSeconds' in kwargs:
            query_execution_timeout_in_seconds = kwargs['queryExecutionTimeoutInSeconds']
        if 'sqlPoolId' in kwargs:
            sql_pool_id = kwargs['sqlPoolId']

        if importance is not None:
            _setter("importance", importance)
        if max_resource_percent is not None:
            _setter("max_resource_percent", max_resource_percent)
        if max_resource_percent_per_request is not None:
            _setter("max_resource_percent_per_request", max_resource_percent_per_request)
        if min_resource_percent is not None:
            _setter("min_resource_percent", min_resource_percent)
        if min_resource_percent_per_request is not None:
            _setter("min_resource_percent_per_request", min_resource_percent_per_request)
        if name is not None:
            _setter("name", name)
        if query_execution_timeout_in_seconds is not None:
            _setter("query_execution_timeout_in_seconds", query_execution_timeout_in_seconds)
        if sql_pool_id is not None:
            _setter("sql_pool_id", sql_pool_id)

    @property
    @pulumi.getter
    def importance(self) -> Optional[pulumi.Input[str]]:
        """
        The workload group importance level. Defaults to `normal`.
        """
        return pulumi.get(self, "importance")

    @importance.setter
    def importance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "importance", value)

    @property
    @pulumi.getter(name="maxResourcePercent")
    def max_resource_percent(self) -> Optional[pulumi.Input[int]]:
        """
        The workload group cap percentage resource.
        """
        return pulumi.get(self, "max_resource_percent")

    @max_resource_percent.setter
    def max_resource_percent(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_resource_percent", value)

    @property
    @pulumi.getter(name="maxResourcePercentPerRequest")
    def max_resource_percent_per_request(self) -> Optional[pulumi.Input[float]]:
        """
        The workload group request maximum grant percentage. Defaults to `3`.
        """
        return pulumi.get(self, "max_resource_percent_per_request")

    @max_resource_percent_per_request.setter
    def max_resource_percent_per_request(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "max_resource_percent_per_request", value)

    @property
    @pulumi.getter(name="minResourcePercent")
    def min_resource_percent(self) -> Optional[pulumi.Input[int]]:
        """
        The workload group minimum percentage resource.
        """
        return pulumi.get(self, "min_resource_percent")

    @min_resource_percent.setter
    def min_resource_percent(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_resource_percent", value)

    @property
    @pulumi.getter(name="minResourcePercentPerRequest")
    def min_resource_percent_per_request(self) -> Optional[pulumi.Input[float]]:
        """
        The workload group request minimum grant percentage.
        """
        return pulumi.get(self, "min_resource_percent_per_request")

    @min_resource_percent_per_request.setter
    def min_resource_percent_per_request(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "min_resource_percent_per_request", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Synapse SQL Pool Workload Group. Changing this forces a new Synapse SQL Pool Workload Group to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="queryExecutionTimeoutInSeconds")
    def query_execution_timeout_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        The workload group query execution timeout.
        """
        return pulumi.get(self, "query_execution_timeout_in_seconds")

    @query_execution_timeout_in_seconds.setter
    def query_execution_timeout_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "query_execution_timeout_in_seconds", value)

    @property
    @pulumi.getter(name="sqlPoolId")
    def sql_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Synapse SQL Pool. Changing this forces a new Synapse SQL Pool Workload Group to be created.
        """
        return pulumi.get(self, "sql_pool_id")

    @sql_pool_id.setter
    def sql_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_pool_id", value)


class SqlPoolWorkloadGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 importance: Optional[pulumi.Input[str]] = None,
                 max_resource_percent: Optional[pulumi.Input[int]] = None,
                 max_resource_percent_per_request: Optional[pulumi.Input[float]] = None,
                 min_resource_percent: Optional[pulumi.Input[int]] = None,
                 min_resource_percent_per_request: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 query_execution_timeout_in_seconds: Optional[pulumi.Input[int]] = None,
                 sql_pool_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Synapse SQL Pool Workload Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="west europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_kind="BlobStorage",
            account_tier="Standard",
            account_replication_type="LRS")
        example_data_lake_gen2_filesystem = azure.storage.DataLakeGen2Filesystem("exampleDataLakeGen2Filesystem", storage_account_id=example_account.id)
        example_workspace = azure.synapse.Workspace("exampleWorkspace",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            storage_data_lake_gen2_filesystem_id=example_data_lake_gen2_filesystem.id,
            sql_administrator_login="sqladminuser",
            sql_administrator_login_password="H@Sh1CoR3!",
            identity=azure.synapse.WorkspaceIdentityArgs(
                type="SystemAssigned",
            ))
        example_sql_pool = azure.synapse.SqlPool("exampleSqlPool",
            synapse_workspace_id=example_workspace.id,
            sku_name="DW100c",
            create_mode="Default")
        example_sql_pool_workload_group = azure.synapse.SqlPoolWorkloadGroup("exampleSqlPoolWorkloadGroup",
            sql_pool_id=example_sql_pool.id,
            importance="normal",
            max_resource_percent=100,
            min_resource_percent=0,
            max_resource_percent_per_request=3,
            min_resource_percent_per_request=3,
            query_execution_timeout_in_seconds=0)
        ```

        ## Import

        Synapse SQL Pool Workload Groups can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:synapse/sqlPoolWorkloadGroup:SqlPoolWorkloadGroup example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resGroup1/providers/Microsoft.Synapse/workspaces/workspace1/sqlPools/sqlPool1/workloadGroups/workloadGroup1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] importance: The workload group importance level. Defaults to `normal`.
        :param pulumi.Input[int] max_resource_percent: The workload group cap percentage resource.
        :param pulumi.Input[float] max_resource_percent_per_request: The workload group request maximum grant percentage. Defaults to `3`.
        :param pulumi.Input[int] min_resource_percent: The workload group minimum percentage resource.
        :param pulumi.Input[float] min_resource_percent_per_request: The workload group request minimum grant percentage.
        :param pulumi.Input[str] name: The name which should be used for this Synapse SQL Pool Workload Group. Changing this forces a new Synapse SQL Pool Workload Group to be created.
        :param pulumi.Input[int] query_execution_timeout_in_seconds: The workload group query execution timeout.
        :param pulumi.Input[str] sql_pool_id: The ID of the Synapse SQL Pool. Changing this forces a new Synapse SQL Pool Workload Group to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SqlPoolWorkloadGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Synapse SQL Pool Workload Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="west europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_kind="BlobStorage",
            account_tier="Standard",
            account_replication_type="LRS")
        example_data_lake_gen2_filesystem = azure.storage.DataLakeGen2Filesystem("exampleDataLakeGen2Filesystem", storage_account_id=example_account.id)
        example_workspace = azure.synapse.Workspace("exampleWorkspace",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            storage_data_lake_gen2_filesystem_id=example_data_lake_gen2_filesystem.id,
            sql_administrator_login="sqladminuser",
            sql_administrator_login_password="H@Sh1CoR3!",
            identity=azure.synapse.WorkspaceIdentityArgs(
                type="SystemAssigned",
            ))
        example_sql_pool = azure.synapse.SqlPool("exampleSqlPool",
            synapse_workspace_id=example_workspace.id,
            sku_name="DW100c",
            create_mode="Default")
        example_sql_pool_workload_group = azure.synapse.SqlPoolWorkloadGroup("exampleSqlPoolWorkloadGroup",
            sql_pool_id=example_sql_pool.id,
            importance="normal",
            max_resource_percent=100,
            min_resource_percent=0,
            max_resource_percent_per_request=3,
            min_resource_percent_per_request=3,
            query_execution_timeout_in_seconds=0)
        ```

        ## Import

        Synapse SQL Pool Workload Groups can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:synapse/sqlPoolWorkloadGroup:SqlPoolWorkloadGroup example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resGroup1/providers/Microsoft.Synapse/workspaces/workspace1/sqlPools/sqlPool1/workloadGroups/workloadGroup1
        ```

        :param str resource_name: The name of the resource.
        :param SqlPoolWorkloadGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SqlPoolWorkloadGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SqlPoolWorkloadGroupArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 importance: Optional[pulumi.Input[str]] = None,
                 max_resource_percent: Optional[pulumi.Input[int]] = None,
                 max_resource_percent_per_request: Optional[pulumi.Input[float]] = None,
                 min_resource_percent: Optional[pulumi.Input[int]] = None,
                 min_resource_percent_per_request: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 query_execution_timeout_in_seconds: Optional[pulumi.Input[int]] = None,
                 sql_pool_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SqlPoolWorkloadGroupArgs.__new__(SqlPoolWorkloadGroupArgs)

            __props__.__dict__["importance"] = importance
            if max_resource_percent is None and not opts.urn:
                raise TypeError("Missing required property 'max_resource_percent'")
            __props__.__dict__["max_resource_percent"] = max_resource_percent
            __props__.__dict__["max_resource_percent_per_request"] = max_resource_percent_per_request
            if min_resource_percent is None and not opts.urn:
                raise TypeError("Missing required property 'min_resource_percent'")
            __props__.__dict__["min_resource_percent"] = min_resource_percent
            __props__.__dict__["min_resource_percent_per_request"] = min_resource_percent_per_request
            __props__.__dict__["name"] = name
            __props__.__dict__["query_execution_timeout_in_seconds"] = query_execution_timeout_in_seconds
            if sql_pool_id is None and not opts.urn:
                raise TypeError("Missing required property 'sql_pool_id'")
            __props__.__dict__["sql_pool_id"] = sql_pool_id
        super(SqlPoolWorkloadGroup, __self__).__init__(
            'azure:synapse/sqlPoolWorkloadGroup:SqlPoolWorkloadGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            importance: Optional[pulumi.Input[str]] = None,
            max_resource_percent: Optional[pulumi.Input[int]] = None,
            max_resource_percent_per_request: Optional[pulumi.Input[float]] = None,
            min_resource_percent: Optional[pulumi.Input[int]] = None,
            min_resource_percent_per_request: Optional[pulumi.Input[float]] = None,
            name: Optional[pulumi.Input[str]] = None,
            query_execution_timeout_in_seconds: Optional[pulumi.Input[int]] = None,
            sql_pool_id: Optional[pulumi.Input[str]] = None) -> 'SqlPoolWorkloadGroup':
        """
        Get an existing SqlPoolWorkloadGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] importance: The workload group importance level. Defaults to `normal`.
        :param pulumi.Input[int] max_resource_percent: The workload group cap percentage resource.
        :param pulumi.Input[float] max_resource_percent_per_request: The workload group request maximum grant percentage. Defaults to `3`.
        :param pulumi.Input[int] min_resource_percent: The workload group minimum percentage resource.
        :param pulumi.Input[float] min_resource_percent_per_request: The workload group request minimum grant percentage.
        :param pulumi.Input[str] name: The name which should be used for this Synapse SQL Pool Workload Group. Changing this forces a new Synapse SQL Pool Workload Group to be created.
        :param pulumi.Input[int] query_execution_timeout_in_seconds: The workload group query execution timeout.
        :param pulumi.Input[str] sql_pool_id: The ID of the Synapse SQL Pool. Changing this forces a new Synapse SQL Pool Workload Group to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SqlPoolWorkloadGroupState.__new__(_SqlPoolWorkloadGroupState)

        __props__.__dict__["importance"] = importance
        __props__.__dict__["max_resource_percent"] = max_resource_percent
        __props__.__dict__["max_resource_percent_per_request"] = max_resource_percent_per_request
        __props__.__dict__["min_resource_percent"] = min_resource_percent
        __props__.__dict__["min_resource_percent_per_request"] = min_resource_percent_per_request
        __props__.__dict__["name"] = name
        __props__.__dict__["query_execution_timeout_in_seconds"] = query_execution_timeout_in_seconds
        __props__.__dict__["sql_pool_id"] = sql_pool_id
        return SqlPoolWorkloadGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def importance(self) -> pulumi.Output[Optional[str]]:
        """
        The workload group importance level. Defaults to `normal`.
        """
        return pulumi.get(self, "importance")

    @property
    @pulumi.getter(name="maxResourcePercent")
    def max_resource_percent(self) -> pulumi.Output[int]:
        """
        The workload group cap percentage resource.
        """
        return pulumi.get(self, "max_resource_percent")

    @property
    @pulumi.getter(name="maxResourcePercentPerRequest")
    def max_resource_percent_per_request(self) -> pulumi.Output[Optional[float]]:
        """
        The workload group request maximum grant percentage. Defaults to `3`.
        """
        return pulumi.get(self, "max_resource_percent_per_request")

    @property
    @pulumi.getter(name="minResourcePercent")
    def min_resource_percent(self) -> pulumi.Output[int]:
        """
        The workload group minimum percentage resource.
        """
        return pulumi.get(self, "min_resource_percent")

    @property
    @pulumi.getter(name="minResourcePercentPerRequest")
    def min_resource_percent_per_request(self) -> pulumi.Output[Optional[float]]:
        """
        The workload group request minimum grant percentage.
        """
        return pulumi.get(self, "min_resource_percent_per_request")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Synapse SQL Pool Workload Group. Changing this forces a new Synapse SQL Pool Workload Group to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="queryExecutionTimeoutInSeconds")
    def query_execution_timeout_in_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        The workload group query execution timeout.
        """
        return pulumi.get(self, "query_execution_timeout_in_seconds")

    @property
    @pulumi.getter(name="sqlPoolId")
    def sql_pool_id(self) -> pulumi.Output[str]:
        """
        The ID of the Synapse SQL Pool. Changing this forces a new Synapse SQL Pool Workload Group to be created.
        """
        return pulumi.get(self, "sql_pool_id")


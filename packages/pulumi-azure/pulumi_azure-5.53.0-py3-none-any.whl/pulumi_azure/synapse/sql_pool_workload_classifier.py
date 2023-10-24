# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SqlPoolWorkloadClassifierArgs', 'SqlPoolWorkloadClassifier']

@pulumi.input_type
class SqlPoolWorkloadClassifierArgs:
    def __init__(__self__, *,
                 member_name: pulumi.Input[str],
                 workload_group_id: pulumi.Input[str],
                 context: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 importance: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SqlPoolWorkloadClassifier resource.
        :param pulumi.Input[str] member_name: The workload classifier member name used to classified against.
        :param pulumi.Input[str] workload_group_id: The ID of the Synapse SQL Pool Workload Group. Changing this forces a new Synapse SQL Pool Workload Classifier to be created.
        :param pulumi.Input[str] context: Specifies the session context value that a request can be classified against.
        :param pulumi.Input[str] end_time: The workload classifier end time for classification. It's of the `HH:MM` format in UTC time zone.
        :param pulumi.Input[str] importance: The workload classifier importance. The allowed values are `low`, `below_normal`, `normal`, `above_normal` and `high`.
        :param pulumi.Input[str] label: Specifies the label value that a request can be classified against.
        :param pulumi.Input[str] name: The name which should be used for this Synapse SQL Pool Workload Classifier. Changing this forces a new Synapse SQL Pool Workload Classifier to be created.
        :param pulumi.Input[str] start_time: The workload classifier start time for classification. It's of the `HH:MM` format in UTC time zone.
        """
        SqlPoolWorkloadClassifierArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            member_name=member_name,
            workload_group_id=workload_group_id,
            context=context,
            end_time=end_time,
            importance=importance,
            label=label,
            name=name,
            start_time=start_time,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             member_name: pulumi.Input[str],
             workload_group_id: pulumi.Input[str],
             context: Optional[pulumi.Input[str]] = None,
             end_time: Optional[pulumi.Input[str]] = None,
             importance: Optional[pulumi.Input[str]] = None,
             label: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             start_time: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'memberName' in kwargs:
            member_name = kwargs['memberName']
        if 'workloadGroupId' in kwargs:
            workload_group_id = kwargs['workloadGroupId']
        if 'endTime' in kwargs:
            end_time = kwargs['endTime']
        if 'startTime' in kwargs:
            start_time = kwargs['startTime']

        _setter("member_name", member_name)
        _setter("workload_group_id", workload_group_id)
        if context is not None:
            _setter("context", context)
        if end_time is not None:
            _setter("end_time", end_time)
        if importance is not None:
            _setter("importance", importance)
        if label is not None:
            _setter("label", label)
        if name is not None:
            _setter("name", name)
        if start_time is not None:
            _setter("start_time", start_time)

    @property
    @pulumi.getter(name="memberName")
    def member_name(self) -> pulumi.Input[str]:
        """
        The workload classifier member name used to classified against.
        """
        return pulumi.get(self, "member_name")

    @member_name.setter
    def member_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "member_name", value)

    @property
    @pulumi.getter(name="workloadGroupId")
    def workload_group_id(self) -> pulumi.Input[str]:
        """
        The ID of the Synapse SQL Pool Workload Group. Changing this forces a new Synapse SQL Pool Workload Classifier to be created.
        """
        return pulumi.get(self, "workload_group_id")

    @workload_group_id.setter
    def workload_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "workload_group_id", value)

    @property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the session context value that a request can be classified against.
        """
        return pulumi.get(self, "context")

    @context.setter
    def context(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "context", value)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[str]]:
        """
        The workload classifier end time for classification. It's of the `HH:MM` format in UTC time zone.
        """
        return pulumi.get(self, "end_time")

    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_time", value)

    @property
    @pulumi.getter
    def importance(self) -> Optional[pulumi.Input[str]]:
        """
        The workload classifier importance. The allowed values are `low`, `below_normal`, `normal`, `above_normal` and `high`.
        """
        return pulumi.get(self, "importance")

    @importance.setter
    def importance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "importance", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the label value that a request can be classified against.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Synapse SQL Pool Workload Classifier. Changing this forces a new Synapse SQL Pool Workload Classifier to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[str]]:
        """
        The workload classifier start time for classification. It's of the `HH:MM` format in UTC time zone.
        """
        return pulumi.get(self, "start_time")

    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_time", value)


@pulumi.input_type
class _SqlPoolWorkloadClassifierState:
    def __init__(__self__, *,
                 context: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 importance: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 member_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 workload_group_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SqlPoolWorkloadClassifier resources.
        :param pulumi.Input[str] context: Specifies the session context value that a request can be classified against.
        :param pulumi.Input[str] end_time: The workload classifier end time for classification. It's of the `HH:MM` format in UTC time zone.
        :param pulumi.Input[str] importance: The workload classifier importance. The allowed values are `low`, `below_normal`, `normal`, `above_normal` and `high`.
        :param pulumi.Input[str] label: Specifies the label value that a request can be classified against.
        :param pulumi.Input[str] member_name: The workload classifier member name used to classified against.
        :param pulumi.Input[str] name: The name which should be used for this Synapse SQL Pool Workload Classifier. Changing this forces a new Synapse SQL Pool Workload Classifier to be created.
        :param pulumi.Input[str] start_time: The workload classifier start time for classification. It's of the `HH:MM` format in UTC time zone.
        :param pulumi.Input[str] workload_group_id: The ID of the Synapse SQL Pool Workload Group. Changing this forces a new Synapse SQL Pool Workload Classifier to be created.
        """
        _SqlPoolWorkloadClassifierState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            context=context,
            end_time=end_time,
            importance=importance,
            label=label,
            member_name=member_name,
            name=name,
            start_time=start_time,
            workload_group_id=workload_group_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             context: Optional[pulumi.Input[str]] = None,
             end_time: Optional[pulumi.Input[str]] = None,
             importance: Optional[pulumi.Input[str]] = None,
             label: Optional[pulumi.Input[str]] = None,
             member_name: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             start_time: Optional[pulumi.Input[str]] = None,
             workload_group_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'endTime' in kwargs:
            end_time = kwargs['endTime']
        if 'memberName' in kwargs:
            member_name = kwargs['memberName']
        if 'startTime' in kwargs:
            start_time = kwargs['startTime']
        if 'workloadGroupId' in kwargs:
            workload_group_id = kwargs['workloadGroupId']

        if context is not None:
            _setter("context", context)
        if end_time is not None:
            _setter("end_time", end_time)
        if importance is not None:
            _setter("importance", importance)
        if label is not None:
            _setter("label", label)
        if member_name is not None:
            _setter("member_name", member_name)
        if name is not None:
            _setter("name", name)
        if start_time is not None:
            _setter("start_time", start_time)
        if workload_group_id is not None:
            _setter("workload_group_id", workload_group_id)

    @property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the session context value that a request can be classified against.
        """
        return pulumi.get(self, "context")

    @context.setter
    def context(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "context", value)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[str]]:
        """
        The workload classifier end time for classification. It's of the `HH:MM` format in UTC time zone.
        """
        return pulumi.get(self, "end_time")

    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_time", value)

    @property
    @pulumi.getter
    def importance(self) -> Optional[pulumi.Input[str]]:
        """
        The workload classifier importance. The allowed values are `low`, `below_normal`, `normal`, `above_normal` and `high`.
        """
        return pulumi.get(self, "importance")

    @importance.setter
    def importance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "importance", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the label value that a request can be classified against.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="memberName")
    def member_name(self) -> Optional[pulumi.Input[str]]:
        """
        The workload classifier member name used to classified against.
        """
        return pulumi.get(self, "member_name")

    @member_name.setter
    def member_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "member_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Synapse SQL Pool Workload Classifier. Changing this forces a new Synapse SQL Pool Workload Classifier to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[str]]:
        """
        The workload classifier start time for classification. It's of the `HH:MM` format in UTC time zone.
        """
        return pulumi.get(self, "start_time")

    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_time", value)

    @property
    @pulumi.getter(name="workloadGroupId")
    def workload_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Synapse SQL Pool Workload Group. Changing this forces a new Synapse SQL Pool Workload Classifier to be created.
        """
        return pulumi.get(self, "workload_group_id")

    @workload_group_id.setter
    def workload_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workload_group_id", value)


class SqlPoolWorkloadClassifier(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 context: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 importance: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 member_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 workload_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Synapse SQL Pool Workload Classifier.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
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
        example_sql_pool_workload_classifier = azure.synapse.SqlPoolWorkloadClassifier("exampleSqlPoolWorkloadClassifier",
            workload_group_id=example_sql_pool_workload_group.id,
            context="example_context",
            end_time="14:00",
            importance="high",
            label="example_label",
            member_name="dbo",
            start_time="12:00")
        ```

        ## Import

        Synapse SQL Pool Workload Classifiers can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:synapse/sqlPoolWorkloadClassifier:SqlPoolWorkloadClassifier example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.Synapse/workspaces/workspace1/sqlPools/sqlPool1/workloadGroups/workloadGroup1/workloadClassifiers/workloadClassifier1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] context: Specifies the session context value that a request can be classified against.
        :param pulumi.Input[str] end_time: The workload classifier end time for classification. It's of the `HH:MM` format in UTC time zone.
        :param pulumi.Input[str] importance: The workload classifier importance. The allowed values are `low`, `below_normal`, `normal`, `above_normal` and `high`.
        :param pulumi.Input[str] label: Specifies the label value that a request can be classified against.
        :param pulumi.Input[str] member_name: The workload classifier member name used to classified against.
        :param pulumi.Input[str] name: The name which should be used for this Synapse SQL Pool Workload Classifier. Changing this forces a new Synapse SQL Pool Workload Classifier to be created.
        :param pulumi.Input[str] start_time: The workload classifier start time for classification. It's of the `HH:MM` format in UTC time zone.
        :param pulumi.Input[str] workload_group_id: The ID of the Synapse SQL Pool Workload Group. Changing this forces a new Synapse SQL Pool Workload Classifier to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SqlPoolWorkloadClassifierArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Synapse SQL Pool Workload Classifier.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
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
        example_sql_pool_workload_classifier = azure.synapse.SqlPoolWorkloadClassifier("exampleSqlPoolWorkloadClassifier",
            workload_group_id=example_sql_pool_workload_group.id,
            context="example_context",
            end_time="14:00",
            importance="high",
            label="example_label",
            member_name="dbo",
            start_time="12:00")
        ```

        ## Import

        Synapse SQL Pool Workload Classifiers can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:synapse/sqlPoolWorkloadClassifier:SqlPoolWorkloadClassifier example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.Synapse/workspaces/workspace1/sqlPools/sqlPool1/workloadGroups/workloadGroup1/workloadClassifiers/workloadClassifier1
        ```

        :param str resource_name: The name of the resource.
        :param SqlPoolWorkloadClassifierArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SqlPoolWorkloadClassifierArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SqlPoolWorkloadClassifierArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 context: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 importance: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 member_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 workload_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SqlPoolWorkloadClassifierArgs.__new__(SqlPoolWorkloadClassifierArgs)

            __props__.__dict__["context"] = context
            __props__.__dict__["end_time"] = end_time
            __props__.__dict__["importance"] = importance
            __props__.__dict__["label"] = label
            if member_name is None and not opts.urn:
                raise TypeError("Missing required property 'member_name'")
            __props__.__dict__["member_name"] = member_name
            __props__.__dict__["name"] = name
            __props__.__dict__["start_time"] = start_time
            if workload_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'workload_group_id'")
            __props__.__dict__["workload_group_id"] = workload_group_id
        super(SqlPoolWorkloadClassifier, __self__).__init__(
            'azure:synapse/sqlPoolWorkloadClassifier:SqlPoolWorkloadClassifier',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            context: Optional[pulumi.Input[str]] = None,
            end_time: Optional[pulumi.Input[str]] = None,
            importance: Optional[pulumi.Input[str]] = None,
            label: Optional[pulumi.Input[str]] = None,
            member_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            start_time: Optional[pulumi.Input[str]] = None,
            workload_group_id: Optional[pulumi.Input[str]] = None) -> 'SqlPoolWorkloadClassifier':
        """
        Get an existing SqlPoolWorkloadClassifier resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] context: Specifies the session context value that a request can be classified against.
        :param pulumi.Input[str] end_time: The workload classifier end time for classification. It's of the `HH:MM` format in UTC time zone.
        :param pulumi.Input[str] importance: The workload classifier importance. The allowed values are `low`, `below_normal`, `normal`, `above_normal` and `high`.
        :param pulumi.Input[str] label: Specifies the label value that a request can be classified against.
        :param pulumi.Input[str] member_name: The workload classifier member name used to classified against.
        :param pulumi.Input[str] name: The name which should be used for this Synapse SQL Pool Workload Classifier. Changing this forces a new Synapse SQL Pool Workload Classifier to be created.
        :param pulumi.Input[str] start_time: The workload classifier start time for classification. It's of the `HH:MM` format in UTC time zone.
        :param pulumi.Input[str] workload_group_id: The ID of the Synapse SQL Pool Workload Group. Changing this forces a new Synapse SQL Pool Workload Classifier to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SqlPoolWorkloadClassifierState.__new__(_SqlPoolWorkloadClassifierState)

        __props__.__dict__["context"] = context
        __props__.__dict__["end_time"] = end_time
        __props__.__dict__["importance"] = importance
        __props__.__dict__["label"] = label
        __props__.__dict__["member_name"] = member_name
        __props__.__dict__["name"] = name
        __props__.__dict__["start_time"] = start_time
        __props__.__dict__["workload_group_id"] = workload_group_id
        return SqlPoolWorkloadClassifier(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def context(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the session context value that a request can be classified against.
        """
        return pulumi.get(self, "context")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[Optional[str]]:
        """
        The workload classifier end time for classification. It's of the `HH:MM` format in UTC time zone.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter
    def importance(self) -> pulumi.Output[Optional[str]]:
        """
        The workload classifier importance. The allowed values are `low`, `below_normal`, `normal`, `above_normal` and `high`.
        """
        return pulumi.get(self, "importance")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the label value that a request can be classified against.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="memberName")
    def member_name(self) -> pulumi.Output[str]:
        """
        The workload classifier member name used to classified against.
        """
        return pulumi.get(self, "member_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Synapse SQL Pool Workload Classifier. Changing this forces a new Synapse SQL Pool Workload Classifier to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[Optional[str]]:
        """
        The workload classifier start time for classification. It's of the `HH:MM` format in UTC time zone.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter(name="workloadGroupId")
    def workload_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the Synapse SQL Pool Workload Group. Changing this forces a new Synapse SQL Pool Workload Classifier to be created.
        """
        return pulumi.get(self, "workload_group_id")


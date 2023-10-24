# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['LinkedStorageAccountArgs', 'LinkedStorageAccount']

@pulumi.input_type
class LinkedStorageAccountArgs:
    def __init__(__self__, *,
                 data_source_type: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 storage_account_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 workspace_resource_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a LinkedStorageAccount resource.
        :param pulumi.Input[str] data_source_type: The data source type which should be used for this Log Analytics Linked Storage Account. Possible values are `CustomLogs`, `AzureWatson`, `Query`, `Ingestion` and `Alerts`. Changing this forces a new Log Analytics Linked Storage Account to be created.
               
               > **Note:** The `data_source_type` is case-insensitive in current 3.x version. And in 4.0 or later versions, Case-sensitivity will be required.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Log Analytics Linked Storage Account should exist. Changing this forces a new Log Analytics Linked Storage Account to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] storage_account_ids: The storage account resource ids to be linked.
        :param pulumi.Input[str] workspace_resource_id: The resource ID of the Log Analytics Workspace. Changing this forces a new Log Analytics Linked Storage Account to be created.
        """
        LinkedStorageAccountArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            data_source_type=data_source_type,
            resource_group_name=resource_group_name,
            storage_account_ids=storage_account_ids,
            workspace_resource_id=workspace_resource_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             data_source_type: pulumi.Input[str],
             resource_group_name: pulumi.Input[str],
             storage_account_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
             workspace_resource_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'dataSourceType' in kwargs:
            data_source_type = kwargs['dataSourceType']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'storageAccountIds' in kwargs:
            storage_account_ids = kwargs['storageAccountIds']
        if 'workspaceResourceId' in kwargs:
            workspace_resource_id = kwargs['workspaceResourceId']

        _setter("data_source_type", data_source_type)
        _setter("resource_group_name", resource_group_name)
        _setter("storage_account_ids", storage_account_ids)
        _setter("workspace_resource_id", workspace_resource_id)

    @property
    @pulumi.getter(name="dataSourceType")
    def data_source_type(self) -> pulumi.Input[str]:
        """
        The data source type which should be used for this Log Analytics Linked Storage Account. Possible values are `CustomLogs`, `AzureWatson`, `Query`, `Ingestion` and `Alerts`. Changing this forces a new Log Analytics Linked Storage Account to be created.

        > **Note:** The `data_source_type` is case-insensitive in current 3.x version. And in 4.0 or later versions, Case-sensitivity will be required.
        """
        return pulumi.get(self, "data_source_type")

    @data_source_type.setter
    def data_source_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_source_type", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group where the Log Analytics Linked Storage Account should exist. Changing this forces a new Log Analytics Linked Storage Account to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="storageAccountIds")
    def storage_account_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The storage account resource ids to be linked.
        """
        return pulumi.get(self, "storage_account_ids")

    @storage_account_ids.setter
    def storage_account_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "storage_account_ids", value)

    @property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the Log Analytics Workspace. Changing this forces a new Log Analytics Linked Storage Account to be created.
        """
        return pulumi.get(self, "workspace_resource_id")

    @workspace_resource_id.setter
    def workspace_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_resource_id", value)


@pulumi.input_type
class _LinkedStorageAccountState:
    def __init__(__self__, *,
                 data_source_type: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 workspace_resource_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering LinkedStorageAccount resources.
        :param pulumi.Input[str] data_source_type: The data source type which should be used for this Log Analytics Linked Storage Account. Possible values are `CustomLogs`, `AzureWatson`, `Query`, `Ingestion` and `Alerts`. Changing this forces a new Log Analytics Linked Storage Account to be created.
               
               > **Note:** The `data_source_type` is case-insensitive in current 3.x version. And in 4.0 or later versions, Case-sensitivity will be required.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Log Analytics Linked Storage Account should exist. Changing this forces a new Log Analytics Linked Storage Account to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] storage_account_ids: The storage account resource ids to be linked.
        :param pulumi.Input[str] workspace_resource_id: The resource ID of the Log Analytics Workspace. Changing this forces a new Log Analytics Linked Storage Account to be created.
        """
        _LinkedStorageAccountState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            data_source_type=data_source_type,
            resource_group_name=resource_group_name,
            storage_account_ids=storage_account_ids,
            workspace_resource_id=workspace_resource_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             data_source_type: Optional[pulumi.Input[str]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             storage_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             workspace_resource_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'dataSourceType' in kwargs:
            data_source_type = kwargs['dataSourceType']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'storageAccountIds' in kwargs:
            storage_account_ids = kwargs['storageAccountIds']
        if 'workspaceResourceId' in kwargs:
            workspace_resource_id = kwargs['workspaceResourceId']

        if data_source_type is not None:
            _setter("data_source_type", data_source_type)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if storage_account_ids is not None:
            _setter("storage_account_ids", storage_account_ids)
        if workspace_resource_id is not None:
            _setter("workspace_resource_id", workspace_resource_id)

    @property
    @pulumi.getter(name="dataSourceType")
    def data_source_type(self) -> Optional[pulumi.Input[str]]:
        """
        The data source type which should be used for this Log Analytics Linked Storage Account. Possible values are `CustomLogs`, `AzureWatson`, `Query`, `Ingestion` and `Alerts`. Changing this forces a new Log Analytics Linked Storage Account to be created.

        > **Note:** The `data_source_type` is case-insensitive in current 3.x version. And in 4.0 or later versions, Case-sensitivity will be required.
        """
        return pulumi.get(self, "data_source_type")

    @data_source_type.setter
    def data_source_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_source_type", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group where the Log Analytics Linked Storage Account should exist. Changing this forces a new Log Analytics Linked Storage Account to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="storageAccountIds")
    def storage_account_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The storage account resource ids to be linked.
        """
        return pulumi.get(self, "storage_account_ids")

    @storage_account_ids.setter
    def storage_account_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "storage_account_ids", value)

    @property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the Log Analytics Workspace. Changing this forces a new Log Analytics Linked Storage Account to be created.
        """
        return pulumi.get(self, "workspace_resource_id")

    @workspace_resource_id.setter
    def workspace_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_resource_id", value)


class LinkedStorageAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_source_type: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 workspace_resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Log Analytics Linked Storage Account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="GRS")
        example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="PerGB2018")
        example_linked_storage_account = azure.loganalytics.LinkedStorageAccount("exampleLinkedStorageAccount",
            data_source_type="CustomLogs",
            resource_group_name=example_resource_group.name,
            workspace_resource_id=example_analytics_workspace.id,
            storage_account_ids=[example_account.id])
        ```

        ## Import

        Log Analytics Linked Storage Accounts can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:loganalytics/linkedStorageAccount:LinkedStorageAccount example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.OperationalInsights/workspaces/workspace1/linkedStorageAccounts/{dataSourceType}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data_source_type: The data source type which should be used for this Log Analytics Linked Storage Account. Possible values are `CustomLogs`, `AzureWatson`, `Query`, `Ingestion` and `Alerts`. Changing this forces a new Log Analytics Linked Storage Account to be created.
               
               > **Note:** The `data_source_type` is case-insensitive in current 3.x version. And in 4.0 or later versions, Case-sensitivity will be required.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Log Analytics Linked Storage Account should exist. Changing this forces a new Log Analytics Linked Storage Account to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] storage_account_ids: The storage account resource ids to be linked.
        :param pulumi.Input[str] workspace_resource_id: The resource ID of the Log Analytics Workspace. Changing this forces a new Log Analytics Linked Storage Account to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LinkedStorageAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Log Analytics Linked Storage Account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="GRS")
        example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="PerGB2018")
        example_linked_storage_account = azure.loganalytics.LinkedStorageAccount("exampleLinkedStorageAccount",
            data_source_type="CustomLogs",
            resource_group_name=example_resource_group.name,
            workspace_resource_id=example_analytics_workspace.id,
            storage_account_ids=[example_account.id])
        ```

        ## Import

        Log Analytics Linked Storage Accounts can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:loganalytics/linkedStorageAccount:LinkedStorageAccount example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.OperationalInsights/workspaces/workspace1/linkedStorageAccounts/{dataSourceType}
        ```

        :param str resource_name: The name of the resource.
        :param LinkedStorageAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LinkedStorageAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            LinkedStorageAccountArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_source_type: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 workspace_resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LinkedStorageAccountArgs.__new__(LinkedStorageAccountArgs)

            if data_source_type is None and not opts.urn:
                raise TypeError("Missing required property 'data_source_type'")
            __props__.__dict__["data_source_type"] = data_source_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if storage_account_ids is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_ids'")
            __props__.__dict__["storage_account_ids"] = storage_account_ids
            if workspace_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_resource_id'")
            __props__.__dict__["workspace_resource_id"] = workspace_resource_id
        super(LinkedStorageAccount, __self__).__init__(
            'azure:loganalytics/linkedStorageAccount:LinkedStorageAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            data_source_type: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            storage_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            workspace_resource_id: Optional[pulumi.Input[str]] = None) -> 'LinkedStorageAccount':
        """
        Get an existing LinkedStorageAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data_source_type: The data source type which should be used for this Log Analytics Linked Storage Account. Possible values are `CustomLogs`, `AzureWatson`, `Query`, `Ingestion` and `Alerts`. Changing this forces a new Log Analytics Linked Storage Account to be created.
               
               > **Note:** The `data_source_type` is case-insensitive in current 3.x version. And in 4.0 or later versions, Case-sensitivity will be required.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Log Analytics Linked Storage Account should exist. Changing this forces a new Log Analytics Linked Storage Account to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] storage_account_ids: The storage account resource ids to be linked.
        :param pulumi.Input[str] workspace_resource_id: The resource ID of the Log Analytics Workspace. Changing this forces a new Log Analytics Linked Storage Account to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LinkedStorageAccountState.__new__(_LinkedStorageAccountState)

        __props__.__dict__["data_source_type"] = data_source_type
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["storage_account_ids"] = storage_account_ids
        __props__.__dict__["workspace_resource_id"] = workspace_resource_id
        return LinkedStorageAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataSourceType")
    def data_source_type(self) -> pulumi.Output[str]:
        """
        The data source type which should be used for this Log Analytics Linked Storage Account. Possible values are `CustomLogs`, `AzureWatson`, `Query`, `Ingestion` and `Alerts`. Changing this forces a new Log Analytics Linked Storage Account to be created.

        > **Note:** The `data_source_type` is case-insensitive in current 3.x version. And in 4.0 or later versions, Case-sensitivity will be required.
        """
        return pulumi.get(self, "data_source_type")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Log Analytics Linked Storage Account should exist. Changing this forces a new Log Analytics Linked Storage Account to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="storageAccountIds")
    def storage_account_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The storage account resource ids to be linked.
        """
        return pulumi.get(self, "storage_account_ids")

    @property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the Log Analytics Workspace. Changing this forces a new Log Analytics Linked Storage Account to be created.
        """
        return pulumi.get(self, "workspace_resource_id")


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DataConnectorOffice365Args', 'DataConnectorOffice365']

@pulumi.input_type
class DataConnectorOffice365Args:
    def __init__(__self__, *,
                 log_analytics_workspace_id: pulumi.Input[str],
                 exchange_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sharepoint_enabled: Optional[pulumi.Input[bool]] = None,
                 teams_enabled: Optional[pulumi.Input[bool]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DataConnectorOffice365 resource.
        :param pulumi.Input[str] log_analytics_workspace_id: The ID of the Log Analytics Workspace that this Office 365 Data Connector resides in. Changing this forces a new Office 365 Data Connector to be created.
        :param pulumi.Input[bool] exchange_enabled: Should the Exchange data connector be enabled? Defaults to `true`.
        :param pulumi.Input[str] name: The name which should be used for this Office 365 Data Connector. Changing this forces a new Office 365 Data Connector to be created.
        :param pulumi.Input[bool] sharepoint_enabled: Should the SharePoint data connector be enabled? Defaults to `true`.
        :param pulumi.Input[bool] teams_enabled: Should the Microsoft Teams data connector be enabled? Defaults to `true`.
               
               > **NOTE:** At least one of `exchange_enabled`, `sharedpoint_enabled` and `teams_enabled` has to be specified.
        :param pulumi.Input[str] tenant_id: The ID of the Tenant that this Office 365 Data Connector connects to. Changing this forces a new Office 365 Data Connector to be created.
               
               > **NOTE** Currently, only the same tenant as the running account is allowed. Cross-tenant scenario is not supported yet.
        """
        DataConnectorOffice365Args._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            log_analytics_workspace_id=log_analytics_workspace_id,
            exchange_enabled=exchange_enabled,
            name=name,
            sharepoint_enabled=sharepoint_enabled,
            teams_enabled=teams_enabled,
            tenant_id=tenant_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             log_analytics_workspace_id: pulumi.Input[str],
             exchange_enabled: Optional[pulumi.Input[bool]] = None,
             name: Optional[pulumi.Input[str]] = None,
             sharepoint_enabled: Optional[pulumi.Input[bool]] = None,
             teams_enabled: Optional[pulumi.Input[bool]] = None,
             tenant_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'logAnalyticsWorkspaceId' in kwargs:
            log_analytics_workspace_id = kwargs['logAnalyticsWorkspaceId']
        if 'exchangeEnabled' in kwargs:
            exchange_enabled = kwargs['exchangeEnabled']
        if 'sharepointEnabled' in kwargs:
            sharepoint_enabled = kwargs['sharepointEnabled']
        if 'teamsEnabled' in kwargs:
            teams_enabled = kwargs['teamsEnabled']
        if 'tenantId' in kwargs:
            tenant_id = kwargs['tenantId']

        _setter("log_analytics_workspace_id", log_analytics_workspace_id)
        if exchange_enabled is not None:
            _setter("exchange_enabled", exchange_enabled)
        if name is not None:
            _setter("name", name)
        if sharepoint_enabled is not None:
            _setter("sharepoint_enabled", sharepoint_enabled)
        if teams_enabled is not None:
            _setter("teams_enabled", teams_enabled)
        if tenant_id is not None:
            _setter("tenant_id", tenant_id)

    @property
    @pulumi.getter(name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> pulumi.Input[str]:
        """
        The ID of the Log Analytics Workspace that this Office 365 Data Connector resides in. Changing this forces a new Office 365 Data Connector to be created.
        """
        return pulumi.get(self, "log_analytics_workspace_id")

    @log_analytics_workspace_id.setter
    def log_analytics_workspace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "log_analytics_workspace_id", value)

    @property
    @pulumi.getter(name="exchangeEnabled")
    def exchange_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the Exchange data connector be enabled? Defaults to `true`.
        """
        return pulumi.get(self, "exchange_enabled")

    @exchange_enabled.setter
    def exchange_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "exchange_enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Office 365 Data Connector. Changing this forces a new Office 365 Data Connector to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sharepointEnabled")
    def sharepoint_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the SharePoint data connector be enabled? Defaults to `true`.
        """
        return pulumi.get(self, "sharepoint_enabled")

    @sharepoint_enabled.setter
    def sharepoint_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sharepoint_enabled", value)

    @property
    @pulumi.getter(name="teamsEnabled")
    def teams_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the Microsoft Teams data connector be enabled? Defaults to `true`.

        > **NOTE:** At least one of `exchange_enabled`, `sharedpoint_enabled` and `teams_enabled` has to be specified.
        """
        return pulumi.get(self, "teams_enabled")

    @teams_enabled.setter
    def teams_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "teams_enabled", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Tenant that this Office 365 Data Connector connects to. Changing this forces a new Office 365 Data Connector to be created.

        > **NOTE** Currently, only the same tenant as the running account is allowed. Cross-tenant scenario is not supported yet.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


@pulumi.input_type
class _DataConnectorOffice365State:
    def __init__(__self__, *,
                 exchange_enabled: Optional[pulumi.Input[bool]] = None,
                 log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sharepoint_enabled: Optional[pulumi.Input[bool]] = None,
                 teams_enabled: Optional[pulumi.Input[bool]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DataConnectorOffice365 resources.
        :param pulumi.Input[bool] exchange_enabled: Should the Exchange data connector be enabled? Defaults to `true`.
        :param pulumi.Input[str] log_analytics_workspace_id: The ID of the Log Analytics Workspace that this Office 365 Data Connector resides in. Changing this forces a new Office 365 Data Connector to be created.
        :param pulumi.Input[str] name: The name which should be used for this Office 365 Data Connector. Changing this forces a new Office 365 Data Connector to be created.
        :param pulumi.Input[bool] sharepoint_enabled: Should the SharePoint data connector be enabled? Defaults to `true`.
        :param pulumi.Input[bool] teams_enabled: Should the Microsoft Teams data connector be enabled? Defaults to `true`.
               
               > **NOTE:** At least one of `exchange_enabled`, `sharedpoint_enabled` and `teams_enabled` has to be specified.
        :param pulumi.Input[str] tenant_id: The ID of the Tenant that this Office 365 Data Connector connects to. Changing this forces a new Office 365 Data Connector to be created.
               
               > **NOTE** Currently, only the same tenant as the running account is allowed. Cross-tenant scenario is not supported yet.
        """
        _DataConnectorOffice365State._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            exchange_enabled=exchange_enabled,
            log_analytics_workspace_id=log_analytics_workspace_id,
            name=name,
            sharepoint_enabled=sharepoint_enabled,
            teams_enabled=teams_enabled,
            tenant_id=tenant_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             exchange_enabled: Optional[pulumi.Input[bool]] = None,
             log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             sharepoint_enabled: Optional[pulumi.Input[bool]] = None,
             teams_enabled: Optional[pulumi.Input[bool]] = None,
             tenant_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'exchangeEnabled' in kwargs:
            exchange_enabled = kwargs['exchangeEnabled']
        if 'logAnalyticsWorkspaceId' in kwargs:
            log_analytics_workspace_id = kwargs['logAnalyticsWorkspaceId']
        if 'sharepointEnabled' in kwargs:
            sharepoint_enabled = kwargs['sharepointEnabled']
        if 'teamsEnabled' in kwargs:
            teams_enabled = kwargs['teamsEnabled']
        if 'tenantId' in kwargs:
            tenant_id = kwargs['tenantId']

        if exchange_enabled is not None:
            _setter("exchange_enabled", exchange_enabled)
        if log_analytics_workspace_id is not None:
            _setter("log_analytics_workspace_id", log_analytics_workspace_id)
        if name is not None:
            _setter("name", name)
        if sharepoint_enabled is not None:
            _setter("sharepoint_enabled", sharepoint_enabled)
        if teams_enabled is not None:
            _setter("teams_enabled", teams_enabled)
        if tenant_id is not None:
            _setter("tenant_id", tenant_id)

    @property
    @pulumi.getter(name="exchangeEnabled")
    def exchange_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the Exchange data connector be enabled? Defaults to `true`.
        """
        return pulumi.get(self, "exchange_enabled")

    @exchange_enabled.setter
    def exchange_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "exchange_enabled", value)

    @property
    @pulumi.getter(name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Log Analytics Workspace that this Office 365 Data Connector resides in. Changing this forces a new Office 365 Data Connector to be created.
        """
        return pulumi.get(self, "log_analytics_workspace_id")

    @log_analytics_workspace_id.setter
    def log_analytics_workspace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_analytics_workspace_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Office 365 Data Connector. Changing this forces a new Office 365 Data Connector to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sharepointEnabled")
    def sharepoint_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the SharePoint data connector be enabled? Defaults to `true`.
        """
        return pulumi.get(self, "sharepoint_enabled")

    @sharepoint_enabled.setter
    def sharepoint_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sharepoint_enabled", value)

    @property
    @pulumi.getter(name="teamsEnabled")
    def teams_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the Microsoft Teams data connector be enabled? Defaults to `true`.

        > **NOTE:** At least one of `exchange_enabled`, `sharedpoint_enabled` and `teams_enabled` has to be specified.
        """
        return pulumi.get(self, "teams_enabled")

    @teams_enabled.setter
    def teams_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "teams_enabled", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Tenant that this Office 365 Data Connector connects to. Changing this forces a new Office 365 Data Connector to be created.

        > **NOTE** Currently, only the same tenant as the running account is allowed. Cross-tenant scenario is not supported yet.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


class DataConnectorOffice365(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 exchange_enabled: Optional[pulumi.Input[bool]] = None,
                 log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sharepoint_enabled: Optional[pulumi.Input[bool]] = None,
                 teams_enabled: Optional[pulumi.Input[bool]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Office 365 Data Connector.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="PerGB2018")
        example_log_analytics_workspace_onboarding = azure.sentinel.LogAnalyticsWorkspaceOnboarding("exampleLogAnalyticsWorkspaceOnboarding", workspace_id=example_analytics_workspace.id)
        example_data_connector_office365 = azure.sentinel.DataConnectorOffice365("exampleDataConnectorOffice365", log_analytics_workspace_id=example_log_analytics_workspace_onboarding.workspace_id)
        ```

        ## Import

        Office 365 Data Connectors can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:sentinel/dataConnectorOffice365:DataConnectorOffice365 example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.OperationalInsights/workspaces/workspace1/providers/Microsoft.SecurityInsights/dataConnectors/dc1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] exchange_enabled: Should the Exchange data connector be enabled? Defaults to `true`.
        :param pulumi.Input[str] log_analytics_workspace_id: The ID of the Log Analytics Workspace that this Office 365 Data Connector resides in. Changing this forces a new Office 365 Data Connector to be created.
        :param pulumi.Input[str] name: The name which should be used for this Office 365 Data Connector. Changing this forces a new Office 365 Data Connector to be created.
        :param pulumi.Input[bool] sharepoint_enabled: Should the SharePoint data connector be enabled? Defaults to `true`.
        :param pulumi.Input[bool] teams_enabled: Should the Microsoft Teams data connector be enabled? Defaults to `true`.
               
               > **NOTE:** At least one of `exchange_enabled`, `sharedpoint_enabled` and `teams_enabled` has to be specified.
        :param pulumi.Input[str] tenant_id: The ID of the Tenant that this Office 365 Data Connector connects to. Changing this forces a new Office 365 Data Connector to be created.
               
               > **NOTE** Currently, only the same tenant as the running account is allowed. Cross-tenant scenario is not supported yet.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataConnectorOffice365Args,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Office 365 Data Connector.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="PerGB2018")
        example_log_analytics_workspace_onboarding = azure.sentinel.LogAnalyticsWorkspaceOnboarding("exampleLogAnalyticsWorkspaceOnboarding", workspace_id=example_analytics_workspace.id)
        example_data_connector_office365 = azure.sentinel.DataConnectorOffice365("exampleDataConnectorOffice365", log_analytics_workspace_id=example_log_analytics_workspace_onboarding.workspace_id)
        ```

        ## Import

        Office 365 Data Connectors can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:sentinel/dataConnectorOffice365:DataConnectorOffice365 example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.OperationalInsights/workspaces/workspace1/providers/Microsoft.SecurityInsights/dataConnectors/dc1
        ```

        :param str resource_name: The name of the resource.
        :param DataConnectorOffice365Args args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataConnectorOffice365Args, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DataConnectorOffice365Args._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 exchange_enabled: Optional[pulumi.Input[bool]] = None,
                 log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sharepoint_enabled: Optional[pulumi.Input[bool]] = None,
                 teams_enabled: Optional[pulumi.Input[bool]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataConnectorOffice365Args.__new__(DataConnectorOffice365Args)

            __props__.__dict__["exchange_enabled"] = exchange_enabled
            if log_analytics_workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'log_analytics_workspace_id'")
            __props__.__dict__["log_analytics_workspace_id"] = log_analytics_workspace_id
            __props__.__dict__["name"] = name
            __props__.__dict__["sharepoint_enabled"] = sharepoint_enabled
            __props__.__dict__["teams_enabled"] = teams_enabled
            __props__.__dict__["tenant_id"] = tenant_id
        super(DataConnectorOffice365, __self__).__init__(
            'azure:sentinel/dataConnectorOffice365:DataConnectorOffice365',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            exchange_enabled: Optional[pulumi.Input[bool]] = None,
            log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            sharepoint_enabled: Optional[pulumi.Input[bool]] = None,
            teams_enabled: Optional[pulumi.Input[bool]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None) -> 'DataConnectorOffice365':
        """
        Get an existing DataConnectorOffice365 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] exchange_enabled: Should the Exchange data connector be enabled? Defaults to `true`.
        :param pulumi.Input[str] log_analytics_workspace_id: The ID of the Log Analytics Workspace that this Office 365 Data Connector resides in. Changing this forces a new Office 365 Data Connector to be created.
        :param pulumi.Input[str] name: The name which should be used for this Office 365 Data Connector. Changing this forces a new Office 365 Data Connector to be created.
        :param pulumi.Input[bool] sharepoint_enabled: Should the SharePoint data connector be enabled? Defaults to `true`.
        :param pulumi.Input[bool] teams_enabled: Should the Microsoft Teams data connector be enabled? Defaults to `true`.
               
               > **NOTE:** At least one of `exchange_enabled`, `sharedpoint_enabled` and `teams_enabled` has to be specified.
        :param pulumi.Input[str] tenant_id: The ID of the Tenant that this Office 365 Data Connector connects to. Changing this forces a new Office 365 Data Connector to be created.
               
               > **NOTE** Currently, only the same tenant as the running account is allowed. Cross-tenant scenario is not supported yet.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DataConnectorOffice365State.__new__(_DataConnectorOffice365State)

        __props__.__dict__["exchange_enabled"] = exchange_enabled
        __props__.__dict__["log_analytics_workspace_id"] = log_analytics_workspace_id
        __props__.__dict__["name"] = name
        __props__.__dict__["sharepoint_enabled"] = sharepoint_enabled
        __props__.__dict__["teams_enabled"] = teams_enabled
        __props__.__dict__["tenant_id"] = tenant_id
        return DataConnectorOffice365(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="exchangeEnabled")
    def exchange_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Should the Exchange data connector be enabled? Defaults to `true`.
        """
        return pulumi.get(self, "exchange_enabled")

    @property
    @pulumi.getter(name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> pulumi.Output[str]:
        """
        The ID of the Log Analytics Workspace that this Office 365 Data Connector resides in. Changing this forces a new Office 365 Data Connector to be created.
        """
        return pulumi.get(self, "log_analytics_workspace_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Office 365 Data Connector. Changing this forces a new Office 365 Data Connector to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sharepointEnabled")
    def sharepoint_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Should the SharePoint data connector be enabled? Defaults to `true`.
        """
        return pulumi.get(self, "sharepoint_enabled")

    @property
    @pulumi.getter(name="teamsEnabled")
    def teams_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Should the Microsoft Teams data connector be enabled? Defaults to `true`.

        > **NOTE:** At least one of `exchange_enabled`, `sharedpoint_enabled` and `teams_enabled` has to be specified.
        """
        return pulumi.get(self, "teams_enabled")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The ID of the Tenant that this Office 365 Data Connector connects to. Changing this forces a new Office 365 Data Connector to be created.

        > **NOTE** Currently, only the same tenant as the running account is allowed. Cross-tenant scenario is not supported yet.
        """
        return pulumi.get(self, "tenant_id")


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ApiKeyArgs', 'ApiKey']

@pulumi.input_type
class ApiKeyArgs:
    def __init__(__self__, *,
                 application_insights_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 read_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 write_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ApiKey resource.
        :param pulumi.Input[str] application_insights_id: The ID of the Application Insights component on which the API key operates. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Application Insights API key. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] read_permissions: Specifies the list of read permissions granted to the API key. Valid values are `agentconfig`, `aggregate`, `api`, `draft`, `extendqueries`, `search`. Please note these values are case sensitive. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] write_permissions: Specifies the list of write permissions granted to the API key. Valid values are `annotations`. Please note these values are case sensitive. Changing this forces a new resource to be created.
               
               > **Note:** At least one read or write permission must be defined.
        """
        ApiKeyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            application_insights_id=application_insights_id,
            name=name,
            read_permissions=read_permissions,
            write_permissions=write_permissions,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             application_insights_id: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             read_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             write_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'applicationInsightsId' in kwargs:
            application_insights_id = kwargs['applicationInsightsId']
        if 'readPermissions' in kwargs:
            read_permissions = kwargs['readPermissions']
        if 'writePermissions' in kwargs:
            write_permissions = kwargs['writePermissions']

        _setter("application_insights_id", application_insights_id)
        if name is not None:
            _setter("name", name)
        if read_permissions is not None:
            _setter("read_permissions", read_permissions)
        if write_permissions is not None:
            _setter("write_permissions", write_permissions)

    @property
    @pulumi.getter(name="applicationInsightsId")
    def application_insights_id(self) -> pulumi.Input[str]:
        """
        The ID of the Application Insights component on which the API key operates. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "application_insights_id")

    @application_insights_id.setter
    def application_insights_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_insights_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Application Insights API key. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="readPermissions")
    def read_permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies the list of read permissions granted to the API key. Valid values are `agentconfig`, `aggregate`, `api`, `draft`, `extendqueries`, `search`. Please note these values are case sensitive. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "read_permissions")

    @read_permissions.setter
    def read_permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "read_permissions", value)

    @property
    @pulumi.getter(name="writePermissions")
    def write_permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies the list of write permissions granted to the API key. Valid values are `annotations`. Please note these values are case sensitive. Changing this forces a new resource to be created.

        > **Note:** At least one read or write permission must be defined.
        """
        return pulumi.get(self, "write_permissions")

    @write_permissions.setter
    def write_permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "write_permissions", value)


@pulumi.input_type
class _ApiKeyState:
    def __init__(__self__, *,
                 api_key: Optional[pulumi.Input[str]] = None,
                 application_insights_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 read_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 write_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering ApiKey resources.
        :param pulumi.Input[str] api_key: The API Key secret (Sensitive).
        :param pulumi.Input[str] application_insights_id: The ID of the Application Insights component on which the API key operates. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Application Insights API key. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] read_permissions: Specifies the list of read permissions granted to the API key. Valid values are `agentconfig`, `aggregate`, `api`, `draft`, `extendqueries`, `search`. Please note these values are case sensitive. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] write_permissions: Specifies the list of write permissions granted to the API key. Valid values are `annotations`. Please note these values are case sensitive. Changing this forces a new resource to be created.
               
               > **Note:** At least one read or write permission must be defined.
        """
        _ApiKeyState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            api_key=api_key,
            application_insights_id=application_insights_id,
            name=name,
            read_permissions=read_permissions,
            write_permissions=write_permissions,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             api_key: Optional[pulumi.Input[str]] = None,
             application_insights_id: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             read_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             write_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'apiKey' in kwargs:
            api_key = kwargs['apiKey']
        if 'applicationInsightsId' in kwargs:
            application_insights_id = kwargs['applicationInsightsId']
        if 'readPermissions' in kwargs:
            read_permissions = kwargs['readPermissions']
        if 'writePermissions' in kwargs:
            write_permissions = kwargs['writePermissions']

        if api_key is not None:
            _setter("api_key", api_key)
        if application_insights_id is not None:
            _setter("application_insights_id", application_insights_id)
        if name is not None:
            _setter("name", name)
        if read_permissions is not None:
            _setter("read_permissions", read_permissions)
        if write_permissions is not None:
            _setter("write_permissions", write_permissions)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        The API Key secret (Sensitive).
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="applicationInsightsId")
    def application_insights_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Application Insights component on which the API key operates. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "application_insights_id")

    @application_insights_id.setter
    def application_insights_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_insights_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Application Insights API key. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="readPermissions")
    def read_permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies the list of read permissions granted to the API key. Valid values are `agentconfig`, `aggregate`, `api`, `draft`, `extendqueries`, `search`. Please note these values are case sensitive. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "read_permissions")

    @read_permissions.setter
    def read_permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "read_permissions", value)

    @property
    @pulumi.getter(name="writePermissions")
    def write_permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies the list of write permissions granted to the API key. Valid values are `annotations`. Please note these values are case sensitive. Changing this forces a new resource to be created.

        > **Note:** At least one read or write permission must be defined.
        """
        return pulumi.get(self, "write_permissions")

    @write_permissions.setter
    def write_permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "write_permissions", value)


class ApiKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_insights_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 read_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 write_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages an Application Insights API key.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_insights = azure.appinsights.Insights("exampleInsights",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            application_type="web")
        read_telemetry = azure.appinsights.ApiKey("readTelemetry",
            application_insights_id=example_insights.id,
            read_permissions=[
                "aggregate",
                "api",
                "draft",
                "extendqueries",
                "search",
            ])
        write_annotations = azure.appinsights.ApiKey("writeAnnotations",
            application_insights_id=example_insights.id,
            write_permissions=["annotations"])
        authenticate_sdk_control_channel_api_key = azure.appinsights.ApiKey("authenticateSdkControlChannelApiKey",
            application_insights_id=example_insights.id,
            read_permissions=["agentconfig"])
        full_permissions = azure.appinsights.ApiKey("fullPermissions",
            application_insights_id=example_insights.id,
            read_permissions=[
                "agentconfig",
                "aggregate",
                "api",
                "draft",
                "extendqueries",
                "search",
            ],
            write_permissions=["annotations"])
        pulumi.export("readTelemetryApiKey", read_telemetry.api_key)
        pulumi.export("writeAnnotationsApiKey", write_annotations.api_key)
        pulumi.export("authenticateSdkControlChannel", authenticate_sdk_control_channel_api_key.api_key)
        pulumi.export("fullPermissionsApiKey", full_permissions.api_key)
        ```

        ## Import

        Application Insights API keys can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appinsights/apiKey:ApiKey my_key /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Insights/components/instance1/apiKeys/00000000-0000-0000-0000-000000000000
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_insights_id: The ID of the Application Insights component on which the API key operates. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Application Insights API key. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] read_permissions: Specifies the list of read permissions granted to the API key. Valid values are `agentconfig`, `aggregate`, `api`, `draft`, `extendqueries`, `search`. Please note these values are case sensitive. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] write_permissions: Specifies the list of write permissions granted to the API key. Valid values are `annotations`. Please note these values are case sensitive. Changing this forces a new resource to be created.
               
               > **Note:** At least one read or write permission must be defined.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApiKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Application Insights API key.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_insights = azure.appinsights.Insights("exampleInsights",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            application_type="web")
        read_telemetry = azure.appinsights.ApiKey("readTelemetry",
            application_insights_id=example_insights.id,
            read_permissions=[
                "aggregate",
                "api",
                "draft",
                "extendqueries",
                "search",
            ])
        write_annotations = azure.appinsights.ApiKey("writeAnnotations",
            application_insights_id=example_insights.id,
            write_permissions=["annotations"])
        authenticate_sdk_control_channel_api_key = azure.appinsights.ApiKey("authenticateSdkControlChannelApiKey",
            application_insights_id=example_insights.id,
            read_permissions=["agentconfig"])
        full_permissions = azure.appinsights.ApiKey("fullPermissions",
            application_insights_id=example_insights.id,
            read_permissions=[
                "agentconfig",
                "aggregate",
                "api",
                "draft",
                "extendqueries",
                "search",
            ],
            write_permissions=["annotations"])
        pulumi.export("readTelemetryApiKey", read_telemetry.api_key)
        pulumi.export("writeAnnotationsApiKey", write_annotations.api_key)
        pulumi.export("authenticateSdkControlChannel", authenticate_sdk_control_channel_api_key.api_key)
        pulumi.export("fullPermissionsApiKey", full_permissions.api_key)
        ```

        ## Import

        Application Insights API keys can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appinsights/apiKey:ApiKey my_key /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Insights/components/instance1/apiKeys/00000000-0000-0000-0000-000000000000
        ```

        :param str resource_name: The name of the resource.
        :param ApiKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ApiKeyArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_insights_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 read_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 write_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApiKeyArgs.__new__(ApiKeyArgs)

            if application_insights_id is None and not opts.urn:
                raise TypeError("Missing required property 'application_insights_id'")
            __props__.__dict__["application_insights_id"] = application_insights_id
            __props__.__dict__["name"] = name
            __props__.__dict__["read_permissions"] = read_permissions
            __props__.__dict__["write_permissions"] = write_permissions
            __props__.__dict__["api_key"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["apiKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(ApiKey, __self__).__init__(
            'azure:appinsights/apiKey:ApiKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_key: Optional[pulumi.Input[str]] = None,
            application_insights_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            read_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            write_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'ApiKey':
        """
        Get an existing ApiKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: The API Key secret (Sensitive).
        :param pulumi.Input[str] application_insights_id: The ID of the Application Insights component on which the API key operates. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Application Insights API key. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] read_permissions: Specifies the list of read permissions granted to the API key. Valid values are `agentconfig`, `aggregate`, `api`, `draft`, `extendqueries`, `search`. Please note these values are case sensitive. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] write_permissions: Specifies the list of write permissions granted to the API key. Valid values are `annotations`. Please note these values are case sensitive. Changing this forces a new resource to be created.
               
               > **Note:** At least one read or write permission must be defined.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ApiKeyState.__new__(_ApiKeyState)

        __props__.__dict__["api_key"] = api_key
        __props__.__dict__["application_insights_id"] = application_insights_id
        __props__.__dict__["name"] = name
        __props__.__dict__["read_permissions"] = read_permissions
        __props__.__dict__["write_permissions"] = write_permissions
        return ApiKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[str]:
        """
        The API Key secret (Sensitive).
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="applicationInsightsId")
    def application_insights_id(self) -> pulumi.Output[str]:
        """
        The ID of the Application Insights component on which the API key operates. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "application_insights_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Application Insights API key. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="readPermissions")
    def read_permissions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Specifies the list of read permissions granted to the API key. Valid values are `agentconfig`, `aggregate`, `api`, `draft`, `extendqueries`, `search`. Please note these values are case sensitive. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "read_permissions")

    @property
    @pulumi.getter(name="writePermissions")
    def write_permissions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Specifies the list of write permissions granted to the API key. Valid values are `annotations`. Please note these values are case sensitive. Changing this forces a new resource to be created.

        > **Note:** At least one read or write permission must be defined.
        """
        return pulumi.get(self, "write_permissions")


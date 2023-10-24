# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AnalyticsItemArgs', 'AnalyticsItem']

@pulumi.input_type
class AnalyticsItemArgs:
    def __init__(__self__, *,
                 application_insights_id: pulumi.Input[str],
                 content: pulumi.Input[str],
                 scope: pulumi.Input[str],
                 type: pulumi.Input[str],
                 function_alias: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AnalyticsItem resource.
        :param pulumi.Input[str] application_insights_id: The ID of the Application Insights component on which the Analytics Item exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] content: The content for the Analytics Item, for example the query text if `type` is `query`.
        :param pulumi.Input[str] scope: The scope for the Analytics Item. Can be `shared` or `user`. Changing this forces a new resource to be created. Must be `shared` for functions.
        :param pulumi.Input[str] type: The type of Analytics Item to create. Can be one of `query`, `function`, `folder`, `recent`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] function_alias: The alias to use for the function. Required when `type` is `function`.
        :param pulumi.Input[str] name: Specifies the name of the Application Insights Analytics Item. Changing this forces a new resource to be created.
        """
        AnalyticsItemArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            application_insights_id=application_insights_id,
            content=content,
            scope=scope,
            type=type,
            function_alias=function_alias,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             application_insights_id: pulumi.Input[str],
             content: pulumi.Input[str],
             scope: pulumi.Input[str],
             type: pulumi.Input[str],
             function_alias: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'applicationInsightsId' in kwargs:
            application_insights_id = kwargs['applicationInsightsId']
        if 'functionAlias' in kwargs:
            function_alias = kwargs['functionAlias']

        _setter("application_insights_id", application_insights_id)
        _setter("content", content)
        _setter("scope", scope)
        _setter("type", type)
        if function_alias is not None:
            _setter("function_alias", function_alias)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="applicationInsightsId")
    def application_insights_id(self) -> pulumi.Input[str]:
        """
        The ID of the Application Insights component on which the Analytics Item exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "application_insights_id")

    @application_insights_id.setter
    def application_insights_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_insights_id", value)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[str]:
        """
        The content for the Analytics Item, for example the query text if `type` is `query`.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        The scope for the Analytics Item. Can be `shared` or `user`. Changing this forces a new resource to be created. Must be `shared` for functions.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of Analytics Item to create. Can be one of `query`, `function`, `folder`, `recent`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="functionAlias")
    def function_alias(self) -> Optional[pulumi.Input[str]]:
        """
        The alias to use for the function. Required when `type` is `function`.
        """
        return pulumi.get(self, "function_alias")

    @function_alias.setter
    def function_alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "function_alias", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Application Insights Analytics Item. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _AnalyticsItemState:
    def __init__(__self__, *,
                 application_insights_id: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 function_alias: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_modified: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AnalyticsItem resources.
        :param pulumi.Input[str] application_insights_id: The ID of the Application Insights component on which the Analytics Item exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] content: The content for the Analytics Item, for example the query text if `type` is `query`.
        :param pulumi.Input[str] function_alias: The alias to use for the function. Required when `type` is `function`.
        :param pulumi.Input[str] name: Specifies the name of the Application Insights Analytics Item. Changing this forces a new resource to be created.
        :param pulumi.Input[str] scope: The scope for the Analytics Item. Can be `shared` or `user`. Changing this forces a new resource to be created. Must be `shared` for functions.
        :param pulumi.Input[str] time_created: A string containing the time the Analytics Item was created.
        :param pulumi.Input[str] time_modified: A string containing the time the Analytics Item was last modified.
        :param pulumi.Input[str] type: The type of Analytics Item to create. Can be one of `query`, `function`, `folder`, `recent`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] version: A string indicating the version of the query format
        """
        _AnalyticsItemState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            application_insights_id=application_insights_id,
            content=content,
            function_alias=function_alias,
            name=name,
            scope=scope,
            time_created=time_created,
            time_modified=time_modified,
            type=type,
            version=version,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             application_insights_id: Optional[pulumi.Input[str]] = None,
             content: Optional[pulumi.Input[str]] = None,
             function_alias: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             scope: Optional[pulumi.Input[str]] = None,
             time_created: Optional[pulumi.Input[str]] = None,
             time_modified: Optional[pulumi.Input[str]] = None,
             type: Optional[pulumi.Input[str]] = None,
             version: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'applicationInsightsId' in kwargs:
            application_insights_id = kwargs['applicationInsightsId']
        if 'functionAlias' in kwargs:
            function_alias = kwargs['functionAlias']
        if 'timeCreated' in kwargs:
            time_created = kwargs['timeCreated']
        if 'timeModified' in kwargs:
            time_modified = kwargs['timeModified']

        if application_insights_id is not None:
            _setter("application_insights_id", application_insights_id)
        if content is not None:
            _setter("content", content)
        if function_alias is not None:
            _setter("function_alias", function_alias)
        if name is not None:
            _setter("name", name)
        if scope is not None:
            _setter("scope", scope)
        if time_created is not None:
            _setter("time_created", time_created)
        if time_modified is not None:
            _setter("time_modified", time_modified)
        if type is not None:
            _setter("type", type)
        if version is not None:
            _setter("version", version)

    @property
    @pulumi.getter(name="applicationInsightsId")
    def application_insights_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Application Insights component on which the Analytics Item exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "application_insights_id")

    @application_insights_id.setter
    def application_insights_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_insights_id", value)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[str]]:
        """
        The content for the Analytics Item, for example the query text if `type` is `query`.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="functionAlias")
    def function_alias(self) -> Optional[pulumi.Input[str]]:
        """
        The alias to use for the function. Required when `type` is `function`.
        """
        return pulumi.get(self, "function_alias")

    @function_alias.setter
    def function_alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "function_alias", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Application Insights Analytics Item. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        The scope for the Analytics Item. Can be `shared` or `user`. Changing this forces a new resource to be created. Must be `shared` for functions.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        A string containing the time the Analytics Item was created.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeModified")
    def time_modified(self) -> Optional[pulumi.Input[str]]:
        """
        A string containing the time the Analytics Item was last modified.
        """
        return pulumi.get(self, "time_modified")

    @time_modified.setter
    def time_modified(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_modified", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of Analytics Item to create. Can be one of `query`, `function`, `folder`, `recent`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        A string indicating the version of the query format
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class AnalyticsItem(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_insights_id: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 function_alias: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an Application Insights Analytics Item component.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_insights = azure.appinsights.Insights("exampleInsights",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            application_type="web")
        example_analytics_item = azure.appinsights.AnalyticsItem("exampleAnalyticsItem",
            application_insights_id=example_insights.id,
            content="requests //simple example query",
            scope="shared",
            type="query")
        ```

        ## Import

        Application Insights Analytics Items can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appinsights/analyticsItem:AnalyticsItem example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Insights/components/mycomponent1/analyticsItems/11111111-1111-1111-1111-111111111111
        ```

         To find the Analytics Item ID you can query the REST API using the [`az rest` CLI command](https://docs.microsoft.com/cli/azure/reference-index?view=azure-cli-latest#az-rest), e.g. az rest --method GET --uri "https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/microsoft.insights/components/appinsightstest/analyticsItems?api-version=2015-05-01"

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_insights_id: The ID of the Application Insights component on which the Analytics Item exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] content: The content for the Analytics Item, for example the query text if `type` is `query`.
        :param pulumi.Input[str] function_alias: The alias to use for the function. Required when `type` is `function`.
        :param pulumi.Input[str] name: Specifies the name of the Application Insights Analytics Item. Changing this forces a new resource to be created.
        :param pulumi.Input[str] scope: The scope for the Analytics Item. Can be `shared` or `user`. Changing this forces a new resource to be created. Must be `shared` for functions.
        :param pulumi.Input[str] type: The type of Analytics Item to create. Can be one of `query`, `function`, `folder`, `recent`. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AnalyticsItemArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Application Insights Analytics Item component.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_insights = azure.appinsights.Insights("exampleInsights",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            application_type="web")
        example_analytics_item = azure.appinsights.AnalyticsItem("exampleAnalyticsItem",
            application_insights_id=example_insights.id,
            content="requests //simple example query",
            scope="shared",
            type="query")
        ```

        ## Import

        Application Insights Analytics Items can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appinsights/analyticsItem:AnalyticsItem example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Insights/components/mycomponent1/analyticsItems/11111111-1111-1111-1111-111111111111
        ```

         To find the Analytics Item ID you can query the REST API using the [`az rest` CLI command](https://docs.microsoft.com/cli/azure/reference-index?view=azure-cli-latest#az-rest), e.g. az rest --method GET --uri "https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/microsoft.insights/components/appinsightstest/analyticsItems?api-version=2015-05-01"

        :param str resource_name: The name of the resource.
        :param AnalyticsItemArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AnalyticsItemArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AnalyticsItemArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_insights_id: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 function_alias: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AnalyticsItemArgs.__new__(AnalyticsItemArgs)

            if application_insights_id is None and not opts.urn:
                raise TypeError("Missing required property 'application_insights_id'")
            __props__.__dict__["application_insights_id"] = application_insights_id
            if content is None and not opts.urn:
                raise TypeError("Missing required property 'content'")
            __props__.__dict__["content"] = content
            __props__.__dict__["function_alias"] = function_alias
            __props__.__dict__["name"] = name
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_modified"] = None
            __props__.__dict__["version"] = None
        super(AnalyticsItem, __self__).__init__(
            'azure:appinsights/analyticsItem:AnalyticsItem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            application_insights_id: Optional[pulumi.Input[str]] = None,
            content: Optional[pulumi.Input[str]] = None,
            function_alias: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            scope: Optional[pulumi.Input[str]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_modified: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'AnalyticsItem':
        """
        Get an existing AnalyticsItem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_insights_id: The ID of the Application Insights component on which the Analytics Item exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] content: The content for the Analytics Item, for example the query text if `type` is `query`.
        :param pulumi.Input[str] function_alias: The alias to use for the function. Required when `type` is `function`.
        :param pulumi.Input[str] name: Specifies the name of the Application Insights Analytics Item. Changing this forces a new resource to be created.
        :param pulumi.Input[str] scope: The scope for the Analytics Item. Can be `shared` or `user`. Changing this forces a new resource to be created. Must be `shared` for functions.
        :param pulumi.Input[str] time_created: A string containing the time the Analytics Item was created.
        :param pulumi.Input[str] time_modified: A string containing the time the Analytics Item was last modified.
        :param pulumi.Input[str] type: The type of Analytics Item to create. Can be one of `query`, `function`, `folder`, `recent`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] version: A string indicating the version of the query format
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AnalyticsItemState.__new__(_AnalyticsItemState)

        __props__.__dict__["application_insights_id"] = application_insights_id
        __props__.__dict__["content"] = content
        __props__.__dict__["function_alias"] = function_alias
        __props__.__dict__["name"] = name
        __props__.__dict__["scope"] = scope
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_modified"] = time_modified
        __props__.__dict__["type"] = type
        __props__.__dict__["version"] = version
        return AnalyticsItem(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationInsightsId")
    def application_insights_id(self) -> pulumi.Output[str]:
        """
        The ID of the Application Insights component on which the Analytics Item exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "application_insights_id")

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[str]:
        """
        The content for the Analytics Item, for example the query text if `type` is `query`.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="functionAlias")
    def function_alias(self) -> pulumi.Output[Optional[str]]:
        """
        The alias to use for the function. Required when `type` is `function`.
        """
        return pulumi.get(self, "function_alias")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Application Insights Analytics Item. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[str]:
        """
        The scope for the Analytics Item. Can be `shared` or `user`. Changing this forces a new resource to be created. Must be `shared` for functions.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        A string containing the time the Analytics Item was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeModified")
    def time_modified(self) -> pulumi.Output[str]:
        """
        A string containing the time the Analytics Item was last modified.
        """
        return pulumi.get(self, "time_modified")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of Analytics Item to create. Can be one of `query`, `function`, `folder`, `recent`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        A string indicating the version of the query format
        """
        return pulumi.get(self, "version")


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['AnalyticsSolutionArgs', 'AnalyticsSolution']

@pulumi.input_type
class AnalyticsSolutionArgs:
    def __init__(__self__, *,
                 plan: pulumi.Input['AnalyticsSolutionPlanArgs'],
                 resource_group_name: pulumi.Input[str],
                 solution_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 workspace_resource_id: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AnalyticsSolution resource.
        :param pulumi.Input['AnalyticsSolutionPlanArgs'] plan: A `plan` block as documented below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and its related workspace can only exist in the same resource group.
        :param pulumi.Input[str] solution_name: Specifies the name of the solution to be deployed. See [here for options](https://docs.microsoft.com/azure/log-analytics/log-analytics-add-solutions).Changing this forces a new resource to be created.
        :param pulumi.Input[str] workspace_name: The full name of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.
        :param pulumi.Input[str] workspace_resource_id: The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        AnalyticsSolutionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            plan=plan,
            resource_group_name=resource_group_name,
            solution_name=solution_name,
            workspace_name=workspace_name,
            workspace_resource_id=workspace_resource_id,
            location=location,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             plan: pulumi.Input['AnalyticsSolutionPlanArgs'],
             resource_group_name: pulumi.Input[str],
             solution_name: pulumi.Input[str],
             workspace_name: pulumi.Input[str],
             workspace_resource_id: pulumi.Input[str],
             location: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'solutionName' in kwargs:
            solution_name = kwargs['solutionName']
        if 'workspaceName' in kwargs:
            workspace_name = kwargs['workspaceName']
        if 'workspaceResourceId' in kwargs:
            workspace_resource_id = kwargs['workspaceResourceId']

        _setter("plan", plan)
        _setter("resource_group_name", resource_group_name)
        _setter("solution_name", solution_name)
        _setter("workspace_name", workspace_name)
        _setter("workspace_resource_id", workspace_resource_id)
        if location is not None:
            _setter("location", location)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Input['AnalyticsSolutionPlanArgs']:
        """
        A `plan` block as documented below.
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: pulumi.Input['AnalyticsSolutionPlanArgs']):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and its related workspace can only exist in the same resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="solutionName")
    def solution_name(self) -> pulumi.Input[str]:
        """
        Specifies the name of the solution to be deployed. See [here for options](https://docs.microsoft.com/azure/log-analytics/log-analytics-add-solutions).Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "solution_name")

    @solution_name.setter
    def solution_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "solution_name", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The full name of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> pulumi.Input[str]:
        """
        The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "workspace_resource_id")

    @workspace_resource_id.setter
    def workspace_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_resource_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _AnalyticsSolutionState:
    def __init__(__self__, *,
                 location: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input['AnalyticsSolutionPlanArgs']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 solution_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 workspace_resource_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AnalyticsSolution resources.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input['AnalyticsSolutionPlanArgs'] plan: A `plan` block as documented below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and its related workspace can only exist in the same resource group.
        :param pulumi.Input[str] solution_name: Specifies the name of the solution to be deployed. See [here for options](https://docs.microsoft.com/azure/log-analytics/log-analytics-add-solutions).Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] workspace_name: The full name of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.
        :param pulumi.Input[str] workspace_resource_id: The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.
        """
        _AnalyticsSolutionState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            location=location,
            plan=plan,
            resource_group_name=resource_group_name,
            solution_name=solution_name,
            tags=tags,
            workspace_name=workspace_name,
            workspace_resource_id=workspace_resource_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             location: Optional[pulumi.Input[str]] = None,
             plan: Optional[pulumi.Input['AnalyticsSolutionPlanArgs']] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             solution_name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             workspace_name: Optional[pulumi.Input[str]] = None,
             workspace_resource_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'solutionName' in kwargs:
            solution_name = kwargs['solutionName']
        if 'workspaceName' in kwargs:
            workspace_name = kwargs['workspaceName']
        if 'workspaceResourceId' in kwargs:
            workspace_resource_id = kwargs['workspaceResourceId']

        if location is not None:
            _setter("location", location)
        if plan is not None:
            _setter("plan", plan)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if solution_name is not None:
            _setter("solution_name", solution_name)
        if tags is not None:
            _setter("tags", tags)
        if workspace_name is not None:
            _setter("workspace_name", workspace_name)
        if workspace_resource_id is not None:
            _setter("workspace_resource_id", workspace_resource_id)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input['AnalyticsSolutionPlanArgs']]:
        """
        A `plan` block as documented below.
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input['AnalyticsSolutionPlanArgs']]):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and its related workspace can only exist in the same resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="solutionName")
    def solution_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the solution to be deployed. See [here for options](https://docs.microsoft.com/azure/log-analytics/log-analytics-add-solutions).Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "solution_name")

    @solution_name.setter
    def solution_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "solution_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> Optional[pulumi.Input[str]]:
        """
        The full name of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "workspace_resource_id")

    @workspace_resource_id.setter
    def workspace_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_resource_id", value)


class AnalyticsSolution(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[pulumi.InputType['AnalyticsSolutionPlanArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 solution_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 workspace_resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Log Analytics (formally Operational Insights) Solution.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_random as random

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        workspace = random.RandomId("workspace",
            keepers={
                "group_name": example_resource_group.name,
            },
            byte_length=8)
        example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="PerGB2018")
        example_analytics_solution = azure.operationalinsights.AnalyticsSolution("exampleAnalyticsSolution",
            solution_name="ContainerInsights",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            workspace_resource_id=example_analytics_workspace.id,
            workspace_name=example_analytics_workspace.name,
            plan=azure.operationalinsights.AnalyticsSolutionPlanArgs(
                publisher="Microsoft",
                product="OMSGallery/ContainerInsights",
            ))
        ```

        ## Import

        Log Analytics Solutions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:operationalinsights/analyticsSolution:AnalyticsSolution solution1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.OperationsManagement/solutions/solution1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['AnalyticsSolutionPlanArgs']] plan: A `plan` block as documented below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and its related workspace can only exist in the same resource group.
        :param pulumi.Input[str] solution_name: Specifies the name of the solution to be deployed. See [here for options](https://docs.microsoft.com/azure/log-analytics/log-analytics-add-solutions).Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] workspace_name: The full name of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.
        :param pulumi.Input[str] workspace_resource_id: The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AnalyticsSolutionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Log Analytics (formally Operational Insights) Solution.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_random as random

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        workspace = random.RandomId("workspace",
            keepers={
                "group_name": example_resource_group.name,
            },
            byte_length=8)
        example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="PerGB2018")
        example_analytics_solution = azure.operationalinsights.AnalyticsSolution("exampleAnalyticsSolution",
            solution_name="ContainerInsights",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            workspace_resource_id=example_analytics_workspace.id,
            workspace_name=example_analytics_workspace.name,
            plan=azure.operationalinsights.AnalyticsSolutionPlanArgs(
                publisher="Microsoft",
                product="OMSGallery/ContainerInsights",
            ))
        ```

        ## Import

        Log Analytics Solutions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:operationalinsights/analyticsSolution:AnalyticsSolution solution1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.OperationsManagement/solutions/solution1
        ```

        :param str resource_name: The name of the resource.
        :param AnalyticsSolutionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AnalyticsSolutionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AnalyticsSolutionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[pulumi.InputType['AnalyticsSolutionPlanArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 solution_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 workspace_resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AnalyticsSolutionArgs.__new__(AnalyticsSolutionArgs)

            __props__.__dict__["location"] = location
            if plan is not None and not isinstance(plan, AnalyticsSolutionPlanArgs):
                plan = plan or {}
                def _setter(key, value):
                    plan[key] = value
                AnalyticsSolutionPlanArgs._configure(_setter, **plan)
            if plan is None and not opts.urn:
                raise TypeError("Missing required property 'plan'")
            __props__.__dict__["plan"] = plan
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if solution_name is None and not opts.urn:
                raise TypeError("Missing required property 'solution_name'")
            __props__.__dict__["solution_name"] = solution_name
            __props__.__dict__["tags"] = tags
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            if workspace_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_resource_id'")
            __props__.__dict__["workspace_resource_id"] = workspace_resource_id
        super(AnalyticsSolution, __self__).__init__(
            'azure:operationalinsights/analyticsSolution:AnalyticsSolution',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            location: Optional[pulumi.Input[str]] = None,
            plan: Optional[pulumi.Input[pulumi.InputType['AnalyticsSolutionPlanArgs']]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            solution_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            workspace_name: Optional[pulumi.Input[str]] = None,
            workspace_resource_id: Optional[pulumi.Input[str]] = None) -> 'AnalyticsSolution':
        """
        Get an existing AnalyticsSolution resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['AnalyticsSolutionPlanArgs']] plan: A `plan` block as documented below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and its related workspace can only exist in the same resource group.
        :param pulumi.Input[str] solution_name: Specifies the name of the solution to be deployed. See [here for options](https://docs.microsoft.com/azure/log-analytics/log-analytics-add-solutions).Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] workspace_name: The full name of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.
        :param pulumi.Input[str] workspace_resource_id: The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AnalyticsSolutionState.__new__(_AnalyticsSolutionState)

        __props__.__dict__["location"] = location
        __props__.__dict__["plan"] = plan
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["solution_name"] = solution_name
        __props__.__dict__["tags"] = tags
        __props__.__dict__["workspace_name"] = workspace_name
        __props__.__dict__["workspace_resource_id"] = workspace_resource_id
        return AnalyticsSolution(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Output['outputs.AnalyticsSolutionPlan']:
        """
        A `plan` block as documented below.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and its related workspace can only exist in the same resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="solutionName")
    def solution_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the solution to be deployed. See [here for options](https://docs.microsoft.com/azure/log-analytics/log-analytics-add-solutions).Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "solution_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Output[str]:
        """
        The full name of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "workspace_name")

    @property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> pulumi.Output[str]:
        """
        The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "workspace_resource_id")


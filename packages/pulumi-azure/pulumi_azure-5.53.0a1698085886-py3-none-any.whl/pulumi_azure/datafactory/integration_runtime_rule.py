# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['IntegrationRuntimeRuleArgs', 'IntegrationRuntimeRule']

@pulumi.input_type
class IntegrationRuntimeRuleArgs:
    def __init__(__self__, *,
                 data_factory_id: pulumi.Input[str],
                 cleanup_enabled: Optional[pulumi.Input[bool]] = None,
                 compute_type: Optional[pulumi.Input[str]] = None,
                 core_count: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 time_to_live_min: Optional[pulumi.Input[int]] = None,
                 virtual_network_enabled: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a IntegrationRuntimeRule resource.
        :param pulumi.Input[str] data_factory_id: The Data Factory ID in which to associate the Linked Service with. Changing this forces a new resource.
        :param pulumi.Input[bool] cleanup_enabled: Cluster will not be recycled and it will be used in next data flow activity run until TTL (time to live) is reached if this is set as `false`. Default is `true`.
        :param pulumi.Input[str] compute_type: Compute type of the cluster which will execute data flow job. Valid values are `General`, `ComputeOptimized` and `MemoryOptimized`. Defaults to `General`.
        :param pulumi.Input[int] core_count: Core count of the cluster which will execute data flow job. Valid values are `8`, `16`, `32`, `48`, `80`, `144` and `272`. Defaults to `8`.
        :param pulumi.Input[str] description: Integration runtime description.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Use `AutoResolve` to create an auto-resolve integration runtime. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Managed Integration Runtime. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/azure/data-factory/naming-rules) for all restrictions.
        :param pulumi.Input[int] time_to_live_min: Time to live (in minutes) setting of the cluster which will execute data flow job. Defaults to `0`.
        :param pulumi.Input[bool] virtual_network_enabled: Is Integration Runtime compute provisioned within Managed Virtual Network? Changing this forces a new resource to be created.
        """
        IntegrationRuntimeRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            data_factory_id=data_factory_id,
            cleanup_enabled=cleanup_enabled,
            compute_type=compute_type,
            core_count=core_count,
            description=description,
            location=location,
            name=name,
            time_to_live_min=time_to_live_min,
            virtual_network_enabled=virtual_network_enabled,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             data_factory_id: pulumi.Input[str],
             cleanup_enabled: Optional[pulumi.Input[bool]] = None,
             compute_type: Optional[pulumi.Input[str]] = None,
             core_count: Optional[pulumi.Input[int]] = None,
             description: Optional[pulumi.Input[str]] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             time_to_live_min: Optional[pulumi.Input[int]] = None,
             virtual_network_enabled: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'dataFactoryId' in kwargs:
            data_factory_id = kwargs['dataFactoryId']
        if 'cleanupEnabled' in kwargs:
            cleanup_enabled = kwargs['cleanupEnabled']
        if 'computeType' in kwargs:
            compute_type = kwargs['computeType']
        if 'coreCount' in kwargs:
            core_count = kwargs['coreCount']
        if 'timeToLiveMin' in kwargs:
            time_to_live_min = kwargs['timeToLiveMin']
        if 'virtualNetworkEnabled' in kwargs:
            virtual_network_enabled = kwargs['virtualNetworkEnabled']

        _setter("data_factory_id", data_factory_id)
        if cleanup_enabled is not None:
            _setter("cleanup_enabled", cleanup_enabled)
        if compute_type is not None:
            _setter("compute_type", compute_type)
        if core_count is not None:
            _setter("core_count", core_count)
        if description is not None:
            _setter("description", description)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if time_to_live_min is not None:
            _setter("time_to_live_min", time_to_live_min)
        if virtual_network_enabled is not None:
            _setter("virtual_network_enabled", virtual_network_enabled)

    @property
    @pulumi.getter(name="dataFactoryId")
    def data_factory_id(self) -> pulumi.Input[str]:
        """
        The Data Factory ID in which to associate the Linked Service with. Changing this forces a new resource.
        """
        return pulumi.get(self, "data_factory_id")

    @data_factory_id.setter
    def data_factory_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_factory_id", value)

    @property
    @pulumi.getter(name="cleanupEnabled")
    def cleanup_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Cluster will not be recycled and it will be used in next data flow activity run until TTL (time to live) is reached if this is set as `false`. Default is `true`.
        """
        return pulumi.get(self, "cleanup_enabled")

    @cleanup_enabled.setter
    def cleanup_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "cleanup_enabled", value)

    @property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> Optional[pulumi.Input[str]]:
        """
        Compute type of the cluster which will execute data flow job. Valid values are `General`, `ComputeOptimized` and `MemoryOptimized`. Defaults to `General`.
        """
        return pulumi.get(self, "compute_type")

    @compute_type.setter
    def compute_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compute_type", value)

    @property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> Optional[pulumi.Input[int]]:
        """
        Core count of the cluster which will execute data flow job. Valid values are `8`, `16`, `32`, `48`, `80`, `144` and `272`. Defaults to `8`.
        """
        return pulumi.get(self, "core_count")

    @core_count.setter
    def core_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "core_count", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Integration runtime description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the resource exists. Use `AutoResolve` to create an auto-resolve integration runtime. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Managed Integration Runtime. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/azure/data-factory/naming-rules) for all restrictions.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="timeToLiveMin")
    def time_to_live_min(self) -> Optional[pulumi.Input[int]]:
        """
        Time to live (in minutes) setting of the cluster which will execute data flow job. Defaults to `0`.
        """
        return pulumi.get(self, "time_to_live_min")

    @time_to_live_min.setter
    def time_to_live_min(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "time_to_live_min", value)

    @property
    @pulumi.getter(name="virtualNetworkEnabled")
    def virtual_network_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Is Integration Runtime compute provisioned within Managed Virtual Network? Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "virtual_network_enabled")

    @virtual_network_enabled.setter
    def virtual_network_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "virtual_network_enabled", value)


@pulumi.input_type
class _IntegrationRuntimeRuleState:
    def __init__(__self__, *,
                 cleanup_enabled: Optional[pulumi.Input[bool]] = None,
                 compute_type: Optional[pulumi.Input[str]] = None,
                 core_count: Optional[pulumi.Input[int]] = None,
                 data_factory_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 time_to_live_min: Optional[pulumi.Input[int]] = None,
                 virtual_network_enabled: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering IntegrationRuntimeRule resources.
        :param pulumi.Input[bool] cleanup_enabled: Cluster will not be recycled and it will be used in next data flow activity run until TTL (time to live) is reached if this is set as `false`. Default is `true`.
        :param pulumi.Input[str] compute_type: Compute type of the cluster which will execute data flow job. Valid values are `General`, `ComputeOptimized` and `MemoryOptimized`. Defaults to `General`.
        :param pulumi.Input[int] core_count: Core count of the cluster which will execute data flow job. Valid values are `8`, `16`, `32`, `48`, `80`, `144` and `272`. Defaults to `8`.
        :param pulumi.Input[str] data_factory_id: The Data Factory ID in which to associate the Linked Service with. Changing this forces a new resource.
        :param pulumi.Input[str] description: Integration runtime description.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Use `AutoResolve` to create an auto-resolve integration runtime. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Managed Integration Runtime. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/azure/data-factory/naming-rules) for all restrictions.
        :param pulumi.Input[int] time_to_live_min: Time to live (in minutes) setting of the cluster which will execute data flow job. Defaults to `0`.
        :param pulumi.Input[bool] virtual_network_enabled: Is Integration Runtime compute provisioned within Managed Virtual Network? Changing this forces a new resource to be created.
        """
        _IntegrationRuntimeRuleState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cleanup_enabled=cleanup_enabled,
            compute_type=compute_type,
            core_count=core_count,
            data_factory_id=data_factory_id,
            description=description,
            location=location,
            name=name,
            time_to_live_min=time_to_live_min,
            virtual_network_enabled=virtual_network_enabled,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cleanup_enabled: Optional[pulumi.Input[bool]] = None,
             compute_type: Optional[pulumi.Input[str]] = None,
             core_count: Optional[pulumi.Input[int]] = None,
             data_factory_id: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             time_to_live_min: Optional[pulumi.Input[int]] = None,
             virtual_network_enabled: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'cleanupEnabled' in kwargs:
            cleanup_enabled = kwargs['cleanupEnabled']
        if 'computeType' in kwargs:
            compute_type = kwargs['computeType']
        if 'coreCount' in kwargs:
            core_count = kwargs['coreCount']
        if 'dataFactoryId' in kwargs:
            data_factory_id = kwargs['dataFactoryId']
        if 'timeToLiveMin' in kwargs:
            time_to_live_min = kwargs['timeToLiveMin']
        if 'virtualNetworkEnabled' in kwargs:
            virtual_network_enabled = kwargs['virtualNetworkEnabled']

        if cleanup_enabled is not None:
            _setter("cleanup_enabled", cleanup_enabled)
        if compute_type is not None:
            _setter("compute_type", compute_type)
        if core_count is not None:
            _setter("core_count", core_count)
        if data_factory_id is not None:
            _setter("data_factory_id", data_factory_id)
        if description is not None:
            _setter("description", description)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if time_to_live_min is not None:
            _setter("time_to_live_min", time_to_live_min)
        if virtual_network_enabled is not None:
            _setter("virtual_network_enabled", virtual_network_enabled)

    @property
    @pulumi.getter(name="cleanupEnabled")
    def cleanup_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Cluster will not be recycled and it will be used in next data flow activity run until TTL (time to live) is reached if this is set as `false`. Default is `true`.
        """
        return pulumi.get(self, "cleanup_enabled")

    @cleanup_enabled.setter
    def cleanup_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "cleanup_enabled", value)

    @property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> Optional[pulumi.Input[str]]:
        """
        Compute type of the cluster which will execute data flow job. Valid values are `General`, `ComputeOptimized` and `MemoryOptimized`. Defaults to `General`.
        """
        return pulumi.get(self, "compute_type")

    @compute_type.setter
    def compute_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compute_type", value)

    @property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> Optional[pulumi.Input[int]]:
        """
        Core count of the cluster which will execute data flow job. Valid values are `8`, `16`, `32`, `48`, `80`, `144` and `272`. Defaults to `8`.
        """
        return pulumi.get(self, "core_count")

    @core_count.setter
    def core_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "core_count", value)

    @property
    @pulumi.getter(name="dataFactoryId")
    def data_factory_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Data Factory ID in which to associate the Linked Service with. Changing this forces a new resource.
        """
        return pulumi.get(self, "data_factory_id")

    @data_factory_id.setter
    def data_factory_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_factory_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Integration runtime description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the resource exists. Use `AutoResolve` to create an auto-resolve integration runtime. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Managed Integration Runtime. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/azure/data-factory/naming-rules) for all restrictions.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="timeToLiveMin")
    def time_to_live_min(self) -> Optional[pulumi.Input[int]]:
        """
        Time to live (in minutes) setting of the cluster which will execute data flow job. Defaults to `0`.
        """
        return pulumi.get(self, "time_to_live_min")

    @time_to_live_min.setter
    def time_to_live_min(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "time_to_live_min", value)

    @property
    @pulumi.getter(name="virtualNetworkEnabled")
    def virtual_network_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Is Integration Runtime compute provisioned within Managed Virtual Network? Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "virtual_network_enabled")

    @virtual_network_enabled.setter
    def virtual_network_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "virtual_network_enabled", value)


class IntegrationRuntimeRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cleanup_enabled: Optional[pulumi.Input[bool]] = None,
                 compute_type: Optional[pulumi.Input[str]] = None,
                 core_count: Optional[pulumi.Input[int]] = None,
                 data_factory_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 time_to_live_min: Optional[pulumi.Input[int]] = None,
                 virtual_network_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Manages a Data Factory Azure Integration Runtime.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_factory = azure.datafactory.Factory("exampleFactory",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_integration_runtime_rule = azure.datafactory.IntegrationRuntimeRule("exampleIntegrationRuntimeRule",
            data_factory_id=example_factory.id,
            location=example_resource_group.location)
        ```

        ## Import

        Data Factory Azure Integration Runtimes can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:datafactory/integrationRuntimeRule:IntegrationRuntimeRule example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example/providers/Microsoft.DataFactory/factories/example/integrationruntimes/example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] cleanup_enabled: Cluster will not be recycled and it will be used in next data flow activity run until TTL (time to live) is reached if this is set as `false`. Default is `true`.
        :param pulumi.Input[str] compute_type: Compute type of the cluster which will execute data flow job. Valid values are `General`, `ComputeOptimized` and `MemoryOptimized`. Defaults to `General`.
        :param pulumi.Input[int] core_count: Core count of the cluster which will execute data flow job. Valid values are `8`, `16`, `32`, `48`, `80`, `144` and `272`. Defaults to `8`.
        :param pulumi.Input[str] data_factory_id: The Data Factory ID in which to associate the Linked Service with. Changing this forces a new resource.
        :param pulumi.Input[str] description: Integration runtime description.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Use `AutoResolve` to create an auto-resolve integration runtime. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Managed Integration Runtime. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/azure/data-factory/naming-rules) for all restrictions.
        :param pulumi.Input[int] time_to_live_min: Time to live (in minutes) setting of the cluster which will execute data flow job. Defaults to `0`.
        :param pulumi.Input[bool] virtual_network_enabled: Is Integration Runtime compute provisioned within Managed Virtual Network? Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationRuntimeRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Data Factory Azure Integration Runtime.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_factory = azure.datafactory.Factory("exampleFactory",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_integration_runtime_rule = azure.datafactory.IntegrationRuntimeRule("exampleIntegrationRuntimeRule",
            data_factory_id=example_factory.id,
            location=example_resource_group.location)
        ```

        ## Import

        Data Factory Azure Integration Runtimes can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:datafactory/integrationRuntimeRule:IntegrationRuntimeRule example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example/providers/Microsoft.DataFactory/factories/example/integrationruntimes/example
        ```

        :param str resource_name: The name of the resource.
        :param IntegrationRuntimeRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationRuntimeRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            IntegrationRuntimeRuleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cleanup_enabled: Optional[pulumi.Input[bool]] = None,
                 compute_type: Optional[pulumi.Input[str]] = None,
                 core_count: Optional[pulumi.Input[int]] = None,
                 data_factory_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 time_to_live_min: Optional[pulumi.Input[int]] = None,
                 virtual_network_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IntegrationRuntimeRuleArgs.__new__(IntegrationRuntimeRuleArgs)

            __props__.__dict__["cleanup_enabled"] = cleanup_enabled
            __props__.__dict__["compute_type"] = compute_type
            __props__.__dict__["core_count"] = core_count
            if data_factory_id is None and not opts.urn:
                raise TypeError("Missing required property 'data_factory_id'")
            __props__.__dict__["data_factory_id"] = data_factory_id
            __props__.__dict__["description"] = description
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["time_to_live_min"] = time_to_live_min
            __props__.__dict__["virtual_network_enabled"] = virtual_network_enabled
        super(IntegrationRuntimeRule, __self__).__init__(
            'azure:datafactory/integrationRuntimeRule:IntegrationRuntimeRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cleanup_enabled: Optional[pulumi.Input[bool]] = None,
            compute_type: Optional[pulumi.Input[str]] = None,
            core_count: Optional[pulumi.Input[int]] = None,
            data_factory_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            time_to_live_min: Optional[pulumi.Input[int]] = None,
            virtual_network_enabled: Optional[pulumi.Input[bool]] = None) -> 'IntegrationRuntimeRule':
        """
        Get an existing IntegrationRuntimeRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] cleanup_enabled: Cluster will not be recycled and it will be used in next data flow activity run until TTL (time to live) is reached if this is set as `false`. Default is `true`.
        :param pulumi.Input[str] compute_type: Compute type of the cluster which will execute data flow job. Valid values are `General`, `ComputeOptimized` and `MemoryOptimized`. Defaults to `General`.
        :param pulumi.Input[int] core_count: Core count of the cluster which will execute data flow job. Valid values are `8`, `16`, `32`, `48`, `80`, `144` and `272`. Defaults to `8`.
        :param pulumi.Input[str] data_factory_id: The Data Factory ID in which to associate the Linked Service with. Changing this forces a new resource.
        :param pulumi.Input[str] description: Integration runtime description.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Use `AutoResolve` to create an auto-resolve integration runtime. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Managed Integration Runtime. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/azure/data-factory/naming-rules) for all restrictions.
        :param pulumi.Input[int] time_to_live_min: Time to live (in minutes) setting of the cluster which will execute data flow job. Defaults to `0`.
        :param pulumi.Input[bool] virtual_network_enabled: Is Integration Runtime compute provisioned within Managed Virtual Network? Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IntegrationRuntimeRuleState.__new__(_IntegrationRuntimeRuleState)

        __props__.__dict__["cleanup_enabled"] = cleanup_enabled
        __props__.__dict__["compute_type"] = compute_type
        __props__.__dict__["core_count"] = core_count
        __props__.__dict__["data_factory_id"] = data_factory_id
        __props__.__dict__["description"] = description
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["time_to_live_min"] = time_to_live_min
        __props__.__dict__["virtual_network_enabled"] = virtual_network_enabled
        return IntegrationRuntimeRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cleanupEnabled")
    def cleanup_enabled(self) -> pulumi.Output[bool]:
        """
        Cluster will not be recycled and it will be used in next data flow activity run until TTL (time to live) is reached if this is set as `false`. Default is `true`.
        """
        return pulumi.get(self, "cleanup_enabled")

    @property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Output[Optional[str]]:
        """
        Compute type of the cluster which will execute data flow job. Valid values are `General`, `ComputeOptimized` and `MemoryOptimized`. Defaults to `General`.
        """
        return pulumi.get(self, "compute_type")

    @property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> pulumi.Output[Optional[int]]:
        """
        Core count of the cluster which will execute data flow job. Valid values are `8`, `16`, `32`, `48`, `80`, `144` and `272`. Defaults to `8`.
        """
        return pulumi.get(self, "core_count")

    @property
    @pulumi.getter(name="dataFactoryId")
    def data_factory_id(self) -> pulumi.Output[str]:
        """
        The Data Factory ID in which to associate the Linked Service with. Changing this forces a new resource.
        """
        return pulumi.get(self, "data_factory_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Integration runtime description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Use `AutoResolve` to create an auto-resolve integration runtime. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Managed Integration Runtime. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/azure/data-factory/naming-rules) for all restrictions.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="timeToLiveMin")
    def time_to_live_min(self) -> pulumi.Output[Optional[int]]:
        """
        Time to live (in minutes) setting of the cluster which will execute data flow job. Defaults to `0`.
        """
        return pulumi.get(self, "time_to_live_min")

    @property
    @pulumi.getter(name="virtualNetworkEnabled")
    def virtual_network_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Is Integration Runtime compute provisioned within Managed Virtual Network? Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "virtual_network_enabled")


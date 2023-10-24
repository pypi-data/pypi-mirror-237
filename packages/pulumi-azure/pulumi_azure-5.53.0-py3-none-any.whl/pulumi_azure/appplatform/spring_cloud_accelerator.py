# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SpringCloudAcceleratorArgs', 'SpringCloudAccelerator']

@pulumi.input_type
class SpringCloudAcceleratorArgs:
    def __init__(__self__, *,
                 spring_cloud_service_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SpringCloudAccelerator resource.
        :param pulumi.Input[str] spring_cloud_service_id: The ID of the Spring Cloud Service. Changing this forces a new Spring Cloud Accelerator to be created.
        :param pulumi.Input[str] name: The name which should be used for this Spring Cloud Accelerator. Changing this forces a new Spring Cloud Accelerator to be created. The only possible value is `default`.
        """
        SpringCloudAcceleratorArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            spring_cloud_service_id=spring_cloud_service_id,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             spring_cloud_service_id: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'springCloudServiceId' in kwargs:
            spring_cloud_service_id = kwargs['springCloudServiceId']

        _setter("spring_cloud_service_id", spring_cloud_service_id)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="springCloudServiceId")
    def spring_cloud_service_id(self) -> pulumi.Input[str]:
        """
        The ID of the Spring Cloud Service. Changing this forces a new Spring Cloud Accelerator to be created.
        """
        return pulumi.get(self, "spring_cloud_service_id")

    @spring_cloud_service_id.setter
    def spring_cloud_service_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "spring_cloud_service_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Spring Cloud Accelerator. Changing this forces a new Spring Cloud Accelerator to be created. The only possible value is `default`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _SpringCloudAcceleratorState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 spring_cloud_service_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SpringCloudAccelerator resources.
        :param pulumi.Input[str] name: The name which should be used for this Spring Cloud Accelerator. Changing this forces a new Spring Cloud Accelerator to be created. The only possible value is `default`.
        :param pulumi.Input[str] spring_cloud_service_id: The ID of the Spring Cloud Service. Changing this forces a new Spring Cloud Accelerator to be created.
        """
        _SpringCloudAcceleratorState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            spring_cloud_service_id=spring_cloud_service_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             spring_cloud_service_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'springCloudServiceId' in kwargs:
            spring_cloud_service_id = kwargs['springCloudServiceId']

        if name is not None:
            _setter("name", name)
        if spring_cloud_service_id is not None:
            _setter("spring_cloud_service_id", spring_cloud_service_id)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Spring Cloud Accelerator. Changing this forces a new Spring Cloud Accelerator to be created. The only possible value is `default`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="springCloudServiceId")
    def spring_cloud_service_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Spring Cloud Service. Changing this forces a new Spring Cloud Accelerator to be created.
        """
        return pulumi.get(self, "spring_cloud_service_id")

    @spring_cloud_service_id.setter
    def spring_cloud_service_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "spring_cloud_service_id", value)


class SpringCloudAccelerator(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 spring_cloud_service_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        > **NOTE:** This resource is applicable only for Spring Cloud Service with enterprise tier.

        Manages a Spring Cloud Accelerator.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_spring_cloud_service = azure.appplatform.SpringCloudService("exampleSpringCloudService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="E0")
        example_spring_cloud_accelerator = azure.appplatform.SpringCloudAccelerator("exampleSpringCloudAccelerator", spring_cloud_service_id=example_spring_cloud_service.id)
        ```

        ## Import

        Spring Cloud Accelerators can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appplatform/springCloudAccelerator:SpringCloudAccelerator example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resourceGroup1/providers/Microsoft.AppPlatform/Spring/service1/applicationAccelerators/default
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name which should be used for this Spring Cloud Accelerator. Changing this forces a new Spring Cloud Accelerator to be created. The only possible value is `default`.
        :param pulumi.Input[str] spring_cloud_service_id: The ID of the Spring Cloud Service. Changing this forces a new Spring Cloud Accelerator to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SpringCloudAcceleratorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        > **NOTE:** This resource is applicable only for Spring Cloud Service with enterprise tier.

        Manages a Spring Cloud Accelerator.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_spring_cloud_service = azure.appplatform.SpringCloudService("exampleSpringCloudService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="E0")
        example_spring_cloud_accelerator = azure.appplatform.SpringCloudAccelerator("exampleSpringCloudAccelerator", spring_cloud_service_id=example_spring_cloud_service.id)
        ```

        ## Import

        Spring Cloud Accelerators can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appplatform/springCloudAccelerator:SpringCloudAccelerator example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resourceGroup1/providers/Microsoft.AppPlatform/Spring/service1/applicationAccelerators/default
        ```

        :param str resource_name: The name of the resource.
        :param SpringCloudAcceleratorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SpringCloudAcceleratorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SpringCloudAcceleratorArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 spring_cloud_service_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SpringCloudAcceleratorArgs.__new__(SpringCloudAcceleratorArgs)

            __props__.__dict__["name"] = name
            if spring_cloud_service_id is None and not opts.urn:
                raise TypeError("Missing required property 'spring_cloud_service_id'")
            __props__.__dict__["spring_cloud_service_id"] = spring_cloud_service_id
        super(SpringCloudAccelerator, __self__).__init__(
            'azure:appplatform/springCloudAccelerator:SpringCloudAccelerator',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            spring_cloud_service_id: Optional[pulumi.Input[str]] = None) -> 'SpringCloudAccelerator':
        """
        Get an existing SpringCloudAccelerator resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name which should be used for this Spring Cloud Accelerator. Changing this forces a new Spring Cloud Accelerator to be created. The only possible value is `default`.
        :param pulumi.Input[str] spring_cloud_service_id: The ID of the Spring Cloud Service. Changing this forces a new Spring Cloud Accelerator to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SpringCloudAcceleratorState.__new__(_SpringCloudAcceleratorState)

        __props__.__dict__["name"] = name
        __props__.__dict__["spring_cloud_service_id"] = spring_cloud_service_id
        return SpringCloudAccelerator(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Spring Cloud Accelerator. Changing this forces a new Spring Cloud Accelerator to be created. The only possible value is `default`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="springCloudServiceId")
    def spring_cloud_service_id(self) -> pulumi.Output[str]:
        """
        The ID of the Spring Cloud Service. Changing this forces a new Spring Cloud Accelerator to be created.
        """
        return pulumi.get(self, "spring_cloud_service_id")


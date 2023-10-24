# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['GetHostPoolRegistrationInfoArgs', 'GetHostPoolRegistrationInfo']

@pulumi.input_type
class GetHostPoolRegistrationInfoArgs:
    def __init__(__self__, *,
                 expiration_date: pulumi.Input[str],
                 hostpool_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a GetHostPoolRegistrationInfo resource.
        :param pulumi.Input[str] expiration_date: A valid `RFC3339Time` for the expiration of the token..
        :param pulumi.Input[str] hostpool_id: The ID of the Virtual Desktop Host Pool to link the Registration Info to. Changing this forces a new Registration Info resource to be created. Only a single virtual_desktop_host_pool_registration_info resource should be associated with a given hostpool. Assigning multiple resources will produce inconsistent results.
        """
        GetHostPoolRegistrationInfoArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            expiration_date=expiration_date,
            hostpool_id=hostpool_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             expiration_date: pulumi.Input[str],
             hostpool_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'expirationDate' in kwargs:
            expiration_date = kwargs['expirationDate']
        if 'hostpoolId' in kwargs:
            hostpool_id = kwargs['hostpoolId']

        _setter("expiration_date", expiration_date)
        _setter("hostpool_id", hostpool_id)

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> pulumi.Input[str]:
        """
        A valid `RFC3339Time` for the expiration of the token..
        """
        return pulumi.get(self, "expiration_date")

    @expiration_date.setter
    def expiration_date(self, value: pulumi.Input[str]):
        pulumi.set(self, "expiration_date", value)

    @property
    @pulumi.getter(name="hostpoolId")
    def hostpool_id(self) -> pulumi.Input[str]:
        """
        The ID of the Virtual Desktop Host Pool to link the Registration Info to. Changing this forces a new Registration Info resource to be created. Only a single virtual_desktop_host_pool_registration_info resource should be associated with a given hostpool. Assigning multiple resources will produce inconsistent results.
        """
        return pulumi.get(self, "hostpool_id")

    @hostpool_id.setter
    def hostpool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "hostpool_id", value)


@pulumi.input_type
class _GetHostPoolRegistrationInfoState:
    def __init__(__self__, *,
                 expiration_date: Optional[pulumi.Input[str]] = None,
                 hostpool_id: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GetHostPoolRegistrationInfo resources.
        :param pulumi.Input[str] expiration_date: A valid `RFC3339Time` for the expiration of the token..
        :param pulumi.Input[str] hostpool_id: The ID of the Virtual Desktop Host Pool to link the Registration Info to. Changing this forces a new Registration Info resource to be created. Only a single virtual_desktop_host_pool_registration_info resource should be associated with a given hostpool. Assigning multiple resources will produce inconsistent results.
        :param pulumi.Input[str] token: The registration token generated by the Virtual Desktop Host Pool for registration of session hosts.
        """
        _GetHostPoolRegistrationInfoState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            expiration_date=expiration_date,
            hostpool_id=hostpool_id,
            token=token,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             expiration_date: Optional[pulumi.Input[str]] = None,
             hostpool_id: Optional[pulumi.Input[str]] = None,
             token: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'expirationDate' in kwargs:
            expiration_date = kwargs['expirationDate']
        if 'hostpoolId' in kwargs:
            hostpool_id = kwargs['hostpoolId']

        if expiration_date is not None:
            _setter("expiration_date", expiration_date)
        if hostpool_id is not None:
            _setter("hostpool_id", hostpool_id)
        if token is not None:
            _setter("token", token)

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[pulumi.Input[str]]:
        """
        A valid `RFC3339Time` for the expiration of the token..
        """
        return pulumi.get(self, "expiration_date")

    @expiration_date.setter
    def expiration_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_date", value)

    @property
    @pulumi.getter(name="hostpoolId")
    def hostpool_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Virtual Desktop Host Pool to link the Registration Info to. Changing this forces a new Registration Info resource to be created. Only a single virtual_desktop_host_pool_registration_info resource should be associated with a given hostpool. Assigning multiple resources will produce inconsistent results.
        """
        return pulumi.get(self, "hostpool_id")

    @hostpool_id.setter
    def hostpool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostpool_id", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        The registration token generated by the Virtual Desktop Host Pool for registration of session hosts.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)


class GetHostPoolRegistrationInfo(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 expiration_date: Optional[pulumi.Input[str]] = None,
                 hostpool_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages the Registration Info for a Virtual Desktop Host Pool.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="westeurope")
        example_host_pool = azure.desktopvirtualization.HostPool("exampleHostPool",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            type="Pooled",
            validate_environment=True,
            load_balancer_type="BreadthFirst")
        exampleget_host_pool_registration_info = azure.desktopvirtualization.GetHostPoolRegistrationInfo("examplegetHostPoolRegistrationInfo",
            hostpool_id=example_host_pool.id,
            expiration_date="2022-01-01T23:40:52Z")
        ```

        ## Import

        AVD Registration Infos can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:desktopvirtualization/getHostPoolRegistrationInfo:getHostPoolRegistrationInfo example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.DesktopVirtualization/hostPools/pool1/registrationInfo/default
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] expiration_date: A valid `RFC3339Time` for the expiration of the token..
        :param pulumi.Input[str] hostpool_id: The ID of the Virtual Desktop Host Pool to link the Registration Info to. Changing this forces a new Registration Info resource to be created. Only a single virtual_desktop_host_pool_registration_info resource should be associated with a given hostpool. Assigning multiple resources will produce inconsistent results.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GetHostPoolRegistrationInfoArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages the Registration Info for a Virtual Desktop Host Pool.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="westeurope")
        example_host_pool = azure.desktopvirtualization.HostPool("exampleHostPool",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            type="Pooled",
            validate_environment=True,
            load_balancer_type="BreadthFirst")
        exampleget_host_pool_registration_info = azure.desktopvirtualization.GetHostPoolRegistrationInfo("examplegetHostPoolRegistrationInfo",
            hostpool_id=example_host_pool.id,
            expiration_date="2022-01-01T23:40:52Z")
        ```

        ## Import

        AVD Registration Infos can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:desktopvirtualization/getHostPoolRegistrationInfo:getHostPoolRegistrationInfo example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.DesktopVirtualization/hostPools/pool1/registrationInfo/default
        ```

        :param str resource_name: The name of the resource.
        :param GetHostPoolRegistrationInfoArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GetHostPoolRegistrationInfoArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            GetHostPoolRegistrationInfoArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 expiration_date: Optional[pulumi.Input[str]] = None,
                 hostpool_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GetHostPoolRegistrationInfoArgs.__new__(GetHostPoolRegistrationInfoArgs)

            if expiration_date is None and not opts.urn:
                raise TypeError("Missing required property 'expiration_date'")
            __props__.__dict__["expiration_date"] = expiration_date
            if hostpool_id is None and not opts.urn:
                raise TypeError("Missing required property 'hostpool_id'")
            __props__.__dict__["hostpool_id"] = hostpool_id
            __props__.__dict__["token"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["token"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(GetHostPoolRegistrationInfo, __self__).__init__(
            'azure:desktopvirtualization/getHostPoolRegistrationInfo:getHostPoolRegistrationInfo',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            expiration_date: Optional[pulumi.Input[str]] = None,
            hostpool_id: Optional[pulumi.Input[str]] = None,
            token: Optional[pulumi.Input[str]] = None) -> 'GetHostPoolRegistrationInfo':
        """
        Get an existing GetHostPoolRegistrationInfo resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] expiration_date: A valid `RFC3339Time` for the expiration of the token..
        :param pulumi.Input[str] hostpool_id: The ID of the Virtual Desktop Host Pool to link the Registration Info to. Changing this forces a new Registration Info resource to be created. Only a single virtual_desktop_host_pool_registration_info resource should be associated with a given hostpool. Assigning multiple resources will produce inconsistent results.
        :param pulumi.Input[str] token: The registration token generated by the Virtual Desktop Host Pool for registration of session hosts.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GetHostPoolRegistrationInfoState.__new__(_GetHostPoolRegistrationInfoState)

        __props__.__dict__["expiration_date"] = expiration_date
        __props__.__dict__["hostpool_id"] = hostpool_id
        __props__.__dict__["token"] = token
        return GetHostPoolRegistrationInfo(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> pulumi.Output[str]:
        """
        A valid `RFC3339Time` for the expiration of the token..
        """
        return pulumi.get(self, "expiration_date")

    @property
    @pulumi.getter(name="hostpoolId")
    def hostpool_id(self) -> pulumi.Output[str]:
        """
        The ID of the Virtual Desktop Host Pool to link the Registration Info to. Changing this forces a new Registration Info resource to be created. Only a single virtual_desktop_host_pool_registration_info resource should be associated with a given hostpool. Assigning multiple resources will produce inconsistent results.
        """
        return pulumi.get(self, "hostpool_id")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[str]:
        """
        The registration token generated by the Virtual Desktop Host Pool for registration of session hosts.
        """
        return pulumi.get(self, "token")


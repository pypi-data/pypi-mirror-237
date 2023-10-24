# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CustomHostnameBindingArgs', 'CustomHostnameBinding']

@pulumi.input_type
class CustomHostnameBindingArgs:
    def __init__(__self__, *,
                 app_service_name: pulumi.Input[str],
                 hostname: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 ssl_state: Optional[pulumi.Input[str]] = None,
                 thumbprint: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CustomHostnameBinding resource.
        :param pulumi.Input[str] app_service_name: The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.
        :param pulumi.Input[str] hostname: Specifies the Custom Hostname to use for the App Service, example `www.example.com`. Changing this forces a new resource to be created.
               
               > **NOTE:** A CNAME needs to be configured from this Hostname to the Azure Website - otherwise Azure will reject the Hostname Binding.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] ssl_state: The SSL type. Possible values are `IpBasedEnabled` and `SniEnabled`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] thumbprint: The SSL certificate thumbprint. Changing this forces a new resource to be created.
               
               > **NOTE:** `thumbprint` must be specified when `ssl_state` is set.
        """
        CustomHostnameBindingArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            app_service_name=app_service_name,
            hostname=hostname,
            resource_group_name=resource_group_name,
            ssl_state=ssl_state,
            thumbprint=thumbprint,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             app_service_name: pulumi.Input[str],
             hostname: pulumi.Input[str],
             resource_group_name: pulumi.Input[str],
             ssl_state: Optional[pulumi.Input[str]] = None,
             thumbprint: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'appServiceName' in kwargs:
            app_service_name = kwargs['appServiceName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'sslState' in kwargs:
            ssl_state = kwargs['sslState']

        _setter("app_service_name", app_service_name)
        _setter("hostname", hostname)
        _setter("resource_group_name", resource_group_name)
        if ssl_state is not None:
            _setter("ssl_state", ssl_state)
        if thumbprint is not None:
            _setter("thumbprint", thumbprint)

    @property
    @pulumi.getter(name="appServiceName")
    def app_service_name(self) -> pulumi.Input[str]:
        """
        The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "app_service_name")

    @app_service_name.setter
    def app_service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_service_name", value)

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[str]:
        """
        Specifies the Custom Hostname to use for the App Service, example `www.example.com`. Changing this forces a new resource to be created.

        > **NOTE:** A CNAME needs to be configured from this Hostname to the Azure Website - otherwise Azure will reject the Hostname Binding.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: pulumi.Input[str]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="sslState")
    def ssl_state(self) -> Optional[pulumi.Input[str]]:
        """
        The SSL type. Possible values are `IpBasedEnabled` and `SniEnabled`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "ssl_state")

    @ssl_state.setter
    def ssl_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_state", value)

    @property
    @pulumi.getter
    def thumbprint(self) -> Optional[pulumi.Input[str]]:
        """
        The SSL certificate thumbprint. Changing this forces a new resource to be created.

        > **NOTE:** `thumbprint` must be specified when `ssl_state` is set.
        """
        return pulumi.get(self, "thumbprint")

    @thumbprint.setter
    def thumbprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "thumbprint", value)


@pulumi.input_type
class _CustomHostnameBindingState:
    def __init__(__self__, *,
                 app_service_name: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 ssl_state: Optional[pulumi.Input[str]] = None,
                 thumbprint: Optional[pulumi.Input[str]] = None,
                 virtual_ip: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CustomHostnameBinding resources.
        :param pulumi.Input[str] app_service_name: The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.
        :param pulumi.Input[str] hostname: Specifies the Custom Hostname to use for the App Service, example `www.example.com`. Changing this forces a new resource to be created.
               
               > **NOTE:** A CNAME needs to be configured from this Hostname to the Azure Website - otherwise Azure will reject the Hostname Binding.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] ssl_state: The SSL type. Possible values are `IpBasedEnabled` and `SniEnabled`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] thumbprint: The SSL certificate thumbprint. Changing this forces a new resource to be created.
               
               > **NOTE:** `thumbprint` must be specified when `ssl_state` is set.
        :param pulumi.Input[str] virtual_ip: The virtual IP address assigned to the hostname if IP based SSL is enabled.
        """
        _CustomHostnameBindingState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            app_service_name=app_service_name,
            hostname=hostname,
            resource_group_name=resource_group_name,
            ssl_state=ssl_state,
            thumbprint=thumbprint,
            virtual_ip=virtual_ip,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             app_service_name: Optional[pulumi.Input[str]] = None,
             hostname: Optional[pulumi.Input[str]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             ssl_state: Optional[pulumi.Input[str]] = None,
             thumbprint: Optional[pulumi.Input[str]] = None,
             virtual_ip: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'appServiceName' in kwargs:
            app_service_name = kwargs['appServiceName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'sslState' in kwargs:
            ssl_state = kwargs['sslState']
        if 'virtualIp' in kwargs:
            virtual_ip = kwargs['virtualIp']

        if app_service_name is not None:
            _setter("app_service_name", app_service_name)
        if hostname is not None:
            _setter("hostname", hostname)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if ssl_state is not None:
            _setter("ssl_state", ssl_state)
        if thumbprint is not None:
            _setter("thumbprint", thumbprint)
        if virtual_ip is not None:
            _setter("virtual_ip", virtual_ip)

    @property
    @pulumi.getter(name="appServiceName")
    def app_service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "app_service_name")

    @app_service_name.setter
    def app_service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_service_name", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Custom Hostname to use for the App Service, example `www.example.com`. Changing this forces a new resource to be created.

        > **NOTE:** A CNAME needs to be configured from this Hostname to the Azure Website - otherwise Azure will reject the Hostname Binding.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="sslState")
    def ssl_state(self) -> Optional[pulumi.Input[str]]:
        """
        The SSL type. Possible values are `IpBasedEnabled` and `SniEnabled`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "ssl_state")

    @ssl_state.setter
    def ssl_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_state", value)

    @property
    @pulumi.getter
    def thumbprint(self) -> Optional[pulumi.Input[str]]:
        """
        The SSL certificate thumbprint. Changing this forces a new resource to be created.

        > **NOTE:** `thumbprint` must be specified when `ssl_state` is set.
        """
        return pulumi.get(self, "thumbprint")

    @thumbprint.setter
    def thumbprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "thumbprint", value)

    @property
    @pulumi.getter(name="virtualIp")
    def virtual_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The virtual IP address assigned to the hostname if IP based SSL is enabled.
        """
        return pulumi.get(self, "virtual_ip")

    @virtual_ip.setter
    def virtual_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_ip", value)


class CustomHostnameBinding(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_service_name: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 ssl_state: Optional[pulumi.Input[str]] = None,
                 thumbprint: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Hostname Binding within an App Service (or Function App).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_random as random

        server = random.RandomId("server",
            keepers={
                "azi_id": 1,
            },
            byte_length=8)
        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_plan = azure.appservice.Plan("examplePlan",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku=azure.appservice.PlanSkuArgs(
                tier="Standard",
                size="S1",
            ))
        example_app_service = azure.appservice.AppService("exampleAppService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            app_service_plan_id=example_plan.id)
        example_custom_hostname_binding = azure.appservice.CustomHostnameBinding("exampleCustomHostnameBinding",
            hostname="www.mywebsite.com",
            app_service_name=example_app_service.name,
            resource_group_name=example_resource_group.name)
        ```

        ## Import

        App Service Custom Hostname Bindings can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appservice/customHostnameBinding:CustomHostnameBinding mywebsite /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Web/sites/instance1/hostNameBindings/mywebsite.com
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_service_name: The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.
        :param pulumi.Input[str] hostname: Specifies the Custom Hostname to use for the App Service, example `www.example.com`. Changing this forces a new resource to be created.
               
               > **NOTE:** A CNAME needs to be configured from this Hostname to the Azure Website - otherwise Azure will reject the Hostname Binding.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] ssl_state: The SSL type. Possible values are `IpBasedEnabled` and `SniEnabled`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] thumbprint: The SSL certificate thumbprint. Changing this forces a new resource to be created.
               
               > **NOTE:** `thumbprint` must be specified when `ssl_state` is set.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomHostnameBindingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Hostname Binding within an App Service (or Function App).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_random as random

        server = random.RandomId("server",
            keepers={
                "azi_id": 1,
            },
            byte_length=8)
        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_plan = azure.appservice.Plan("examplePlan",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku=azure.appservice.PlanSkuArgs(
                tier="Standard",
                size="S1",
            ))
        example_app_service = azure.appservice.AppService("exampleAppService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            app_service_plan_id=example_plan.id)
        example_custom_hostname_binding = azure.appservice.CustomHostnameBinding("exampleCustomHostnameBinding",
            hostname="www.mywebsite.com",
            app_service_name=example_app_service.name,
            resource_group_name=example_resource_group.name)
        ```

        ## Import

        App Service Custom Hostname Bindings can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appservice/customHostnameBinding:CustomHostnameBinding mywebsite /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Web/sites/instance1/hostNameBindings/mywebsite.com
        ```

        :param str resource_name: The name of the resource.
        :param CustomHostnameBindingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomHostnameBindingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CustomHostnameBindingArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_service_name: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 ssl_state: Optional[pulumi.Input[str]] = None,
                 thumbprint: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomHostnameBindingArgs.__new__(CustomHostnameBindingArgs)

            if app_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'app_service_name'")
            __props__.__dict__["app_service_name"] = app_service_name
            if hostname is None and not opts.urn:
                raise TypeError("Missing required property 'hostname'")
            __props__.__dict__["hostname"] = hostname
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["ssl_state"] = ssl_state
            __props__.__dict__["thumbprint"] = thumbprint
            __props__.__dict__["virtual_ip"] = None
        super(CustomHostnameBinding, __self__).__init__(
            'azure:appservice/customHostnameBinding:CustomHostnameBinding',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_service_name: Optional[pulumi.Input[str]] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            ssl_state: Optional[pulumi.Input[str]] = None,
            thumbprint: Optional[pulumi.Input[str]] = None,
            virtual_ip: Optional[pulumi.Input[str]] = None) -> 'CustomHostnameBinding':
        """
        Get an existing CustomHostnameBinding resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_service_name: The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.
        :param pulumi.Input[str] hostname: Specifies the Custom Hostname to use for the App Service, example `www.example.com`. Changing this forces a new resource to be created.
               
               > **NOTE:** A CNAME needs to be configured from this Hostname to the Azure Website - otherwise Azure will reject the Hostname Binding.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] ssl_state: The SSL type. Possible values are `IpBasedEnabled` and `SniEnabled`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] thumbprint: The SSL certificate thumbprint. Changing this forces a new resource to be created.
               
               > **NOTE:** `thumbprint` must be specified when `ssl_state` is set.
        :param pulumi.Input[str] virtual_ip: The virtual IP address assigned to the hostname if IP based SSL is enabled.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CustomHostnameBindingState.__new__(_CustomHostnameBindingState)

        __props__.__dict__["app_service_name"] = app_service_name
        __props__.__dict__["hostname"] = hostname
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["ssl_state"] = ssl_state
        __props__.__dict__["thumbprint"] = thumbprint
        __props__.__dict__["virtual_ip"] = virtual_ip
        return CustomHostnameBinding(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appServiceName")
    def app_service_name(self) -> pulumi.Output[str]:
        """
        The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "app_service_name")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[str]:
        """
        Specifies the Custom Hostname to use for the App Service, example `www.example.com`. Changing this forces a new resource to be created.

        > **NOTE:** A CNAME needs to be configured from this Hostname to the Azure Website - otherwise Azure will reject the Hostname Binding.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="sslState")
    def ssl_state(self) -> pulumi.Output[str]:
        """
        The SSL type. Possible values are `IpBasedEnabled` and `SniEnabled`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "ssl_state")

    @property
    @pulumi.getter
    def thumbprint(self) -> pulumi.Output[str]:
        """
        The SSL certificate thumbprint. Changing this forces a new resource to be created.

        > **NOTE:** `thumbprint` must be specified when `ssl_state` is set.
        """
        return pulumi.get(self, "thumbprint")

    @property
    @pulumi.getter(name="virtualIp")
    def virtual_ip(self) -> pulumi.Output[str]:
        """
        The virtual IP address assigned to the hostname if IP based SSL is enabled.
        """
        return pulumi.get(self, "virtual_ip")


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['VirtualNetworkRuleArgs', 'VirtualNetworkRule']

@pulumi.input_type
class VirtualNetworkRuleArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 subnet_id: pulumi.Input[str],
                 ignore_missing_vnet_service_endpoint: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VirtualNetworkRule resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the PostgreSQL server resides. Changing this forces a new resource to be created.
        :param pulumi.Input[str] server_name: The name of the SQL Server to which this PostgreSQL virtual network rule will be applied to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subnet_id: The ID of the subnet that the PostgreSQL server will be connected to.
        :param pulumi.Input[bool] ignore_missing_vnet_service_endpoint: Should the Virtual Network Rule be created before the Subnet has the Virtual Network Service Endpoint enabled?
        :param pulumi.Input[str] name: The name of the PostgreSQL virtual network rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.
               
               > **NOTE:** `name` must be between 1-128 characters long and must satisfy all of the requirements below:
               
               1. Contains only alphanumeric and hyphen characters
               2. Cannot start with a number or hyphen
               3. Cannot end with a hyphen
        """
        VirtualNetworkRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            resource_group_name=resource_group_name,
            server_name=server_name,
            subnet_id=subnet_id,
            ignore_missing_vnet_service_endpoint=ignore_missing_vnet_service_endpoint,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             resource_group_name: pulumi.Input[str],
             server_name: pulumi.Input[str],
             subnet_id: pulumi.Input[str],
             ignore_missing_vnet_service_endpoint: Optional[pulumi.Input[bool]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'serverName' in kwargs:
            server_name = kwargs['serverName']
        if 'subnetId' in kwargs:
            subnet_id = kwargs['subnetId']
        if 'ignoreMissingVnetServiceEndpoint' in kwargs:
            ignore_missing_vnet_service_endpoint = kwargs['ignoreMissingVnetServiceEndpoint']

        _setter("resource_group_name", resource_group_name)
        _setter("server_name", server_name)
        _setter("subnet_id", subnet_id)
        if ignore_missing_vnet_service_endpoint is not None:
            _setter("ignore_missing_vnet_service_endpoint", ignore_missing_vnet_service_endpoint)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group where the PostgreSQL server resides. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        The name of the SQL Server to which this PostgreSQL virtual network rule will be applied to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        The ID of the subnet that the PostgreSQL server will be connected to.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter(name="ignoreMissingVnetServiceEndpoint")
    def ignore_missing_vnet_service_endpoint(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the Virtual Network Rule be created before the Subnet has the Virtual Network Service Endpoint enabled?
        """
        return pulumi.get(self, "ignore_missing_vnet_service_endpoint")

    @ignore_missing_vnet_service_endpoint.setter
    def ignore_missing_vnet_service_endpoint(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_missing_vnet_service_endpoint", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the PostgreSQL virtual network rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.

        > **NOTE:** `name` must be between 1-128 characters long and must satisfy all of the requirements below:

        1. Contains only alphanumeric and hyphen characters
        2. Cannot start with a number or hyphen
        3. Cannot end with a hyphen
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _VirtualNetworkRuleState:
    def __init__(__self__, *,
                 ignore_missing_vnet_service_endpoint: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VirtualNetworkRule resources.
        :param pulumi.Input[bool] ignore_missing_vnet_service_endpoint: Should the Virtual Network Rule be created before the Subnet has the Virtual Network Service Endpoint enabled?
        :param pulumi.Input[str] name: The name of the PostgreSQL virtual network rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.
               
               > **NOTE:** `name` must be between 1-128 characters long and must satisfy all of the requirements below:
               
               1. Contains only alphanumeric and hyphen characters
               2. Cannot start with a number or hyphen
               3. Cannot end with a hyphen
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the PostgreSQL server resides. Changing this forces a new resource to be created.
        :param pulumi.Input[str] server_name: The name of the SQL Server to which this PostgreSQL virtual network rule will be applied to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subnet_id: The ID of the subnet that the PostgreSQL server will be connected to.
        """
        _VirtualNetworkRuleState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            ignore_missing_vnet_service_endpoint=ignore_missing_vnet_service_endpoint,
            name=name,
            resource_group_name=resource_group_name,
            server_name=server_name,
            subnet_id=subnet_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             ignore_missing_vnet_service_endpoint: Optional[pulumi.Input[bool]] = None,
             name: Optional[pulumi.Input[str]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             server_name: Optional[pulumi.Input[str]] = None,
             subnet_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'ignoreMissingVnetServiceEndpoint' in kwargs:
            ignore_missing_vnet_service_endpoint = kwargs['ignoreMissingVnetServiceEndpoint']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'serverName' in kwargs:
            server_name = kwargs['serverName']
        if 'subnetId' in kwargs:
            subnet_id = kwargs['subnetId']

        if ignore_missing_vnet_service_endpoint is not None:
            _setter("ignore_missing_vnet_service_endpoint", ignore_missing_vnet_service_endpoint)
        if name is not None:
            _setter("name", name)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if server_name is not None:
            _setter("server_name", server_name)
        if subnet_id is not None:
            _setter("subnet_id", subnet_id)

    @property
    @pulumi.getter(name="ignoreMissingVnetServiceEndpoint")
    def ignore_missing_vnet_service_endpoint(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the Virtual Network Rule be created before the Subnet has the Virtual Network Service Endpoint enabled?
        """
        return pulumi.get(self, "ignore_missing_vnet_service_endpoint")

    @ignore_missing_vnet_service_endpoint.setter
    def ignore_missing_vnet_service_endpoint(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_missing_vnet_service_endpoint", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the PostgreSQL virtual network rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.

        > **NOTE:** `name` must be between 1-128 characters long and must satisfy all of the requirements below:

        1. Contains only alphanumeric and hyphen characters
        2. Cannot start with a number or hyphen
        3. Cannot end with a hyphen
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group where the PostgreSQL server resides. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the SQL Server to which this PostgreSQL virtual network rule will be applied to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the subnet that the PostgreSQL server will be connected to.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_id", value)


class VirtualNetworkRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ignore_missing_vnet_service_endpoint: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a PostgreSQL Virtual Network Rule.

        > **NOTE:** PostgreSQL Virtual Network Rules [can only be used with SKU Tiers of `GeneralPurpose` or `MemoryOptimized`](https://docs.microsoft.com/azure/postgresql/concepts-data-access-and-security-vnet)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            address_spaces=["10.7.29.0/29"],
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        internal = azure.network.Subnet("internal",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.7.29.0/29"],
            service_endpoints=["Microsoft.Sql"])
        example_server = azure.postgresql.Server("exampleServer",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="GP_Gen5_2",
            storage_mb=5120,
            backup_retention_days=7,
            administrator_login="psqladmin",
            administrator_login_password="H@Sh1CoR3!",
            version="9.5",
            ssl_enforcement_enabled=True)
        example_virtual_network_rule = azure.postgresql.VirtualNetworkRule("exampleVirtualNetworkRule",
            resource_group_name=example_resource_group.name,
            server_name=example_server.name,
            subnet_id=internal.id,
            ignore_missing_vnet_service_endpoint=True)
        ```

        ## Import

        PostgreSQL Virtual Network Rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:postgresql/virtualNetworkRule:VirtualNetworkRule rule1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myresourcegroup/providers/Microsoft.DBforPostgreSQL/servers/myserver/virtualNetworkRules/vnetrulename
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] ignore_missing_vnet_service_endpoint: Should the Virtual Network Rule be created before the Subnet has the Virtual Network Service Endpoint enabled?
        :param pulumi.Input[str] name: The name of the PostgreSQL virtual network rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.
               
               > **NOTE:** `name` must be between 1-128 characters long and must satisfy all of the requirements below:
               
               1. Contains only alphanumeric and hyphen characters
               2. Cannot start with a number or hyphen
               3. Cannot end with a hyphen
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the PostgreSQL server resides. Changing this forces a new resource to be created.
        :param pulumi.Input[str] server_name: The name of the SQL Server to which this PostgreSQL virtual network rule will be applied to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subnet_id: The ID of the subnet that the PostgreSQL server will be connected to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualNetworkRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a PostgreSQL Virtual Network Rule.

        > **NOTE:** PostgreSQL Virtual Network Rules [can only be used with SKU Tiers of `GeneralPurpose` or `MemoryOptimized`](https://docs.microsoft.com/azure/postgresql/concepts-data-access-and-security-vnet)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            address_spaces=["10.7.29.0/29"],
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        internal = azure.network.Subnet("internal",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.7.29.0/29"],
            service_endpoints=["Microsoft.Sql"])
        example_server = azure.postgresql.Server("exampleServer",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="GP_Gen5_2",
            storage_mb=5120,
            backup_retention_days=7,
            administrator_login="psqladmin",
            administrator_login_password="H@Sh1CoR3!",
            version="9.5",
            ssl_enforcement_enabled=True)
        example_virtual_network_rule = azure.postgresql.VirtualNetworkRule("exampleVirtualNetworkRule",
            resource_group_name=example_resource_group.name,
            server_name=example_server.name,
            subnet_id=internal.id,
            ignore_missing_vnet_service_endpoint=True)
        ```

        ## Import

        PostgreSQL Virtual Network Rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:postgresql/virtualNetworkRule:VirtualNetworkRule rule1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myresourcegroup/providers/Microsoft.DBforPostgreSQL/servers/myserver/virtualNetworkRules/vnetrulename
        ```

        :param str resource_name: The name of the resource.
        :param VirtualNetworkRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualNetworkRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            VirtualNetworkRuleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ignore_missing_vnet_service_endpoint: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualNetworkRuleArgs.__new__(VirtualNetworkRuleArgs)

            __props__.__dict__["ignore_missing_vnet_service_endpoint"] = ignore_missing_vnet_service_endpoint
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            if subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_id'")
            __props__.__dict__["subnet_id"] = subnet_id
        super(VirtualNetworkRule, __self__).__init__(
            'azure:postgresql/virtualNetworkRule:VirtualNetworkRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            ignore_missing_vnet_service_endpoint: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            server_name: Optional[pulumi.Input[str]] = None,
            subnet_id: Optional[pulumi.Input[str]] = None) -> 'VirtualNetworkRule':
        """
        Get an existing VirtualNetworkRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] ignore_missing_vnet_service_endpoint: Should the Virtual Network Rule be created before the Subnet has the Virtual Network Service Endpoint enabled?
        :param pulumi.Input[str] name: The name of the PostgreSQL virtual network rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.
               
               > **NOTE:** `name` must be between 1-128 characters long and must satisfy all of the requirements below:
               
               1. Contains only alphanumeric and hyphen characters
               2. Cannot start with a number or hyphen
               3. Cannot end with a hyphen
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the PostgreSQL server resides. Changing this forces a new resource to be created.
        :param pulumi.Input[str] server_name: The name of the SQL Server to which this PostgreSQL virtual network rule will be applied to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subnet_id: The ID of the subnet that the PostgreSQL server will be connected to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VirtualNetworkRuleState.__new__(_VirtualNetworkRuleState)

        __props__.__dict__["ignore_missing_vnet_service_endpoint"] = ignore_missing_vnet_service_endpoint
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["server_name"] = server_name
        __props__.__dict__["subnet_id"] = subnet_id
        return VirtualNetworkRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ignoreMissingVnetServiceEndpoint")
    def ignore_missing_vnet_service_endpoint(self) -> pulumi.Output[Optional[bool]]:
        """
        Should the Virtual Network Rule be created before the Subnet has the Virtual Network Service Endpoint enabled?
        """
        return pulumi.get(self, "ignore_missing_vnet_service_endpoint")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the PostgreSQL virtual network rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.

        > **NOTE:** `name` must be between 1-128 characters long and must satisfy all of the requirements below:

        1. Contains only alphanumeric and hyphen characters
        2. Cannot start with a number or hyphen
        3. Cannot end with a hyphen
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group where the PostgreSQL server resides. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Output[str]:
        """
        The name of the SQL Server to which this PostgreSQL virtual network rule will be applied to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "server_name")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        The ID of the subnet that the PostgreSQL server will be connected to.
        """
        return pulumi.get(self, "subnet_id")


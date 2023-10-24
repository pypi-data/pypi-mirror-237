# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['FlexibleServerFirewallRuleArgs', 'FlexibleServerFirewallRule']

@pulumi.input_type
class FlexibleServerFirewallRuleArgs:
    def __init__(__self__, *,
                 end_ip_address: pulumi.Input[str],
                 server_id: pulumi.Input[str],
                 start_ip_address: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FlexibleServerFirewallRule resource.
        :param pulumi.Input[str] end_ip_address: The End IP Address associated with this PostgreSQL Flexible Server Firewall Rule.
        :param pulumi.Input[str] server_id: The ID of the PostgreSQL Flexible Server from which to create this PostgreSQL Flexible Server Firewall Rule. Changing this forces a new PostgreSQL Flexible Server Firewall Rule to be created.
        :param pulumi.Input[str] start_ip_address: The Start IP Address associated with this PostgreSQL Flexible Server Firewall Rule.
        :param pulumi.Input[str] name: The name which should be used for this PostgreSQL Flexible Server Firewall Rule. Changing this forces a new PostgreSQL Flexible Server Firewall Rule to be created.
        """
        FlexibleServerFirewallRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            end_ip_address=end_ip_address,
            server_id=server_id,
            start_ip_address=start_ip_address,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             end_ip_address: pulumi.Input[str],
             server_id: pulumi.Input[str],
             start_ip_address: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'endIpAddress' in kwargs:
            end_ip_address = kwargs['endIpAddress']
        if 'serverId' in kwargs:
            server_id = kwargs['serverId']
        if 'startIpAddress' in kwargs:
            start_ip_address = kwargs['startIpAddress']

        _setter("end_ip_address", end_ip_address)
        _setter("server_id", server_id)
        _setter("start_ip_address", start_ip_address)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> pulumi.Input[str]:
        """
        The End IP Address associated with this PostgreSQL Flexible Server Firewall Rule.
        """
        return pulumi.get(self, "end_ip_address")

    @end_ip_address.setter
    def end_ip_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "end_ip_address", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Input[str]:
        """
        The ID of the PostgreSQL Flexible Server from which to create this PostgreSQL Flexible Server Firewall Rule. Changing this forces a new PostgreSQL Flexible Server Firewall Rule to be created.
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> pulumi.Input[str]:
        """
        The Start IP Address associated with this PostgreSQL Flexible Server Firewall Rule.
        """
        return pulumi.get(self, "start_ip_address")

    @start_ip_address.setter
    def start_ip_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "start_ip_address", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this PostgreSQL Flexible Server Firewall Rule. Changing this forces a new PostgreSQL Flexible Server Firewall Rule to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _FlexibleServerFirewallRuleState:
    def __init__(__self__, *,
                 end_ip_address: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 start_ip_address: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FlexibleServerFirewallRule resources.
        :param pulumi.Input[str] end_ip_address: The End IP Address associated with this PostgreSQL Flexible Server Firewall Rule.
        :param pulumi.Input[str] name: The name which should be used for this PostgreSQL Flexible Server Firewall Rule. Changing this forces a new PostgreSQL Flexible Server Firewall Rule to be created.
        :param pulumi.Input[str] server_id: The ID of the PostgreSQL Flexible Server from which to create this PostgreSQL Flexible Server Firewall Rule. Changing this forces a new PostgreSQL Flexible Server Firewall Rule to be created.
        :param pulumi.Input[str] start_ip_address: The Start IP Address associated with this PostgreSQL Flexible Server Firewall Rule.
        """
        _FlexibleServerFirewallRuleState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            end_ip_address=end_ip_address,
            name=name,
            server_id=server_id,
            start_ip_address=start_ip_address,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             end_ip_address: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             server_id: Optional[pulumi.Input[str]] = None,
             start_ip_address: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'endIpAddress' in kwargs:
            end_ip_address = kwargs['endIpAddress']
        if 'serverId' in kwargs:
            server_id = kwargs['serverId']
        if 'startIpAddress' in kwargs:
            start_ip_address = kwargs['startIpAddress']

        if end_ip_address is not None:
            _setter("end_ip_address", end_ip_address)
        if name is not None:
            _setter("name", name)
        if server_id is not None:
            _setter("server_id", server_id)
        if start_ip_address is not None:
            _setter("start_ip_address", start_ip_address)

    @property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The End IP Address associated with this PostgreSQL Flexible Server Firewall Rule.
        """
        return pulumi.get(self, "end_ip_address")

    @end_ip_address.setter
    def end_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_ip_address", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this PostgreSQL Flexible Server Firewall Rule. Changing this forces a new PostgreSQL Flexible Server Firewall Rule to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the PostgreSQL Flexible Server from which to create this PostgreSQL Flexible Server Firewall Rule. Changing this forces a new PostgreSQL Flexible Server Firewall Rule to be created.
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The Start IP Address associated with this PostgreSQL Flexible Server Firewall Rule.
        """
        return pulumi.get(self, "start_ip_address")

    @start_ip_address.setter
    def start_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_ip_address", value)


class FlexibleServerFirewallRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 end_ip_address: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 start_ip_address: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a PostgreSQL Flexible Server Firewall Rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_flexible_server = azure.postgresql.FlexibleServer("exampleFlexibleServer",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            version="12",
            administrator_login="psqladmin",
            administrator_password="H@Sh1CoR3!",
            storage_mb=32768,
            sku_name="GP_Standard_D4s_v3")
        example_flexible_server_firewall_rule = azure.postgresql.FlexibleServerFirewallRule("exampleFlexibleServerFirewallRule",
            server_id=example_flexible_server.id,
            start_ip_address="122.122.0.0",
            end_ip_address="122.122.0.0")
        ```

        ## Import

        PostgreSQL Flexible Server Firewall Rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:postgresql/flexibleServerFirewallRule:FlexibleServerFirewallRule example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.DBforPostgreSQL/flexibleServers/flexibleServer1/firewallRules/firewallRule1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] end_ip_address: The End IP Address associated with this PostgreSQL Flexible Server Firewall Rule.
        :param pulumi.Input[str] name: The name which should be used for this PostgreSQL Flexible Server Firewall Rule. Changing this forces a new PostgreSQL Flexible Server Firewall Rule to be created.
        :param pulumi.Input[str] server_id: The ID of the PostgreSQL Flexible Server from which to create this PostgreSQL Flexible Server Firewall Rule. Changing this forces a new PostgreSQL Flexible Server Firewall Rule to be created.
        :param pulumi.Input[str] start_ip_address: The Start IP Address associated with this PostgreSQL Flexible Server Firewall Rule.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FlexibleServerFirewallRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a PostgreSQL Flexible Server Firewall Rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_flexible_server = azure.postgresql.FlexibleServer("exampleFlexibleServer",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            version="12",
            administrator_login="psqladmin",
            administrator_password="H@Sh1CoR3!",
            storage_mb=32768,
            sku_name="GP_Standard_D4s_v3")
        example_flexible_server_firewall_rule = azure.postgresql.FlexibleServerFirewallRule("exampleFlexibleServerFirewallRule",
            server_id=example_flexible_server.id,
            start_ip_address="122.122.0.0",
            end_ip_address="122.122.0.0")
        ```

        ## Import

        PostgreSQL Flexible Server Firewall Rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:postgresql/flexibleServerFirewallRule:FlexibleServerFirewallRule example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.DBforPostgreSQL/flexibleServers/flexibleServer1/firewallRules/firewallRule1
        ```

        :param str resource_name: The name of the resource.
        :param FlexibleServerFirewallRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FlexibleServerFirewallRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            FlexibleServerFirewallRuleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 end_ip_address: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 start_ip_address: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FlexibleServerFirewallRuleArgs.__new__(FlexibleServerFirewallRuleArgs)

            if end_ip_address is None and not opts.urn:
                raise TypeError("Missing required property 'end_ip_address'")
            __props__.__dict__["end_ip_address"] = end_ip_address
            __props__.__dict__["name"] = name
            if server_id is None and not opts.urn:
                raise TypeError("Missing required property 'server_id'")
            __props__.__dict__["server_id"] = server_id
            if start_ip_address is None and not opts.urn:
                raise TypeError("Missing required property 'start_ip_address'")
            __props__.__dict__["start_ip_address"] = start_ip_address
        super(FlexibleServerFirewallRule, __self__).__init__(
            'azure:postgresql/flexibleServerFirewallRule:FlexibleServerFirewallRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            end_ip_address: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            server_id: Optional[pulumi.Input[str]] = None,
            start_ip_address: Optional[pulumi.Input[str]] = None) -> 'FlexibleServerFirewallRule':
        """
        Get an existing FlexibleServerFirewallRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] end_ip_address: The End IP Address associated with this PostgreSQL Flexible Server Firewall Rule.
        :param pulumi.Input[str] name: The name which should be used for this PostgreSQL Flexible Server Firewall Rule. Changing this forces a new PostgreSQL Flexible Server Firewall Rule to be created.
        :param pulumi.Input[str] server_id: The ID of the PostgreSQL Flexible Server from which to create this PostgreSQL Flexible Server Firewall Rule. Changing this forces a new PostgreSQL Flexible Server Firewall Rule to be created.
        :param pulumi.Input[str] start_ip_address: The Start IP Address associated with this PostgreSQL Flexible Server Firewall Rule.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FlexibleServerFirewallRuleState.__new__(_FlexibleServerFirewallRuleState)

        __props__.__dict__["end_ip_address"] = end_ip_address
        __props__.__dict__["name"] = name
        __props__.__dict__["server_id"] = server_id
        __props__.__dict__["start_ip_address"] = start_ip_address
        return FlexibleServerFirewallRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> pulumi.Output[str]:
        """
        The End IP Address associated with this PostgreSQL Flexible Server Firewall Rule.
        """
        return pulumi.get(self, "end_ip_address")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this PostgreSQL Flexible Server Firewall Rule. Changing this forces a new PostgreSQL Flexible Server Firewall Rule to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[str]:
        """
        The ID of the PostgreSQL Flexible Server from which to create this PostgreSQL Flexible Server Firewall Rule. Changing this forces a new PostgreSQL Flexible Server Firewall Rule to be created.
        """
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> pulumi.Output[str]:
        """
        The Start IP Address associated with this PostgreSQL Flexible Server Firewall Rule.
        """
        return pulumi.get(self, "start_ip_address")


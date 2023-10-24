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

__all__ = ['FirewallNatRuleCollectionArgs', 'FirewallNatRuleCollection']

@pulumi.input_type
class FirewallNatRuleCollectionArgs:
    def __init__(__self__, *,
                 action: pulumi.Input[str],
                 azure_firewall_name: pulumi.Input[str],
                 priority: pulumi.Input[int],
                 resource_group_name: pulumi.Input[str],
                 rules: pulumi.Input[Sequence[pulumi.Input['FirewallNatRuleCollectionRuleArgs']]],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FirewallNatRuleCollection resource.
        :param pulumi.Input[str] action: Specifies the action the rule will apply to matching traffic. Possible values are `Dnat` and `Snat`.
        :param pulumi.Input[str] azure_firewall_name: Specifies the name of the Firewall in which the NAT Rule Collection should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[int] priority: Specifies the priority of the rule collection. Possible values are between `100` - `65000`.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input['FirewallNatRuleCollectionRuleArgs']]] rules: One or more `rule` blocks as defined below.
        :param pulumi.Input[str] name: Specifies the name of the NAT Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.
        """
        FirewallNatRuleCollectionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            action=action,
            azure_firewall_name=azure_firewall_name,
            priority=priority,
            resource_group_name=resource_group_name,
            rules=rules,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             action: pulumi.Input[str],
             azure_firewall_name: pulumi.Input[str],
             priority: pulumi.Input[int],
             resource_group_name: pulumi.Input[str],
             rules: pulumi.Input[Sequence[pulumi.Input['FirewallNatRuleCollectionRuleArgs']]],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'azureFirewallName' in kwargs:
            azure_firewall_name = kwargs['azureFirewallName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']

        _setter("action", action)
        _setter("azure_firewall_name", azure_firewall_name)
        _setter("priority", priority)
        _setter("resource_group_name", resource_group_name)
        _setter("rules", rules)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[str]:
        """
        Specifies the action the rule will apply to matching traffic. Possible values are `Dnat` and `Snat`.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[str]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="azureFirewallName")
    def azure_firewall_name(self) -> pulumi.Input[str]:
        """
        Specifies the name of the Firewall in which the NAT Rule Collection should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "azure_firewall_name")

    @azure_firewall_name.setter
    def azure_firewall_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "azure_firewall_name", value)

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Input[int]:
        """
        Specifies the priority of the rule collection. Possible values are between `100` - `65000`.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: pulumi.Input[int]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input['FirewallNatRuleCollectionRuleArgs']]]:
        """
        One or more `rule` blocks as defined below.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input['FirewallNatRuleCollectionRuleArgs']]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the NAT Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _FirewallNatRuleCollectionState:
    def __init__(__self__, *,
                 action: Optional[pulumi.Input[str]] = None,
                 azure_firewall_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallNatRuleCollectionRuleArgs']]]] = None):
        """
        Input properties used for looking up and filtering FirewallNatRuleCollection resources.
        :param pulumi.Input[str] action: Specifies the action the rule will apply to matching traffic. Possible values are `Dnat` and `Snat`.
        :param pulumi.Input[str] azure_firewall_name: Specifies the name of the Firewall in which the NAT Rule Collection should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the NAT Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.
        :param pulumi.Input[int] priority: Specifies the priority of the rule collection. Possible values are between `100` - `65000`.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input['FirewallNatRuleCollectionRuleArgs']]] rules: One or more `rule` blocks as defined below.
        """
        _FirewallNatRuleCollectionState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            action=action,
            azure_firewall_name=azure_firewall_name,
            name=name,
            priority=priority,
            resource_group_name=resource_group_name,
            rules=rules,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             action: Optional[pulumi.Input[str]] = None,
             azure_firewall_name: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             priority: Optional[pulumi.Input[int]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             rules: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallNatRuleCollectionRuleArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'azureFirewallName' in kwargs:
            azure_firewall_name = kwargs['azureFirewallName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']

        if action is not None:
            _setter("action", action)
        if azure_firewall_name is not None:
            _setter("azure_firewall_name", azure_firewall_name)
        if name is not None:
            _setter("name", name)
        if priority is not None:
            _setter("priority", priority)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if rules is not None:
            _setter("rules", rules)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the action the rule will apply to matching traffic. Possible values are `Dnat` and `Snat`.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="azureFirewallName")
    def azure_firewall_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Firewall in which the NAT Rule Collection should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "azure_firewall_name")

    @azure_firewall_name.setter
    def azure_firewall_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "azure_firewall_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the NAT Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the priority of the rule collection. Possible values are between `100` - `65000`.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FirewallNatRuleCollectionRuleArgs']]]]:
        """
        One or more `rule` blocks as defined below.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallNatRuleCollectionRuleArgs']]]]):
        pulumi.set(self, "rules", value)


class FirewallNatRuleCollection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 azure_firewall_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallNatRuleCollectionRuleArgs']]]]] = None,
                 __props__=None):
        """
        Manages a NAT Rule Collection within an Azure Firewall.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            address_spaces=["10.0.0.0/16"],
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_subnet = azure.network.Subnet("exampleSubnet",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.0.1.0/24"])
        example_public_ip = azure.network.PublicIp("examplePublicIp",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            allocation_method="Static",
            sku="Standard")
        example_firewall = azure.network.Firewall("exampleFirewall",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="AZFW_VNet",
            sku_tier="Standard",
            ip_configurations=[azure.network.FirewallIpConfigurationArgs(
                name="configuration",
                subnet_id=example_subnet.id,
                public_ip_address_id=example_public_ip.id,
            )])
        example_firewall_nat_rule_collection = azure.network.FirewallNatRuleCollection("exampleFirewallNatRuleCollection",
            azure_firewall_name=example_firewall.name,
            resource_group_name=example_resource_group.name,
            priority=100,
            action="Dnat",
            rules=[azure.network.FirewallNatRuleCollectionRuleArgs(
                name="testrule",
                source_addresses=["10.0.0.0/16"],
                destination_ports=["53"],
                destination_addresses=[example_public_ip.ip_address],
                translated_port="53",
                translated_address="8.8.8.8",
                protocols=[
                    "TCP",
                    "UDP",
                ],
            )])
        ```

        ## Import

        Azure Firewall NAT Rule Collections can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/firewallNatRuleCollection:FirewallNatRuleCollection example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/azureFirewalls/myfirewall/natRuleCollections/mycollection
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: Specifies the action the rule will apply to matching traffic. Possible values are `Dnat` and `Snat`.
        :param pulumi.Input[str] azure_firewall_name: Specifies the name of the Firewall in which the NAT Rule Collection should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the NAT Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.
        :param pulumi.Input[int] priority: Specifies the priority of the rule collection. Possible values are between `100` - `65000`.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallNatRuleCollectionRuleArgs']]]] rules: One or more `rule` blocks as defined below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FirewallNatRuleCollectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a NAT Rule Collection within an Azure Firewall.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            address_spaces=["10.0.0.0/16"],
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_subnet = azure.network.Subnet("exampleSubnet",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.0.1.0/24"])
        example_public_ip = azure.network.PublicIp("examplePublicIp",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            allocation_method="Static",
            sku="Standard")
        example_firewall = azure.network.Firewall("exampleFirewall",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="AZFW_VNet",
            sku_tier="Standard",
            ip_configurations=[azure.network.FirewallIpConfigurationArgs(
                name="configuration",
                subnet_id=example_subnet.id,
                public_ip_address_id=example_public_ip.id,
            )])
        example_firewall_nat_rule_collection = azure.network.FirewallNatRuleCollection("exampleFirewallNatRuleCollection",
            azure_firewall_name=example_firewall.name,
            resource_group_name=example_resource_group.name,
            priority=100,
            action="Dnat",
            rules=[azure.network.FirewallNatRuleCollectionRuleArgs(
                name="testrule",
                source_addresses=["10.0.0.0/16"],
                destination_ports=["53"],
                destination_addresses=[example_public_ip.ip_address],
                translated_port="53",
                translated_address="8.8.8.8",
                protocols=[
                    "TCP",
                    "UDP",
                ],
            )])
        ```

        ## Import

        Azure Firewall NAT Rule Collections can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/firewallNatRuleCollection:FirewallNatRuleCollection example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/azureFirewalls/myfirewall/natRuleCollections/mycollection
        ```

        :param str resource_name: The name of the resource.
        :param FirewallNatRuleCollectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallNatRuleCollectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            FirewallNatRuleCollectionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 azure_firewall_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallNatRuleCollectionRuleArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FirewallNatRuleCollectionArgs.__new__(FirewallNatRuleCollectionArgs)

            if action is None and not opts.urn:
                raise TypeError("Missing required property 'action'")
            __props__.__dict__["action"] = action
            if azure_firewall_name is None and not opts.urn:
                raise TypeError("Missing required property 'azure_firewall_name'")
            __props__.__dict__["azure_firewall_name"] = azure_firewall_name
            __props__.__dict__["name"] = name
            if priority is None and not opts.urn:
                raise TypeError("Missing required property 'priority'")
            __props__.__dict__["priority"] = priority
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if rules is None and not opts.urn:
                raise TypeError("Missing required property 'rules'")
            __props__.__dict__["rules"] = rules
        super(FirewallNatRuleCollection, __self__).__init__(
            'azure:network/firewallNatRuleCollection:FirewallNatRuleCollection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action: Optional[pulumi.Input[str]] = None,
            azure_firewall_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallNatRuleCollectionRuleArgs']]]]] = None) -> 'FirewallNatRuleCollection':
        """
        Get an existing FirewallNatRuleCollection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: Specifies the action the rule will apply to matching traffic. Possible values are `Dnat` and `Snat`.
        :param pulumi.Input[str] azure_firewall_name: Specifies the name of the Firewall in which the NAT Rule Collection should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the NAT Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.
        :param pulumi.Input[int] priority: Specifies the priority of the rule collection. Possible values are between `100` - `65000`.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallNatRuleCollectionRuleArgs']]]] rules: One or more `rule` blocks as defined below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FirewallNatRuleCollectionState.__new__(_FirewallNatRuleCollectionState)

        __props__.__dict__["action"] = action
        __props__.__dict__["azure_firewall_name"] = azure_firewall_name
        __props__.__dict__["name"] = name
        __props__.__dict__["priority"] = priority
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["rules"] = rules
        return FirewallNatRuleCollection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output[str]:
        """
        Specifies the action the rule will apply to matching traffic. Possible values are `Dnat` and `Snat`.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="azureFirewallName")
    def azure_firewall_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Firewall in which the NAT Rule Collection should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "azure_firewall_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the NAT Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        Specifies the priority of the rule collection. Possible values are between `100` - `65000`.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.FirewallNatRuleCollectionRule']]:
        """
        One or more `rule` blocks as defined below.
        """
        return pulumi.get(self, "rules")


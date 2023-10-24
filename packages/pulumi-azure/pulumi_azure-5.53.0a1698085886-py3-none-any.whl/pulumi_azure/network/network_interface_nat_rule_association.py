# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['NetworkInterfaceNatRuleAssociationArgs', 'NetworkInterfaceNatRuleAssociation']

@pulumi.input_type
class NetworkInterfaceNatRuleAssociationArgs:
    def __init__(__self__, *,
                 ip_configuration_name: pulumi.Input[str],
                 nat_rule_id: pulumi.Input[str],
                 network_interface_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a NetworkInterfaceNatRuleAssociation resource.
        :param pulumi.Input[str] ip_configuration_name: The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] nat_rule_id: The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] network_interface_id: The ID of the Network Interface. Changing this forces a new resource to be created.
        """
        NetworkInterfaceNatRuleAssociationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            ip_configuration_name=ip_configuration_name,
            nat_rule_id=nat_rule_id,
            network_interface_id=network_interface_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             ip_configuration_name: pulumi.Input[str],
             nat_rule_id: pulumi.Input[str],
             network_interface_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'ipConfigurationName' in kwargs:
            ip_configuration_name = kwargs['ipConfigurationName']
        if 'natRuleId' in kwargs:
            nat_rule_id = kwargs['natRuleId']
        if 'networkInterfaceId' in kwargs:
            network_interface_id = kwargs['networkInterfaceId']

        _setter("ip_configuration_name", ip_configuration_name)
        _setter("nat_rule_id", nat_rule_id)
        _setter("network_interface_id", network_interface_id)

    @property
    @pulumi.getter(name="ipConfigurationName")
    def ip_configuration_name(self) -> pulumi.Input[str]:
        """
        The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "ip_configuration_name")

    @ip_configuration_name.setter
    def ip_configuration_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "ip_configuration_name", value)

    @property
    @pulumi.getter(name="natRuleId")
    def nat_rule_id(self) -> pulumi.Input[str]:
        """
        The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "nat_rule_id")

    @nat_rule_id.setter
    def nat_rule_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "nat_rule_id", value)

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Input[str]:
        """
        The ID of the Network Interface. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "network_interface_id")

    @network_interface_id.setter
    def network_interface_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_interface_id", value)


@pulumi.input_type
class _NetworkInterfaceNatRuleAssociationState:
    def __init__(__self__, *,
                 ip_configuration_name: Optional[pulumi.Input[str]] = None,
                 nat_rule_id: Optional[pulumi.Input[str]] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering NetworkInterfaceNatRuleAssociation resources.
        :param pulumi.Input[str] ip_configuration_name: The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] nat_rule_id: The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] network_interface_id: The ID of the Network Interface. Changing this forces a new resource to be created.
        """
        _NetworkInterfaceNatRuleAssociationState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            ip_configuration_name=ip_configuration_name,
            nat_rule_id=nat_rule_id,
            network_interface_id=network_interface_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             ip_configuration_name: Optional[pulumi.Input[str]] = None,
             nat_rule_id: Optional[pulumi.Input[str]] = None,
             network_interface_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'ipConfigurationName' in kwargs:
            ip_configuration_name = kwargs['ipConfigurationName']
        if 'natRuleId' in kwargs:
            nat_rule_id = kwargs['natRuleId']
        if 'networkInterfaceId' in kwargs:
            network_interface_id = kwargs['networkInterfaceId']

        if ip_configuration_name is not None:
            _setter("ip_configuration_name", ip_configuration_name)
        if nat_rule_id is not None:
            _setter("nat_rule_id", nat_rule_id)
        if network_interface_id is not None:
            _setter("network_interface_id", network_interface_id)

    @property
    @pulumi.getter(name="ipConfigurationName")
    def ip_configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "ip_configuration_name")

    @ip_configuration_name.setter
    def ip_configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_configuration_name", value)

    @property
    @pulumi.getter(name="natRuleId")
    def nat_rule_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "nat_rule_id")

    @nat_rule_id.setter
    def nat_rule_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "nat_rule_id", value)

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Network Interface. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "network_interface_id")

    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_interface_id", value)


class NetworkInterfaceNatRuleAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip_configuration_name: Optional[pulumi.Input[str]] = None,
                 nat_rule_id: Optional[pulumi.Input[str]] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages the association between a Network Interface and a Load Balancer's NAT Rule.

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
            address_prefixes=["10.0.2.0/24"])
        example_public_ip = azure.network.PublicIp("examplePublicIp",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            allocation_method="Static")
        example_load_balancer = azure.lb.LoadBalancer("exampleLoadBalancer",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            frontend_ip_configurations=[azure.lb.LoadBalancerFrontendIpConfigurationArgs(
                name="primary",
                public_ip_address_id=example_public_ip.id,
            )])
        example_nat_rule = azure.lb.NatRule("exampleNatRule",
            resource_group_name=example_resource_group.name,
            loadbalancer_id=example_load_balancer.id,
            protocol="Tcp",
            frontend_port=3389,
            backend_port=3389,
            frontend_ip_configuration_name="primary")
        example_network_interface = azure.network.NetworkInterface("exampleNetworkInterface",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            ip_configurations=[azure.network.NetworkInterfaceIpConfigurationArgs(
                name="testconfiguration1",
                subnet_id=example_subnet.id,
                private_ip_address_allocation="Dynamic",
            )])
        example_network_interface_nat_rule_association = azure.network.NetworkInterfaceNatRuleAssociation("exampleNetworkInterfaceNatRuleAssociation",
            network_interface_id=example_network_interface.id,
            ip_configuration_name="testconfiguration1",
            nat_rule_id=example_nat_rule.id)
        ```

        ## Import

        Associations between Network Interfaces and Load Balancer NAT Rule can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/networkInterfaceNatRuleAssociation:NetworkInterfaceNatRuleAssociation association1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/networkInterfaces/nic1/ipConfigurations/example|/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Network/loadBalancers/lb1/inboundNatRules/rule1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ip_configuration_name: The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] nat_rule_id: The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] network_interface_id: The ID of the Network Interface. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkInterfaceNatRuleAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages the association between a Network Interface and a Load Balancer's NAT Rule.

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
            address_prefixes=["10.0.2.0/24"])
        example_public_ip = azure.network.PublicIp("examplePublicIp",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            allocation_method="Static")
        example_load_balancer = azure.lb.LoadBalancer("exampleLoadBalancer",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            frontend_ip_configurations=[azure.lb.LoadBalancerFrontendIpConfigurationArgs(
                name="primary",
                public_ip_address_id=example_public_ip.id,
            )])
        example_nat_rule = azure.lb.NatRule("exampleNatRule",
            resource_group_name=example_resource_group.name,
            loadbalancer_id=example_load_balancer.id,
            protocol="Tcp",
            frontend_port=3389,
            backend_port=3389,
            frontend_ip_configuration_name="primary")
        example_network_interface = azure.network.NetworkInterface("exampleNetworkInterface",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            ip_configurations=[azure.network.NetworkInterfaceIpConfigurationArgs(
                name="testconfiguration1",
                subnet_id=example_subnet.id,
                private_ip_address_allocation="Dynamic",
            )])
        example_network_interface_nat_rule_association = azure.network.NetworkInterfaceNatRuleAssociation("exampleNetworkInterfaceNatRuleAssociation",
            network_interface_id=example_network_interface.id,
            ip_configuration_name="testconfiguration1",
            nat_rule_id=example_nat_rule.id)
        ```

        ## Import

        Associations between Network Interfaces and Load Balancer NAT Rule can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/networkInterfaceNatRuleAssociation:NetworkInterfaceNatRuleAssociation association1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/networkInterfaces/nic1/ipConfigurations/example|/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Network/loadBalancers/lb1/inboundNatRules/rule1
        ```

        :param str resource_name: The name of the resource.
        :param NetworkInterfaceNatRuleAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkInterfaceNatRuleAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            NetworkInterfaceNatRuleAssociationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip_configuration_name: Optional[pulumi.Input[str]] = None,
                 nat_rule_id: Optional[pulumi.Input[str]] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkInterfaceNatRuleAssociationArgs.__new__(NetworkInterfaceNatRuleAssociationArgs)

            if ip_configuration_name is None and not opts.urn:
                raise TypeError("Missing required property 'ip_configuration_name'")
            __props__.__dict__["ip_configuration_name"] = ip_configuration_name
            if nat_rule_id is None and not opts.urn:
                raise TypeError("Missing required property 'nat_rule_id'")
            __props__.__dict__["nat_rule_id"] = nat_rule_id
            if network_interface_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_interface_id'")
            __props__.__dict__["network_interface_id"] = network_interface_id
        super(NetworkInterfaceNatRuleAssociation, __self__).__init__(
            'azure:network/networkInterfaceNatRuleAssociation:NetworkInterfaceNatRuleAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            ip_configuration_name: Optional[pulumi.Input[str]] = None,
            nat_rule_id: Optional[pulumi.Input[str]] = None,
            network_interface_id: Optional[pulumi.Input[str]] = None) -> 'NetworkInterfaceNatRuleAssociation':
        """
        Get an existing NetworkInterfaceNatRuleAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ip_configuration_name: The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] nat_rule_id: The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] network_interface_id: The ID of the Network Interface. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NetworkInterfaceNatRuleAssociationState.__new__(_NetworkInterfaceNatRuleAssociationState)

        __props__.__dict__["ip_configuration_name"] = ip_configuration_name
        __props__.__dict__["nat_rule_id"] = nat_rule_id
        __props__.__dict__["network_interface_id"] = network_interface_id
        return NetworkInterfaceNatRuleAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ipConfigurationName")
    def ip_configuration_name(self) -> pulumi.Output[str]:
        """
        The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "ip_configuration_name")

    @property
    @pulumi.getter(name="natRuleId")
    def nat_rule_id(self) -> pulumi.Output[str]:
        """
        The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "nat_rule_id")

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Output[str]:
        """
        The ID of the Network Interface. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "network_interface_id")


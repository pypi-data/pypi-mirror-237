# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ExpressRouteCircuitConnectionArgs', 'ExpressRouteCircuitConnection']

@pulumi.input_type
class ExpressRouteCircuitConnectionArgs:
    def __init__(__self__, *,
                 address_prefix_ipv4: pulumi.Input[str],
                 peer_peering_id: pulumi.Input[str],
                 peering_id: pulumi.Input[str],
                 address_prefix_ipv6: Optional[pulumi.Input[str]] = None,
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ExpressRouteCircuitConnection resource.
        :param pulumi.Input[str] address_prefix_ipv4: The IPv4 address space from which to allocate customer address for global reach. Changing this forces a new Express Route Circuit Connection to be created.
        :param pulumi.Input[str] peer_peering_id: The ID of the peered Express Route Circuit Private Peering. Changing this forces a new Express Route Circuit Connection to be created.
        :param pulumi.Input[str] peering_id: The ID of the Express Route Circuit Private Peering that this Express Route Circuit Connection connects with. Changing this forces a new Express Route Circuit Connection to be created.
        :param pulumi.Input[str] address_prefix_ipv6: The IPv6 address space from which to allocate customer addresses for global reach.
               
               > **NOTE:** `address_prefix_ipv6` cannot be set when ExpressRoute Circuit Connection with ExpressRoute Circuit based on ExpressRoute Port.
        :param pulumi.Input[str] authorization_key: The authorization key which is associated with the Express Route Circuit Connection.
        :param pulumi.Input[str] name: The name which should be used for this Express Route Circuit Connection. Changing this forces a new Express Route Circuit Connection to be created.
        """
        ExpressRouteCircuitConnectionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            address_prefix_ipv4=address_prefix_ipv4,
            peer_peering_id=peer_peering_id,
            peering_id=peering_id,
            address_prefix_ipv6=address_prefix_ipv6,
            authorization_key=authorization_key,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             address_prefix_ipv4: pulumi.Input[str],
             peer_peering_id: pulumi.Input[str],
             peering_id: pulumi.Input[str],
             address_prefix_ipv6: Optional[pulumi.Input[str]] = None,
             authorization_key: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'addressPrefixIpv4' in kwargs:
            address_prefix_ipv4 = kwargs['addressPrefixIpv4']
        if 'peerPeeringId' in kwargs:
            peer_peering_id = kwargs['peerPeeringId']
        if 'peeringId' in kwargs:
            peering_id = kwargs['peeringId']
        if 'addressPrefixIpv6' in kwargs:
            address_prefix_ipv6 = kwargs['addressPrefixIpv6']
        if 'authorizationKey' in kwargs:
            authorization_key = kwargs['authorizationKey']

        _setter("address_prefix_ipv4", address_prefix_ipv4)
        _setter("peer_peering_id", peer_peering_id)
        _setter("peering_id", peering_id)
        if address_prefix_ipv6 is not None:
            _setter("address_prefix_ipv6", address_prefix_ipv6)
        if authorization_key is not None:
            _setter("authorization_key", authorization_key)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="addressPrefixIpv4")
    def address_prefix_ipv4(self) -> pulumi.Input[str]:
        """
        The IPv4 address space from which to allocate customer address for global reach. Changing this forces a new Express Route Circuit Connection to be created.
        """
        return pulumi.get(self, "address_prefix_ipv4")

    @address_prefix_ipv4.setter
    def address_prefix_ipv4(self, value: pulumi.Input[str]):
        pulumi.set(self, "address_prefix_ipv4", value)

    @property
    @pulumi.getter(name="peerPeeringId")
    def peer_peering_id(self) -> pulumi.Input[str]:
        """
        The ID of the peered Express Route Circuit Private Peering. Changing this forces a new Express Route Circuit Connection to be created.
        """
        return pulumi.get(self, "peer_peering_id")

    @peer_peering_id.setter
    def peer_peering_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "peer_peering_id", value)

    @property
    @pulumi.getter(name="peeringId")
    def peering_id(self) -> pulumi.Input[str]:
        """
        The ID of the Express Route Circuit Private Peering that this Express Route Circuit Connection connects with. Changing this forces a new Express Route Circuit Connection to be created.
        """
        return pulumi.get(self, "peering_id")

    @peering_id.setter
    def peering_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "peering_id", value)

    @property
    @pulumi.getter(name="addressPrefixIpv6")
    def address_prefix_ipv6(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv6 address space from which to allocate customer addresses for global reach.

        > **NOTE:** `address_prefix_ipv6` cannot be set when ExpressRoute Circuit Connection with ExpressRoute Circuit based on ExpressRoute Port.
        """
        return pulumi.get(self, "address_prefix_ipv6")

    @address_prefix_ipv6.setter
    def address_prefix_ipv6(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_prefix_ipv6", value)

    @property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[pulumi.Input[str]]:
        """
        The authorization key which is associated with the Express Route Circuit Connection.
        """
        return pulumi.get(self, "authorization_key")

    @authorization_key.setter
    def authorization_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization_key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Express Route Circuit Connection. Changing this forces a new Express Route Circuit Connection to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ExpressRouteCircuitConnectionState:
    def __init__(__self__, *,
                 address_prefix_ipv4: Optional[pulumi.Input[str]] = None,
                 address_prefix_ipv6: Optional[pulumi.Input[str]] = None,
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peer_peering_id: Optional[pulumi.Input[str]] = None,
                 peering_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ExpressRouteCircuitConnection resources.
        :param pulumi.Input[str] address_prefix_ipv4: The IPv4 address space from which to allocate customer address for global reach. Changing this forces a new Express Route Circuit Connection to be created.
        :param pulumi.Input[str] address_prefix_ipv6: The IPv6 address space from which to allocate customer addresses for global reach.
               
               > **NOTE:** `address_prefix_ipv6` cannot be set when ExpressRoute Circuit Connection with ExpressRoute Circuit based on ExpressRoute Port.
        :param pulumi.Input[str] authorization_key: The authorization key which is associated with the Express Route Circuit Connection.
        :param pulumi.Input[str] name: The name which should be used for this Express Route Circuit Connection. Changing this forces a new Express Route Circuit Connection to be created.
        :param pulumi.Input[str] peer_peering_id: The ID of the peered Express Route Circuit Private Peering. Changing this forces a new Express Route Circuit Connection to be created.
        :param pulumi.Input[str] peering_id: The ID of the Express Route Circuit Private Peering that this Express Route Circuit Connection connects with. Changing this forces a new Express Route Circuit Connection to be created.
        """
        _ExpressRouteCircuitConnectionState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            address_prefix_ipv4=address_prefix_ipv4,
            address_prefix_ipv6=address_prefix_ipv6,
            authorization_key=authorization_key,
            name=name,
            peer_peering_id=peer_peering_id,
            peering_id=peering_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             address_prefix_ipv4: Optional[pulumi.Input[str]] = None,
             address_prefix_ipv6: Optional[pulumi.Input[str]] = None,
             authorization_key: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             peer_peering_id: Optional[pulumi.Input[str]] = None,
             peering_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'addressPrefixIpv4' in kwargs:
            address_prefix_ipv4 = kwargs['addressPrefixIpv4']
        if 'addressPrefixIpv6' in kwargs:
            address_prefix_ipv6 = kwargs['addressPrefixIpv6']
        if 'authorizationKey' in kwargs:
            authorization_key = kwargs['authorizationKey']
        if 'peerPeeringId' in kwargs:
            peer_peering_id = kwargs['peerPeeringId']
        if 'peeringId' in kwargs:
            peering_id = kwargs['peeringId']

        if address_prefix_ipv4 is not None:
            _setter("address_prefix_ipv4", address_prefix_ipv4)
        if address_prefix_ipv6 is not None:
            _setter("address_prefix_ipv6", address_prefix_ipv6)
        if authorization_key is not None:
            _setter("authorization_key", authorization_key)
        if name is not None:
            _setter("name", name)
        if peer_peering_id is not None:
            _setter("peer_peering_id", peer_peering_id)
        if peering_id is not None:
            _setter("peering_id", peering_id)

    @property
    @pulumi.getter(name="addressPrefixIpv4")
    def address_prefix_ipv4(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 address space from which to allocate customer address for global reach. Changing this forces a new Express Route Circuit Connection to be created.
        """
        return pulumi.get(self, "address_prefix_ipv4")

    @address_prefix_ipv4.setter
    def address_prefix_ipv4(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_prefix_ipv4", value)

    @property
    @pulumi.getter(name="addressPrefixIpv6")
    def address_prefix_ipv6(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv6 address space from which to allocate customer addresses for global reach.

        > **NOTE:** `address_prefix_ipv6` cannot be set when ExpressRoute Circuit Connection with ExpressRoute Circuit based on ExpressRoute Port.
        """
        return pulumi.get(self, "address_prefix_ipv6")

    @address_prefix_ipv6.setter
    def address_prefix_ipv6(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_prefix_ipv6", value)

    @property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[pulumi.Input[str]]:
        """
        The authorization key which is associated with the Express Route Circuit Connection.
        """
        return pulumi.get(self, "authorization_key")

    @authorization_key.setter
    def authorization_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization_key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Express Route Circuit Connection. Changing this forces a new Express Route Circuit Connection to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="peerPeeringId")
    def peer_peering_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the peered Express Route Circuit Private Peering. Changing this forces a new Express Route Circuit Connection to be created.
        """
        return pulumi.get(self, "peer_peering_id")

    @peer_peering_id.setter
    def peer_peering_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_peering_id", value)

    @property
    @pulumi.getter(name="peeringId")
    def peering_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Express Route Circuit Private Peering that this Express Route Circuit Connection connects with. Changing this forces a new Express Route Circuit Connection to be created.
        """
        return pulumi.get(self, "peering_id")

    @peering_id.setter
    def peering_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peering_id", value)


class ExpressRouteCircuitConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_prefix_ipv4: Optional[pulumi.Input[str]] = None,
                 address_prefix_ipv6: Optional[pulumi.Input[str]] = None,
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peer_peering_id: Optional[pulumi.Input[str]] = None,
                 peering_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an Express Route Circuit Connection.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_express_route_port = azure.network.ExpressRoutePort("exampleExpressRoutePort",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            peering_location="Equinix-Seattle-SE2",
            bandwidth_in_gbps=10,
            encapsulation="Dot1Q")
        example_express_route_circuit = azure.network.ExpressRouteCircuit("exampleExpressRouteCircuit",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            express_route_port_id=example_express_route_port.id,
            bandwidth_in_gbps=5,
            sku=azure.network.ExpressRouteCircuitSkuArgs(
                tier="Standard",
                family="MeteredData",
            ))
        example2_express_route_port = azure.network.ExpressRoutePort("example2ExpressRoutePort",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            peering_location="Allied-Toronto-King-West",
            bandwidth_in_gbps=10,
            encapsulation="Dot1Q")
        example2_express_route_circuit = azure.network.ExpressRouteCircuit("example2ExpressRouteCircuit",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            express_route_port_id=example2_express_route_port.id,
            bandwidth_in_gbps=5,
            sku=azure.network.ExpressRouteCircuitSkuArgs(
                tier="Standard",
                family="MeteredData",
            ))
        example_express_route_circuit_peering = azure.network.ExpressRouteCircuitPeering("exampleExpressRouteCircuitPeering",
            peering_type="AzurePrivatePeering",
            express_route_circuit_name=example_express_route_circuit.name,
            resource_group_name=example_resource_group.name,
            shared_key="ItsASecret",
            peer_asn=100,
            primary_peer_address_prefix="192.168.1.0/30",
            secondary_peer_address_prefix="192.168.1.0/30",
            vlan_id=100)
        example2_express_route_circuit_peering = azure.network.ExpressRouteCircuitPeering("example2ExpressRouteCircuitPeering",
            peering_type="AzurePrivatePeering",
            express_route_circuit_name=example2_express_route_circuit.name,
            resource_group_name=example_resource_group.name,
            shared_key="ItsASecret",
            peer_asn=100,
            primary_peer_address_prefix="192.168.1.0/30",
            secondary_peer_address_prefix="192.168.1.0/30",
            vlan_id=100)
        example_express_route_circuit_connection = azure.network.ExpressRouteCircuitConnection("exampleExpressRouteCircuitConnection",
            peering_id=example_express_route_circuit_peering.id,
            peer_peering_id=example2_express_route_circuit_peering.id,
            address_prefix_ipv4="192.169.9.0/29",
            authorization_key="846a1918-b7a2-4917-b43c-8c4cdaee006a")
        ```

        ## Import

        Express Route Circuit Connections can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/expressRouteCircuitConnection:ExpressRouteCircuitConnection example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Network/expressRouteCircuits/circuit1/peerings/peering1/connections/connection1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_prefix_ipv4: The IPv4 address space from which to allocate customer address for global reach. Changing this forces a new Express Route Circuit Connection to be created.
        :param pulumi.Input[str] address_prefix_ipv6: The IPv6 address space from which to allocate customer addresses for global reach.
               
               > **NOTE:** `address_prefix_ipv6` cannot be set when ExpressRoute Circuit Connection with ExpressRoute Circuit based on ExpressRoute Port.
        :param pulumi.Input[str] authorization_key: The authorization key which is associated with the Express Route Circuit Connection.
        :param pulumi.Input[str] name: The name which should be used for this Express Route Circuit Connection. Changing this forces a new Express Route Circuit Connection to be created.
        :param pulumi.Input[str] peer_peering_id: The ID of the peered Express Route Circuit Private Peering. Changing this forces a new Express Route Circuit Connection to be created.
        :param pulumi.Input[str] peering_id: The ID of the Express Route Circuit Private Peering that this Express Route Circuit Connection connects with. Changing this forces a new Express Route Circuit Connection to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExpressRouteCircuitConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Express Route Circuit Connection.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_express_route_port = azure.network.ExpressRoutePort("exampleExpressRoutePort",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            peering_location="Equinix-Seattle-SE2",
            bandwidth_in_gbps=10,
            encapsulation="Dot1Q")
        example_express_route_circuit = azure.network.ExpressRouteCircuit("exampleExpressRouteCircuit",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            express_route_port_id=example_express_route_port.id,
            bandwidth_in_gbps=5,
            sku=azure.network.ExpressRouteCircuitSkuArgs(
                tier="Standard",
                family="MeteredData",
            ))
        example2_express_route_port = azure.network.ExpressRoutePort("example2ExpressRoutePort",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            peering_location="Allied-Toronto-King-West",
            bandwidth_in_gbps=10,
            encapsulation="Dot1Q")
        example2_express_route_circuit = azure.network.ExpressRouteCircuit("example2ExpressRouteCircuit",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            express_route_port_id=example2_express_route_port.id,
            bandwidth_in_gbps=5,
            sku=azure.network.ExpressRouteCircuitSkuArgs(
                tier="Standard",
                family="MeteredData",
            ))
        example_express_route_circuit_peering = azure.network.ExpressRouteCircuitPeering("exampleExpressRouteCircuitPeering",
            peering_type="AzurePrivatePeering",
            express_route_circuit_name=example_express_route_circuit.name,
            resource_group_name=example_resource_group.name,
            shared_key="ItsASecret",
            peer_asn=100,
            primary_peer_address_prefix="192.168.1.0/30",
            secondary_peer_address_prefix="192.168.1.0/30",
            vlan_id=100)
        example2_express_route_circuit_peering = azure.network.ExpressRouteCircuitPeering("example2ExpressRouteCircuitPeering",
            peering_type="AzurePrivatePeering",
            express_route_circuit_name=example2_express_route_circuit.name,
            resource_group_name=example_resource_group.name,
            shared_key="ItsASecret",
            peer_asn=100,
            primary_peer_address_prefix="192.168.1.0/30",
            secondary_peer_address_prefix="192.168.1.0/30",
            vlan_id=100)
        example_express_route_circuit_connection = azure.network.ExpressRouteCircuitConnection("exampleExpressRouteCircuitConnection",
            peering_id=example_express_route_circuit_peering.id,
            peer_peering_id=example2_express_route_circuit_peering.id,
            address_prefix_ipv4="192.169.9.0/29",
            authorization_key="846a1918-b7a2-4917-b43c-8c4cdaee006a")
        ```

        ## Import

        Express Route Circuit Connections can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/expressRouteCircuitConnection:ExpressRouteCircuitConnection example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Network/expressRouteCircuits/circuit1/peerings/peering1/connections/connection1
        ```

        :param str resource_name: The name of the resource.
        :param ExpressRouteCircuitConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExpressRouteCircuitConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ExpressRouteCircuitConnectionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_prefix_ipv4: Optional[pulumi.Input[str]] = None,
                 address_prefix_ipv6: Optional[pulumi.Input[str]] = None,
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peer_peering_id: Optional[pulumi.Input[str]] = None,
                 peering_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExpressRouteCircuitConnectionArgs.__new__(ExpressRouteCircuitConnectionArgs)

            if address_prefix_ipv4 is None and not opts.urn:
                raise TypeError("Missing required property 'address_prefix_ipv4'")
            __props__.__dict__["address_prefix_ipv4"] = address_prefix_ipv4
            __props__.__dict__["address_prefix_ipv6"] = address_prefix_ipv6
            __props__.__dict__["authorization_key"] = None if authorization_key is None else pulumi.Output.secret(authorization_key)
            __props__.__dict__["name"] = name
            if peer_peering_id is None and not opts.urn:
                raise TypeError("Missing required property 'peer_peering_id'")
            __props__.__dict__["peer_peering_id"] = peer_peering_id
            if peering_id is None and not opts.urn:
                raise TypeError("Missing required property 'peering_id'")
            __props__.__dict__["peering_id"] = peering_id
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["authorizationKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(ExpressRouteCircuitConnection, __self__).__init__(
            'azure:network/expressRouteCircuitConnection:ExpressRouteCircuitConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address_prefix_ipv4: Optional[pulumi.Input[str]] = None,
            address_prefix_ipv6: Optional[pulumi.Input[str]] = None,
            authorization_key: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            peer_peering_id: Optional[pulumi.Input[str]] = None,
            peering_id: Optional[pulumi.Input[str]] = None) -> 'ExpressRouteCircuitConnection':
        """
        Get an existing ExpressRouteCircuitConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_prefix_ipv4: The IPv4 address space from which to allocate customer address for global reach. Changing this forces a new Express Route Circuit Connection to be created.
        :param pulumi.Input[str] address_prefix_ipv6: The IPv6 address space from which to allocate customer addresses for global reach.
               
               > **NOTE:** `address_prefix_ipv6` cannot be set when ExpressRoute Circuit Connection with ExpressRoute Circuit based on ExpressRoute Port.
        :param pulumi.Input[str] authorization_key: The authorization key which is associated with the Express Route Circuit Connection.
        :param pulumi.Input[str] name: The name which should be used for this Express Route Circuit Connection. Changing this forces a new Express Route Circuit Connection to be created.
        :param pulumi.Input[str] peer_peering_id: The ID of the peered Express Route Circuit Private Peering. Changing this forces a new Express Route Circuit Connection to be created.
        :param pulumi.Input[str] peering_id: The ID of the Express Route Circuit Private Peering that this Express Route Circuit Connection connects with. Changing this forces a new Express Route Circuit Connection to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ExpressRouteCircuitConnectionState.__new__(_ExpressRouteCircuitConnectionState)

        __props__.__dict__["address_prefix_ipv4"] = address_prefix_ipv4
        __props__.__dict__["address_prefix_ipv6"] = address_prefix_ipv6
        __props__.__dict__["authorization_key"] = authorization_key
        __props__.__dict__["name"] = name
        __props__.__dict__["peer_peering_id"] = peer_peering_id
        __props__.__dict__["peering_id"] = peering_id
        return ExpressRouteCircuitConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressPrefixIpv4")
    def address_prefix_ipv4(self) -> pulumi.Output[str]:
        """
        The IPv4 address space from which to allocate customer address for global reach. Changing this forces a new Express Route Circuit Connection to be created.
        """
        return pulumi.get(self, "address_prefix_ipv4")

    @property
    @pulumi.getter(name="addressPrefixIpv6")
    def address_prefix_ipv6(self) -> pulumi.Output[Optional[str]]:
        """
        The IPv6 address space from which to allocate customer addresses for global reach.

        > **NOTE:** `address_prefix_ipv6` cannot be set when ExpressRoute Circuit Connection with ExpressRoute Circuit based on ExpressRoute Port.
        """
        return pulumi.get(self, "address_prefix_ipv6")

    @property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> pulumi.Output[Optional[str]]:
        """
        The authorization key which is associated with the Express Route Circuit Connection.
        """
        return pulumi.get(self, "authorization_key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Express Route Circuit Connection. Changing this forces a new Express Route Circuit Connection to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peerPeeringId")
    def peer_peering_id(self) -> pulumi.Output[str]:
        """
        The ID of the peered Express Route Circuit Private Peering. Changing this forces a new Express Route Circuit Connection to be created.
        """
        return pulumi.get(self, "peer_peering_id")

    @property
    @pulumi.getter(name="peeringId")
    def peering_id(self) -> pulumi.Output[str]:
        """
        The ID of the Express Route Circuit Private Peering that this Express Route Circuit Connection connects with. Changing this forces a new Express Route Circuit Connection to be created.
        """
        return pulumi.get(self, "peering_id")


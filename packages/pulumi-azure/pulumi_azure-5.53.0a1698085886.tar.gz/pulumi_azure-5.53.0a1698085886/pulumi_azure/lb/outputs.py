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

__all__ = [
    'BackendAddressPoolAddressInboundNatRulePortMapping',
    'BackendAddressPoolTunnelInterface',
    'LoadBalancerFrontendIpConfiguration',
    'OutboundRuleFrontendIpConfiguration',
    'GetBackendAddressPoolBackendAddressResult',
    'GetBackendAddressPoolBackendAddressInboundNatRulePortMappingResult',
    'GetBackendAddressPoolBackendIpConfigurationResult',
    'GetLBFrontendIpConfigurationResult',
    'GetLBOutboundRuleFrontendIpConfigurationResult',
]

@pulumi.output_type
class BackendAddressPoolAddressInboundNatRulePortMapping(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "backendPort":
            suggest = "backend_port"
        elif key == "frontendPort":
            suggest = "frontend_port"
        elif key == "inboundNatRuleName":
            suggest = "inbound_nat_rule_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BackendAddressPoolAddressInboundNatRulePortMapping. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BackendAddressPoolAddressInboundNatRulePortMapping.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BackendAddressPoolAddressInboundNatRulePortMapping.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 backend_port: Optional[int] = None,
                 frontend_port: Optional[int] = None,
                 inbound_nat_rule_name: Optional[str] = None):
        """
        :param int backend_port: The Backend Port of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        :param int frontend_port: The Frontend Port of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        :param str inbound_nat_rule_name: The name of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        """
        BackendAddressPoolAddressInboundNatRulePortMapping._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            backend_port=backend_port,
            frontend_port=frontend_port,
            inbound_nat_rule_name=inbound_nat_rule_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             backend_port: Optional[int] = None,
             frontend_port: Optional[int] = None,
             inbound_nat_rule_name: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'backendPort' in kwargs:
            backend_port = kwargs['backendPort']
        if 'frontendPort' in kwargs:
            frontend_port = kwargs['frontendPort']
        if 'inboundNatRuleName' in kwargs:
            inbound_nat_rule_name = kwargs['inboundNatRuleName']

        if backend_port is not None:
            _setter("backend_port", backend_port)
        if frontend_port is not None:
            _setter("frontend_port", frontend_port)
        if inbound_nat_rule_name is not None:
            _setter("inbound_nat_rule_name", inbound_nat_rule_name)

    @property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> Optional[int]:
        """
        The Backend Port of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        """
        return pulumi.get(self, "backend_port")

    @property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> Optional[int]:
        """
        The Frontend Port of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        """
        return pulumi.get(self, "frontend_port")

    @property
    @pulumi.getter(name="inboundNatRuleName")
    def inbound_nat_rule_name(self) -> Optional[str]:
        """
        The name of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        """
        return pulumi.get(self, "inbound_nat_rule_name")


@pulumi.output_type
class BackendAddressPoolTunnelInterface(dict):
    def __init__(__self__, *,
                 identifier: int,
                 port: int,
                 protocol: str,
                 type: str):
        """
        :param int identifier: The unique identifier of this Gateway Lodbalancer Tunnel Interface.
        :param int port: The port number that this Gateway Lodbalancer Tunnel Interface listens to.
        :param str protocol: The protocol used for this Gateway Lodbalancer Tunnel Interface. Possible values are `None`, `Native` and `VXLAN`.
        :param str type: The traffic type of this Gateway Lodbalancer Tunnel Interface. Possible values are `None`, `Internal` and `External`.
        """
        BackendAddressPoolTunnelInterface._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            identifier=identifier,
            port=port,
            protocol=protocol,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             identifier: int,
             port: int,
             protocol: str,
             type: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        _setter("identifier", identifier)
        _setter("port", port)
        _setter("protocol", protocol)
        _setter("type", type)

    @property
    @pulumi.getter
    def identifier(self) -> int:
        """
        The unique identifier of this Gateway Lodbalancer Tunnel Interface.
        """
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        The port number that this Gateway Lodbalancer Tunnel Interface listens to.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        The protocol used for this Gateway Lodbalancer Tunnel Interface. Possible values are `None`, `Native` and `VXLAN`.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The traffic type of this Gateway Lodbalancer Tunnel Interface. Possible values are `None`, `Internal` and `External`.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class LoadBalancerFrontendIpConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "gatewayLoadBalancerFrontendIpConfigurationId":
            suggest = "gateway_load_balancer_frontend_ip_configuration_id"
        elif key == "inboundNatRules":
            suggest = "inbound_nat_rules"
        elif key == "loadBalancerRules":
            suggest = "load_balancer_rules"
        elif key == "outboundRules":
            suggest = "outbound_rules"
        elif key == "privateIpAddress":
            suggest = "private_ip_address"
        elif key == "privateIpAddressAllocation":
            suggest = "private_ip_address_allocation"
        elif key == "privateIpAddressVersion":
            suggest = "private_ip_address_version"
        elif key == "publicIpAddressId":
            suggest = "public_ip_address_id"
        elif key == "publicIpPrefixId":
            suggest = "public_ip_prefix_id"
        elif key == "subnetId":
            suggest = "subnet_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LoadBalancerFrontendIpConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LoadBalancerFrontendIpConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LoadBalancerFrontendIpConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 gateway_load_balancer_frontend_ip_configuration_id: Optional[str] = None,
                 id: Optional[str] = None,
                 inbound_nat_rules: Optional[Sequence[str]] = None,
                 load_balancer_rules: Optional[Sequence[str]] = None,
                 outbound_rules: Optional[Sequence[str]] = None,
                 private_ip_address: Optional[str] = None,
                 private_ip_address_allocation: Optional[str] = None,
                 private_ip_address_version: Optional[str] = None,
                 public_ip_address_id: Optional[str] = None,
                 public_ip_prefix_id: Optional[str] = None,
                 subnet_id: Optional[str] = None,
                 zones: Optional[Sequence[str]] = None):
        """
        :param str name: Specifies the name of the frontend IP configuration.
        :param str gateway_load_balancer_frontend_ip_configuration_id: The Frontend IP Configuration ID of a Gateway SKU Load Balancer.
        :param str id: The id of the Frontend IP Configuration.
        :param Sequence[str] inbound_nat_rules: The list of IDs of inbound rules that use this frontend IP.
        :param Sequence[str] load_balancer_rules: The list of IDs of load balancing rules that use this frontend IP.
        :param Sequence[str] outbound_rules: The list of IDs outbound rules that use this frontend IP.
        :param str private_ip_address: Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.
        :param str private_ip_address_allocation: The allocation method for the Private IP Address used by this Load Balancer. Possible values as `Dynamic` and `Static`.
        :param str private_ip_address_version: The version of IP that the Private IP Address is. Possible values are `IPv4` or `IPv6`.
        :param str public_ip_address_id: The ID of a Public IP Address which should be associated with the Load Balancer.
        :param str public_ip_prefix_id: The ID of a Public IP Prefix which should be associated with the Load Balancer. Public IP Prefix can only be used with outbound rules.
        :param str subnet_id: The ID of the Subnet which should be associated with the IP Configuration.
        :param Sequence[str] zones: Specifies a list of Availability Zones in which the IP Address for this Load Balancer should be located.
               
               > **NOTE:** Availability Zones are only supported with a [Standard SKU](https://docs.microsoft.com/azure/load-balancer/load-balancer-standard-availability-zones) and [in select regions](https://docs.microsoft.com/azure/availability-zones/az-overview) at this time.
        """
        LoadBalancerFrontendIpConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            gateway_load_balancer_frontend_ip_configuration_id=gateway_load_balancer_frontend_ip_configuration_id,
            id=id,
            inbound_nat_rules=inbound_nat_rules,
            load_balancer_rules=load_balancer_rules,
            outbound_rules=outbound_rules,
            private_ip_address=private_ip_address,
            private_ip_address_allocation=private_ip_address_allocation,
            private_ip_address_version=private_ip_address_version,
            public_ip_address_id=public_ip_address_id,
            public_ip_prefix_id=public_ip_prefix_id,
            subnet_id=subnet_id,
            zones=zones,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: str,
             gateway_load_balancer_frontend_ip_configuration_id: Optional[str] = None,
             id: Optional[str] = None,
             inbound_nat_rules: Optional[Sequence[str]] = None,
             load_balancer_rules: Optional[Sequence[str]] = None,
             outbound_rules: Optional[Sequence[str]] = None,
             private_ip_address: Optional[str] = None,
             private_ip_address_allocation: Optional[str] = None,
             private_ip_address_version: Optional[str] = None,
             public_ip_address_id: Optional[str] = None,
             public_ip_prefix_id: Optional[str] = None,
             subnet_id: Optional[str] = None,
             zones: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'gatewayLoadBalancerFrontendIpConfigurationId' in kwargs:
            gateway_load_balancer_frontend_ip_configuration_id = kwargs['gatewayLoadBalancerFrontendIpConfigurationId']
        if 'inboundNatRules' in kwargs:
            inbound_nat_rules = kwargs['inboundNatRules']
        if 'loadBalancerRules' in kwargs:
            load_balancer_rules = kwargs['loadBalancerRules']
        if 'outboundRules' in kwargs:
            outbound_rules = kwargs['outboundRules']
        if 'privateIpAddress' in kwargs:
            private_ip_address = kwargs['privateIpAddress']
        if 'privateIpAddressAllocation' in kwargs:
            private_ip_address_allocation = kwargs['privateIpAddressAllocation']
        if 'privateIpAddressVersion' in kwargs:
            private_ip_address_version = kwargs['privateIpAddressVersion']
        if 'publicIpAddressId' in kwargs:
            public_ip_address_id = kwargs['publicIpAddressId']
        if 'publicIpPrefixId' in kwargs:
            public_ip_prefix_id = kwargs['publicIpPrefixId']
        if 'subnetId' in kwargs:
            subnet_id = kwargs['subnetId']

        _setter("name", name)
        if gateway_load_balancer_frontend_ip_configuration_id is not None:
            _setter("gateway_load_balancer_frontend_ip_configuration_id", gateway_load_balancer_frontend_ip_configuration_id)
        if id is not None:
            _setter("id", id)
        if inbound_nat_rules is not None:
            _setter("inbound_nat_rules", inbound_nat_rules)
        if load_balancer_rules is not None:
            _setter("load_balancer_rules", load_balancer_rules)
        if outbound_rules is not None:
            _setter("outbound_rules", outbound_rules)
        if private_ip_address is not None:
            _setter("private_ip_address", private_ip_address)
        if private_ip_address_allocation is not None:
            _setter("private_ip_address_allocation", private_ip_address_allocation)
        if private_ip_address_version is not None:
            _setter("private_ip_address_version", private_ip_address_version)
        if public_ip_address_id is not None:
            _setter("public_ip_address_id", public_ip_address_id)
        if public_ip_prefix_id is not None:
            _setter("public_ip_prefix_id", public_ip_prefix_id)
        if subnet_id is not None:
            _setter("subnet_id", subnet_id)
        if zones is not None:
            _setter("zones", zones)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Specifies the name of the frontend IP configuration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="gatewayLoadBalancerFrontendIpConfigurationId")
    def gateway_load_balancer_frontend_ip_configuration_id(self) -> Optional[str]:
        """
        The Frontend IP Configuration ID of a Gateway SKU Load Balancer.
        """
        return pulumi.get(self, "gateway_load_balancer_frontend_ip_configuration_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The id of the Frontend IP Configuration.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="inboundNatRules")
    def inbound_nat_rules(self) -> Optional[Sequence[str]]:
        """
        The list of IDs of inbound rules that use this frontend IP.
        """
        return pulumi.get(self, "inbound_nat_rules")

    @property
    @pulumi.getter(name="loadBalancerRules")
    def load_balancer_rules(self) -> Optional[Sequence[str]]:
        """
        The list of IDs of load balancing rules that use this frontend IP.
        """
        return pulumi.get(self, "load_balancer_rules")

    @property
    @pulumi.getter(name="outboundRules")
    def outbound_rules(self) -> Optional[Sequence[str]]:
        """
        The list of IDs outbound rules that use this frontend IP.
        """
        return pulumi.get(self, "outbound_rules")

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[str]:
        """
        Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.
        """
        return pulumi.get(self, "private_ip_address")

    @property
    @pulumi.getter(name="privateIpAddressAllocation")
    def private_ip_address_allocation(self) -> Optional[str]:
        """
        The allocation method for the Private IP Address used by this Load Balancer. Possible values as `Dynamic` and `Static`.
        """
        return pulumi.get(self, "private_ip_address_allocation")

    @property
    @pulumi.getter(name="privateIpAddressVersion")
    def private_ip_address_version(self) -> Optional[str]:
        """
        The version of IP that the Private IP Address is. Possible values are `IPv4` or `IPv6`.
        """
        return pulumi.get(self, "private_ip_address_version")

    @property
    @pulumi.getter(name="publicIpAddressId")
    def public_ip_address_id(self) -> Optional[str]:
        """
        The ID of a Public IP Address which should be associated with the Load Balancer.
        """
        return pulumi.get(self, "public_ip_address_id")

    @property
    @pulumi.getter(name="publicIpPrefixId")
    def public_ip_prefix_id(self) -> Optional[str]:
        """
        The ID of a Public IP Prefix which should be associated with the Load Balancer. Public IP Prefix can only be used with outbound rules.
        """
        return pulumi.get(self, "public_ip_prefix_id")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[str]:
        """
        The ID of the Subnet which should be associated with the IP Configuration.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[str]]:
        """
        Specifies a list of Availability Zones in which the IP Address for this Load Balancer should be located.

        > **NOTE:** Availability Zones are only supported with a [Standard SKU](https://docs.microsoft.com/azure/load-balancer/load-balancer-standard-availability-zones) and [in select regions](https://docs.microsoft.com/azure/availability-zones/az-overview) at this time.
        """
        return pulumi.get(self, "zones")


@pulumi.output_type
class OutboundRuleFrontendIpConfiguration(dict):
    def __init__(__self__, *,
                 name: str,
                 id: Optional[str] = None):
        """
        :param str name: The name of the Frontend IP Configuration.
        :param str id: The ID of the Load Balancer Outbound Rule.
        """
        OutboundRuleFrontendIpConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            id=id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: str,
             id: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        _setter("name", name)
        if id is not None:
            _setter("id", id)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Frontend IP Configuration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The ID of the Load Balancer Outbound Rule.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class GetBackendAddressPoolBackendAddressResult(dict):
    def __init__(__self__, *,
                 inbound_nat_rule_port_mappings: Sequence['outputs.GetBackendAddressPoolBackendAddressInboundNatRulePortMappingResult'],
                 ip_address: str,
                 name: str,
                 virtual_network_id: str):
        """
        :param Sequence['GetBackendAddressPoolBackendAddressInboundNatRulePortMappingArgs'] inbound_nat_rule_port_mappings: A list of `inbound_nat_rule_port_mapping` block as defined below.
        :param str ip_address: The Static IP address for this Load Balancer within the Virtual Network.
        :param str name: Specifies the name of the Backend Address Pool.
        :param str virtual_network_id: The ID of the Virtual Network where the Backend Address of the Load Balancer exists.
        """
        GetBackendAddressPoolBackendAddressResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            inbound_nat_rule_port_mappings=inbound_nat_rule_port_mappings,
            ip_address=ip_address,
            name=name,
            virtual_network_id=virtual_network_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             inbound_nat_rule_port_mappings: Sequence['outputs.GetBackendAddressPoolBackendAddressInboundNatRulePortMappingResult'],
             ip_address: str,
             name: str,
             virtual_network_id: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'inboundNatRulePortMappings' in kwargs:
            inbound_nat_rule_port_mappings = kwargs['inboundNatRulePortMappings']
        if 'ipAddress' in kwargs:
            ip_address = kwargs['ipAddress']
        if 'virtualNetworkId' in kwargs:
            virtual_network_id = kwargs['virtualNetworkId']

        _setter("inbound_nat_rule_port_mappings", inbound_nat_rule_port_mappings)
        _setter("ip_address", ip_address)
        _setter("name", name)
        _setter("virtual_network_id", virtual_network_id)

    @property
    @pulumi.getter(name="inboundNatRulePortMappings")
    def inbound_nat_rule_port_mappings(self) -> Sequence['outputs.GetBackendAddressPoolBackendAddressInboundNatRulePortMappingResult']:
        """
        A list of `inbound_nat_rule_port_mapping` block as defined below.
        """
        return pulumi.get(self, "inbound_nat_rule_port_mappings")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> str:
        """
        The Static IP address for this Load Balancer within the Virtual Network.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Specifies the name of the Backend Address Pool.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="virtualNetworkId")
    def virtual_network_id(self) -> str:
        """
        The ID of the Virtual Network where the Backend Address of the Load Balancer exists.
        """
        return pulumi.get(self, "virtual_network_id")


@pulumi.output_type
class GetBackendAddressPoolBackendAddressInboundNatRulePortMappingResult(dict):
    def __init__(__self__, *,
                 backend_port: int,
                 frontend_port: int,
                 inbound_nat_rule_name: str):
        """
        :param int backend_port: The Backend Port of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        :param int frontend_port: The Frontend Port of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        :param str inbound_nat_rule_name: The name of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        """
        GetBackendAddressPoolBackendAddressInboundNatRulePortMappingResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            backend_port=backend_port,
            frontend_port=frontend_port,
            inbound_nat_rule_name=inbound_nat_rule_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             backend_port: int,
             frontend_port: int,
             inbound_nat_rule_name: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'backendPort' in kwargs:
            backend_port = kwargs['backendPort']
        if 'frontendPort' in kwargs:
            frontend_port = kwargs['frontendPort']
        if 'inboundNatRuleName' in kwargs:
            inbound_nat_rule_name = kwargs['inboundNatRuleName']

        _setter("backend_port", backend_port)
        _setter("frontend_port", frontend_port)
        _setter("inbound_nat_rule_name", inbound_nat_rule_name)

    @property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> int:
        """
        The Backend Port of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        """
        return pulumi.get(self, "backend_port")

    @property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> int:
        """
        The Frontend Port of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        """
        return pulumi.get(self, "frontend_port")

    @property
    @pulumi.getter(name="inboundNatRuleName")
    def inbound_nat_rule_name(self) -> str:
        """
        The name of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        """
        return pulumi.get(self, "inbound_nat_rule_name")


@pulumi.output_type
class GetBackendAddressPoolBackendIpConfigurationResult(dict):
    def __init__(__self__, *,
                 id: str):
        """
        :param str id: The ID of the Backend Address Pool.
        """
        GetBackendAddressPoolBackendIpConfigurationResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            id=id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             id: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        _setter("id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Backend Address Pool.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class GetLBFrontendIpConfigurationResult(dict):
    def __init__(__self__, *,
                 id: str,
                 name: str,
                 private_ip_address: str,
                 private_ip_address_allocation: str,
                 private_ip_address_version: str,
                 public_ip_address_id: str,
                 subnet_id: str,
                 zones: Sequence[str]):
        """
        :param str id: The id of the Frontend IP Configuration.
        :param str name: Specifies the name of the Load Balancer.
        :param str private_ip_address: Private IP Address to assign to the Load Balancer.
        :param str private_ip_address_allocation: The allocation method for the Private IP Address used by this Load Balancer.
        :param str private_ip_address_version: The Private IP Address Version, either `IPv4` or `IPv6`.
        :param str public_ip_address_id: The ID of a  Public IP Address which is associated with this Load Balancer.
        :param str subnet_id: The ID of the Subnet which is associated with the IP Configuration.
        :param Sequence[str] zones: A list of Availability Zones which the Load Balancer's IP Addresses should be created in.
        """
        GetLBFrontendIpConfigurationResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            id=id,
            name=name,
            private_ip_address=private_ip_address,
            private_ip_address_allocation=private_ip_address_allocation,
            private_ip_address_version=private_ip_address_version,
            public_ip_address_id=public_ip_address_id,
            subnet_id=subnet_id,
            zones=zones,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             id: str,
             name: str,
             private_ip_address: str,
             private_ip_address_allocation: str,
             private_ip_address_version: str,
             public_ip_address_id: str,
             subnet_id: str,
             zones: Sequence[str],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'privateIpAddress' in kwargs:
            private_ip_address = kwargs['privateIpAddress']
        if 'privateIpAddressAllocation' in kwargs:
            private_ip_address_allocation = kwargs['privateIpAddressAllocation']
        if 'privateIpAddressVersion' in kwargs:
            private_ip_address_version = kwargs['privateIpAddressVersion']
        if 'publicIpAddressId' in kwargs:
            public_ip_address_id = kwargs['publicIpAddressId']
        if 'subnetId' in kwargs:
            subnet_id = kwargs['subnetId']

        _setter("id", id)
        _setter("name", name)
        _setter("private_ip_address", private_ip_address)
        _setter("private_ip_address_allocation", private_ip_address_allocation)
        _setter("private_ip_address_version", private_ip_address_version)
        _setter("public_ip_address_id", public_ip_address_id)
        _setter("subnet_id", subnet_id)
        _setter("zones", zones)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the Frontend IP Configuration.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Specifies the name of the Load Balancer.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> str:
        """
        Private IP Address to assign to the Load Balancer.
        """
        return pulumi.get(self, "private_ip_address")

    @property
    @pulumi.getter(name="privateIpAddressAllocation")
    def private_ip_address_allocation(self) -> str:
        """
        The allocation method for the Private IP Address used by this Load Balancer.
        """
        return pulumi.get(self, "private_ip_address_allocation")

    @property
    @pulumi.getter(name="privateIpAddressVersion")
    def private_ip_address_version(self) -> str:
        """
        The Private IP Address Version, either `IPv4` or `IPv6`.
        """
        return pulumi.get(self, "private_ip_address_version")

    @property
    @pulumi.getter(name="publicIpAddressId")
    def public_ip_address_id(self) -> str:
        """
        The ID of a  Public IP Address which is associated with this Load Balancer.
        """
        return pulumi.get(self, "public_ip_address_id")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The ID of the Subnet which is associated with the IP Configuration.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def zones(self) -> Sequence[str]:
        """
        A list of Availability Zones which the Load Balancer's IP Addresses should be created in.
        """
        return pulumi.get(self, "zones")


@pulumi.output_type
class GetLBOutboundRuleFrontendIpConfigurationResult(dict):
    def __init__(__self__, *,
                 id: str,
                 name: str):
        """
        :param str id: The ID of the Frontend IP Configuration.
        :param str name: The name of this Load Balancer Outbound Rule.
        """
        GetLBOutboundRuleFrontendIpConfigurationResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            id=id,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             id: str,
             name: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        _setter("id", id)
        _setter("name", name)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Frontend IP Configuration.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of this Load Balancer Outbound Rule.
        """
        return pulumi.get(self, "name")



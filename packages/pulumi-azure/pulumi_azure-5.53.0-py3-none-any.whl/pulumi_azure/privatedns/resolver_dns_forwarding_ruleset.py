# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ResolverDnsForwardingRulesetArgs', 'ResolverDnsForwardingRuleset']

@pulumi.input_type
class ResolverDnsForwardingRulesetArgs:
    def __init__(__self__, *,
                 private_dns_resolver_outbound_endpoint_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ResolverDnsForwardingRuleset resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] private_dns_resolver_outbound_endpoint_ids: The list of IDs of the Private DNS Resolver Outbound Endpoint that is linked to the Private DNS Resolver Dns Forwarding Ruleset.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group where the Private DNS Resolver Dns Forwarding Ruleset should exist. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Private DNS Resolver Dns Forwarding Ruleset should exist. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Private DNS Resolver Dns Forwarding Ruleset. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the Private DNS Resolver Dns Forwarding Ruleset.
        """
        ResolverDnsForwardingRulesetArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            private_dns_resolver_outbound_endpoint_ids=private_dns_resolver_outbound_endpoint_ids,
            resource_group_name=resource_group_name,
            location=location,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             private_dns_resolver_outbound_endpoint_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
             resource_group_name: pulumi.Input[str],
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'privateDnsResolverOutboundEndpointIds' in kwargs:
            private_dns_resolver_outbound_endpoint_ids = kwargs['privateDnsResolverOutboundEndpointIds']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']

        _setter("private_dns_resolver_outbound_endpoint_ids", private_dns_resolver_outbound_endpoint_ids)
        _setter("resource_group_name", resource_group_name)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="privateDnsResolverOutboundEndpointIds")
    def private_dns_resolver_outbound_endpoint_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of IDs of the Private DNS Resolver Outbound Endpoint that is linked to the Private DNS Resolver Dns Forwarding Ruleset.
        """
        return pulumi.get(self, "private_dns_resolver_outbound_endpoint_ids")

    @private_dns_resolver_outbound_endpoint_ids.setter
    def private_dns_resolver_outbound_endpoint_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "private_dns_resolver_outbound_endpoint_ids", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Specifies the name of the Resource Group where the Private DNS Resolver Dns Forwarding Ruleset should exist. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Azure Region where the Private DNS Resolver Dns Forwarding Ruleset should exist. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name which should be used for this Private DNS Resolver Dns Forwarding Ruleset. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the Private DNS Resolver Dns Forwarding Ruleset.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _ResolverDnsForwardingRulesetState:
    def __init__(__self__, *,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_dns_resolver_outbound_endpoint_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering ResolverDnsForwardingRuleset resources.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Private DNS Resolver Dns Forwarding Ruleset should exist. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Private DNS Resolver Dns Forwarding Ruleset. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] private_dns_resolver_outbound_endpoint_ids: The list of IDs of the Private DNS Resolver Outbound Endpoint that is linked to the Private DNS Resolver Dns Forwarding Ruleset.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group where the Private DNS Resolver Dns Forwarding Ruleset should exist. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the Private DNS Resolver Dns Forwarding Ruleset.
        """
        _ResolverDnsForwardingRulesetState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            location=location,
            name=name,
            private_dns_resolver_outbound_endpoint_ids=private_dns_resolver_outbound_endpoint_ids,
            resource_group_name=resource_group_name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             private_dns_resolver_outbound_endpoint_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'privateDnsResolverOutboundEndpointIds' in kwargs:
            private_dns_resolver_outbound_endpoint_ids = kwargs['privateDnsResolverOutboundEndpointIds']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']

        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if private_dns_resolver_outbound_endpoint_ids is not None:
            _setter("private_dns_resolver_outbound_endpoint_ids", private_dns_resolver_outbound_endpoint_ids)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Azure Region where the Private DNS Resolver Dns Forwarding Ruleset should exist. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name which should be used for this Private DNS Resolver Dns Forwarding Ruleset. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="privateDnsResolverOutboundEndpointIds")
    def private_dns_resolver_outbound_endpoint_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of IDs of the Private DNS Resolver Outbound Endpoint that is linked to the Private DNS Resolver Dns Forwarding Ruleset.
        """
        return pulumi.get(self, "private_dns_resolver_outbound_endpoint_ids")

    @private_dns_resolver_outbound_endpoint_ids.setter
    def private_dns_resolver_outbound_endpoint_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "private_dns_resolver_outbound_endpoint_ids", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Resource Group where the Private DNS Resolver Dns Forwarding Ruleset should exist. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the Private DNS Resolver Dns Forwarding Ruleset.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class ResolverDnsForwardingRuleset(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_dns_resolver_outbound_endpoint_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages a Private DNS Resolver Dns Forwarding Ruleset.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="west europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            address_spaces=["10.0.0.0/16"])
        example_subnet = azure.network.Subnet("exampleSubnet",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.0.0.64/28"],
            delegations=[azure.network.SubnetDelegationArgs(
                name="Microsoft.Network.dnsResolvers",
                service_delegation=azure.network.SubnetDelegationServiceDelegationArgs(
                    actions=["Microsoft.Network/virtualNetworks/subnets/join/action"],
                    name="Microsoft.Network/dnsResolvers",
                ),
            )])
        example_resolver = azure.privatedns.Resolver("exampleResolver",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            virtual_network_id=example_virtual_network.id)
        example_resolver_outbound_endpoint = azure.privatedns.ResolverOutboundEndpoint("exampleResolverOutboundEndpoint",
            private_dns_resolver_id=example_resolver.id,
            location=example_resolver.location,
            subnet_id=example_subnet.id,
            tags={
                "key": "value",
            })
        example_resolver_dns_forwarding_ruleset = azure.privatedns.ResolverDnsForwardingRuleset("exampleResolverDnsForwardingRuleset",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            private_dns_resolver_outbound_endpoint_ids=[example_resolver_outbound_endpoint.id],
            tags={
                "key": "value",
            })
        ```

        ## Import

        Private DNS Resolver Dns Forwarding Ruleset can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:privatedns/resolverDnsForwardingRuleset:ResolverDnsForwardingRuleset example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resourceGroup1/providers/Microsoft.Network/dnsForwardingRulesets/dnsForwardingRuleset1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Private DNS Resolver Dns Forwarding Ruleset should exist. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Private DNS Resolver Dns Forwarding Ruleset. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] private_dns_resolver_outbound_endpoint_ids: The list of IDs of the Private DNS Resolver Outbound Endpoint that is linked to the Private DNS Resolver Dns Forwarding Ruleset.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group where the Private DNS Resolver Dns Forwarding Ruleset should exist. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the Private DNS Resolver Dns Forwarding Ruleset.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResolverDnsForwardingRulesetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Private DNS Resolver Dns Forwarding Ruleset.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="west europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            address_spaces=["10.0.0.0/16"])
        example_subnet = azure.network.Subnet("exampleSubnet",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.0.0.64/28"],
            delegations=[azure.network.SubnetDelegationArgs(
                name="Microsoft.Network.dnsResolvers",
                service_delegation=azure.network.SubnetDelegationServiceDelegationArgs(
                    actions=["Microsoft.Network/virtualNetworks/subnets/join/action"],
                    name="Microsoft.Network/dnsResolvers",
                ),
            )])
        example_resolver = azure.privatedns.Resolver("exampleResolver",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            virtual_network_id=example_virtual_network.id)
        example_resolver_outbound_endpoint = azure.privatedns.ResolverOutboundEndpoint("exampleResolverOutboundEndpoint",
            private_dns_resolver_id=example_resolver.id,
            location=example_resolver.location,
            subnet_id=example_subnet.id,
            tags={
                "key": "value",
            })
        example_resolver_dns_forwarding_ruleset = azure.privatedns.ResolverDnsForwardingRuleset("exampleResolverDnsForwardingRuleset",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            private_dns_resolver_outbound_endpoint_ids=[example_resolver_outbound_endpoint.id],
            tags={
                "key": "value",
            })
        ```

        ## Import

        Private DNS Resolver Dns Forwarding Ruleset can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:privatedns/resolverDnsForwardingRuleset:ResolverDnsForwardingRuleset example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resourceGroup1/providers/Microsoft.Network/dnsForwardingRulesets/dnsForwardingRuleset1
        ```

        :param str resource_name: The name of the resource.
        :param ResolverDnsForwardingRulesetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResolverDnsForwardingRulesetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ResolverDnsForwardingRulesetArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_dns_resolver_outbound_endpoint_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResolverDnsForwardingRulesetArgs.__new__(ResolverDnsForwardingRulesetArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if private_dns_resolver_outbound_endpoint_ids is None and not opts.urn:
                raise TypeError("Missing required property 'private_dns_resolver_outbound_endpoint_ids'")
            __props__.__dict__["private_dns_resolver_outbound_endpoint_ids"] = private_dns_resolver_outbound_endpoint_ids
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
        super(ResolverDnsForwardingRuleset, __self__).__init__(
            'azure:privatedns/resolverDnsForwardingRuleset:ResolverDnsForwardingRuleset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            private_dns_resolver_outbound_endpoint_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'ResolverDnsForwardingRuleset':
        """
        Get an existing ResolverDnsForwardingRuleset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Private DNS Resolver Dns Forwarding Ruleset should exist. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Private DNS Resolver Dns Forwarding Ruleset. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] private_dns_resolver_outbound_endpoint_ids: The list of IDs of the Private DNS Resolver Outbound Endpoint that is linked to the Private DNS Resolver Dns Forwarding Ruleset.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group where the Private DNS Resolver Dns Forwarding Ruleset should exist. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the Private DNS Resolver Dns Forwarding Ruleset.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ResolverDnsForwardingRulesetState.__new__(_ResolverDnsForwardingRulesetState)

        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["private_dns_resolver_outbound_endpoint_ids"] = private_dns_resolver_outbound_endpoint_ids
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["tags"] = tags
        return ResolverDnsForwardingRuleset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the Azure Region where the Private DNS Resolver Dns Forwarding Ruleset should exist. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name which should be used for this Private DNS Resolver Dns Forwarding Ruleset. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateDnsResolverOutboundEndpointIds")
    def private_dns_resolver_outbound_endpoint_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of IDs of the Private DNS Resolver Outbound Endpoint that is linked to the Private DNS Resolver Dns Forwarding Ruleset.
        """
        return pulumi.get(self, "private_dns_resolver_outbound_endpoint_ids")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Resource Group where the Private DNS Resolver Dns Forwarding Ruleset should exist. Changing this forces a new Private DNS Resolver Dns Forwarding Ruleset to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the Private DNS Resolver Dns Forwarding Ruleset.
        """
        return pulumi.get(self, "tags")


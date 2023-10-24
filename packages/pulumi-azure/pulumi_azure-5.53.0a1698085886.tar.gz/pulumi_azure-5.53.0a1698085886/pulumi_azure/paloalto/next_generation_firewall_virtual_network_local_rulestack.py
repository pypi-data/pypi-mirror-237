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

__all__ = ['NextGenerationFirewallVirtualNetworkLocalRulestackArgs', 'NextGenerationFirewallVirtualNetworkLocalRulestack']

@pulumi.input_type
class NextGenerationFirewallVirtualNetworkLocalRulestackArgs:
    def __init__(__self__, *,
                 network_profile: pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfileArgs'],
                 resource_group_name: pulumi.Input[str],
                 rulestack_id: pulumi.Input[str],
                 destination_nats: Optional[pulumi.Input[Sequence[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDestinationNatArgs']]]] = None,
                 dns_settings: Optional[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettingsArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a NextGenerationFirewallVirtualNetworkLocalRulestack resource.
        :param pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfileArgs'] network_profile: A `network_profile` block as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Palo Alto Next Generation Firewall Virtual Network Local Rulestack should exist. Changing this forces a new Palo Alto Next Generation Firewall Virtual Network Local Rulestack to be created.
        :param pulumi.Input[str] rulestack_id: The ID of the Local Rulestack which will be used to configure this Firewall Resource.
        :param pulumi.Input[Sequence[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDestinationNatArgs']]] destination_nats: One or more `destination_nat` blocks as defined below.
        :param pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettingsArgs'] dns_settings: A `dns_settings` block as defined below.
        :param pulumi.Input[str] name: The name which should be used for this Palo Alto Next Generation Firewall Virtual Network Local Rulestack. Changing this forces a new Palo Alto Next Generation Firewall Virtual Network Local Rulestack to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Palo Alto Next Generation Firewall Virtual Network Local Rulestack.
        """
        NextGenerationFirewallVirtualNetworkLocalRulestackArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            network_profile=network_profile,
            resource_group_name=resource_group_name,
            rulestack_id=rulestack_id,
            destination_nats=destination_nats,
            dns_settings=dns_settings,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             network_profile: pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfileArgs'],
             resource_group_name: pulumi.Input[str],
             rulestack_id: pulumi.Input[str],
             destination_nats: Optional[pulumi.Input[Sequence[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDestinationNatArgs']]]] = None,
             dns_settings: Optional[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettingsArgs']] = None,
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'networkProfile' in kwargs:
            network_profile = kwargs['networkProfile']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'rulestackId' in kwargs:
            rulestack_id = kwargs['rulestackId']
        if 'destinationNats' in kwargs:
            destination_nats = kwargs['destinationNats']
        if 'dnsSettings' in kwargs:
            dns_settings = kwargs['dnsSettings']

        _setter("network_profile", network_profile)
        _setter("resource_group_name", resource_group_name)
        _setter("rulestack_id", rulestack_id)
        if destination_nats is not None:
            _setter("destination_nats", destination_nats)
        if dns_settings is not None:
            _setter("dns_settings", dns_settings)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfileArgs']:
        """
        A `network_profile` block as defined below.
        """
        return pulumi.get(self, "network_profile")

    @network_profile.setter
    def network_profile(self, value: pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfileArgs']):
        pulumi.set(self, "network_profile", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group where the Palo Alto Next Generation Firewall Virtual Network Local Rulestack should exist. Changing this forces a new Palo Alto Next Generation Firewall Virtual Network Local Rulestack to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="rulestackId")
    def rulestack_id(self) -> pulumi.Input[str]:
        """
        The ID of the Local Rulestack which will be used to configure this Firewall Resource.
        """
        return pulumi.get(self, "rulestack_id")

    @rulestack_id.setter
    def rulestack_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "rulestack_id", value)

    @property
    @pulumi.getter(name="destinationNats")
    def destination_nats(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDestinationNatArgs']]]]:
        """
        One or more `destination_nat` blocks as defined below.
        """
        return pulumi.get(self, "destination_nats")

    @destination_nats.setter
    def destination_nats(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDestinationNatArgs']]]]):
        pulumi.set(self, "destination_nats", value)

    @property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettingsArgs']]:
        """
        A `dns_settings` block as defined below.
        """
        return pulumi.get(self, "dns_settings")

    @dns_settings.setter
    def dns_settings(self, value: Optional[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettingsArgs']]):
        pulumi.set(self, "dns_settings", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Palo Alto Next Generation Firewall Virtual Network Local Rulestack. Changing this forces a new Palo Alto Next Generation Firewall Virtual Network Local Rulestack to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Palo Alto Next Generation Firewall Virtual Network Local Rulestack.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _NextGenerationFirewallVirtualNetworkLocalRulestackState:
    def __init__(__self__, *,
                 destination_nats: Optional[pulumi.Input[Sequence[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDestinationNatArgs']]]] = None,
                 dns_settings: Optional[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettingsArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfileArgs']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rulestack_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering NextGenerationFirewallVirtualNetworkLocalRulestack resources.
        :param pulumi.Input[Sequence[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDestinationNatArgs']]] destination_nats: One or more `destination_nat` blocks as defined below.
        :param pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettingsArgs'] dns_settings: A `dns_settings` block as defined below.
        :param pulumi.Input[str] name: The name which should be used for this Palo Alto Next Generation Firewall Virtual Network Local Rulestack. Changing this forces a new Palo Alto Next Generation Firewall Virtual Network Local Rulestack to be created.
        :param pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfileArgs'] network_profile: A `network_profile` block as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Palo Alto Next Generation Firewall Virtual Network Local Rulestack should exist. Changing this forces a new Palo Alto Next Generation Firewall Virtual Network Local Rulestack to be created.
        :param pulumi.Input[str] rulestack_id: The ID of the Local Rulestack which will be used to configure this Firewall Resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Palo Alto Next Generation Firewall Virtual Network Local Rulestack.
        """
        _NextGenerationFirewallVirtualNetworkLocalRulestackState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            destination_nats=destination_nats,
            dns_settings=dns_settings,
            name=name,
            network_profile=network_profile,
            resource_group_name=resource_group_name,
            rulestack_id=rulestack_id,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             destination_nats: Optional[pulumi.Input[Sequence[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDestinationNatArgs']]]] = None,
             dns_settings: Optional[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettingsArgs']] = None,
             name: Optional[pulumi.Input[str]] = None,
             network_profile: Optional[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfileArgs']] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             rulestack_id: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'destinationNats' in kwargs:
            destination_nats = kwargs['destinationNats']
        if 'dnsSettings' in kwargs:
            dns_settings = kwargs['dnsSettings']
        if 'networkProfile' in kwargs:
            network_profile = kwargs['networkProfile']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'rulestackId' in kwargs:
            rulestack_id = kwargs['rulestackId']

        if destination_nats is not None:
            _setter("destination_nats", destination_nats)
        if dns_settings is not None:
            _setter("dns_settings", dns_settings)
        if name is not None:
            _setter("name", name)
        if network_profile is not None:
            _setter("network_profile", network_profile)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if rulestack_id is not None:
            _setter("rulestack_id", rulestack_id)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="destinationNats")
    def destination_nats(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDestinationNatArgs']]]]:
        """
        One or more `destination_nat` blocks as defined below.
        """
        return pulumi.get(self, "destination_nats")

    @destination_nats.setter
    def destination_nats(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDestinationNatArgs']]]]):
        pulumi.set(self, "destination_nats", value)

    @property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettingsArgs']]:
        """
        A `dns_settings` block as defined below.
        """
        return pulumi.get(self, "dns_settings")

    @dns_settings.setter
    def dns_settings(self, value: Optional[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettingsArgs']]):
        pulumi.set(self, "dns_settings", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Palo Alto Next Generation Firewall Virtual Network Local Rulestack. Changing this forces a new Palo Alto Next Generation Firewall Virtual Network Local Rulestack to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfileArgs']]:
        """
        A `network_profile` block as defined below.
        """
        return pulumi.get(self, "network_profile")

    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input['NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfileArgs']]):
        pulumi.set(self, "network_profile", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group where the Palo Alto Next Generation Firewall Virtual Network Local Rulestack should exist. Changing this forces a new Palo Alto Next Generation Firewall Virtual Network Local Rulestack to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="rulestackId")
    def rulestack_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Local Rulestack which will be used to configure this Firewall Resource.
        """
        return pulumi.get(self, "rulestack_id")

    @rulestack_id.setter
    def rulestack_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rulestack_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Palo Alto Next Generation Firewall Virtual Network Local Rulestack.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class NextGenerationFirewallVirtualNetworkLocalRulestack(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_nats: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NextGenerationFirewallVirtualNetworkLocalRulestackDestinationNatArgs']]]]] = None,
                 dns_settings: Optional[pulumi.Input[pulumi.InputType['NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettingsArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfileArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rulestack_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages a Palo Alto Next Generation Firewall Deployed in a Virtual Network and configured via a Local Rulestack.

        ## Import

        Palo Alto Next Generation Firewall Virtual Network Local Rulestacks can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:paloalto/nextGenerationFirewallVirtualNetworkLocalRulestack:NextGenerationFirewallVirtualNetworkLocalRulestack example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/PaloAltoNetworks.Cloudngfw/firewalls/myVNetRulestackFW
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NextGenerationFirewallVirtualNetworkLocalRulestackDestinationNatArgs']]]] destination_nats: One or more `destination_nat` blocks as defined below.
        :param pulumi.Input[pulumi.InputType['NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettingsArgs']] dns_settings: A `dns_settings` block as defined below.
        :param pulumi.Input[str] name: The name which should be used for this Palo Alto Next Generation Firewall Virtual Network Local Rulestack. Changing this forces a new Palo Alto Next Generation Firewall Virtual Network Local Rulestack to be created.
        :param pulumi.Input[pulumi.InputType['NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfileArgs']] network_profile: A `network_profile` block as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Palo Alto Next Generation Firewall Virtual Network Local Rulestack should exist. Changing this forces a new Palo Alto Next Generation Firewall Virtual Network Local Rulestack to be created.
        :param pulumi.Input[str] rulestack_id: The ID of the Local Rulestack which will be used to configure this Firewall Resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Palo Alto Next Generation Firewall Virtual Network Local Rulestack.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NextGenerationFirewallVirtualNetworkLocalRulestackArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Palo Alto Next Generation Firewall Deployed in a Virtual Network and configured via a Local Rulestack.

        ## Import

        Palo Alto Next Generation Firewall Virtual Network Local Rulestacks can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:paloalto/nextGenerationFirewallVirtualNetworkLocalRulestack:NextGenerationFirewallVirtualNetworkLocalRulestack example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/PaloAltoNetworks.Cloudngfw/firewalls/myVNetRulestackFW
        ```

        :param str resource_name: The name of the resource.
        :param NextGenerationFirewallVirtualNetworkLocalRulestackArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NextGenerationFirewallVirtualNetworkLocalRulestackArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            NextGenerationFirewallVirtualNetworkLocalRulestackArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_nats: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NextGenerationFirewallVirtualNetworkLocalRulestackDestinationNatArgs']]]]] = None,
                 dns_settings: Optional[pulumi.Input[pulumi.InputType['NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettingsArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfileArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rulestack_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NextGenerationFirewallVirtualNetworkLocalRulestackArgs.__new__(NextGenerationFirewallVirtualNetworkLocalRulestackArgs)

            __props__.__dict__["destination_nats"] = destination_nats
            if dns_settings is not None and not isinstance(dns_settings, NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettingsArgs):
                dns_settings = dns_settings or {}
                def _setter(key, value):
                    dns_settings[key] = value
                NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettingsArgs._configure(_setter, **dns_settings)
            __props__.__dict__["dns_settings"] = dns_settings
            __props__.__dict__["name"] = name
            if network_profile is not None and not isinstance(network_profile, NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfileArgs):
                network_profile = network_profile or {}
                def _setter(key, value):
                    network_profile[key] = value
                NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfileArgs._configure(_setter, **network_profile)
            if network_profile is None and not opts.urn:
                raise TypeError("Missing required property 'network_profile'")
            __props__.__dict__["network_profile"] = network_profile
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if rulestack_id is None and not opts.urn:
                raise TypeError("Missing required property 'rulestack_id'")
            __props__.__dict__["rulestack_id"] = rulestack_id
            __props__.__dict__["tags"] = tags
        super(NextGenerationFirewallVirtualNetworkLocalRulestack, __self__).__init__(
            'azure:paloalto/nextGenerationFirewallVirtualNetworkLocalRulestack:NextGenerationFirewallVirtualNetworkLocalRulestack',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            destination_nats: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NextGenerationFirewallVirtualNetworkLocalRulestackDestinationNatArgs']]]]] = None,
            dns_settings: Optional[pulumi.Input[pulumi.InputType['NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettingsArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_profile: Optional[pulumi.Input[pulumi.InputType['NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfileArgs']]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            rulestack_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'NextGenerationFirewallVirtualNetworkLocalRulestack':
        """
        Get an existing NextGenerationFirewallVirtualNetworkLocalRulestack resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NextGenerationFirewallVirtualNetworkLocalRulestackDestinationNatArgs']]]] destination_nats: One or more `destination_nat` blocks as defined below.
        :param pulumi.Input[pulumi.InputType['NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettingsArgs']] dns_settings: A `dns_settings` block as defined below.
        :param pulumi.Input[str] name: The name which should be used for this Palo Alto Next Generation Firewall Virtual Network Local Rulestack. Changing this forces a new Palo Alto Next Generation Firewall Virtual Network Local Rulestack to be created.
        :param pulumi.Input[pulumi.InputType['NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfileArgs']] network_profile: A `network_profile` block as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Palo Alto Next Generation Firewall Virtual Network Local Rulestack should exist. Changing this forces a new Palo Alto Next Generation Firewall Virtual Network Local Rulestack to be created.
        :param pulumi.Input[str] rulestack_id: The ID of the Local Rulestack which will be used to configure this Firewall Resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Palo Alto Next Generation Firewall Virtual Network Local Rulestack.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NextGenerationFirewallVirtualNetworkLocalRulestackState.__new__(_NextGenerationFirewallVirtualNetworkLocalRulestackState)

        __props__.__dict__["destination_nats"] = destination_nats
        __props__.__dict__["dns_settings"] = dns_settings
        __props__.__dict__["name"] = name
        __props__.__dict__["network_profile"] = network_profile
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["rulestack_id"] = rulestack_id
        __props__.__dict__["tags"] = tags
        return NextGenerationFirewallVirtualNetworkLocalRulestack(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="destinationNats")
    def destination_nats(self) -> pulumi.Output[Optional[Sequence['outputs.NextGenerationFirewallVirtualNetworkLocalRulestackDestinationNat']]]:
        """
        One or more `destination_nat` blocks as defined below.
        """
        return pulumi.get(self, "destination_nats")

    @property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> pulumi.Output[Optional['outputs.NextGenerationFirewallVirtualNetworkLocalRulestackDnsSettings']]:
        """
        A `dns_settings` block as defined below.
        """
        return pulumi.get(self, "dns_settings")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Palo Alto Next Generation Firewall Virtual Network Local Rulestack. Changing this forces a new Palo Alto Next Generation Firewall Virtual Network Local Rulestack to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output['outputs.NextGenerationFirewallVirtualNetworkLocalRulestackNetworkProfile']:
        """
        A `network_profile` block as defined below.
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Palo Alto Next Generation Firewall Virtual Network Local Rulestack should exist. Changing this forces a new Palo Alto Next Generation Firewall Virtual Network Local Rulestack to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="rulestackId")
    def rulestack_id(self) -> pulumi.Output[str]:
        """
        The ID of the Local Rulestack which will be used to configure this Firewall Resource.
        """
        return pulumi.get(self, "rulestack_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags which should be assigned to the Palo Alto Next Generation Firewall Virtual Network Local Rulestack.
        """
        return pulumi.get(self, "tags")


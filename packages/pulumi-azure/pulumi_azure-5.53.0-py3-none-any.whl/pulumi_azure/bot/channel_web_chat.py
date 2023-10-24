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

__all__ = ['ChannelWebChatArgs', 'ChannelWebChat']

@pulumi.input_type
class ChannelWebChatArgs:
    def __init__(__self__, *,
                 bot_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 site_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sites: Optional[pulumi.Input[Sequence[pulumi.Input['ChannelWebChatSiteArgs']]]] = None):
        """
        The set of arguments for constructing a ChannelWebChat resource.
        :param pulumi.Input[str] bot_name: The name of the Bot Resource this channel will be associated with. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the Web Chat Channel should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] site_names: A list of Web Chat Site names.
               
               > **NOTE:** `site_names` is deprecated and will be removed in favour of the property `site` in version 4.0 of the AzureRM Provider.
        :param pulumi.Input[Sequence[pulumi.Input['ChannelWebChatSiteArgs']]] sites: A site represents a client application that you want to connect to your bot. Multiple `site` blocks may be defined as below
        """
        ChannelWebChatArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bot_name=bot_name,
            resource_group_name=resource_group_name,
            location=location,
            site_names=site_names,
            sites=sites,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bot_name: pulumi.Input[str],
             resource_group_name: pulumi.Input[str],
             location: Optional[pulumi.Input[str]] = None,
             site_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             sites: Optional[pulumi.Input[Sequence[pulumi.Input['ChannelWebChatSiteArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'botName' in kwargs:
            bot_name = kwargs['botName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'siteNames' in kwargs:
            site_names = kwargs['siteNames']

        _setter("bot_name", bot_name)
        _setter("resource_group_name", resource_group_name)
        if location is not None:
            _setter("location", location)
        if site_names is not None:
            warnings.warn("""`site_names` will be removed in favour of the property `site` in version 4.0 of the AzureRM Provider.""", DeprecationWarning)
            pulumi.log.warn("""site_names is deprecated: `site_names` will be removed in favour of the property `site` in version 4.0 of the AzureRM Provider.""")
        if site_names is not None:
            _setter("site_names", site_names)
        if sites is not None:
            _setter("sites", sites)

    @property
    @pulumi.getter(name="botName")
    def bot_name(self) -> pulumi.Input[str]:
        """
        The name of the Bot Resource this channel will be associated with. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "bot_name")

    @bot_name.setter
    def bot_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "bot_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group where the Web Chat Channel should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="siteNames")
    def site_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of Web Chat Site names.

        > **NOTE:** `site_names` is deprecated and will be removed in favour of the property `site` in version 4.0 of the AzureRM Provider.
        """
        warnings.warn("""`site_names` will be removed in favour of the property `site` in version 4.0 of the AzureRM Provider.""", DeprecationWarning)
        pulumi.log.warn("""site_names is deprecated: `site_names` will be removed in favour of the property `site` in version 4.0 of the AzureRM Provider.""")

        return pulumi.get(self, "site_names")

    @site_names.setter
    def site_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "site_names", value)

    @property
    @pulumi.getter
    def sites(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ChannelWebChatSiteArgs']]]]:
        """
        A site represents a client application that you want to connect to your bot. Multiple `site` blocks may be defined as below
        """
        return pulumi.get(self, "sites")

    @sites.setter
    def sites(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ChannelWebChatSiteArgs']]]]):
        pulumi.set(self, "sites", value)


@pulumi.input_type
class _ChannelWebChatState:
    def __init__(__self__, *,
                 bot_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sites: Optional[pulumi.Input[Sequence[pulumi.Input['ChannelWebChatSiteArgs']]]] = None):
        """
        Input properties used for looking up and filtering ChannelWebChat resources.
        :param pulumi.Input[str] bot_name: The name of the Bot Resource this channel will be associated with. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the Web Chat Channel should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] site_names: A list of Web Chat Site names.
               
               > **NOTE:** `site_names` is deprecated and will be removed in favour of the property `site` in version 4.0 of the AzureRM Provider.
        :param pulumi.Input[Sequence[pulumi.Input['ChannelWebChatSiteArgs']]] sites: A site represents a client application that you want to connect to your bot. Multiple `site` blocks may be defined as below
        """
        _ChannelWebChatState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bot_name=bot_name,
            location=location,
            resource_group_name=resource_group_name,
            site_names=site_names,
            sites=sites,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bot_name: Optional[pulumi.Input[str]] = None,
             location: Optional[pulumi.Input[str]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             site_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             sites: Optional[pulumi.Input[Sequence[pulumi.Input['ChannelWebChatSiteArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'botName' in kwargs:
            bot_name = kwargs['botName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'siteNames' in kwargs:
            site_names = kwargs['siteNames']

        if bot_name is not None:
            _setter("bot_name", bot_name)
        if location is not None:
            _setter("location", location)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if site_names is not None:
            warnings.warn("""`site_names` will be removed in favour of the property `site` in version 4.0 of the AzureRM Provider.""", DeprecationWarning)
            pulumi.log.warn("""site_names is deprecated: `site_names` will be removed in favour of the property `site` in version 4.0 of the AzureRM Provider.""")
        if site_names is not None:
            _setter("site_names", site_names)
        if sites is not None:
            _setter("sites", sites)

    @property
    @pulumi.getter(name="botName")
    def bot_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Bot Resource this channel will be associated with. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "bot_name")

    @bot_name.setter
    def bot_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bot_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group where the Web Chat Channel should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="siteNames")
    def site_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of Web Chat Site names.

        > **NOTE:** `site_names` is deprecated and will be removed in favour of the property `site` in version 4.0 of the AzureRM Provider.
        """
        warnings.warn("""`site_names` will be removed in favour of the property `site` in version 4.0 of the AzureRM Provider.""", DeprecationWarning)
        pulumi.log.warn("""site_names is deprecated: `site_names` will be removed in favour of the property `site` in version 4.0 of the AzureRM Provider.""")

        return pulumi.get(self, "site_names")

    @site_names.setter
    def site_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "site_names", value)

    @property
    @pulumi.getter
    def sites(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ChannelWebChatSiteArgs']]]]:
        """
        A site represents a client application that you want to connect to your bot. Multiple `site` blocks may be defined as below
        """
        return pulumi.get(self, "sites")

    @sites.setter
    def sites(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ChannelWebChatSiteArgs']]]]):
        pulumi.set(self, "sites", value)


class ChannelWebChat(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bot_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sites: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChannelWebChatSiteArgs']]]]] = None,
                 __props__=None):
        """
        Manages a Web Chat integration for a Bot Channel

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        current = azure.core.get_client_config()
        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_channels_registration = azure.bot.ChannelsRegistration("exampleChannelsRegistration",
            location="global",
            resource_group_name=example_resource_group.name,
            sku="F0",
            microsoft_app_id=current.client_id)
        example_channel_web_chat = azure.bot.ChannelWebChat("exampleChannelWebChat",
            bot_name=example_channels_registration.name,
            location=example_channels_registration.location,
            resource_group_name=example_resource_group.name,
            sites=[azure.bot.ChannelWebChatSiteArgs(
                name="TestSite",
            )])
        ```

        ## Import

        Web Chat Channels can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:bot/channelWebChat:ChannelWebChat example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.BotService/botServices/botService1/channels/WebChatChannel
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bot_name: The name of the Bot Resource this channel will be associated with. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the Web Chat Channel should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] site_names: A list of Web Chat Site names.
               
               > **NOTE:** `site_names` is deprecated and will be removed in favour of the property `site` in version 4.0 of the AzureRM Provider.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChannelWebChatSiteArgs']]]] sites: A site represents a client application that you want to connect to your bot. Multiple `site` blocks may be defined as below
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ChannelWebChatArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Web Chat integration for a Bot Channel

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        current = azure.core.get_client_config()
        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_channels_registration = azure.bot.ChannelsRegistration("exampleChannelsRegistration",
            location="global",
            resource_group_name=example_resource_group.name,
            sku="F0",
            microsoft_app_id=current.client_id)
        example_channel_web_chat = azure.bot.ChannelWebChat("exampleChannelWebChat",
            bot_name=example_channels_registration.name,
            location=example_channels_registration.location,
            resource_group_name=example_resource_group.name,
            sites=[azure.bot.ChannelWebChatSiteArgs(
                name="TestSite",
            )])
        ```

        ## Import

        Web Chat Channels can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:bot/channelWebChat:ChannelWebChat example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.BotService/botServices/botService1/channels/WebChatChannel
        ```

        :param str resource_name: The name of the resource.
        :param ChannelWebChatArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ChannelWebChatArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ChannelWebChatArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bot_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sites: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChannelWebChatSiteArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ChannelWebChatArgs.__new__(ChannelWebChatArgs)

            if bot_name is None and not opts.urn:
                raise TypeError("Missing required property 'bot_name'")
            __props__.__dict__["bot_name"] = bot_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["site_names"] = site_names
            __props__.__dict__["sites"] = sites
        super(ChannelWebChat, __self__).__init__(
            'azure:bot/channelWebChat:ChannelWebChat',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bot_name: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            site_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            sites: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChannelWebChatSiteArgs']]]]] = None) -> 'ChannelWebChat':
        """
        Get an existing ChannelWebChat resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bot_name: The name of the Bot Resource this channel will be associated with. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the Web Chat Channel should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] site_names: A list of Web Chat Site names.
               
               > **NOTE:** `site_names` is deprecated and will be removed in favour of the property `site` in version 4.0 of the AzureRM Provider.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChannelWebChatSiteArgs']]]] sites: A site represents a client application that you want to connect to your bot. Multiple `site` blocks may be defined as below
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ChannelWebChatState.__new__(_ChannelWebChatState)

        __props__.__dict__["bot_name"] = bot_name
        __props__.__dict__["location"] = location
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["site_names"] = site_names
        __props__.__dict__["sites"] = sites
        return ChannelWebChat(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="botName")
    def bot_name(self) -> pulumi.Output[str]:
        """
        The name of the Bot Resource this channel will be associated with. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "bot_name")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group where the Web Chat Channel should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="siteNames")
    def site_names(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of Web Chat Site names.

        > **NOTE:** `site_names` is deprecated and will be removed in favour of the property `site` in version 4.0 of the AzureRM Provider.
        """
        warnings.warn("""`site_names` will be removed in favour of the property `site` in version 4.0 of the AzureRM Provider.""", DeprecationWarning)
        pulumi.log.warn("""site_names is deprecated: `site_names` will be removed in favour of the property `site` in version 4.0 of the AzureRM Provider.""")

        return pulumi.get(self, "site_names")

    @property
    @pulumi.getter
    def sites(self) -> pulumi.Output[Sequence['outputs.ChannelWebChatSite']]:
        """
        A site represents a client application that you want to connect to your bot. Multiple `site` blocks may be defined as below
        """
        return pulumi.get(self, "sites")


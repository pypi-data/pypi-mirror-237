# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['HyperVSiteArgs', 'HyperVSite']

@pulumi.input_type
class HyperVSiteArgs:
    def __init__(__self__, *,
                 recovery_vault_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a HyperVSite resource.
        :param pulumi.Input[str] recovery_vault_id: The ID of the Recovery Services Vault where the Site created. Changing this forces a new Site to be created.
        :param pulumi.Input[str] name: The name which should be used for this Recovery Service. Changing this forces a new Site to be created.
        """
        HyperVSiteArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            recovery_vault_id=recovery_vault_id,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             recovery_vault_id: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'recoveryVaultId' in kwargs:
            recovery_vault_id = kwargs['recoveryVaultId']

        _setter("recovery_vault_id", recovery_vault_id)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="recoveryVaultId")
    def recovery_vault_id(self) -> pulumi.Input[str]:
        """
        The ID of the Recovery Services Vault where the Site created. Changing this forces a new Site to be created.
        """
        return pulumi.get(self, "recovery_vault_id")

    @recovery_vault_id.setter
    def recovery_vault_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "recovery_vault_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Recovery Service. Changing this forces a new Site to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _HyperVSiteState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 recovery_vault_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering HyperVSite resources.
        :param pulumi.Input[str] name: The name which should be used for this Recovery Service. Changing this forces a new Site to be created.
        :param pulumi.Input[str] recovery_vault_id: The ID of the Recovery Services Vault where the Site created. Changing this forces a new Site to be created.
        """
        _HyperVSiteState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            recovery_vault_id=recovery_vault_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             recovery_vault_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'recoveryVaultId' in kwargs:
            recovery_vault_id = kwargs['recoveryVaultId']

        if name is not None:
            _setter("name", name)
        if recovery_vault_id is not None:
            _setter("recovery_vault_id", recovery_vault_id)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Recovery Service. Changing this forces a new Site to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="recoveryVaultId")
    def recovery_vault_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Recovery Services Vault where the Site created. Changing this forces a new Site to be created.
        """
        return pulumi.get(self, "recovery_vault_id")

    @recovery_vault_id.setter
    def recovery_vault_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recovery_vault_id", value)


class HyperVSite(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recovery_vault_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a HyperV Site in Recovery Service Vault.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="eastus")
        example_vault = azure.recoveryservices.Vault("exampleVault",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="Standard",
            soft_delete_enabled=False)
        example_hyper_v_site = azure.siterecovery.HyperVSite("exampleHyperVSite", recovery_vault_id=example_vault.id)
        ```

        ## Import

        Recovery Services can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:siterecovery/hyperVSite:HyperVSite example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.RecoveryServices/vaults/vault1/replicationFabrics/fabric1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name which should be used for this Recovery Service. Changing this forces a new Site to be created.
        :param pulumi.Input[str] recovery_vault_id: The ID of the Recovery Services Vault where the Site created. Changing this forces a new Site to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HyperVSiteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a HyperV Site in Recovery Service Vault.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="eastus")
        example_vault = azure.recoveryservices.Vault("exampleVault",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="Standard",
            soft_delete_enabled=False)
        example_hyper_v_site = azure.siterecovery.HyperVSite("exampleHyperVSite", recovery_vault_id=example_vault.id)
        ```

        ## Import

        Recovery Services can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:siterecovery/hyperVSite:HyperVSite example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.RecoveryServices/vaults/vault1/replicationFabrics/fabric1
        ```

        :param str resource_name: The name of the resource.
        :param HyperVSiteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HyperVSiteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            HyperVSiteArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recovery_vault_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HyperVSiteArgs.__new__(HyperVSiteArgs)

            __props__.__dict__["name"] = name
            if recovery_vault_id is None and not opts.urn:
                raise TypeError("Missing required property 'recovery_vault_id'")
            __props__.__dict__["recovery_vault_id"] = recovery_vault_id
        super(HyperVSite, __self__).__init__(
            'azure:siterecovery/hyperVSite:HyperVSite',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            recovery_vault_id: Optional[pulumi.Input[str]] = None) -> 'HyperVSite':
        """
        Get an existing HyperVSite resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name which should be used for this Recovery Service. Changing this forces a new Site to be created.
        :param pulumi.Input[str] recovery_vault_id: The ID of the Recovery Services Vault where the Site created. Changing this forces a new Site to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HyperVSiteState.__new__(_HyperVSiteState)

        __props__.__dict__["name"] = name
        __props__.__dict__["recovery_vault_id"] = recovery_vault_id
        return HyperVSite(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Recovery Service. Changing this forces a new Site to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recoveryVaultId")
    def recovery_vault_id(self) -> pulumi.Output[str]:
        """
        The ID of the Recovery Services Vault where the Site created. Changing this forces a new Site to be created.
        """
        return pulumi.get(self, "recovery_vault_id")


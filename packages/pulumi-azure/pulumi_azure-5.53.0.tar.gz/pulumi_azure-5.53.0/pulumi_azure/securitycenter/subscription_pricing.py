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

__all__ = ['SubscriptionPricingArgs', 'SubscriptionPricing']

@pulumi.input_type
class SubscriptionPricingArgs:
    def __init__(__self__, *,
                 tier: pulumi.Input[str],
                 extensions: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionPricingExtensionArgs']]]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 subplan: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SubscriptionPricing resource.
        :param pulumi.Input[str] tier: The pricing tier to use. Possible values are `Free` and `Standard`.
        :param pulumi.Input[Sequence[pulumi.Input['SubscriptionPricingExtensionArgs']]] extensions: One or more `extension` blocks as defined below.
        :param pulumi.Input[str] resource_type: The resource type this setting affects. Possible values are `Api`, `AppServices`, `ContainerRegistry`, `KeyVaults`, `KubernetesService`, `SqlServers`, `SqlServerVirtualMachines`, `StorageAccounts`, `VirtualMachines`, `Arm`, `Dns`, `OpenSourceRelationalDatabases`, `Containers`, `CosmosDbs` and `CloudPosture`. Defaults to `VirtualMachines`
        :param pulumi.Input[str] subplan: Resource type pricing subplan. Contact your MSFT representative for possible values.
        """
        SubscriptionPricingArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            tier=tier,
            extensions=extensions,
            resource_type=resource_type,
            subplan=subplan,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             tier: pulumi.Input[str],
             extensions: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionPricingExtensionArgs']]]] = None,
             resource_type: Optional[pulumi.Input[str]] = None,
             subplan: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'resourceType' in kwargs:
            resource_type = kwargs['resourceType']

        _setter("tier", tier)
        if extensions is not None:
            _setter("extensions", extensions)
        if resource_type is not None:
            _setter("resource_type", resource_type)
        if subplan is not None:
            _setter("subplan", subplan)

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Input[str]:
        """
        The pricing tier to use. Possible values are `Free` and `Standard`.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: pulumi.Input[str]):
        pulumi.set(self, "tier", value)

    @property
    @pulumi.getter
    def extensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionPricingExtensionArgs']]]]:
        """
        One or more `extension` blocks as defined below.
        """
        return pulumi.get(self, "extensions")

    @extensions.setter
    def extensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionPricingExtensionArgs']]]]):
        pulumi.set(self, "extensions", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        The resource type this setting affects. Possible values are `Api`, `AppServices`, `ContainerRegistry`, `KeyVaults`, `KubernetesService`, `SqlServers`, `SqlServerVirtualMachines`, `StorageAccounts`, `VirtualMachines`, `Arm`, `Dns`, `OpenSourceRelationalDatabases`, `Containers`, `CosmosDbs` and `CloudPosture`. Defaults to `VirtualMachines`
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter
    def subplan(self) -> Optional[pulumi.Input[str]]:
        """
        Resource type pricing subplan. Contact your MSFT representative for possible values.
        """
        return pulumi.get(self, "subplan")

    @subplan.setter
    def subplan(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subplan", value)


@pulumi.input_type
class _SubscriptionPricingState:
    def __init__(__self__, *,
                 extensions: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionPricingExtensionArgs']]]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 subplan: Optional[pulumi.Input[str]] = None,
                 tier: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SubscriptionPricing resources.
        :param pulumi.Input[Sequence[pulumi.Input['SubscriptionPricingExtensionArgs']]] extensions: One or more `extension` blocks as defined below.
        :param pulumi.Input[str] resource_type: The resource type this setting affects. Possible values are `Api`, `AppServices`, `ContainerRegistry`, `KeyVaults`, `KubernetesService`, `SqlServers`, `SqlServerVirtualMachines`, `StorageAccounts`, `VirtualMachines`, `Arm`, `Dns`, `OpenSourceRelationalDatabases`, `Containers`, `CosmosDbs` and `CloudPosture`. Defaults to `VirtualMachines`
        :param pulumi.Input[str] subplan: Resource type pricing subplan. Contact your MSFT representative for possible values.
        :param pulumi.Input[str] tier: The pricing tier to use. Possible values are `Free` and `Standard`.
        """
        _SubscriptionPricingState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            extensions=extensions,
            resource_type=resource_type,
            subplan=subplan,
            tier=tier,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             extensions: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionPricingExtensionArgs']]]] = None,
             resource_type: Optional[pulumi.Input[str]] = None,
             subplan: Optional[pulumi.Input[str]] = None,
             tier: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'resourceType' in kwargs:
            resource_type = kwargs['resourceType']

        if extensions is not None:
            _setter("extensions", extensions)
        if resource_type is not None:
            _setter("resource_type", resource_type)
        if subplan is not None:
            _setter("subplan", subplan)
        if tier is not None:
            _setter("tier", tier)

    @property
    @pulumi.getter
    def extensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionPricingExtensionArgs']]]]:
        """
        One or more `extension` blocks as defined below.
        """
        return pulumi.get(self, "extensions")

    @extensions.setter
    def extensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionPricingExtensionArgs']]]]):
        pulumi.set(self, "extensions", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        The resource type this setting affects. Possible values are `Api`, `AppServices`, `ContainerRegistry`, `KeyVaults`, `KubernetesService`, `SqlServers`, `SqlServerVirtualMachines`, `StorageAccounts`, `VirtualMachines`, `Arm`, `Dns`, `OpenSourceRelationalDatabases`, `Containers`, `CosmosDbs` and `CloudPosture`. Defaults to `VirtualMachines`
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter
    def subplan(self) -> Optional[pulumi.Input[str]]:
        """
        Resource type pricing subplan. Contact your MSFT representative for possible values.
        """
        return pulumi.get(self, "subplan")

    @subplan.setter
    def subplan(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subplan", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[str]]:
        """
        The pricing tier to use. Possible values are `Free` and `Standard`.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tier", value)


class SubscriptionPricing(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extensions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriptionPricingExtensionArgs']]]]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 subplan: Optional[pulumi.Input[str]] = None,
                 tier: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages the Pricing Tier for Azure Security Center in the current subscription.

        > **NOTE:** Deletion of this resource will reset the pricing tier to `Free`

        ## Example Usage
        ### Basic usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.securitycenter.SubscriptionPricing("example",
            resource_type="VirtualMachines",
            tier="Standard")
        ```
        ### Using Extensions with Defender CSPM

        ```python
        import pulumi
        import pulumi_azure as azure

        example1 = azure.securitycenter.SubscriptionPricing("example1",
            extensions=[
                azure.securitycenter.SubscriptionPricingExtensionArgs(
                    name="ContainerRegistriesVulnerabilityAssessments",
                ),
                azure.securitycenter.SubscriptionPricingExtensionArgs(
                    additional_extension_properties={
                        "ExclusionTags": "[]",
                    },
                    name="AgentlessVmScanning",
                ),
                azure.securitycenter.SubscriptionPricingExtensionArgs(
                    name="AgentlessDiscoveryForKubernetes",
                ),
                azure.securitycenter.SubscriptionPricingExtensionArgs(
                    name="SensitiveDataDiscovery",
                ),
            ],
            resource_type="CloudPosture",
            tier="Standard")
        ```

        ## Import

        The pricing tier can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:securitycenter/subscriptionPricing:SubscriptionPricing example /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Security/pricings/<resource_type>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriptionPricingExtensionArgs']]]] extensions: One or more `extension` blocks as defined below.
        :param pulumi.Input[str] resource_type: The resource type this setting affects. Possible values are `Api`, `AppServices`, `ContainerRegistry`, `KeyVaults`, `KubernetesService`, `SqlServers`, `SqlServerVirtualMachines`, `StorageAccounts`, `VirtualMachines`, `Arm`, `Dns`, `OpenSourceRelationalDatabases`, `Containers`, `CosmosDbs` and `CloudPosture`. Defaults to `VirtualMachines`
        :param pulumi.Input[str] subplan: Resource type pricing subplan. Contact your MSFT representative for possible values.
        :param pulumi.Input[str] tier: The pricing tier to use. Possible values are `Free` and `Standard`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubscriptionPricingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages the Pricing Tier for Azure Security Center in the current subscription.

        > **NOTE:** Deletion of this resource will reset the pricing tier to `Free`

        ## Example Usage
        ### Basic usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.securitycenter.SubscriptionPricing("example",
            resource_type="VirtualMachines",
            tier="Standard")
        ```
        ### Using Extensions with Defender CSPM

        ```python
        import pulumi
        import pulumi_azure as azure

        example1 = azure.securitycenter.SubscriptionPricing("example1",
            extensions=[
                azure.securitycenter.SubscriptionPricingExtensionArgs(
                    name="ContainerRegistriesVulnerabilityAssessments",
                ),
                azure.securitycenter.SubscriptionPricingExtensionArgs(
                    additional_extension_properties={
                        "ExclusionTags": "[]",
                    },
                    name="AgentlessVmScanning",
                ),
                azure.securitycenter.SubscriptionPricingExtensionArgs(
                    name="AgentlessDiscoveryForKubernetes",
                ),
                azure.securitycenter.SubscriptionPricingExtensionArgs(
                    name="SensitiveDataDiscovery",
                ),
            ],
            resource_type="CloudPosture",
            tier="Standard")
        ```

        ## Import

        The pricing tier can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:securitycenter/subscriptionPricing:SubscriptionPricing example /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Security/pricings/<resource_type>
        ```

        :param str resource_name: The name of the resource.
        :param SubscriptionPricingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubscriptionPricingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SubscriptionPricingArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extensions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriptionPricingExtensionArgs']]]]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 subplan: Optional[pulumi.Input[str]] = None,
                 tier: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SubscriptionPricingArgs.__new__(SubscriptionPricingArgs)

            __props__.__dict__["extensions"] = extensions
            __props__.__dict__["resource_type"] = resource_type
            __props__.__dict__["subplan"] = subplan
            if tier is None and not opts.urn:
                raise TypeError("Missing required property 'tier'")
            __props__.__dict__["tier"] = tier
        super(SubscriptionPricing, __self__).__init__(
            'azure:securitycenter/subscriptionPricing:SubscriptionPricing',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            extensions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriptionPricingExtensionArgs']]]]] = None,
            resource_type: Optional[pulumi.Input[str]] = None,
            subplan: Optional[pulumi.Input[str]] = None,
            tier: Optional[pulumi.Input[str]] = None) -> 'SubscriptionPricing':
        """
        Get an existing SubscriptionPricing resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriptionPricingExtensionArgs']]]] extensions: One or more `extension` blocks as defined below.
        :param pulumi.Input[str] resource_type: The resource type this setting affects. Possible values are `Api`, `AppServices`, `ContainerRegistry`, `KeyVaults`, `KubernetesService`, `SqlServers`, `SqlServerVirtualMachines`, `StorageAccounts`, `VirtualMachines`, `Arm`, `Dns`, `OpenSourceRelationalDatabases`, `Containers`, `CosmosDbs` and `CloudPosture`. Defaults to `VirtualMachines`
        :param pulumi.Input[str] subplan: Resource type pricing subplan. Contact your MSFT representative for possible values.
        :param pulumi.Input[str] tier: The pricing tier to use. Possible values are `Free` and `Standard`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SubscriptionPricingState.__new__(_SubscriptionPricingState)

        __props__.__dict__["extensions"] = extensions
        __props__.__dict__["resource_type"] = resource_type
        __props__.__dict__["subplan"] = subplan
        __props__.__dict__["tier"] = tier
        return SubscriptionPricing(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def extensions(self) -> pulumi.Output[Optional[Sequence['outputs.SubscriptionPricingExtension']]]:
        """
        One or more `extension` blocks as defined below.
        """
        return pulumi.get(self, "extensions")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[Optional[str]]:
        """
        The resource type this setting affects. Possible values are `Api`, `AppServices`, `ContainerRegistry`, `KeyVaults`, `KubernetesService`, `SqlServers`, `SqlServerVirtualMachines`, `StorageAccounts`, `VirtualMachines`, `Arm`, `Dns`, `OpenSourceRelationalDatabases`, `Containers`, `CosmosDbs` and `CloudPosture`. Defaults to `VirtualMachines`
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter
    def subplan(self) -> pulumi.Output[Optional[str]]:
        """
        Resource type pricing subplan. Contact your MSFT representative for possible values.
        """
        return pulumi.get(self, "subplan")

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Output[str]:
        """
        The pricing tier to use. Possible values are `Free` and `Standard`.
        """
        return pulumi.get(self, "tier")


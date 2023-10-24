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

__all__ = ['AccountNetworkRulesInitArgs', 'AccountNetworkRules']

@pulumi.input_type
class AccountNetworkRulesInitArgs:
    def __init__(__self__, *,
                 default_action: pulumi.Input[str],
                 storage_account_id: pulumi.Input[str],
                 bypasses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 private_link_access_rules: Optional[pulumi.Input[Sequence[pulumi.Input['AccountNetworkRulesPrivateLinkAccessRuleArgs']]]] = None,
                 virtual_network_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AccountNetworkRules resource.
        :param pulumi.Input[str] default_action: Specifies the default action of allow or deny when no other rules match. Valid options are `Deny` or `Allow`.
        :param pulumi.Input[str] storage_account_id: Specifies the ID of the storage account. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] bypasses: Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Valid options are any combination of `Logging`, `Metrics`, `AzureServices`, or `None`.
               
               > **NOTE** User has to explicitly set `bypass` to empty slice (`[]`) to remove it.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_rules: List of public IP or IP ranges in CIDR Format. Only IPv4 addresses are allowed. Private IP address ranges (as defined in [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3)) are not allowed.
               
               > **NOTE** Small address ranges using "/31" or "/32" prefix sizes are not supported. These ranges should be configured using individual IP address rules without prefix specified.
               
               > **NOTE** IP network rules have no effect on requests originating from the same Azure region as the storage account. Use Virtual network rules to allow same-region requests. Services deployed in the same region as the storage account use private Azure IP addresses for communication. Thus, you cannot restrict access to specific Azure services based on their public outbound IP address range.
               
               > **NOTE** User has to explicitly set `ip_rules` to empty slice (`[]`) to remove it.
        :param pulumi.Input[Sequence[pulumi.Input['AccountNetworkRulesPrivateLinkAccessRuleArgs']]] private_link_access_rules: One or More `private_link_access` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] virtual_network_subnet_ids: A list of virtual network subnet ids to secure the storage account.
               
               > **NOTE** User has to explicitly set `virtual_network_subnet_ids` to empty slice (`[]`) to remove it.
        """
        AccountNetworkRulesInitArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            default_action=default_action,
            storage_account_id=storage_account_id,
            bypasses=bypasses,
            ip_rules=ip_rules,
            private_link_access_rules=private_link_access_rules,
            virtual_network_subnet_ids=virtual_network_subnet_ids,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             default_action: pulumi.Input[str],
             storage_account_id: pulumi.Input[str],
             bypasses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             private_link_access_rules: Optional[pulumi.Input[Sequence[pulumi.Input['AccountNetworkRulesPrivateLinkAccessRuleArgs']]]] = None,
             virtual_network_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'defaultAction' in kwargs:
            default_action = kwargs['defaultAction']
        if 'storageAccountId' in kwargs:
            storage_account_id = kwargs['storageAccountId']
        if 'ipRules' in kwargs:
            ip_rules = kwargs['ipRules']
        if 'privateLinkAccessRules' in kwargs:
            private_link_access_rules = kwargs['privateLinkAccessRules']
        if 'virtualNetworkSubnetIds' in kwargs:
            virtual_network_subnet_ids = kwargs['virtualNetworkSubnetIds']

        _setter("default_action", default_action)
        _setter("storage_account_id", storage_account_id)
        if bypasses is not None:
            _setter("bypasses", bypasses)
        if ip_rules is not None:
            _setter("ip_rules", ip_rules)
        if private_link_access_rules is not None:
            _setter("private_link_access_rules", private_link_access_rules)
        if virtual_network_subnet_ids is not None:
            _setter("virtual_network_subnet_ids", virtual_network_subnet_ids)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Input[str]:
        """
        Specifies the default action of allow or deny when no other rules match. Valid options are `Deny` or `Allow`.
        """
        return pulumi.get(self, "default_action")

    @default_action.setter
    def default_action(self, value: pulumi.Input[str]):
        pulumi.set(self, "default_action", value)

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Input[str]:
        """
        Specifies the ID of the storage account. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "storage_account_id")

    @storage_account_id.setter
    def storage_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_id", value)

    @property
    @pulumi.getter
    def bypasses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Valid options are any combination of `Logging`, `Metrics`, `AzureServices`, or `None`.

        > **NOTE** User has to explicitly set `bypass` to empty slice (`[]`) to remove it.
        """
        return pulumi.get(self, "bypasses")

    @bypasses.setter
    def bypasses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "bypasses", value)

    @property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of public IP or IP ranges in CIDR Format. Only IPv4 addresses are allowed. Private IP address ranges (as defined in [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3)) are not allowed.

        > **NOTE** Small address ranges using "/31" or "/32" prefix sizes are not supported. These ranges should be configured using individual IP address rules without prefix specified.

        > **NOTE** IP network rules have no effect on requests originating from the same Azure region as the storage account. Use Virtual network rules to allow same-region requests. Services deployed in the same region as the storage account use private Azure IP addresses for communication. Thus, you cannot restrict access to specific Azure services based on their public outbound IP address range.

        > **NOTE** User has to explicitly set `ip_rules` to empty slice (`[]`) to remove it.
        """
        return pulumi.get(self, "ip_rules")

    @ip_rules.setter
    def ip_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ip_rules", value)

    @property
    @pulumi.getter(name="privateLinkAccessRules")
    def private_link_access_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccountNetworkRulesPrivateLinkAccessRuleArgs']]]]:
        """
        One or More `private_link_access` block as defined below.
        """
        return pulumi.get(self, "private_link_access_rules")

    @private_link_access_rules.setter
    def private_link_access_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccountNetworkRulesPrivateLinkAccessRuleArgs']]]]):
        pulumi.set(self, "private_link_access_rules", value)

    @property
    @pulumi.getter(name="virtualNetworkSubnetIds")
    def virtual_network_subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of virtual network subnet ids to secure the storage account.

        > **NOTE** User has to explicitly set `virtual_network_subnet_ids` to empty slice (`[]`) to remove it.
        """
        return pulumi.get(self, "virtual_network_subnet_ids")

    @virtual_network_subnet_ids.setter
    def virtual_network_subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "virtual_network_subnet_ids", value)


@pulumi.input_type
class _AccountNetworkRulesState:
    def __init__(__self__, *,
                 bypasses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_action: Optional[pulumi.Input[str]] = None,
                 ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 private_link_access_rules: Optional[pulumi.Input[Sequence[pulumi.Input['AccountNetworkRulesPrivateLinkAccessRuleArgs']]]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 virtual_network_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering AccountNetworkRules resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] bypasses: Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Valid options are any combination of `Logging`, `Metrics`, `AzureServices`, or `None`.
               
               > **NOTE** User has to explicitly set `bypass` to empty slice (`[]`) to remove it.
        :param pulumi.Input[str] default_action: Specifies the default action of allow or deny when no other rules match. Valid options are `Deny` or `Allow`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_rules: List of public IP or IP ranges in CIDR Format. Only IPv4 addresses are allowed. Private IP address ranges (as defined in [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3)) are not allowed.
               
               > **NOTE** Small address ranges using "/31" or "/32" prefix sizes are not supported. These ranges should be configured using individual IP address rules without prefix specified.
               
               > **NOTE** IP network rules have no effect on requests originating from the same Azure region as the storage account. Use Virtual network rules to allow same-region requests. Services deployed in the same region as the storage account use private Azure IP addresses for communication. Thus, you cannot restrict access to specific Azure services based on their public outbound IP address range.
               
               > **NOTE** User has to explicitly set `ip_rules` to empty slice (`[]`) to remove it.
        :param pulumi.Input[Sequence[pulumi.Input['AccountNetworkRulesPrivateLinkAccessRuleArgs']]] private_link_access_rules: One or More `private_link_access` block as defined below.
        :param pulumi.Input[str] storage_account_id: Specifies the ID of the storage account. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] virtual_network_subnet_ids: A list of virtual network subnet ids to secure the storage account.
               
               > **NOTE** User has to explicitly set `virtual_network_subnet_ids` to empty slice (`[]`) to remove it.
        """
        _AccountNetworkRulesState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bypasses=bypasses,
            default_action=default_action,
            ip_rules=ip_rules,
            private_link_access_rules=private_link_access_rules,
            storage_account_id=storage_account_id,
            virtual_network_subnet_ids=virtual_network_subnet_ids,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bypasses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             default_action: Optional[pulumi.Input[str]] = None,
             ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             private_link_access_rules: Optional[pulumi.Input[Sequence[pulumi.Input['AccountNetworkRulesPrivateLinkAccessRuleArgs']]]] = None,
             storage_account_id: Optional[pulumi.Input[str]] = None,
             virtual_network_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'defaultAction' in kwargs:
            default_action = kwargs['defaultAction']
        if 'ipRules' in kwargs:
            ip_rules = kwargs['ipRules']
        if 'privateLinkAccessRules' in kwargs:
            private_link_access_rules = kwargs['privateLinkAccessRules']
        if 'storageAccountId' in kwargs:
            storage_account_id = kwargs['storageAccountId']
        if 'virtualNetworkSubnetIds' in kwargs:
            virtual_network_subnet_ids = kwargs['virtualNetworkSubnetIds']

        if bypasses is not None:
            _setter("bypasses", bypasses)
        if default_action is not None:
            _setter("default_action", default_action)
        if ip_rules is not None:
            _setter("ip_rules", ip_rules)
        if private_link_access_rules is not None:
            _setter("private_link_access_rules", private_link_access_rules)
        if storage_account_id is not None:
            _setter("storage_account_id", storage_account_id)
        if virtual_network_subnet_ids is not None:
            _setter("virtual_network_subnet_ids", virtual_network_subnet_ids)

    @property
    @pulumi.getter
    def bypasses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Valid options are any combination of `Logging`, `Metrics`, `AzureServices`, or `None`.

        > **NOTE** User has to explicitly set `bypass` to empty slice (`[]`) to remove it.
        """
        return pulumi.get(self, "bypasses")

    @bypasses.setter
    def bypasses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "bypasses", value)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the default action of allow or deny when no other rules match. Valid options are `Deny` or `Allow`.
        """
        return pulumi.get(self, "default_action")

    @default_action.setter
    def default_action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_action", value)

    @property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of public IP or IP ranges in CIDR Format. Only IPv4 addresses are allowed. Private IP address ranges (as defined in [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3)) are not allowed.

        > **NOTE** Small address ranges using "/31" or "/32" prefix sizes are not supported. These ranges should be configured using individual IP address rules without prefix specified.

        > **NOTE** IP network rules have no effect on requests originating from the same Azure region as the storage account. Use Virtual network rules to allow same-region requests. Services deployed in the same region as the storage account use private Azure IP addresses for communication. Thus, you cannot restrict access to specific Azure services based on their public outbound IP address range.

        > **NOTE** User has to explicitly set `ip_rules` to empty slice (`[]`) to remove it.
        """
        return pulumi.get(self, "ip_rules")

    @ip_rules.setter
    def ip_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ip_rules", value)

    @property
    @pulumi.getter(name="privateLinkAccessRules")
    def private_link_access_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccountNetworkRulesPrivateLinkAccessRuleArgs']]]]:
        """
        One or More `private_link_access` block as defined below.
        """
        return pulumi.get(self, "private_link_access_rules")

    @private_link_access_rules.setter
    def private_link_access_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccountNetworkRulesPrivateLinkAccessRuleArgs']]]]):
        pulumi.set(self, "private_link_access_rules", value)

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the ID of the storage account. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "storage_account_id")

    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_id", value)

    @property
    @pulumi.getter(name="virtualNetworkSubnetIds")
    def virtual_network_subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of virtual network subnet ids to secure the storage account.

        > **NOTE** User has to explicitly set `virtual_network_subnet_ids` to empty slice (`[]`) to remove it.
        """
        return pulumi.get(self, "virtual_network_subnet_ids")

    @virtual_network_subnet_ids.setter
    def virtual_network_subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "virtual_network_subnet_ids", value)


class AccountNetworkRules(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bypasses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_action: Optional[pulumi.Input[str]] = None,
                 ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 private_link_access_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccountNetworkRulesPrivateLinkAccessRuleArgs']]]]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 virtual_network_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages network rules inside of a Azure Storage Account.

        > **NOTE:** Network Rules can be defined either directly on the `storage.Account` resource, or using the `storage.AccountNetworkRules` resource - but the two cannot be used together. Spurious changes will occur if both are used against the same Storage Account.

        > **NOTE:** Only one `storage.AccountNetworkRules` can be tied to an `storage.Account`. Spurious changes will occur if more than `storage.AccountNetworkRules` is tied to the same `storage.Account`.

        > **NOTE:** Deleting this resource updates the storage account back to the default values it had when the storage account was created.

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
            address_prefixes=["10.0.2.0/24"],
            service_endpoints=["Microsoft.Storage"])
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="GRS",
            tags={
                "environment": "staging",
            })
        example_account_network_rules = azure.storage.AccountNetworkRules("exampleAccountNetworkRules",
            storage_account_id=example_account.id,
            default_action="Allow",
            ip_rules=["127.0.0.1"],
            virtual_network_subnet_ids=[example_subnet.id],
            bypasses=["Metrics"])
        ```

        ## Import

        Storage Account Network Rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:storage/accountNetworkRules:AccountNetworkRules storageAcc1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myresourcegroup/providers/Microsoft.Storage/storageAccounts/myaccount
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] bypasses: Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Valid options are any combination of `Logging`, `Metrics`, `AzureServices`, or `None`.
               
               > **NOTE** User has to explicitly set `bypass` to empty slice (`[]`) to remove it.
        :param pulumi.Input[str] default_action: Specifies the default action of allow or deny when no other rules match. Valid options are `Deny` or `Allow`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_rules: List of public IP or IP ranges in CIDR Format. Only IPv4 addresses are allowed. Private IP address ranges (as defined in [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3)) are not allowed.
               
               > **NOTE** Small address ranges using "/31" or "/32" prefix sizes are not supported. These ranges should be configured using individual IP address rules without prefix specified.
               
               > **NOTE** IP network rules have no effect on requests originating from the same Azure region as the storage account. Use Virtual network rules to allow same-region requests. Services deployed in the same region as the storage account use private Azure IP addresses for communication. Thus, you cannot restrict access to specific Azure services based on their public outbound IP address range.
               
               > **NOTE** User has to explicitly set `ip_rules` to empty slice (`[]`) to remove it.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccountNetworkRulesPrivateLinkAccessRuleArgs']]]] private_link_access_rules: One or More `private_link_access` block as defined below.
        :param pulumi.Input[str] storage_account_id: Specifies the ID of the storage account. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] virtual_network_subnet_ids: A list of virtual network subnet ids to secure the storage account.
               
               > **NOTE** User has to explicitly set `virtual_network_subnet_ids` to empty slice (`[]`) to remove it.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccountNetworkRulesInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages network rules inside of a Azure Storage Account.

        > **NOTE:** Network Rules can be defined either directly on the `storage.Account` resource, or using the `storage.AccountNetworkRules` resource - but the two cannot be used together. Spurious changes will occur if both are used against the same Storage Account.

        > **NOTE:** Only one `storage.AccountNetworkRules` can be tied to an `storage.Account`. Spurious changes will occur if more than `storage.AccountNetworkRules` is tied to the same `storage.Account`.

        > **NOTE:** Deleting this resource updates the storage account back to the default values it had when the storage account was created.

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
            address_prefixes=["10.0.2.0/24"],
            service_endpoints=["Microsoft.Storage"])
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="GRS",
            tags={
                "environment": "staging",
            })
        example_account_network_rules = azure.storage.AccountNetworkRules("exampleAccountNetworkRules",
            storage_account_id=example_account.id,
            default_action="Allow",
            ip_rules=["127.0.0.1"],
            virtual_network_subnet_ids=[example_subnet.id],
            bypasses=["Metrics"])
        ```

        ## Import

        Storage Account Network Rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:storage/accountNetworkRules:AccountNetworkRules storageAcc1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myresourcegroup/providers/Microsoft.Storage/storageAccounts/myaccount
        ```

        :param str resource_name: The name of the resource.
        :param AccountNetworkRulesInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountNetworkRulesInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AccountNetworkRulesInitArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bypasses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_action: Optional[pulumi.Input[str]] = None,
                 ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 private_link_access_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccountNetworkRulesPrivateLinkAccessRuleArgs']]]]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 virtual_network_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccountNetworkRulesInitArgs.__new__(AccountNetworkRulesInitArgs)

            __props__.__dict__["bypasses"] = bypasses
            if default_action is None and not opts.urn:
                raise TypeError("Missing required property 'default_action'")
            __props__.__dict__["default_action"] = default_action
            __props__.__dict__["ip_rules"] = ip_rules
            __props__.__dict__["private_link_access_rules"] = private_link_access_rules
            if storage_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_id'")
            __props__.__dict__["storage_account_id"] = storage_account_id
            __props__.__dict__["virtual_network_subnet_ids"] = virtual_network_subnet_ids
        super(AccountNetworkRules, __self__).__init__(
            'azure:storage/accountNetworkRules:AccountNetworkRules',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bypasses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            default_action: Optional[pulumi.Input[str]] = None,
            ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            private_link_access_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccountNetworkRulesPrivateLinkAccessRuleArgs']]]]] = None,
            storage_account_id: Optional[pulumi.Input[str]] = None,
            virtual_network_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'AccountNetworkRules':
        """
        Get an existing AccountNetworkRules resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] bypasses: Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Valid options are any combination of `Logging`, `Metrics`, `AzureServices`, or `None`.
               
               > **NOTE** User has to explicitly set `bypass` to empty slice (`[]`) to remove it.
        :param pulumi.Input[str] default_action: Specifies the default action of allow or deny when no other rules match. Valid options are `Deny` or `Allow`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_rules: List of public IP or IP ranges in CIDR Format. Only IPv4 addresses are allowed. Private IP address ranges (as defined in [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3)) are not allowed.
               
               > **NOTE** Small address ranges using "/31" or "/32" prefix sizes are not supported. These ranges should be configured using individual IP address rules without prefix specified.
               
               > **NOTE** IP network rules have no effect on requests originating from the same Azure region as the storage account. Use Virtual network rules to allow same-region requests. Services deployed in the same region as the storage account use private Azure IP addresses for communication. Thus, you cannot restrict access to specific Azure services based on their public outbound IP address range.
               
               > **NOTE** User has to explicitly set `ip_rules` to empty slice (`[]`) to remove it.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccountNetworkRulesPrivateLinkAccessRuleArgs']]]] private_link_access_rules: One or More `private_link_access` block as defined below.
        :param pulumi.Input[str] storage_account_id: Specifies the ID of the storage account. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] virtual_network_subnet_ids: A list of virtual network subnet ids to secure the storage account.
               
               > **NOTE** User has to explicitly set `virtual_network_subnet_ids` to empty slice (`[]`) to remove it.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccountNetworkRulesState.__new__(_AccountNetworkRulesState)

        __props__.__dict__["bypasses"] = bypasses
        __props__.__dict__["default_action"] = default_action
        __props__.__dict__["ip_rules"] = ip_rules
        __props__.__dict__["private_link_access_rules"] = private_link_access_rules
        __props__.__dict__["storage_account_id"] = storage_account_id
        __props__.__dict__["virtual_network_subnet_ids"] = virtual_network_subnet_ids
        return AccountNetworkRules(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bypasses(self) -> pulumi.Output[Sequence[str]]:
        """
        Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Valid options are any combination of `Logging`, `Metrics`, `AzureServices`, or `None`.

        > **NOTE** User has to explicitly set `bypass` to empty slice (`[]`) to remove it.
        """
        return pulumi.get(self, "bypasses")

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Output[str]:
        """
        Specifies the default action of allow or deny when no other rules match. Valid options are `Deny` or `Allow`.
        """
        return pulumi.get(self, "default_action")

    @property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> pulumi.Output[Sequence[str]]:
        """
        List of public IP or IP ranges in CIDR Format. Only IPv4 addresses are allowed. Private IP address ranges (as defined in [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3)) are not allowed.

        > **NOTE** Small address ranges using "/31" or "/32" prefix sizes are not supported. These ranges should be configured using individual IP address rules without prefix specified.

        > **NOTE** IP network rules have no effect on requests originating from the same Azure region as the storage account. Use Virtual network rules to allow same-region requests. Services deployed in the same region as the storage account use private Azure IP addresses for communication. Thus, you cannot restrict access to specific Azure services based on their public outbound IP address range.

        > **NOTE** User has to explicitly set `ip_rules` to empty slice (`[]`) to remove it.
        """
        return pulumi.get(self, "ip_rules")

    @property
    @pulumi.getter(name="privateLinkAccessRules")
    def private_link_access_rules(self) -> pulumi.Output[Optional[Sequence['outputs.AccountNetworkRulesPrivateLinkAccessRule']]]:
        """
        One or More `private_link_access` block as defined below.
        """
        return pulumi.get(self, "private_link_access_rules")

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Output[str]:
        """
        Specifies the ID of the storage account. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "storage_account_id")

    @property
    @pulumi.getter(name="virtualNetworkSubnetIds")
    def virtual_network_subnet_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of virtual network subnet ids to secure the storage account.

        > **NOTE** User has to explicitly set `virtual_network_subnet_ids` to empty slice (`[]`) to remove it.
        """
        return pulumi.get(self, "virtual_network_subnet_ids")


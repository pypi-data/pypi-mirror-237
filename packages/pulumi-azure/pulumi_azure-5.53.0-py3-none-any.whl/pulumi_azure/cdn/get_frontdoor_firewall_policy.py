# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetFrontdoorFirewallPolicyResult',
    'AwaitableGetFrontdoorFirewallPolicyResult',
    'get_frontdoor_firewall_policy',
    'get_frontdoor_firewall_policy_output',
]

@pulumi.output_type
class GetFrontdoorFirewallPolicyResult:
    """
    A collection of values returned by getFrontdoorFirewallPolicy.
    """
    def __init__(__self__, enabled=None, frontend_endpoint_ids=None, id=None, mode=None, name=None, redirect_url=None, resource_group_name=None, sku_name=None):
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if frontend_endpoint_ids and not isinstance(frontend_endpoint_ids, list):
            raise TypeError("Expected argument 'frontend_endpoint_ids' to be a list")
        pulumi.set(__self__, "frontend_endpoint_ids", frontend_endpoint_ids)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        pulumi.set(__self__, "mode", mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if redirect_url and not isinstance(redirect_url, str):
            raise TypeError("Expected argument 'redirect_url' to be a str")
        pulumi.set(__self__, "redirect_url", redirect_url)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if sku_name and not isinstance(sku_name, str):
            raise TypeError("Expected argument 'sku_name' to be a str")
        pulumi.set(__self__, "sku_name", sku_name)

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        The enabled state of the Front Door Firewall Policy.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="frontendEndpointIds")
    def frontend_endpoint_ids(self) -> Sequence[str]:
        """
        The Front Door Profiles frontend endpoints associated with this Front Door Firewall Policy.
        """
        return pulumi.get(self, "frontend_endpoint_ids")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def mode(self) -> str:
        """
        The Front Door Firewall Policy mode.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> str:
        """
        The redirect URL for the client.
        """
        return pulumi.get(self, "redirect_url")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> str:
        """
        The sku's pricing tier for this Front Door Firewall Policy.
        """
        return pulumi.get(self, "sku_name")


class AwaitableGetFrontdoorFirewallPolicyResult(GetFrontdoorFirewallPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFrontdoorFirewallPolicyResult(
            enabled=self.enabled,
            frontend_endpoint_ids=self.frontend_endpoint_ids,
            id=self.id,
            mode=self.mode,
            name=self.name,
            redirect_url=self.redirect_url,
            resource_group_name=self.resource_group_name,
            sku_name=self.sku_name)


def get_frontdoor_firewall_policy(name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFrontdoorFirewallPolicyResult:
    """
    Use this data source to access information about an existing Front Door (standard/premium) Firewall Policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.cdn.get_frontdoor_firewall_policy(name="examplecdnfdwafpolicy",
        resource_group_name=azurerm_resource_group["example"]["name"])
    ```


    :param str name: The name of the Front Door Firewall Policy.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:cdn/getFrontdoorFirewallPolicy:getFrontdoorFirewallPolicy', __args__, opts=opts, typ=GetFrontdoorFirewallPolicyResult).value

    return AwaitableGetFrontdoorFirewallPolicyResult(
        enabled=pulumi.get(__ret__, 'enabled'),
        frontend_endpoint_ids=pulumi.get(__ret__, 'frontend_endpoint_ids'),
        id=pulumi.get(__ret__, 'id'),
        mode=pulumi.get(__ret__, 'mode'),
        name=pulumi.get(__ret__, 'name'),
        redirect_url=pulumi.get(__ret__, 'redirect_url'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        sku_name=pulumi.get(__ret__, 'sku_name'))


@_utilities.lift_output_func(get_frontdoor_firewall_policy)
def get_frontdoor_firewall_policy_output(name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFrontdoorFirewallPolicyResult]:
    """
    Use this data source to access information about an existing Front Door (standard/premium) Firewall Policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.cdn.get_frontdoor_firewall_policy(name="examplecdnfdwafpolicy",
        resource_group_name=azurerm_resource_group["example"]["name"])
    ```


    :param str name: The name of the Front Door Firewall Policy.
    :param str resource_group_name: The name of the resource group.
    """
    ...

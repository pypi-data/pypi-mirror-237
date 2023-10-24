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
    'GetNetworkSecurityGroupResult',
    'AwaitableGetNetworkSecurityGroupResult',
    'get_network_security_group',
    'get_network_security_group_output',
]

@pulumi.output_type
class GetNetworkSecurityGroupResult:
    """
    A collection of values returned by getNetworkSecurityGroup.
    """
    def __init__(__self__, id=None, location=None, name=None, resource_group_name=None, security_rules=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if security_rules and not isinstance(security_rules, list):
            raise TypeError("Expected argument 'security_rules' to be a list")
        pulumi.set(__self__, "security_rules", security_rules)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The supported Azure location where the resource exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the security rule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="securityRules")
    def security_rules(self) -> Sequence['outputs.GetNetworkSecurityGroupSecurityRuleResult']:
        """
        One or more `security_rule` blocks as defined below.
        """
        return pulumi.get(self, "security_rules")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags assigned to the resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetNetworkSecurityGroupResult(GetNetworkSecurityGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkSecurityGroupResult(
            id=self.id,
            location=self.location,
            name=self.name,
            resource_group_name=self.resource_group_name,
            security_rules=self.security_rules,
            tags=self.tags)


def get_network_security_group(name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkSecurityGroupResult:
    """
    Use this data source to access information about an existing Network Security Group.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.network.get_network_security_group(name="example",
        resource_group_name=azurerm_resource_group["example"]["name"])
    pulumi.export("location", example.location)
    ```


    :param str name: Specifies the Name of the Network Security Group.
    :param str resource_group_name: Specifies the Name of the Resource Group within which the Network Security Group exists
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:network/getNetworkSecurityGroup:getNetworkSecurityGroup', __args__, opts=opts, typ=GetNetworkSecurityGroupResult).value

    return AwaitableGetNetworkSecurityGroupResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        security_rules=pulumi.get(__ret__, 'security_rules'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_network_security_group)
def get_network_security_group_output(name: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkSecurityGroupResult]:
    """
    Use this data source to access information about an existing Network Security Group.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.network.get_network_security_group(name="example",
        resource_group_name=azurerm_resource_group["example"]["name"])
    pulumi.export("location", example.location)
    ```


    :param str name: Specifies the Name of the Network Security Group.
    :param str resource_group_name: Specifies the Name of the Resource Group within which the Network Security Group exists
    """
    ...

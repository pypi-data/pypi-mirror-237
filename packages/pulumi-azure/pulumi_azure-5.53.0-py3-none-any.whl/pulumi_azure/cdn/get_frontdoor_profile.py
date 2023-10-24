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
    'GetFrontdoorProfileResult',
    'AwaitableGetFrontdoorProfileResult',
    'get_frontdoor_profile',
    'get_frontdoor_profile_output',
]

@pulumi.output_type
class GetFrontdoorProfileResult:
    """
    A collection of values returned by getFrontdoorProfile.
    """
    def __init__(__self__, id=None, name=None, resource_group_name=None, resource_guid=None, response_timeout_seconds=None, sku_name=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if resource_guid and not isinstance(resource_guid, str):
            raise TypeError("Expected argument 'resource_guid' to be a str")
        pulumi.set(__self__, "resource_guid", resource_guid)
        if response_timeout_seconds and not isinstance(response_timeout_seconds, int):
            raise TypeError("Expected argument 'response_timeout_seconds' to be a int")
        pulumi.set(__self__, "response_timeout_seconds", response_timeout_seconds)
        if sku_name and not isinstance(sku_name, str):
            raise TypeError("Expected argument 'sku_name' to be a str")
        pulumi.set(__self__, "sku_name", sku_name)
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
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> str:
        """
        The UUID of the Front Door Profile which will be sent in the HTTP Header as the `X-Azure-FDID` attribute.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter(name="responseTimeoutSeconds")
    def response_timeout_seconds(self) -> int:
        """
        Specifies the maximum response timeout in seconds.
        """
        return pulumi.get(self, "response_timeout_seconds")

    @property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> str:
        """
        Specifies the SKU for this Front Door Profile.
        """
        return pulumi.get(self, "sku_name")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Specifies a mapping of Tags assigned to this Front Door Profile.
        """
        return pulumi.get(self, "tags")


class AwaitableGetFrontdoorProfileResult(GetFrontdoorProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFrontdoorProfileResult(
            id=self.id,
            name=self.name,
            resource_group_name=self.resource_group_name,
            resource_guid=self.resource_guid,
            response_timeout_seconds=self.response_timeout_seconds,
            sku_name=self.sku_name,
            tags=self.tags)


def get_frontdoor_profile(name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFrontdoorProfileResult:
    """
    Use this data source to access information about an existing Front Door (standard/premium) Profile.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.cdn.get_frontdoor_profile(name="existing-cdn-profile",
        resource_group_name="existing-resources")
    ```


    :param str name: Specifies the name of the Front Door Profile.
    :param str resource_group_name: The name of the Resource Group where this Front Door Profile exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:cdn/getFrontdoorProfile:getFrontdoorProfile', __args__, opts=opts, typ=GetFrontdoorProfileResult).value

    return AwaitableGetFrontdoorProfileResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        resource_guid=pulumi.get(__ret__, 'resource_guid'),
        response_timeout_seconds=pulumi.get(__ret__, 'response_timeout_seconds'),
        sku_name=pulumi.get(__ret__, 'sku_name'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_frontdoor_profile)
def get_frontdoor_profile_output(name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFrontdoorProfileResult]:
    """
    Use this data source to access information about an existing Front Door (standard/premium) Profile.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.cdn.get_frontdoor_profile(name="existing-cdn-profile",
        resource_group_name="existing-resources")
    ```


    :param str name: Specifies the name of the Front Door Profile.
    :param str resource_group_name: The name of the Resource Group where this Front Door Profile exists.
    """
    ...

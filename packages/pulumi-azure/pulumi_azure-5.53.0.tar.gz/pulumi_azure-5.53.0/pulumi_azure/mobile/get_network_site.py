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
    'GetNetworkSiteResult',
    'AwaitableGetNetworkSiteResult',
    'get_network_site',
    'get_network_site_output',
]

@pulumi.output_type
class GetNetworkSiteResult:
    """
    A collection of values returned by getNetworkSite.
    """
    def __init__(__self__, id=None, location=None, mobile_network_id=None, name=None, network_function_ids=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if mobile_network_id and not isinstance(mobile_network_id, str):
            raise TypeError("Expected argument 'mobile_network_id' to be a str")
        pulumi.set(__self__, "mobile_network_id", mobile_network_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_function_ids and not isinstance(network_function_ids, list):
            raise TypeError("Expected argument 'network_function_ids' to be a list")
        pulumi.set(__self__, "network_function_ids", network_function_ids)
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
        The Azure Region where the Mobile Network Site should exist.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mobileNetworkId")
    def mobile_network_id(self) -> str:
        return pulumi.get(self, "mobile_network_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkFunctionIds")
    def network_function_ids(self) -> Sequence[str]:
        """
        An array of Id of Network Functions deployed on the site.
        """
        return pulumi.get(self, "network_function_ids")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags which should be assigned to the Mobile Network Site.
        """
        return pulumi.get(self, "tags")


class AwaitableGetNetworkSiteResult(GetNetworkSiteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkSiteResult(
            id=self.id,
            location=self.location,
            mobile_network_id=self.mobile_network_id,
            name=self.name,
            network_function_ids=self.network_function_ids,
            tags=self.tags)


def get_network_site(mobile_network_id: Optional[str] = None,
                     name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkSiteResult:
    """
    Get information about a Mobile Network Site.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example_network = azure.mobile.get_network(name="example-mn",
        resource_group_name="example-rg")
    example_network_site = azure.mobile.get_network_site(name="example-mns",
        mobile_network_id=example_network.id)
    ```


    :param str mobile_network_id: the ID of the Mobile Network which the Mobile Network Site belongs to.
    :param str name: The name which should be used for this Mobile Network Site.
    """
    __args__ = dict()
    __args__['mobileNetworkId'] = mobile_network_id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:mobile/getNetworkSite:getNetworkSite', __args__, opts=opts, typ=GetNetworkSiteResult).value

    return AwaitableGetNetworkSiteResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        mobile_network_id=pulumi.get(__ret__, 'mobile_network_id'),
        name=pulumi.get(__ret__, 'name'),
        network_function_ids=pulumi.get(__ret__, 'network_function_ids'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_network_site)
def get_network_site_output(mobile_network_id: Optional[pulumi.Input[str]] = None,
                            name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkSiteResult]:
    """
    Get information about a Mobile Network Site.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example_network = azure.mobile.get_network(name="example-mn",
        resource_group_name="example-rg")
    example_network_site = azure.mobile.get_network_site(name="example-mns",
        mobile_network_id=example_network.id)
    ```


    :param str mobile_network_id: the ID of the Mobile Network which the Mobile Network Site belongs to.
    :param str name: The name which should be used for this Mobile Network Site.
    """
    ...

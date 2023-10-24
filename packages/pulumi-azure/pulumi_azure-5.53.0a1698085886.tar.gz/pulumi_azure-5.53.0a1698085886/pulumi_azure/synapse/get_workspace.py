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
    'GetWorkspaceResult',
    'AwaitableGetWorkspaceResult',
    'get_workspace',
    'get_workspace_output',
]

@pulumi.output_type
class GetWorkspaceResult:
    """
    A collection of values returned by getWorkspace.
    """
    def __init__(__self__, connectivity_endpoints=None, id=None, identities=None, location=None, name=None, resource_group_name=None, tags=None):
        if connectivity_endpoints and not isinstance(connectivity_endpoints, dict):
            raise TypeError("Expected argument 'connectivity_endpoints' to be a dict")
        pulumi.set(__self__, "connectivity_endpoints", connectivity_endpoints)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identities and not isinstance(identities, list):
            raise TypeError("Expected argument 'identities' to be a list")
        pulumi.set(__self__, "identities", identities)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="connectivityEndpoints")
    def connectivity_endpoints(self) -> Mapping[str, str]:
        """
        A list of Connectivity endpoints for this Synapse Workspace.
        """
        return pulumi.get(self, "connectivity_endpoints")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identities(self) -> Sequence['outputs.GetWorkspaceIdentityResult']:
        """
        An `identity` block as defined below, which contains the Managed Service Identity information for this Synapse Workspace.
        """
        return pulumi.get(self, "identities")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The Azure location where the Synapse Workspace exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags assigned to the resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetWorkspaceResult(GetWorkspaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceResult(
            connectivity_endpoints=self.connectivity_endpoints,
            id=self.id,
            identities=self.identities,
            location=self.location,
            name=self.name,
            resource_group_name=self.resource_group_name,
            tags=self.tags)


def get_workspace(name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceResult:
    """
    Use this data source to access information about an existing Synapse Workspace.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.synapse.get_workspace(name="existing",
        resource_group_name="example-resource-group")
    pulumi.export("id", example.id)
    ```


    :param str name: The name of this Synapse Workspace.
    :param str resource_group_name: The name of the Resource Group where the Synapse Workspace exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:synapse/getWorkspace:getWorkspace', __args__, opts=opts, typ=GetWorkspaceResult).value

    return AwaitableGetWorkspaceResult(
        connectivity_endpoints=pulumi.get(__ret__, 'connectivity_endpoints'),
        id=pulumi.get(__ret__, 'id'),
        identities=pulumi.get(__ret__, 'identities'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_workspace)
def get_workspace_output(name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceResult]:
    """
    Use this data source to access information about an existing Synapse Workspace.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.synapse.get_workspace(name="existing",
        resource_group_name="example-resource-group")
    pulumi.export("id", example.id)
    ```


    :param str name: The name of this Synapse Workspace.
    :param str resource_group_name: The name of the Resource Group where the Synapse Workspace exists.
    """
    ...

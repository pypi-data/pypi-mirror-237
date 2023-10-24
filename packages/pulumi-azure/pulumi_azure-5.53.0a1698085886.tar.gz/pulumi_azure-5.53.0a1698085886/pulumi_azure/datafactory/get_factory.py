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
    'GetFactoryResult',
    'AwaitableGetFactoryResult',
    'get_factory',
    'get_factory_output',
]

@pulumi.output_type
class GetFactoryResult:
    """
    A collection of values returned by getFactory.
    """
    def __init__(__self__, github_configurations=None, id=None, identities=None, location=None, name=None, resource_group_name=None, tags=None, vsts_configurations=None):
        if github_configurations and not isinstance(github_configurations, list):
            raise TypeError("Expected argument 'github_configurations' to be a list")
        pulumi.set(__self__, "github_configurations", github_configurations)
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
        if vsts_configurations and not isinstance(vsts_configurations, list):
            raise TypeError("Expected argument 'vsts_configurations' to be a list")
        pulumi.set(__self__, "vsts_configurations", vsts_configurations)

    @property
    @pulumi.getter(name="githubConfigurations")
    def github_configurations(self) -> Sequence['outputs.GetFactoryGithubConfigurationResult']:
        """
        A `github_configuration` block as defined below.
        """
        return pulumi.get(self, "github_configurations")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identities(self) -> Sequence['outputs.GetFactoryIdentityResult']:
        """
        An `identity` block as defined below.
        """
        return pulumi.get(self, "identities")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The Azure Region where the Azure Data Factory exists.
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
        A mapping of tags assigned to the Azure Data Factory.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vstsConfigurations")
    def vsts_configurations(self) -> Sequence['outputs.GetFactoryVstsConfigurationResult']:
        """
        A `vsts_configuration` block as defined below.
        """
        return pulumi.get(self, "vsts_configurations")


class AwaitableGetFactoryResult(GetFactoryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFactoryResult(
            github_configurations=self.github_configurations,
            id=self.id,
            identities=self.identities,
            location=self.location,
            name=self.name,
            resource_group_name=self.resource_group_name,
            tags=self.tags,
            vsts_configurations=self.vsts_configurations)


def get_factory(name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFactoryResult:
    """
    Use this data source to access information about an existing Azure Data Factory (Version 2).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.datafactory.get_factory(name="existing-adf",
        resource_group_name="existing-rg")
    pulumi.export("id", example.id)
    ```


    :param str name: The name of this Azure Data Factory.
    :param str resource_group_name: The name of the Resource Group where the Azure Data Factory exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:datafactory/getFactory:getFactory', __args__, opts=opts, typ=GetFactoryResult).value

    return AwaitableGetFactoryResult(
        github_configurations=pulumi.get(__ret__, 'github_configurations'),
        id=pulumi.get(__ret__, 'id'),
        identities=pulumi.get(__ret__, 'identities'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        tags=pulumi.get(__ret__, 'tags'),
        vsts_configurations=pulumi.get(__ret__, 'vsts_configurations'))


@_utilities.lift_output_func(get_factory)
def get_factory_output(name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFactoryResult]:
    """
    Use this data source to access information about an existing Azure Data Factory (Version 2).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.datafactory.get_factory(name="existing-adf",
        resource_group_name="existing-rg")
    pulumi.export("id", example.id)
    ```


    :param str name: The name of this Azure Data Factory.
    :param str resource_group_name: The name of the Resource Group where the Azure Data Factory exists.
    """
    ...

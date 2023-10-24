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
    'GetConfidentialLedgerResult',
    'AwaitableGetConfidentialLedgerResult',
    'get_confidential_ledger',
    'get_confidential_ledger_output',
]

@pulumi.output_type
class GetConfidentialLedgerResult:
    """
    A collection of values returned by getConfidentialLedger.
    """
    def __init__(__self__, azuread_based_service_principals=None, certificate_based_security_principals=None, id=None, identity_service_endpoint=None, ledger_endpoint=None, ledger_type=None, location=None, name=None, resource_group_name=None, tags=None):
        if azuread_based_service_principals and not isinstance(azuread_based_service_principals, list):
            raise TypeError("Expected argument 'azuread_based_service_principals' to be a list")
        pulumi.set(__self__, "azuread_based_service_principals", azuread_based_service_principals)
        if certificate_based_security_principals and not isinstance(certificate_based_security_principals, list):
            raise TypeError("Expected argument 'certificate_based_security_principals' to be a list")
        pulumi.set(__self__, "certificate_based_security_principals", certificate_based_security_principals)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity_service_endpoint and not isinstance(identity_service_endpoint, str):
            raise TypeError("Expected argument 'identity_service_endpoint' to be a str")
        pulumi.set(__self__, "identity_service_endpoint", identity_service_endpoint)
        if ledger_endpoint and not isinstance(ledger_endpoint, str):
            raise TypeError("Expected argument 'ledger_endpoint' to be a str")
        pulumi.set(__self__, "ledger_endpoint", ledger_endpoint)
        if ledger_type and not isinstance(ledger_type, str):
            raise TypeError("Expected argument 'ledger_type' to be a str")
        pulumi.set(__self__, "ledger_type", ledger_type)
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
    @pulumi.getter(name="azureadBasedServicePrincipals")
    def azuread_based_service_principals(self) -> Sequence['outputs.GetConfidentialLedgerAzureadBasedServicePrincipalResult']:
        return pulumi.get(self, "azuread_based_service_principals")

    @property
    @pulumi.getter(name="certificateBasedSecurityPrincipals")
    def certificate_based_security_principals(self) -> Sequence['outputs.GetConfidentialLedgerCertificateBasedSecurityPrincipalResult']:
        return pulumi.get(self, "certificate_based_security_principals")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="identityServiceEndpoint")
    def identity_service_endpoint(self) -> str:
        """
        The Identity Service Endpoint for this Confidential Ledger.
        """
        return pulumi.get(self, "identity_service_endpoint")

    @property
    @pulumi.getter(name="ledgerEndpoint")
    def ledger_endpoint(self) -> str:
        """
        The Endpoint for this Confidential Ledger.
        """
        return pulumi.get(self, "ledger_endpoint")

    @property
    @pulumi.getter(name="ledgerType")
    def ledger_type(self) -> str:
        """
        The type of Confidential Ledger.
        """
        return pulumi.get(self, "ledger_type")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The supported Azure location where the Confidential Ledger exists.
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
        A mapping of tags to assign to the Confidential Ledger.
        """
        return pulumi.get(self, "tags")


class AwaitableGetConfidentialLedgerResult(GetConfidentialLedgerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfidentialLedgerResult(
            azuread_based_service_principals=self.azuread_based_service_principals,
            certificate_based_security_principals=self.certificate_based_security_principals,
            id=self.id,
            identity_service_endpoint=self.identity_service_endpoint,
            ledger_endpoint=self.ledger_endpoint,
            ledger_type=self.ledger_type,
            location=self.location,
            name=self.name,
            resource_group_name=self.resource_group_name,
            tags=self.tags)


def get_confidential_ledger(name: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfidentialLedgerResult:
    """
    Gets information about an existing Confidential Ledger.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    current = azure.compute.get_confidential_ledger(name="example-ledger",
        resource_group_name="example-resources")
    pulumi.export("ledgerEndpoint", current.ledger_endpoint)
    ```


    :param str name: Specifies the name of this Confidential Ledger.
    :param str resource_group_name: Specifies the name of the Resource Group where this Confidential Ledger exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:compute/getConfidentialLedger:getConfidentialLedger', __args__, opts=opts, typ=GetConfidentialLedgerResult).value

    return AwaitableGetConfidentialLedgerResult(
        azuread_based_service_principals=pulumi.get(__ret__, 'azuread_based_service_principals'),
        certificate_based_security_principals=pulumi.get(__ret__, 'certificate_based_security_principals'),
        id=pulumi.get(__ret__, 'id'),
        identity_service_endpoint=pulumi.get(__ret__, 'identity_service_endpoint'),
        ledger_endpoint=pulumi.get(__ret__, 'ledger_endpoint'),
        ledger_type=pulumi.get(__ret__, 'ledger_type'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_confidential_ledger)
def get_confidential_ledger_output(name: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfidentialLedgerResult]:
    """
    Gets information about an existing Confidential Ledger.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    current = azure.compute.get_confidential_ledger(name="example-ledger",
        resource_group_name="example-resources")
    pulumi.export("ledgerEndpoint", current.ledger_endpoint)
    ```


    :param str name: Specifies the name of this Confidential Ledger.
    :param str resource_group_name: Specifies the name of the Resource Group where this Confidential Ledger exists.
    """
    ...

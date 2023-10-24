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
    'LedgerAzureadBasedServicePrincipal',
    'LedgerCertificateBasedSecurityPrincipal',
]

@pulumi.output_type
class LedgerAzureadBasedServicePrincipal(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ledgerRoleName":
            suggest = "ledger_role_name"
        elif key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LedgerAzureadBasedServicePrincipal. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LedgerAzureadBasedServicePrincipal.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LedgerAzureadBasedServicePrincipal.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 ledger_role_name: str,
                 principal_id: str,
                 tenant_id: str):
        """
        :param str ledger_role_name: Specifies the Ledger Role to grant this AzureAD Service Principal. Possible values are `Administrator`, `Contributor` and `Reader`.
        :param str principal_id: Specifies the Principal ID of the AzureAD Service Principal.
        :param str tenant_id: Specifies the Tenant ID for this AzureAD Service Principal.
        """
        LedgerAzureadBasedServicePrincipal._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            ledger_role_name=ledger_role_name,
            principal_id=principal_id,
            tenant_id=tenant_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             ledger_role_name: str,
             principal_id: str,
             tenant_id: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'ledgerRoleName' in kwargs:
            ledger_role_name = kwargs['ledgerRoleName']
        if 'principalId' in kwargs:
            principal_id = kwargs['principalId']
        if 'tenantId' in kwargs:
            tenant_id = kwargs['tenantId']

        _setter("ledger_role_name", ledger_role_name)
        _setter("principal_id", principal_id)
        _setter("tenant_id", tenant_id)

    @property
    @pulumi.getter(name="ledgerRoleName")
    def ledger_role_name(self) -> str:
        """
        Specifies the Ledger Role to grant this AzureAD Service Principal. Possible values are `Administrator`, `Contributor` and `Reader`.
        """
        return pulumi.get(self, "ledger_role_name")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        Specifies the Principal ID of the AzureAD Service Principal.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        Specifies the Tenant ID for this AzureAD Service Principal.
        """
        return pulumi.get(self, "tenant_id")


@pulumi.output_type
class LedgerCertificateBasedSecurityPrincipal(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ledgerRoleName":
            suggest = "ledger_role_name"
        elif key == "pemPublicKey":
            suggest = "pem_public_key"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LedgerCertificateBasedSecurityPrincipal. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LedgerCertificateBasedSecurityPrincipal.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LedgerCertificateBasedSecurityPrincipal.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 ledger_role_name: str,
                 pem_public_key: str):
        """
        :param str ledger_role_name: Specifies the Ledger Role to grant this Certificate Security Principal. Possible values are `Administrator`, `Contributor` and `Reader`.
        :param str pem_public_key: The public key, in PEM format, of the certificate used by this identity to authenticate with the Confidential Ledger.
        """
        LedgerCertificateBasedSecurityPrincipal._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            ledger_role_name=ledger_role_name,
            pem_public_key=pem_public_key,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             ledger_role_name: str,
             pem_public_key: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'ledgerRoleName' in kwargs:
            ledger_role_name = kwargs['ledgerRoleName']
        if 'pemPublicKey' in kwargs:
            pem_public_key = kwargs['pemPublicKey']

        _setter("ledger_role_name", ledger_role_name)
        _setter("pem_public_key", pem_public_key)

    @property
    @pulumi.getter(name="ledgerRoleName")
    def ledger_role_name(self) -> str:
        """
        Specifies the Ledger Role to grant this Certificate Security Principal. Possible values are `Administrator`, `Contributor` and `Reader`.
        """
        return pulumi.get(self, "ledger_role_name")

    @property
    @pulumi.getter(name="pemPublicKey")
    def pem_public_key(self) -> str:
        """
        The public key, in PEM format, of the certificate used by this identity to authenticate with the Confidential Ledger.
        """
        return pulumi.get(self, "pem_public_key")



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
    'ServiceInitialReplicaSet',
    'ServiceNotifications',
    'ServiceSecureLdap',
    'ServiceSecurity',
    'GetServiceNotificationResult',
    'GetServiceReplicaSetResult',
    'GetServiceSecureLdapResult',
    'GetServiceSecurityResult',
]

@pulumi.output_type
class ServiceInitialReplicaSet(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subnetId":
            suggest = "subnet_id"
        elif key == "domainControllerIpAddresses":
            suggest = "domain_controller_ip_addresses"
        elif key == "externalAccessIpAddress":
            suggest = "external_access_ip_address"
        elif key == "serviceStatus":
            suggest = "service_status"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceInitialReplicaSet. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceInitialReplicaSet.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceInitialReplicaSet.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 subnet_id: str,
                 domain_controller_ip_addresses: Optional[Sequence[str]] = None,
                 external_access_ip_address: Optional[str] = None,
                 id: Optional[str] = None,
                 location: Optional[str] = None,
                 service_status: Optional[str] = None):
        """
        :param str subnet_id: The ID of the subnet in which to place the initial replica set. Changing this forces a new resource to be created.
        :param Sequence[str] domain_controller_ip_addresses: A list of subnet IP addresses for the domain controllers in the initial replica set, typically two.
        :param str external_access_ip_address: The publicly routable IP address for the domain controllers in the initial replica set.
        :param str id: A unique ID for the replica set.
        :param str location: The Azure location where the Domain Service exists. Changing this forces a new resource to be created.
        :param str service_status: The current service status for the initial replica set.
        """
        ServiceInitialReplicaSet._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            subnet_id=subnet_id,
            domain_controller_ip_addresses=domain_controller_ip_addresses,
            external_access_ip_address=external_access_ip_address,
            id=id,
            location=location,
            service_status=service_status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             subnet_id: str,
             domain_controller_ip_addresses: Optional[Sequence[str]] = None,
             external_access_ip_address: Optional[str] = None,
             id: Optional[str] = None,
             location: Optional[str] = None,
             service_status: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'subnetId' in kwargs:
            subnet_id = kwargs['subnetId']
        if 'domainControllerIpAddresses' in kwargs:
            domain_controller_ip_addresses = kwargs['domainControllerIpAddresses']
        if 'externalAccessIpAddress' in kwargs:
            external_access_ip_address = kwargs['externalAccessIpAddress']
        if 'serviceStatus' in kwargs:
            service_status = kwargs['serviceStatus']

        _setter("subnet_id", subnet_id)
        if domain_controller_ip_addresses is not None:
            _setter("domain_controller_ip_addresses", domain_controller_ip_addresses)
        if external_access_ip_address is not None:
            _setter("external_access_ip_address", external_access_ip_address)
        if id is not None:
            _setter("id", id)
        if location is not None:
            _setter("location", location)
        if service_status is not None:
            _setter("service_status", service_status)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The ID of the subnet in which to place the initial replica set. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="domainControllerIpAddresses")
    def domain_controller_ip_addresses(self) -> Optional[Sequence[str]]:
        """
        A list of subnet IP addresses for the domain controllers in the initial replica set, typically two.
        """
        return pulumi.get(self, "domain_controller_ip_addresses")

    @property
    @pulumi.getter(name="externalAccessIpAddress")
    def external_access_ip_address(self) -> Optional[str]:
        """
        The publicly routable IP address for the domain controllers in the initial replica set.
        """
        return pulumi.get(self, "external_access_ip_address")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        A unique ID for the replica set.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The Azure location where the Domain Service exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="serviceStatus")
    def service_status(self) -> Optional[str]:
        """
        The current service status for the initial replica set.
        """
        return pulumi.get(self, "service_status")


@pulumi.output_type
class ServiceNotifications(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "additionalRecipients":
            suggest = "additional_recipients"
        elif key == "notifyDcAdmins":
            suggest = "notify_dc_admins"
        elif key == "notifyGlobalAdmins":
            suggest = "notify_global_admins"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceNotifications. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceNotifications.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceNotifications.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 additional_recipients: Optional[Sequence[str]] = None,
                 notify_dc_admins: Optional[bool] = None,
                 notify_global_admins: Optional[bool] = None):
        """
        :param Sequence[str] additional_recipients: A list of additional email addresses to notify when there are alerts in the managed domain.
        :param bool notify_dc_admins: Whether to notify members of the _AAD DC Administrators_ group when there are alerts in the managed domain.
        :param bool notify_global_admins: Whether to notify all Global Administrators when there are alerts in the managed domain.
        """
        ServiceNotifications._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            additional_recipients=additional_recipients,
            notify_dc_admins=notify_dc_admins,
            notify_global_admins=notify_global_admins,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             additional_recipients: Optional[Sequence[str]] = None,
             notify_dc_admins: Optional[bool] = None,
             notify_global_admins: Optional[bool] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'additionalRecipients' in kwargs:
            additional_recipients = kwargs['additionalRecipients']
        if 'notifyDcAdmins' in kwargs:
            notify_dc_admins = kwargs['notifyDcAdmins']
        if 'notifyGlobalAdmins' in kwargs:
            notify_global_admins = kwargs['notifyGlobalAdmins']

        if additional_recipients is not None:
            _setter("additional_recipients", additional_recipients)
        if notify_dc_admins is not None:
            _setter("notify_dc_admins", notify_dc_admins)
        if notify_global_admins is not None:
            _setter("notify_global_admins", notify_global_admins)

    @property
    @pulumi.getter(name="additionalRecipients")
    def additional_recipients(self) -> Optional[Sequence[str]]:
        """
        A list of additional email addresses to notify when there are alerts in the managed domain.
        """
        return pulumi.get(self, "additional_recipients")

    @property
    @pulumi.getter(name="notifyDcAdmins")
    def notify_dc_admins(self) -> Optional[bool]:
        """
        Whether to notify members of the _AAD DC Administrators_ group when there are alerts in the managed domain.
        """
        return pulumi.get(self, "notify_dc_admins")

    @property
    @pulumi.getter(name="notifyGlobalAdmins")
    def notify_global_admins(self) -> Optional[bool]:
        """
        Whether to notify all Global Administrators when there are alerts in the managed domain.
        """
        return pulumi.get(self, "notify_global_admins")


@pulumi.output_type
class ServiceSecureLdap(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "pfxCertificate":
            suggest = "pfx_certificate"
        elif key == "pfxCertificatePassword":
            suggest = "pfx_certificate_password"
        elif key == "certificateExpiry":
            suggest = "certificate_expiry"
        elif key == "certificateThumbprint":
            suggest = "certificate_thumbprint"
        elif key == "externalAccessEnabled":
            suggest = "external_access_enabled"
        elif key == "publicCertificate":
            suggest = "public_certificate"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceSecureLdap. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceSecureLdap.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceSecureLdap.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: bool,
                 pfx_certificate: str,
                 pfx_certificate_password: str,
                 certificate_expiry: Optional[str] = None,
                 certificate_thumbprint: Optional[str] = None,
                 external_access_enabled: Optional[bool] = None,
                 public_certificate: Optional[str] = None):
        """
        :param bool enabled: Whether to enable secure LDAP for the managed domain. For more information, please see [official documentation on enabling LDAPS](https://docs.microsoft.com/azure/active-directory-domain-services/tutorial-configure-ldaps), paying particular attention to the section on network security to avoid unnecessarily exposing your service to Internet-borne bruteforce attacks.
        :param str pfx_certificate: The certificate/private key to use for LDAPS, as a base64-encoded TripleDES-SHA1 encrypted PKCS#12 bundle (PFX file).
        :param str pfx_certificate_password: The password to use for decrypting the PKCS#12 bundle (PFX file).
        :param str certificate_expiry: The expiry time of the certificate.
        :param str certificate_thumbprint: The thumbprint of the certificate.
        :param bool external_access_enabled: Whether to enable external access to LDAPS over the Internet. Defaults to `false`.
        :param str public_certificate: The public certificate.
        """
        ServiceSecureLdap._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            enabled=enabled,
            pfx_certificate=pfx_certificate,
            pfx_certificate_password=pfx_certificate_password,
            certificate_expiry=certificate_expiry,
            certificate_thumbprint=certificate_thumbprint,
            external_access_enabled=external_access_enabled,
            public_certificate=public_certificate,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             enabled: bool,
             pfx_certificate: str,
             pfx_certificate_password: str,
             certificate_expiry: Optional[str] = None,
             certificate_thumbprint: Optional[str] = None,
             external_access_enabled: Optional[bool] = None,
             public_certificate: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'pfxCertificate' in kwargs:
            pfx_certificate = kwargs['pfxCertificate']
        if 'pfxCertificatePassword' in kwargs:
            pfx_certificate_password = kwargs['pfxCertificatePassword']
        if 'certificateExpiry' in kwargs:
            certificate_expiry = kwargs['certificateExpiry']
        if 'certificateThumbprint' in kwargs:
            certificate_thumbprint = kwargs['certificateThumbprint']
        if 'externalAccessEnabled' in kwargs:
            external_access_enabled = kwargs['externalAccessEnabled']
        if 'publicCertificate' in kwargs:
            public_certificate = kwargs['publicCertificate']

        _setter("enabled", enabled)
        _setter("pfx_certificate", pfx_certificate)
        _setter("pfx_certificate_password", pfx_certificate_password)
        if certificate_expiry is not None:
            _setter("certificate_expiry", certificate_expiry)
        if certificate_thumbprint is not None:
            _setter("certificate_thumbprint", certificate_thumbprint)
        if external_access_enabled is not None:
            _setter("external_access_enabled", external_access_enabled)
        if public_certificate is not None:
            _setter("public_certificate", public_certificate)

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Whether to enable secure LDAP for the managed domain. For more information, please see [official documentation on enabling LDAPS](https://docs.microsoft.com/azure/active-directory-domain-services/tutorial-configure-ldaps), paying particular attention to the section on network security to avoid unnecessarily exposing your service to Internet-borne bruteforce attacks.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="pfxCertificate")
    def pfx_certificate(self) -> str:
        """
        The certificate/private key to use for LDAPS, as a base64-encoded TripleDES-SHA1 encrypted PKCS#12 bundle (PFX file).
        """
        return pulumi.get(self, "pfx_certificate")

    @property
    @pulumi.getter(name="pfxCertificatePassword")
    def pfx_certificate_password(self) -> str:
        """
        The password to use for decrypting the PKCS#12 bundle (PFX file).
        """
        return pulumi.get(self, "pfx_certificate_password")

    @property
    @pulumi.getter(name="certificateExpiry")
    def certificate_expiry(self) -> Optional[str]:
        """
        The expiry time of the certificate.
        """
        return pulumi.get(self, "certificate_expiry")

    @property
    @pulumi.getter(name="certificateThumbprint")
    def certificate_thumbprint(self) -> Optional[str]:
        """
        The thumbprint of the certificate.
        """
        return pulumi.get(self, "certificate_thumbprint")

    @property
    @pulumi.getter(name="externalAccessEnabled")
    def external_access_enabled(self) -> Optional[bool]:
        """
        Whether to enable external access to LDAPS over the Internet. Defaults to `false`.
        """
        return pulumi.get(self, "external_access_enabled")

    @property
    @pulumi.getter(name="publicCertificate")
    def public_certificate(self) -> Optional[str]:
        """
        The public certificate.
        """
        return pulumi.get(self, "public_certificate")


@pulumi.output_type
class ServiceSecurity(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "kerberosArmoringEnabled":
            suggest = "kerberos_armoring_enabled"
        elif key == "kerberosRc4EncryptionEnabled":
            suggest = "kerberos_rc4_encryption_enabled"
        elif key == "ntlmV1Enabled":
            suggest = "ntlm_v1_enabled"
        elif key == "syncKerberosPasswords":
            suggest = "sync_kerberos_passwords"
        elif key == "syncNtlmPasswords":
            suggest = "sync_ntlm_passwords"
        elif key == "syncOnPremPasswords":
            suggest = "sync_on_prem_passwords"
        elif key == "tlsV1Enabled":
            suggest = "tls_v1_enabled"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceSecurity. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceSecurity.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceSecurity.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 kerberos_armoring_enabled: Optional[bool] = None,
                 kerberos_rc4_encryption_enabled: Optional[bool] = None,
                 ntlm_v1_enabled: Optional[bool] = None,
                 sync_kerberos_passwords: Optional[bool] = None,
                 sync_ntlm_passwords: Optional[bool] = None,
                 sync_on_prem_passwords: Optional[bool] = None,
                 tls_v1_enabled: Optional[bool] = None):
        """
        :param bool kerberos_armoring_enabled: Whether to enable Kerberos Armoring. Defaults to `false`.
        :param bool kerberos_rc4_encryption_enabled: Whether to enable Kerberos RC4 Encryption. Defaults to `false`.
        :param bool ntlm_v1_enabled: Whether to enable legacy NTLM v1 support. Defaults to `false`.
        :param bool sync_kerberos_passwords: Whether to synchronize Kerberos password hashes to the managed domain. Defaults to `false`.
        :param bool sync_ntlm_passwords: Whether to synchronize NTLM password hashes to the managed domain. Defaults to `false`.
        :param bool sync_on_prem_passwords: Whether to synchronize on-premises password hashes to the managed domain. Defaults to `false`.
        :param bool tls_v1_enabled: Whether to enable legacy TLS v1 support. Defaults to `false`.
        """
        ServiceSecurity._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            kerberos_armoring_enabled=kerberos_armoring_enabled,
            kerberos_rc4_encryption_enabled=kerberos_rc4_encryption_enabled,
            ntlm_v1_enabled=ntlm_v1_enabled,
            sync_kerberos_passwords=sync_kerberos_passwords,
            sync_ntlm_passwords=sync_ntlm_passwords,
            sync_on_prem_passwords=sync_on_prem_passwords,
            tls_v1_enabled=tls_v1_enabled,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             kerberos_armoring_enabled: Optional[bool] = None,
             kerberos_rc4_encryption_enabled: Optional[bool] = None,
             ntlm_v1_enabled: Optional[bool] = None,
             sync_kerberos_passwords: Optional[bool] = None,
             sync_ntlm_passwords: Optional[bool] = None,
             sync_on_prem_passwords: Optional[bool] = None,
             tls_v1_enabled: Optional[bool] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'kerberosArmoringEnabled' in kwargs:
            kerberos_armoring_enabled = kwargs['kerberosArmoringEnabled']
        if 'kerberosRc4EncryptionEnabled' in kwargs:
            kerberos_rc4_encryption_enabled = kwargs['kerberosRc4EncryptionEnabled']
        if 'ntlmV1Enabled' in kwargs:
            ntlm_v1_enabled = kwargs['ntlmV1Enabled']
        if 'syncKerberosPasswords' in kwargs:
            sync_kerberos_passwords = kwargs['syncKerberosPasswords']
        if 'syncNtlmPasswords' in kwargs:
            sync_ntlm_passwords = kwargs['syncNtlmPasswords']
        if 'syncOnPremPasswords' in kwargs:
            sync_on_prem_passwords = kwargs['syncOnPremPasswords']
        if 'tlsV1Enabled' in kwargs:
            tls_v1_enabled = kwargs['tlsV1Enabled']

        if kerberos_armoring_enabled is not None:
            _setter("kerberos_armoring_enabled", kerberos_armoring_enabled)
        if kerberos_rc4_encryption_enabled is not None:
            _setter("kerberos_rc4_encryption_enabled", kerberos_rc4_encryption_enabled)
        if ntlm_v1_enabled is not None:
            _setter("ntlm_v1_enabled", ntlm_v1_enabled)
        if sync_kerberos_passwords is not None:
            _setter("sync_kerberos_passwords", sync_kerberos_passwords)
        if sync_ntlm_passwords is not None:
            _setter("sync_ntlm_passwords", sync_ntlm_passwords)
        if sync_on_prem_passwords is not None:
            _setter("sync_on_prem_passwords", sync_on_prem_passwords)
        if tls_v1_enabled is not None:
            _setter("tls_v1_enabled", tls_v1_enabled)

    @property
    @pulumi.getter(name="kerberosArmoringEnabled")
    def kerberos_armoring_enabled(self) -> Optional[bool]:
        """
        Whether to enable Kerberos Armoring. Defaults to `false`.
        """
        return pulumi.get(self, "kerberos_armoring_enabled")

    @property
    @pulumi.getter(name="kerberosRc4EncryptionEnabled")
    def kerberos_rc4_encryption_enabled(self) -> Optional[bool]:
        """
        Whether to enable Kerberos RC4 Encryption. Defaults to `false`.
        """
        return pulumi.get(self, "kerberos_rc4_encryption_enabled")

    @property
    @pulumi.getter(name="ntlmV1Enabled")
    def ntlm_v1_enabled(self) -> Optional[bool]:
        """
        Whether to enable legacy NTLM v1 support. Defaults to `false`.
        """
        return pulumi.get(self, "ntlm_v1_enabled")

    @property
    @pulumi.getter(name="syncKerberosPasswords")
    def sync_kerberos_passwords(self) -> Optional[bool]:
        """
        Whether to synchronize Kerberos password hashes to the managed domain. Defaults to `false`.
        """
        return pulumi.get(self, "sync_kerberos_passwords")

    @property
    @pulumi.getter(name="syncNtlmPasswords")
    def sync_ntlm_passwords(self) -> Optional[bool]:
        """
        Whether to synchronize NTLM password hashes to the managed domain. Defaults to `false`.
        """
        return pulumi.get(self, "sync_ntlm_passwords")

    @property
    @pulumi.getter(name="syncOnPremPasswords")
    def sync_on_prem_passwords(self) -> Optional[bool]:
        """
        Whether to synchronize on-premises password hashes to the managed domain. Defaults to `false`.
        """
        return pulumi.get(self, "sync_on_prem_passwords")

    @property
    @pulumi.getter(name="tlsV1Enabled")
    def tls_v1_enabled(self) -> Optional[bool]:
        """
        Whether to enable legacy TLS v1 support. Defaults to `false`.
        """
        return pulumi.get(self, "tls_v1_enabled")


@pulumi.output_type
class GetServiceNotificationResult(dict):
    def __init__(__self__, *,
                 additional_recipients: Sequence[str],
                 notify_dc_admins: bool,
                 notify_global_admins: bool):
        """
        :param Sequence[str] additional_recipients: A list of additional email addresses to notify when there are alerts in the managed domain.
        :param bool notify_dc_admins: Whethermembers of the _AAD DC Administrators_ group are notified when there are alerts in the managed domain.
        :param bool notify_global_admins: Whether all Global Administrators are notified when there are alerts in the managed domain.
        """
        GetServiceNotificationResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            additional_recipients=additional_recipients,
            notify_dc_admins=notify_dc_admins,
            notify_global_admins=notify_global_admins,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             additional_recipients: Sequence[str],
             notify_dc_admins: bool,
             notify_global_admins: bool,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'additionalRecipients' in kwargs:
            additional_recipients = kwargs['additionalRecipients']
        if 'notifyDcAdmins' in kwargs:
            notify_dc_admins = kwargs['notifyDcAdmins']
        if 'notifyGlobalAdmins' in kwargs:
            notify_global_admins = kwargs['notifyGlobalAdmins']

        _setter("additional_recipients", additional_recipients)
        _setter("notify_dc_admins", notify_dc_admins)
        _setter("notify_global_admins", notify_global_admins)

    @property
    @pulumi.getter(name="additionalRecipients")
    def additional_recipients(self) -> Sequence[str]:
        """
        A list of additional email addresses to notify when there are alerts in the managed domain.
        """
        return pulumi.get(self, "additional_recipients")

    @property
    @pulumi.getter(name="notifyDcAdmins")
    def notify_dc_admins(self) -> bool:
        """
        Whethermembers of the _AAD DC Administrators_ group are notified when there are alerts in the managed domain.
        """
        return pulumi.get(self, "notify_dc_admins")

    @property
    @pulumi.getter(name="notifyGlobalAdmins")
    def notify_global_admins(self) -> bool:
        """
        Whether all Global Administrators are notified when there are alerts in the managed domain.
        """
        return pulumi.get(self, "notify_global_admins")


@pulumi.output_type
class GetServiceReplicaSetResult(dict):
    def __init__(__self__, *,
                 domain_controller_ip_addresses: Sequence[str],
                 external_access_ip_address: str,
                 id: str,
                 location: str,
                 service_status: str,
                 subnet_id: str):
        """
        :param Sequence[str] domain_controller_ip_addresses: A list of subnet IP addresses for the domain controllers in the replica set, typically two.
        :param str external_access_ip_address: The publicly routable IP address for the domain controllers in the replica set.
        :param str id: The ID of the Domain Service.
        :param str location: The Azure location in which the replica set resides.
        :param str service_status: The current service status for the replica set.
        :param str subnet_id: The ID of the subnet in which the replica set resides.
        """
        GetServiceReplicaSetResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            domain_controller_ip_addresses=domain_controller_ip_addresses,
            external_access_ip_address=external_access_ip_address,
            id=id,
            location=location,
            service_status=service_status,
            subnet_id=subnet_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             domain_controller_ip_addresses: Sequence[str],
             external_access_ip_address: str,
             id: str,
             location: str,
             service_status: str,
             subnet_id: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'domainControllerIpAddresses' in kwargs:
            domain_controller_ip_addresses = kwargs['domainControllerIpAddresses']
        if 'externalAccessIpAddress' in kwargs:
            external_access_ip_address = kwargs['externalAccessIpAddress']
        if 'serviceStatus' in kwargs:
            service_status = kwargs['serviceStatus']
        if 'subnetId' in kwargs:
            subnet_id = kwargs['subnetId']

        _setter("domain_controller_ip_addresses", domain_controller_ip_addresses)
        _setter("external_access_ip_address", external_access_ip_address)
        _setter("id", id)
        _setter("location", location)
        _setter("service_status", service_status)
        _setter("subnet_id", subnet_id)

    @property
    @pulumi.getter(name="domainControllerIpAddresses")
    def domain_controller_ip_addresses(self) -> Sequence[str]:
        """
        A list of subnet IP addresses for the domain controllers in the replica set, typically two.
        """
        return pulumi.get(self, "domain_controller_ip_addresses")

    @property
    @pulumi.getter(name="externalAccessIpAddress")
    def external_access_ip_address(self) -> str:
        """
        The publicly routable IP address for the domain controllers in the replica set.
        """
        return pulumi.get(self, "external_access_ip_address")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Domain Service.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The Azure location in which the replica set resides.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="serviceStatus")
    def service_status(self) -> str:
        """
        The current service status for the replica set.
        """
        return pulumi.get(self, "service_status")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The ID of the subnet in which the replica set resides.
        """
        return pulumi.get(self, "subnet_id")


@pulumi.output_type
class GetServiceSecureLdapResult(dict):
    def __init__(__self__, *,
                 certificate_expiry: str,
                 certificate_thumbprint: str,
                 enabled: bool,
                 external_access_enabled: bool,
                 public_certificate: str):
        """
        :param bool enabled: Whether secure LDAP is enabled for the managed domain.
        :param bool external_access_enabled: Whether external access to LDAPS over the Internet, is enabled.
        """
        GetServiceSecureLdapResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            certificate_expiry=certificate_expiry,
            certificate_thumbprint=certificate_thumbprint,
            enabled=enabled,
            external_access_enabled=external_access_enabled,
            public_certificate=public_certificate,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             certificate_expiry: str,
             certificate_thumbprint: str,
             enabled: bool,
             external_access_enabled: bool,
             public_certificate: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'certificateExpiry' in kwargs:
            certificate_expiry = kwargs['certificateExpiry']
        if 'certificateThumbprint' in kwargs:
            certificate_thumbprint = kwargs['certificateThumbprint']
        if 'externalAccessEnabled' in kwargs:
            external_access_enabled = kwargs['externalAccessEnabled']
        if 'publicCertificate' in kwargs:
            public_certificate = kwargs['publicCertificate']

        _setter("certificate_expiry", certificate_expiry)
        _setter("certificate_thumbprint", certificate_thumbprint)
        _setter("enabled", enabled)
        _setter("external_access_enabled", external_access_enabled)
        _setter("public_certificate", public_certificate)

    @property
    @pulumi.getter(name="certificateExpiry")
    def certificate_expiry(self) -> str:
        return pulumi.get(self, "certificate_expiry")

    @property
    @pulumi.getter(name="certificateThumbprint")
    def certificate_thumbprint(self) -> str:
        return pulumi.get(self, "certificate_thumbprint")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Whether secure LDAP is enabled for the managed domain.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="externalAccessEnabled")
    def external_access_enabled(self) -> bool:
        """
        Whether external access to LDAPS over the Internet, is enabled.
        """
        return pulumi.get(self, "external_access_enabled")

    @property
    @pulumi.getter(name="publicCertificate")
    def public_certificate(self) -> str:
        return pulumi.get(self, "public_certificate")


@pulumi.output_type
class GetServiceSecurityResult(dict):
    def __init__(__self__, *,
                 kerberos_armoring_enabled: bool,
                 kerberos_rc4_encryption_enabled: bool,
                 ntlm_v1_enabled: bool,
                 sync_kerberos_passwords: bool,
                 sync_ntlm_passwords: bool,
                 sync_on_prem_passwords: bool,
                 tls_v1_enabled: bool):
        """
        :param bool kerberos_armoring_enabled: (Optional) Whether the Kerberos Armoring is enabled.
        :param bool kerberos_rc4_encryption_enabled: (Optional) Whether the Kerberos RC4 Encryption is enabled.
        :param bool ntlm_v1_enabled: Whether legacy NTLM v1 support is enabled.
        :param bool sync_kerberos_passwords: Whether Kerberos password hashes are synchronized to the managed domain.
        :param bool sync_ntlm_passwords: Whether NTLM password hashes are synchronized to the managed domain.
        :param bool sync_on_prem_passwords: Whether on-premises password hashes are synchronized to the managed domain.
        :param bool tls_v1_enabled: Whether legacy TLS v1 support is enabled.
        """
        GetServiceSecurityResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            kerberos_armoring_enabled=kerberos_armoring_enabled,
            kerberos_rc4_encryption_enabled=kerberos_rc4_encryption_enabled,
            ntlm_v1_enabled=ntlm_v1_enabled,
            sync_kerberos_passwords=sync_kerberos_passwords,
            sync_ntlm_passwords=sync_ntlm_passwords,
            sync_on_prem_passwords=sync_on_prem_passwords,
            tls_v1_enabled=tls_v1_enabled,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             kerberos_armoring_enabled: bool,
             kerberos_rc4_encryption_enabled: bool,
             ntlm_v1_enabled: bool,
             sync_kerberos_passwords: bool,
             sync_ntlm_passwords: bool,
             sync_on_prem_passwords: bool,
             tls_v1_enabled: bool,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'kerberosArmoringEnabled' in kwargs:
            kerberos_armoring_enabled = kwargs['kerberosArmoringEnabled']
        if 'kerberosRc4EncryptionEnabled' in kwargs:
            kerberos_rc4_encryption_enabled = kwargs['kerberosRc4EncryptionEnabled']
        if 'ntlmV1Enabled' in kwargs:
            ntlm_v1_enabled = kwargs['ntlmV1Enabled']
        if 'syncKerberosPasswords' in kwargs:
            sync_kerberos_passwords = kwargs['syncKerberosPasswords']
        if 'syncNtlmPasswords' in kwargs:
            sync_ntlm_passwords = kwargs['syncNtlmPasswords']
        if 'syncOnPremPasswords' in kwargs:
            sync_on_prem_passwords = kwargs['syncOnPremPasswords']
        if 'tlsV1Enabled' in kwargs:
            tls_v1_enabled = kwargs['tlsV1Enabled']

        _setter("kerberos_armoring_enabled", kerberos_armoring_enabled)
        _setter("kerberos_rc4_encryption_enabled", kerberos_rc4_encryption_enabled)
        _setter("ntlm_v1_enabled", ntlm_v1_enabled)
        _setter("sync_kerberos_passwords", sync_kerberos_passwords)
        _setter("sync_ntlm_passwords", sync_ntlm_passwords)
        _setter("sync_on_prem_passwords", sync_on_prem_passwords)
        _setter("tls_v1_enabled", tls_v1_enabled)

    @property
    @pulumi.getter(name="kerberosArmoringEnabled")
    def kerberos_armoring_enabled(self) -> bool:
        """
        (Optional) Whether the Kerberos Armoring is enabled.
        """
        return pulumi.get(self, "kerberos_armoring_enabled")

    @property
    @pulumi.getter(name="kerberosRc4EncryptionEnabled")
    def kerberos_rc4_encryption_enabled(self) -> bool:
        """
        (Optional) Whether the Kerberos RC4 Encryption is enabled.
        """
        return pulumi.get(self, "kerberos_rc4_encryption_enabled")

    @property
    @pulumi.getter(name="ntlmV1Enabled")
    def ntlm_v1_enabled(self) -> bool:
        """
        Whether legacy NTLM v1 support is enabled.
        """
        return pulumi.get(self, "ntlm_v1_enabled")

    @property
    @pulumi.getter(name="syncKerberosPasswords")
    def sync_kerberos_passwords(self) -> bool:
        """
        Whether Kerberos password hashes are synchronized to the managed domain.
        """
        return pulumi.get(self, "sync_kerberos_passwords")

    @property
    @pulumi.getter(name="syncNtlmPasswords")
    def sync_ntlm_passwords(self) -> bool:
        """
        Whether NTLM password hashes are synchronized to the managed domain.
        """
        return pulumi.get(self, "sync_ntlm_passwords")

    @property
    @pulumi.getter(name="syncOnPremPasswords")
    def sync_on_prem_passwords(self) -> bool:
        """
        Whether on-premises password hashes are synchronized to the managed domain.
        """
        return pulumi.get(self, "sync_on_prem_passwords")

    @property
    @pulumi.getter(name="tlsV1Enabled")
    def tls_v1_enabled(self) -> bool:
        """
        Whether legacy TLS v1 support is enabled.
        """
        return pulumi.get(self, "tls_v1_enabled")



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
    'GetAgentResult',
    'GetAgentExtensionsAllowListResult',
    'GetAgentExtensionsBlockListResult',
    'GetCloudMetadataResult',
    'GetIdentityResult',
    'GetLocationDataResult',
    'GetOsProfileResult',
    'GetOsProfileLinuxResult',
    'GetOsProfileLinuxPatchResult',
    'GetOsProfileWindowResult',
    'GetOsProfileWindowPatchResult',
    'GetServiceStatusResult',
    'GetServiceStatusExtensionServiceResult',
    'GetServiceStatusGuestConfigurationServiceResult',
]

@pulumi.output_type
class GetAgentResult(dict):
    def __init__(__self__, *,
                 extensions_allow_lists: Sequence['outputs.GetAgentExtensionsAllowListResult'],
                 extensions_block_lists: Sequence['outputs.GetAgentExtensionsBlockListResult'],
                 extensions_enabled: bool,
                 guest_configuration_enabled: bool,
                 incoming_connections_ports: Sequence[str],
                 proxy_bypasses: Sequence[str],
                 proxy_url: str):
        """
        :param Sequence['GetAgentExtensionsAllowListArgs'] extensions_allow_lists: A `extensions_allow_list` block as defined below.
        :param Sequence['GetAgentExtensionsBlockListArgs'] extensions_block_lists: A `extensions_block_list` block as defined below.
        :param bool extensions_enabled: Specifies whether the extension service is enabled or disabled.
        :param bool guest_configuration_enabled: Specified whether the guest configuration service is enabled or disabled.
        :param Sequence[str] incoming_connections_ports: Specifies the list of ports that the agent will be able to listen on.
        :param Sequence[str] proxy_bypasses: List of service names which should not use the specified proxy server.
        :param str proxy_url: Specifies the URL of the proxy to be used.
        """
        GetAgentResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            extensions_allow_lists=extensions_allow_lists,
            extensions_block_lists=extensions_block_lists,
            extensions_enabled=extensions_enabled,
            guest_configuration_enabled=guest_configuration_enabled,
            incoming_connections_ports=incoming_connections_ports,
            proxy_bypasses=proxy_bypasses,
            proxy_url=proxy_url,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             extensions_allow_lists: Sequence['outputs.GetAgentExtensionsAllowListResult'],
             extensions_block_lists: Sequence['outputs.GetAgentExtensionsBlockListResult'],
             extensions_enabled: bool,
             guest_configuration_enabled: bool,
             incoming_connections_ports: Sequence[str],
             proxy_bypasses: Sequence[str],
             proxy_url: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'extensionsAllowLists' in kwargs:
            extensions_allow_lists = kwargs['extensionsAllowLists']
        if 'extensionsBlockLists' in kwargs:
            extensions_block_lists = kwargs['extensionsBlockLists']
        if 'extensionsEnabled' in kwargs:
            extensions_enabled = kwargs['extensionsEnabled']
        if 'guestConfigurationEnabled' in kwargs:
            guest_configuration_enabled = kwargs['guestConfigurationEnabled']
        if 'incomingConnectionsPorts' in kwargs:
            incoming_connections_ports = kwargs['incomingConnectionsPorts']
        if 'proxyBypasses' in kwargs:
            proxy_bypasses = kwargs['proxyBypasses']
        if 'proxyUrl' in kwargs:
            proxy_url = kwargs['proxyUrl']

        _setter("extensions_allow_lists", extensions_allow_lists)
        _setter("extensions_block_lists", extensions_block_lists)
        _setter("extensions_enabled", extensions_enabled)
        _setter("guest_configuration_enabled", guest_configuration_enabled)
        _setter("incoming_connections_ports", incoming_connections_ports)
        _setter("proxy_bypasses", proxy_bypasses)
        _setter("proxy_url", proxy_url)

    @property
    @pulumi.getter(name="extensionsAllowLists")
    def extensions_allow_lists(self) -> Sequence['outputs.GetAgentExtensionsAllowListResult']:
        """
        A `extensions_allow_list` block as defined below.
        """
        return pulumi.get(self, "extensions_allow_lists")

    @property
    @pulumi.getter(name="extensionsBlockLists")
    def extensions_block_lists(self) -> Sequence['outputs.GetAgentExtensionsBlockListResult']:
        """
        A `extensions_block_list` block as defined below.
        """
        return pulumi.get(self, "extensions_block_lists")

    @property
    @pulumi.getter(name="extensionsEnabled")
    def extensions_enabled(self) -> bool:
        """
        Specifies whether the extension service is enabled or disabled.
        """
        return pulumi.get(self, "extensions_enabled")

    @property
    @pulumi.getter(name="guestConfigurationEnabled")
    def guest_configuration_enabled(self) -> bool:
        """
        Specified whether the guest configuration service is enabled or disabled.
        """
        return pulumi.get(self, "guest_configuration_enabled")

    @property
    @pulumi.getter(name="incomingConnectionsPorts")
    def incoming_connections_ports(self) -> Sequence[str]:
        """
        Specifies the list of ports that the agent will be able to listen on.
        """
        return pulumi.get(self, "incoming_connections_ports")

    @property
    @pulumi.getter(name="proxyBypasses")
    def proxy_bypasses(self) -> Sequence[str]:
        """
        List of service names which should not use the specified proxy server.
        """
        return pulumi.get(self, "proxy_bypasses")

    @property
    @pulumi.getter(name="proxyUrl")
    def proxy_url(self) -> str:
        """
        Specifies the URL of the proxy to be used.
        """
        return pulumi.get(self, "proxy_url")


@pulumi.output_type
class GetAgentExtensionsAllowListResult(dict):
    def __init__(__self__, *,
                 publisher: str,
                 type: str):
        """
        :param str publisher: Publisher of the extension.
        :param str type: The identity type.
        """
        GetAgentExtensionsAllowListResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            publisher=publisher,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             publisher: str,
             type: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        _setter("publisher", publisher)
        _setter("type", type)

    @property
    @pulumi.getter
    def publisher(self) -> str:
        """
        Publisher of the extension.
        """
        return pulumi.get(self, "publisher")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The identity type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetAgentExtensionsBlockListResult(dict):
    def __init__(__self__, *,
                 publisher: str,
                 type: str):
        """
        :param str publisher: Publisher of the extension.
        :param str type: The identity type.
        """
        GetAgentExtensionsBlockListResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            publisher=publisher,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             publisher: str,
             type: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        _setter("publisher", publisher)
        _setter("type", type)

    @property
    @pulumi.getter
    def publisher(self) -> str:
        """
        Publisher of the extension.
        """
        return pulumi.get(self, "publisher")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The identity type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetCloudMetadataResult(dict):
    def __init__(__self__, *,
                 provider: str):
        """
        :param str provider: Specifies the cloud provider. For example `Azure`, `AWS` and `GCP`.
        """
        GetCloudMetadataResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            provider=provider,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             provider: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        _setter("provider", provider)

    @property
    @pulumi.getter
    def provider(self) -> str:
        """
        Specifies the cloud provider. For example `Azure`, `AWS` and `GCP`.
        """
        return pulumi.get(self, "provider")


@pulumi.output_type
class GetIdentityResult(dict):
    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: str):
        """
        :param str principal_id: The principal ID of resource identity.
        :param str tenant_id: The tenant ID of resource.
        :param str type: The identity type.
        """
        GetIdentityResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            principal_id=principal_id,
            tenant_id=tenant_id,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             principal_id: str,
             tenant_id: str,
             type: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'principalId' in kwargs:
            principal_id = kwargs['principalId']
        if 'tenantId' in kwargs:
            tenant_id = kwargs['tenantId']

        _setter("principal_id", principal_id)
        _setter("tenant_id", tenant_id)
        _setter("type", type)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal ID of resource identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of resource.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The identity type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetLocationDataResult(dict):
    def __init__(__self__, *,
                 city: str,
                 country_or_region: str,
                 district: str,
                 name: str):
        """
        :param str city: The city or locality where the resource is located.
        :param str country_or_region: The country or region where the resource is located.
        :param str district: The district, state, or province where the resource is located.
        :param str name: The name of this Azure Arc machine.
        """
        GetLocationDataResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            city=city,
            country_or_region=country_or_region,
            district=district,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             city: str,
             country_or_region: str,
             district: str,
             name: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'countryOrRegion' in kwargs:
            country_or_region = kwargs['countryOrRegion']

        _setter("city", city)
        _setter("country_or_region", country_or_region)
        _setter("district", district)
        _setter("name", name)

    @property
    @pulumi.getter
    def city(self) -> str:
        """
        The city or locality where the resource is located.
        """
        return pulumi.get(self, "city")

    @property
    @pulumi.getter(name="countryOrRegion")
    def country_or_region(self) -> str:
        """
        The country or region where the resource is located.
        """
        return pulumi.get(self, "country_or_region")

    @property
    @pulumi.getter
    def district(self) -> str:
        """
        The district, state, or province where the resource is located.
        """
        return pulumi.get(self, "district")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of this Azure Arc machine.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetOsProfileResult(dict):
    def __init__(__self__, *,
                 computer_name: str,
                 linuxes: Sequence['outputs.GetOsProfileLinuxResult'],
                 windows: Sequence['outputs.GetOsProfileWindowResult']):
        """
        :param str computer_name: Specifies the host OS name of the Azure Arc machine.
        :param Sequence['GetOsProfileLinuxArgs'] linuxes: A `linux` block as defined above.
        :param Sequence['GetOsProfileWindowArgs'] windows: A `windows` block as defined below.
        """
        GetOsProfileResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            computer_name=computer_name,
            linuxes=linuxes,
            windows=windows,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             computer_name: str,
             linuxes: Sequence['outputs.GetOsProfileLinuxResult'],
             windows: Sequence['outputs.GetOsProfileWindowResult'],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'computerName' in kwargs:
            computer_name = kwargs['computerName']

        _setter("computer_name", computer_name)
        _setter("linuxes", linuxes)
        _setter("windows", windows)

    @property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> str:
        """
        Specifies the host OS name of the Azure Arc machine.
        """
        return pulumi.get(self, "computer_name")

    @property
    @pulumi.getter
    def linuxes(self) -> Sequence['outputs.GetOsProfileLinuxResult']:
        """
        A `linux` block as defined above.
        """
        return pulumi.get(self, "linuxes")

    @property
    @pulumi.getter
    def windows(self) -> Sequence['outputs.GetOsProfileWindowResult']:
        """
        A `windows` block as defined below.
        """
        return pulumi.get(self, "windows")


@pulumi.output_type
class GetOsProfileLinuxResult(dict):
    def __init__(__self__, *,
                 patches: Sequence['outputs.GetOsProfileLinuxPatchResult']):
        """
        :param Sequence['GetOsProfileLinuxPatchArgs'] patches: A `patch` block as defined above.
        """
        GetOsProfileLinuxResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            patches=patches,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             patches: Sequence['outputs.GetOsProfileLinuxPatchResult'],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        _setter("patches", patches)

    @property
    @pulumi.getter
    def patches(self) -> Sequence['outputs.GetOsProfileLinuxPatchResult']:
        """
        A `patch` block as defined above.
        """
        return pulumi.get(self, "patches")


@pulumi.output_type
class GetOsProfileLinuxPatchResult(dict):
    def __init__(__self__, *,
                 assessment_mode: str,
                 patch_mode: str):
        """
        :param str assessment_mode: Specifies the assessment mode.
        :param str patch_mode: Specifies the patch mode.
        """
        GetOsProfileLinuxPatchResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            assessment_mode=assessment_mode,
            patch_mode=patch_mode,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             assessment_mode: str,
             patch_mode: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'assessmentMode' in kwargs:
            assessment_mode = kwargs['assessmentMode']
        if 'patchMode' in kwargs:
            patch_mode = kwargs['patchMode']

        _setter("assessment_mode", assessment_mode)
        _setter("patch_mode", patch_mode)

    @property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(self) -> str:
        """
        Specifies the assessment mode.
        """
        return pulumi.get(self, "assessment_mode")

    @property
    @pulumi.getter(name="patchMode")
    def patch_mode(self) -> str:
        """
        Specifies the patch mode.
        """
        return pulumi.get(self, "patch_mode")


@pulumi.output_type
class GetOsProfileWindowResult(dict):
    def __init__(__self__, *,
                 patches: Sequence['outputs.GetOsProfileWindowPatchResult']):
        """
        :param Sequence['GetOsProfileWindowPatchArgs'] patches: A `patch` block as defined above.
        """
        GetOsProfileWindowResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            patches=patches,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             patches: Sequence['outputs.GetOsProfileWindowPatchResult'],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        _setter("patches", patches)

    @property
    @pulumi.getter
    def patches(self) -> Sequence['outputs.GetOsProfileWindowPatchResult']:
        """
        A `patch` block as defined above.
        """
        return pulumi.get(self, "patches")


@pulumi.output_type
class GetOsProfileWindowPatchResult(dict):
    def __init__(__self__, *,
                 assessment_mode: str,
                 patch_mode: str):
        """
        :param str assessment_mode: Specifies the assessment mode.
        :param str patch_mode: Specifies the patch mode.
        """
        GetOsProfileWindowPatchResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            assessment_mode=assessment_mode,
            patch_mode=patch_mode,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             assessment_mode: str,
             patch_mode: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'assessmentMode' in kwargs:
            assessment_mode = kwargs['assessmentMode']
        if 'patchMode' in kwargs:
            patch_mode = kwargs['patchMode']

        _setter("assessment_mode", assessment_mode)
        _setter("patch_mode", patch_mode)

    @property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(self) -> str:
        """
        Specifies the assessment mode.
        """
        return pulumi.get(self, "assessment_mode")

    @property
    @pulumi.getter(name="patchMode")
    def patch_mode(self) -> str:
        """
        Specifies the patch mode.
        """
        return pulumi.get(self, "patch_mode")


@pulumi.output_type
class GetServiceStatusResult(dict):
    def __init__(__self__, *,
                 extension_services: Sequence['outputs.GetServiceStatusExtensionServiceResult'],
                 guest_configuration_services: Sequence['outputs.GetServiceStatusGuestConfigurationServiceResult']):
        """
        :param Sequence['GetServiceStatusExtensionServiceArgs'] extension_services: A `extension_service` block as defined above.
        :param Sequence['GetServiceStatusGuestConfigurationServiceArgs'] guest_configuration_services: A `guest_configuration_service` block as defined above.
        """
        GetServiceStatusResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            extension_services=extension_services,
            guest_configuration_services=guest_configuration_services,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             extension_services: Sequence['outputs.GetServiceStatusExtensionServiceResult'],
             guest_configuration_services: Sequence['outputs.GetServiceStatusGuestConfigurationServiceResult'],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'extensionServices' in kwargs:
            extension_services = kwargs['extensionServices']
        if 'guestConfigurationServices' in kwargs:
            guest_configuration_services = kwargs['guestConfigurationServices']

        _setter("extension_services", extension_services)
        _setter("guest_configuration_services", guest_configuration_services)

    @property
    @pulumi.getter(name="extensionServices")
    def extension_services(self) -> Sequence['outputs.GetServiceStatusExtensionServiceResult']:
        """
        A `extension_service` block as defined above.
        """
        return pulumi.get(self, "extension_services")

    @property
    @pulumi.getter(name="guestConfigurationServices")
    def guest_configuration_services(self) -> Sequence['outputs.GetServiceStatusGuestConfigurationServiceResult']:
        """
        A `guest_configuration_service` block as defined above.
        """
        return pulumi.get(self, "guest_configuration_services")


@pulumi.output_type
class GetServiceStatusExtensionServiceResult(dict):
    def __init__(__self__, *,
                 startup_type: str,
                 status: str):
        """
        :param str startup_type: The behavior of the service when the Arc-enabled machine starts up.
        :param str status: The current status of the service.
        """
        GetServiceStatusExtensionServiceResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            startup_type=startup_type,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             startup_type: str,
             status: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'startupType' in kwargs:
            startup_type = kwargs['startupType']

        _setter("startup_type", startup_type)
        _setter("status", status)

    @property
    @pulumi.getter(name="startupType")
    def startup_type(self) -> str:
        """
        The behavior of the service when the Arc-enabled machine starts up.
        """
        return pulumi.get(self, "startup_type")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The current status of the service.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetServiceStatusGuestConfigurationServiceResult(dict):
    def __init__(__self__, *,
                 startup_type: str,
                 status: str):
        """
        :param str startup_type: The behavior of the service when the Arc-enabled machine starts up.
        :param str status: The current status of the service.
        """
        GetServiceStatusGuestConfigurationServiceResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            startup_type=startup_type,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             startup_type: str,
             status: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'startupType' in kwargs:
            startup_type = kwargs['startupType']

        _setter("startup_type", startup_type)
        _setter("status", status)

    @property
    @pulumi.getter(name="startupType")
    def startup_type(self) -> str:
        """
        The behavior of the service when the Arc-enabled machine starts up.
        """
        return pulumi.get(self, "startup_type")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The current status of the service.
        """
        return pulumi.get(self, "status")



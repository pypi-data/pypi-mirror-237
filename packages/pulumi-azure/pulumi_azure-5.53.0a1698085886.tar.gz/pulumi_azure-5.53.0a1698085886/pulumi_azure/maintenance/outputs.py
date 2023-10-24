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
    'ConfigurationInstallPatches',
    'ConfigurationInstallPatchesLinux',
    'ConfigurationInstallPatchesWindow',
    'ConfigurationWindow',
    'GetConfigurationInstallPatchResult',
    'GetConfigurationInstallPatchLinuxResult',
    'GetConfigurationInstallPatchWindowResult',
    'GetConfigurationWindowResult',
    'GetPublicConfigurationsConfigResult',
]

@pulumi.output_type
class ConfigurationInstallPatches(dict):
    def __init__(__self__, *,
                 linuxes: Optional[Sequence['outputs.ConfigurationInstallPatchesLinux']] = None,
                 reboot: Optional[str] = None,
                 windows: Optional[Sequence['outputs.ConfigurationInstallPatchesWindow']] = None):
        """
        :param Sequence['ConfigurationInstallPatchesLinuxArgs'] linuxes: A `linux` block as defined above. This property only applies when `scope` is set to `InGuestPatch`
        :param str reboot: Possible reboot preference as defined by the user based on which it would be decided to reboot the machine or not after the patch operation is completed. Possible values are `Always`, `IfRequired` and `Never`. This property only applies when `scope` is set to `InGuestPatch`.
        :param Sequence['ConfigurationInstallPatchesWindowArgs'] windows: A `windows` block as defined above. This property only applies when `scope` is set to `InGuestPatch`
        """
        ConfigurationInstallPatches._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            linuxes=linuxes,
            reboot=reboot,
            windows=windows,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             linuxes: Optional[Sequence['outputs.ConfigurationInstallPatchesLinux']] = None,
             reboot: Optional[str] = None,
             windows: Optional[Sequence['outputs.ConfigurationInstallPatchesWindow']] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        if linuxes is not None:
            _setter("linuxes", linuxes)
        if reboot is not None:
            _setter("reboot", reboot)
        if windows is not None:
            _setter("windows", windows)

    @property
    @pulumi.getter
    def linuxes(self) -> Optional[Sequence['outputs.ConfigurationInstallPatchesLinux']]:
        """
        A `linux` block as defined above. This property only applies when `scope` is set to `InGuestPatch`
        """
        return pulumi.get(self, "linuxes")

    @property
    @pulumi.getter
    def reboot(self) -> Optional[str]:
        """
        Possible reboot preference as defined by the user based on which it would be decided to reboot the machine or not after the patch operation is completed. Possible values are `Always`, `IfRequired` and `Never`. This property only applies when `scope` is set to `InGuestPatch`.
        """
        return pulumi.get(self, "reboot")

    @property
    @pulumi.getter
    def windows(self) -> Optional[Sequence['outputs.ConfigurationInstallPatchesWindow']]:
        """
        A `windows` block as defined above. This property only applies when `scope` is set to `InGuestPatch`
        """
        return pulumi.get(self, "windows")


@pulumi.output_type
class ConfigurationInstallPatchesLinux(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "classificationsToIncludes":
            suggest = "classifications_to_includes"
        elif key == "packageNamesMaskToExcludes":
            suggest = "package_names_mask_to_excludes"
        elif key == "packageNamesMaskToIncludes":
            suggest = "package_names_mask_to_includes"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationInstallPatchesLinux. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationInstallPatchesLinux.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationInstallPatchesLinux.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 classifications_to_includes: Optional[Sequence[str]] = None,
                 package_names_mask_to_excludes: Optional[Sequence[str]] = None,
                 package_names_mask_to_includes: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] classifications_to_includes: List of Classification category of patches to be patched. Possible values are `Critical`, `Security` and `Other`.
        :param Sequence[str] package_names_mask_to_excludes: List of package names to be excluded from patching.
        :param Sequence[str] package_names_mask_to_includes: List of package names to be included for patching.
        """
        ConfigurationInstallPatchesLinux._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            classifications_to_includes=classifications_to_includes,
            package_names_mask_to_excludes=package_names_mask_to_excludes,
            package_names_mask_to_includes=package_names_mask_to_includes,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             classifications_to_includes: Optional[Sequence[str]] = None,
             package_names_mask_to_excludes: Optional[Sequence[str]] = None,
             package_names_mask_to_includes: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'classificationsToIncludes' in kwargs:
            classifications_to_includes = kwargs['classificationsToIncludes']
        if 'packageNamesMaskToExcludes' in kwargs:
            package_names_mask_to_excludes = kwargs['packageNamesMaskToExcludes']
        if 'packageNamesMaskToIncludes' in kwargs:
            package_names_mask_to_includes = kwargs['packageNamesMaskToIncludes']

        if classifications_to_includes is not None:
            _setter("classifications_to_includes", classifications_to_includes)
        if package_names_mask_to_excludes is not None:
            _setter("package_names_mask_to_excludes", package_names_mask_to_excludes)
        if package_names_mask_to_includes is not None:
            _setter("package_names_mask_to_includes", package_names_mask_to_includes)

    @property
    @pulumi.getter(name="classificationsToIncludes")
    def classifications_to_includes(self) -> Optional[Sequence[str]]:
        """
        List of Classification category of patches to be patched. Possible values are `Critical`, `Security` and `Other`.
        """
        return pulumi.get(self, "classifications_to_includes")

    @property
    @pulumi.getter(name="packageNamesMaskToExcludes")
    def package_names_mask_to_excludes(self) -> Optional[Sequence[str]]:
        """
        List of package names to be excluded from patching.
        """
        return pulumi.get(self, "package_names_mask_to_excludes")

    @property
    @pulumi.getter(name="packageNamesMaskToIncludes")
    def package_names_mask_to_includes(self) -> Optional[Sequence[str]]:
        """
        List of package names to be included for patching.
        """
        return pulumi.get(self, "package_names_mask_to_includes")


@pulumi.output_type
class ConfigurationInstallPatchesWindow(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "classificationsToIncludes":
            suggest = "classifications_to_includes"
        elif key == "kbNumbersToExcludes":
            suggest = "kb_numbers_to_excludes"
        elif key == "kbNumbersToIncludes":
            suggest = "kb_numbers_to_includes"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationInstallPatchesWindow. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationInstallPatchesWindow.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationInstallPatchesWindow.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 classifications_to_includes: Optional[Sequence[str]] = None,
                 kb_numbers_to_excludes: Optional[Sequence[str]] = None,
                 kb_numbers_to_includes: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] classifications_to_includes: List of Classification category of patches to be patched. Possible values are `Critical`, `Security`, `UpdateRollup`, `FeaturePack`, `ServicePack`, `Definition`, `Tools` and `Updates`.
        :param Sequence[str] kb_numbers_to_excludes: List of KB numbers to be excluded from patching.
        :param Sequence[str] kb_numbers_to_includes: List of KB numbers to be included for patching.
        """
        ConfigurationInstallPatchesWindow._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            classifications_to_includes=classifications_to_includes,
            kb_numbers_to_excludes=kb_numbers_to_excludes,
            kb_numbers_to_includes=kb_numbers_to_includes,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             classifications_to_includes: Optional[Sequence[str]] = None,
             kb_numbers_to_excludes: Optional[Sequence[str]] = None,
             kb_numbers_to_includes: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'classificationsToIncludes' in kwargs:
            classifications_to_includes = kwargs['classificationsToIncludes']
        if 'kbNumbersToExcludes' in kwargs:
            kb_numbers_to_excludes = kwargs['kbNumbersToExcludes']
        if 'kbNumbersToIncludes' in kwargs:
            kb_numbers_to_includes = kwargs['kbNumbersToIncludes']

        if classifications_to_includes is not None:
            _setter("classifications_to_includes", classifications_to_includes)
        if kb_numbers_to_excludes is not None:
            _setter("kb_numbers_to_excludes", kb_numbers_to_excludes)
        if kb_numbers_to_includes is not None:
            _setter("kb_numbers_to_includes", kb_numbers_to_includes)

    @property
    @pulumi.getter(name="classificationsToIncludes")
    def classifications_to_includes(self) -> Optional[Sequence[str]]:
        """
        List of Classification category of patches to be patched. Possible values are `Critical`, `Security`, `UpdateRollup`, `FeaturePack`, `ServicePack`, `Definition`, `Tools` and `Updates`.
        """
        return pulumi.get(self, "classifications_to_includes")

    @property
    @pulumi.getter(name="kbNumbersToExcludes")
    def kb_numbers_to_excludes(self) -> Optional[Sequence[str]]:
        """
        List of KB numbers to be excluded from patching.
        """
        return pulumi.get(self, "kb_numbers_to_excludes")

    @property
    @pulumi.getter(name="kbNumbersToIncludes")
    def kb_numbers_to_includes(self) -> Optional[Sequence[str]]:
        """
        List of KB numbers to be included for patching.
        """
        return pulumi.get(self, "kb_numbers_to_includes")


@pulumi.output_type
class ConfigurationWindow(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "startDateTime":
            suggest = "start_date_time"
        elif key == "timeZone":
            suggest = "time_zone"
        elif key == "expirationDateTime":
            suggest = "expiration_date_time"
        elif key == "recurEvery":
            suggest = "recur_every"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationWindow. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationWindow.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationWindow.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 start_date_time: str,
                 time_zone: str,
                 duration: Optional[str] = None,
                 expiration_date_time: Optional[str] = None,
                 recur_every: Optional[str] = None):
        """
        :param str start_date_time: Effective start date of the maintenance window in YYYY-MM-DD hh:mm format.
        :param str time_zone: The time zone for the maintenance window. A list of timezones can be obtained by executing [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell.
        :param str duration: The duration of the maintenance window in HH:mm format.
        :param str expiration_date_time: Effective expiration date of the maintenance window in YYYY-MM-DD hh:mm format.
        :param str recur_every: The rate at which a maintenance window is expected to recur. The rate can be expressed as daily, weekly, or monthly schedules.
        """
        ConfigurationWindow._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            start_date_time=start_date_time,
            time_zone=time_zone,
            duration=duration,
            expiration_date_time=expiration_date_time,
            recur_every=recur_every,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             start_date_time: str,
             time_zone: str,
             duration: Optional[str] = None,
             expiration_date_time: Optional[str] = None,
             recur_every: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'startDateTime' in kwargs:
            start_date_time = kwargs['startDateTime']
        if 'timeZone' in kwargs:
            time_zone = kwargs['timeZone']
        if 'expirationDateTime' in kwargs:
            expiration_date_time = kwargs['expirationDateTime']
        if 'recurEvery' in kwargs:
            recur_every = kwargs['recurEvery']

        _setter("start_date_time", start_date_time)
        _setter("time_zone", time_zone)
        if duration is not None:
            _setter("duration", duration)
        if expiration_date_time is not None:
            _setter("expiration_date_time", expiration_date_time)
        if recur_every is not None:
            _setter("recur_every", recur_every)

    @property
    @pulumi.getter(name="startDateTime")
    def start_date_time(self) -> str:
        """
        Effective start date of the maintenance window in YYYY-MM-DD hh:mm format.
        """
        return pulumi.get(self, "start_date_time")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> str:
        """
        The time zone for the maintenance window. A list of timezones can be obtained by executing [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell.
        """
        return pulumi.get(self, "time_zone")

    @property
    @pulumi.getter
    def duration(self) -> Optional[str]:
        """
        The duration of the maintenance window in HH:mm format.
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter(name="expirationDateTime")
    def expiration_date_time(self) -> Optional[str]:
        """
        Effective expiration date of the maintenance window in YYYY-MM-DD hh:mm format.
        """
        return pulumi.get(self, "expiration_date_time")

    @property
    @pulumi.getter(name="recurEvery")
    def recur_every(self) -> Optional[str]:
        """
        The rate at which a maintenance window is expected to recur. The rate can be expressed as daily, weekly, or monthly schedules.
        """
        return pulumi.get(self, "recur_every")


@pulumi.output_type
class GetConfigurationInstallPatchResult(dict):
    def __init__(__self__, *,
                 linuxes: Sequence['outputs.GetConfigurationInstallPatchLinuxResult'],
                 reboot: str,
                 windows: Sequence['outputs.GetConfigurationInstallPatchWindowResult']):
        """
        :param Sequence['GetConfigurationInstallPatchLinuxArgs'] linuxes: A `linux` block as defined below.
        :param str reboot: Possible reboot preference as defined by the user based on which it would be decided to reboot the machine or not after the patch operation is completed.
        :param Sequence['GetConfigurationInstallPatchWindowArgs'] windows: A `windows` block as defined below.
        """
        GetConfigurationInstallPatchResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            linuxes=linuxes,
            reboot=reboot,
            windows=windows,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             linuxes: Sequence['outputs.GetConfigurationInstallPatchLinuxResult'],
             reboot: str,
             windows: Sequence['outputs.GetConfigurationInstallPatchWindowResult'],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        _setter("linuxes", linuxes)
        _setter("reboot", reboot)
        _setter("windows", windows)

    @property
    @pulumi.getter
    def linuxes(self) -> Sequence['outputs.GetConfigurationInstallPatchLinuxResult']:
        """
        A `linux` block as defined below.
        """
        return pulumi.get(self, "linuxes")

    @property
    @pulumi.getter
    def reboot(self) -> str:
        """
        Possible reboot preference as defined by the user based on which it would be decided to reboot the machine or not after the patch operation is completed.
        """
        return pulumi.get(self, "reboot")

    @property
    @pulumi.getter
    def windows(self) -> Sequence['outputs.GetConfigurationInstallPatchWindowResult']:
        """
        A `windows` block as defined below.
        """
        return pulumi.get(self, "windows")


@pulumi.output_type
class GetConfigurationInstallPatchLinuxResult(dict):
    def __init__(__self__, *,
                 classifications_to_includes: Sequence[str],
                 package_names_mask_to_excludes: Sequence[str],
                 package_names_mask_to_includes: Sequence[str]):
        """
        :param Sequence[str] classifications_to_includes: List of Classification category of patches to be patched.
        :param Sequence[str] package_names_mask_to_excludes: List of package names to be excluded from patching.
        :param Sequence[str] package_names_mask_to_includes: List of package names to be included for patching.
        """
        GetConfigurationInstallPatchLinuxResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            classifications_to_includes=classifications_to_includes,
            package_names_mask_to_excludes=package_names_mask_to_excludes,
            package_names_mask_to_includes=package_names_mask_to_includes,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             classifications_to_includes: Sequence[str],
             package_names_mask_to_excludes: Sequence[str],
             package_names_mask_to_includes: Sequence[str],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'classificationsToIncludes' in kwargs:
            classifications_to_includes = kwargs['classificationsToIncludes']
        if 'packageNamesMaskToExcludes' in kwargs:
            package_names_mask_to_excludes = kwargs['packageNamesMaskToExcludes']
        if 'packageNamesMaskToIncludes' in kwargs:
            package_names_mask_to_includes = kwargs['packageNamesMaskToIncludes']

        _setter("classifications_to_includes", classifications_to_includes)
        _setter("package_names_mask_to_excludes", package_names_mask_to_excludes)
        _setter("package_names_mask_to_includes", package_names_mask_to_includes)

    @property
    @pulumi.getter(name="classificationsToIncludes")
    def classifications_to_includes(self) -> Sequence[str]:
        """
        List of Classification category of patches to be patched.
        """
        return pulumi.get(self, "classifications_to_includes")

    @property
    @pulumi.getter(name="packageNamesMaskToExcludes")
    def package_names_mask_to_excludes(self) -> Sequence[str]:
        """
        List of package names to be excluded from patching.
        """
        return pulumi.get(self, "package_names_mask_to_excludes")

    @property
    @pulumi.getter(name="packageNamesMaskToIncludes")
    def package_names_mask_to_includes(self) -> Sequence[str]:
        """
        List of package names to be included for patching.
        """
        return pulumi.get(self, "package_names_mask_to_includes")


@pulumi.output_type
class GetConfigurationInstallPatchWindowResult(dict):
    def __init__(__self__, *,
                 classifications_to_includes: Sequence[str],
                 kb_numbers_to_excludes: Sequence[str],
                 kb_numbers_to_includes: Sequence[str]):
        """
        :param Sequence[str] classifications_to_includes: List of Classification category of patches to be patched.
        :param Sequence[str] kb_numbers_to_excludes: List of KB numbers to be excluded from patching.
        :param Sequence[str] kb_numbers_to_includes: List of KB numbers to be included for patching.
        """
        GetConfigurationInstallPatchWindowResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            classifications_to_includes=classifications_to_includes,
            kb_numbers_to_excludes=kb_numbers_to_excludes,
            kb_numbers_to_includes=kb_numbers_to_includes,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             classifications_to_includes: Sequence[str],
             kb_numbers_to_excludes: Sequence[str],
             kb_numbers_to_includes: Sequence[str],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'classificationsToIncludes' in kwargs:
            classifications_to_includes = kwargs['classificationsToIncludes']
        if 'kbNumbersToExcludes' in kwargs:
            kb_numbers_to_excludes = kwargs['kbNumbersToExcludes']
        if 'kbNumbersToIncludes' in kwargs:
            kb_numbers_to_includes = kwargs['kbNumbersToIncludes']

        _setter("classifications_to_includes", classifications_to_includes)
        _setter("kb_numbers_to_excludes", kb_numbers_to_excludes)
        _setter("kb_numbers_to_includes", kb_numbers_to_includes)

    @property
    @pulumi.getter(name="classificationsToIncludes")
    def classifications_to_includes(self) -> Sequence[str]:
        """
        List of Classification category of patches to be patched.
        """
        return pulumi.get(self, "classifications_to_includes")

    @property
    @pulumi.getter(name="kbNumbersToExcludes")
    def kb_numbers_to_excludes(self) -> Sequence[str]:
        """
        List of KB numbers to be excluded from patching.
        """
        return pulumi.get(self, "kb_numbers_to_excludes")

    @property
    @pulumi.getter(name="kbNumbersToIncludes")
    def kb_numbers_to_includes(self) -> Sequence[str]:
        """
        List of KB numbers to be included for patching.
        """
        return pulumi.get(self, "kb_numbers_to_includes")


@pulumi.output_type
class GetConfigurationWindowResult(dict):
    def __init__(__self__, *,
                 duration: str,
                 expiration_date_time: str,
                 recur_every: str,
                 start_date_time: str,
                 time_zone: str):
        """
        :param str duration: The duration of the maintenance window.
        :param str expiration_date_time: Effective expiration date of the maintenance window.
        :param str recur_every: The rate at which a maintenance window is expected to recur.
        :param str start_date_time: Effective start date of the maintenance window.
        :param str time_zone: The time zone for the maintenance window.
        """
        GetConfigurationWindowResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            duration=duration,
            expiration_date_time=expiration_date_time,
            recur_every=recur_every,
            start_date_time=start_date_time,
            time_zone=time_zone,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             duration: str,
             expiration_date_time: str,
             recur_every: str,
             start_date_time: str,
             time_zone: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'expirationDateTime' in kwargs:
            expiration_date_time = kwargs['expirationDateTime']
        if 'recurEvery' in kwargs:
            recur_every = kwargs['recurEvery']
        if 'startDateTime' in kwargs:
            start_date_time = kwargs['startDateTime']
        if 'timeZone' in kwargs:
            time_zone = kwargs['timeZone']

        _setter("duration", duration)
        _setter("expiration_date_time", expiration_date_time)
        _setter("recur_every", recur_every)
        _setter("start_date_time", start_date_time)
        _setter("time_zone", time_zone)

    @property
    @pulumi.getter
    def duration(self) -> str:
        """
        The duration of the maintenance window.
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter(name="expirationDateTime")
    def expiration_date_time(self) -> str:
        """
        Effective expiration date of the maintenance window.
        """
        return pulumi.get(self, "expiration_date_time")

    @property
    @pulumi.getter(name="recurEvery")
    def recur_every(self) -> str:
        """
        The rate at which a maintenance window is expected to recur.
        """
        return pulumi.get(self, "recur_every")

    @property
    @pulumi.getter(name="startDateTime")
    def start_date_time(self) -> str:
        """
        Effective start date of the maintenance window.
        """
        return pulumi.get(self, "start_date_time")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> str:
        """
        The time zone for the maintenance window.
        """
        return pulumi.get(self, "time_zone")


@pulumi.output_type
class GetPublicConfigurationsConfigResult(dict):
    def __init__(__self__, *,
                 description: str,
                 duration: str,
                 id: str,
                 location: str,
                 maintenance_scope: str,
                 name: str,
                 recur_every: str,
                 time_zone: str):
        """
        :param str description: A description of the Public Maintenance Configuration.
        :param str duration: The duration of the Public Maintenance Configuration window.
        :param str id: The id of the Public Maintenance Configuration.
        :param str location: The Azure location to filter the list of Public Maintenance Configurations against.
        :param str maintenance_scope: The scope of the Public Maintenance Configuration.
        :param str name: The name of the Public Maintenance Configuration.
        :param str recur_every: The recurring window to filter the list of Public Maintenance Configurations against. Possible values are `Monday-Thursday` and `Friday-Sunday`
        :param str time_zone: The time zone for the maintenance window.
        """
        GetPublicConfigurationsConfigResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            duration=duration,
            id=id,
            location=location,
            maintenance_scope=maintenance_scope,
            name=name,
            recur_every=recur_every,
            time_zone=time_zone,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: str,
             duration: str,
             id: str,
             location: str,
             maintenance_scope: str,
             name: str,
             recur_every: str,
             time_zone: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'maintenanceScope' in kwargs:
            maintenance_scope = kwargs['maintenanceScope']
        if 'recurEvery' in kwargs:
            recur_every = kwargs['recurEvery']
        if 'timeZone' in kwargs:
            time_zone = kwargs['timeZone']

        _setter("description", description)
        _setter("duration", duration)
        _setter("id", id)
        _setter("location", location)
        _setter("maintenance_scope", maintenance_scope)
        _setter("name", name)
        _setter("recur_every", recur_every)
        _setter("time_zone", time_zone)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A description of the Public Maintenance Configuration.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def duration(self) -> str:
        """
        The duration of the Public Maintenance Configuration window.
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the Public Maintenance Configuration.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The Azure location to filter the list of Public Maintenance Configurations against.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maintenanceScope")
    def maintenance_scope(self) -> str:
        """
        The scope of the Public Maintenance Configuration.
        """
        return pulumi.get(self, "maintenance_scope")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Public Maintenance Configuration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recurEvery")
    def recur_every(self) -> str:
        """
        The recurring window to filter the list of Public Maintenance Configurations against. Possible values are `Monday-Thursday` and `Friday-Sunday`
        """
        return pulumi.get(self, "recur_every")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> str:
        """
        The time zone for the maintenance window.
        """
        return pulumi.get(self, "time_zone")



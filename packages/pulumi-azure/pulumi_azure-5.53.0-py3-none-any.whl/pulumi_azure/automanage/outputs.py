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
    'ConfigurationAntimalware',
    'ConfigurationAntimalwareExclusions',
    'ConfigurationAzureSecurityBaseline',
    'ConfigurationBackup',
    'ConfigurationBackupRetentionPolicy',
    'ConfigurationBackupRetentionPolicyDailySchedule',
    'ConfigurationBackupRetentionPolicyDailyScheduleRetentionDuration',
    'ConfigurationBackupRetentionPolicyWeeklySchedule',
    'ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDuration',
    'ConfigurationBackupSchedulePolicy',
]

@pulumi.output_type
class ConfigurationAntimalware(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "realTimeProtectionEnabled":
            suggest = "real_time_protection_enabled"
        elif key == "scheduledScanDay":
            suggest = "scheduled_scan_day"
        elif key == "scheduledScanEnabled":
            suggest = "scheduled_scan_enabled"
        elif key == "scheduledScanTimeInMinutes":
            suggest = "scheduled_scan_time_in_minutes"
        elif key == "scheduledScanType":
            suggest = "scheduled_scan_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationAntimalware. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationAntimalware.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationAntimalware.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 exclusions: Optional['outputs.ConfigurationAntimalwareExclusions'] = None,
                 real_time_protection_enabled: Optional[bool] = None,
                 scheduled_scan_day: Optional[int] = None,
                 scheduled_scan_enabled: Optional[bool] = None,
                 scheduled_scan_time_in_minutes: Optional[int] = None,
                 scheduled_scan_type: Optional[str] = None):
        """
        :param 'ConfigurationAntimalwareExclusionsArgs' exclusions: A `exclusions` block as defined below.
        :param bool real_time_protection_enabled: Whether the real time protection is enabled. Defaults to `false`.
        :param int scheduled_scan_day: The day of the scheduled scan. Possible values are `0` to `8` where `0` is daily, `1` to `7` are the days of the week and `8` is Disabled. Defaults to `8`.
        :param bool scheduled_scan_enabled: Whether the scheduled scan is enabled. Defaults to `false`.
        :param int scheduled_scan_time_in_minutes: The time of the scheduled scan in minutes. Possible values are `0` to `1439` where `0` is 12:00 AM and `1439` is 11:59 PM.
        :param str scheduled_scan_type: The type of the scheduled scan. Possible values are `Quick` and `Full`. Defaults to `Quick`.
        """
        ConfigurationAntimalware._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            exclusions=exclusions,
            real_time_protection_enabled=real_time_protection_enabled,
            scheduled_scan_day=scheduled_scan_day,
            scheduled_scan_enabled=scheduled_scan_enabled,
            scheduled_scan_time_in_minutes=scheduled_scan_time_in_minutes,
            scheduled_scan_type=scheduled_scan_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             exclusions: Optional['outputs.ConfigurationAntimalwareExclusions'] = None,
             real_time_protection_enabled: Optional[bool] = None,
             scheduled_scan_day: Optional[int] = None,
             scheduled_scan_enabled: Optional[bool] = None,
             scheduled_scan_time_in_minutes: Optional[int] = None,
             scheduled_scan_type: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'realTimeProtectionEnabled' in kwargs:
            real_time_protection_enabled = kwargs['realTimeProtectionEnabled']
        if 'scheduledScanDay' in kwargs:
            scheduled_scan_day = kwargs['scheduledScanDay']
        if 'scheduledScanEnabled' in kwargs:
            scheduled_scan_enabled = kwargs['scheduledScanEnabled']
        if 'scheduledScanTimeInMinutes' in kwargs:
            scheduled_scan_time_in_minutes = kwargs['scheduledScanTimeInMinutes']
        if 'scheduledScanType' in kwargs:
            scheduled_scan_type = kwargs['scheduledScanType']

        if exclusions is not None:
            _setter("exclusions", exclusions)
        if real_time_protection_enabled is not None:
            _setter("real_time_protection_enabled", real_time_protection_enabled)
        if scheduled_scan_day is not None:
            _setter("scheduled_scan_day", scheduled_scan_day)
        if scheduled_scan_enabled is not None:
            _setter("scheduled_scan_enabled", scheduled_scan_enabled)
        if scheduled_scan_time_in_minutes is not None:
            _setter("scheduled_scan_time_in_minutes", scheduled_scan_time_in_minutes)
        if scheduled_scan_type is not None:
            _setter("scheduled_scan_type", scheduled_scan_type)

    @property
    @pulumi.getter
    def exclusions(self) -> Optional['outputs.ConfigurationAntimalwareExclusions']:
        """
        A `exclusions` block as defined below.
        """
        return pulumi.get(self, "exclusions")

    @property
    @pulumi.getter(name="realTimeProtectionEnabled")
    def real_time_protection_enabled(self) -> Optional[bool]:
        """
        Whether the real time protection is enabled. Defaults to `false`.
        """
        return pulumi.get(self, "real_time_protection_enabled")

    @property
    @pulumi.getter(name="scheduledScanDay")
    def scheduled_scan_day(self) -> Optional[int]:
        """
        The day of the scheduled scan. Possible values are `0` to `8` where `0` is daily, `1` to `7` are the days of the week and `8` is Disabled. Defaults to `8`.
        """
        return pulumi.get(self, "scheduled_scan_day")

    @property
    @pulumi.getter(name="scheduledScanEnabled")
    def scheduled_scan_enabled(self) -> Optional[bool]:
        """
        Whether the scheduled scan is enabled. Defaults to `false`.
        """
        return pulumi.get(self, "scheduled_scan_enabled")

    @property
    @pulumi.getter(name="scheduledScanTimeInMinutes")
    def scheduled_scan_time_in_minutes(self) -> Optional[int]:
        """
        The time of the scheduled scan in minutes. Possible values are `0` to `1439` where `0` is 12:00 AM and `1439` is 11:59 PM.
        """
        return pulumi.get(self, "scheduled_scan_time_in_minutes")

    @property
    @pulumi.getter(name="scheduledScanType")
    def scheduled_scan_type(self) -> Optional[str]:
        """
        The type of the scheduled scan. Possible values are `Quick` and `Full`. Defaults to `Quick`.
        """
        return pulumi.get(self, "scheduled_scan_type")


@pulumi.output_type
class ConfigurationAntimalwareExclusions(dict):
    def __init__(__self__, *,
                 extensions: Optional[str] = None,
                 paths: Optional[str] = None,
                 processes: Optional[str] = None):
        """
        :param str extensions: The extensions to exclude from the antimalware scan, separated by `;`. For example `.ext1;.ext2`.
        :param str paths: The paths to exclude from the antimalware scan, separated by `;`. For example `C:\\\\Windows\\\\Temp;D:\\\\Temp`.
        :param str processes: The processes to exclude from the antimalware scan, separated by `;`. For example `svchost.exe;notepad.exe`.
        """
        ConfigurationAntimalwareExclusions._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            extensions=extensions,
            paths=paths,
            processes=processes,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             extensions: Optional[str] = None,
             paths: Optional[str] = None,
             processes: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        if extensions is not None:
            _setter("extensions", extensions)
        if paths is not None:
            _setter("paths", paths)
        if processes is not None:
            _setter("processes", processes)

    @property
    @pulumi.getter
    def extensions(self) -> Optional[str]:
        """
        The extensions to exclude from the antimalware scan, separated by `;`. For example `.ext1;.ext2`.
        """
        return pulumi.get(self, "extensions")

    @property
    @pulumi.getter
    def paths(self) -> Optional[str]:
        """
        The paths to exclude from the antimalware scan, separated by `;`. For example `C:\\\\Windows\\\\Temp;D:\\\\Temp`.
        """
        return pulumi.get(self, "paths")

    @property
    @pulumi.getter
    def processes(self) -> Optional[str]:
        """
        The processes to exclude from the antimalware scan, separated by `;`. For example `svchost.exe;notepad.exe`.
        """
        return pulumi.get(self, "processes")


@pulumi.output_type
class ConfigurationAzureSecurityBaseline(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "assignmentType":
            suggest = "assignment_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationAzureSecurityBaseline. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationAzureSecurityBaseline.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationAzureSecurityBaseline.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 assignment_type: Optional[str] = None):
        """
        :param str assignment_type: The assignment type of the azure security baseline. Possible values are `ApplyAndAutoCorrect`, `ApplyAndMonitor`, `Audit` and `DeployAndAutoCorrect`. Defaults to `ApplyAndAutoCorrect`.
        """
        ConfigurationAzureSecurityBaseline._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            assignment_type=assignment_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             assignment_type: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'assignmentType' in kwargs:
            assignment_type = kwargs['assignmentType']

        if assignment_type is not None:
            _setter("assignment_type", assignment_type)

    @property
    @pulumi.getter(name="assignmentType")
    def assignment_type(self) -> Optional[str]:
        """
        The assignment type of the azure security baseline. Possible values are `ApplyAndAutoCorrect`, `ApplyAndMonitor`, `Audit` and `DeployAndAutoCorrect`. Defaults to `ApplyAndAutoCorrect`.
        """
        return pulumi.get(self, "assignment_type")


@pulumi.output_type
class ConfigurationBackup(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "instantRpRetentionRangeInDays":
            suggest = "instant_rp_retention_range_in_days"
        elif key == "policyName":
            suggest = "policy_name"
        elif key == "retentionPolicy":
            suggest = "retention_policy"
        elif key == "schedulePolicy":
            suggest = "schedule_policy"
        elif key == "timeZone":
            suggest = "time_zone"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationBackup. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationBackup.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationBackup.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 instant_rp_retention_range_in_days: Optional[int] = None,
                 policy_name: Optional[str] = None,
                 retention_policy: Optional['outputs.ConfigurationBackupRetentionPolicy'] = None,
                 schedule_policy: Optional['outputs.ConfigurationBackupSchedulePolicy'] = None,
                 time_zone: Optional[str] = None):
        """
        :param int instant_rp_retention_range_in_days: The retention range in days of the backup policy. Defaults to `5`.
        :param str policy_name: The name of the backup policy.
        :param 'ConfigurationBackupRetentionPolicyArgs' retention_policy: A `retention_policy` block as defined below.
        :param 'ConfigurationBackupSchedulePolicyArgs' schedule_policy: A `schedule_policy` block as defined below.
        :param str time_zone: The timezone of the backup policy. Defaults to `UTC`.
        """
        ConfigurationBackup._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            instant_rp_retention_range_in_days=instant_rp_retention_range_in_days,
            policy_name=policy_name,
            retention_policy=retention_policy,
            schedule_policy=schedule_policy,
            time_zone=time_zone,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             instant_rp_retention_range_in_days: Optional[int] = None,
             policy_name: Optional[str] = None,
             retention_policy: Optional['outputs.ConfigurationBackupRetentionPolicy'] = None,
             schedule_policy: Optional['outputs.ConfigurationBackupSchedulePolicy'] = None,
             time_zone: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'instantRpRetentionRangeInDays' in kwargs:
            instant_rp_retention_range_in_days = kwargs['instantRpRetentionRangeInDays']
        if 'policyName' in kwargs:
            policy_name = kwargs['policyName']
        if 'retentionPolicy' in kwargs:
            retention_policy = kwargs['retentionPolicy']
        if 'schedulePolicy' in kwargs:
            schedule_policy = kwargs['schedulePolicy']
        if 'timeZone' in kwargs:
            time_zone = kwargs['timeZone']

        if instant_rp_retention_range_in_days is not None:
            _setter("instant_rp_retention_range_in_days", instant_rp_retention_range_in_days)
        if policy_name is not None:
            _setter("policy_name", policy_name)
        if retention_policy is not None:
            _setter("retention_policy", retention_policy)
        if schedule_policy is not None:
            _setter("schedule_policy", schedule_policy)
        if time_zone is not None:
            _setter("time_zone", time_zone)

    @property
    @pulumi.getter(name="instantRpRetentionRangeInDays")
    def instant_rp_retention_range_in_days(self) -> Optional[int]:
        """
        The retention range in days of the backup policy. Defaults to `5`.
        """
        return pulumi.get(self, "instant_rp_retention_range_in_days")

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[str]:
        """
        The name of the backup policy.
        """
        return pulumi.get(self, "policy_name")

    @property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional['outputs.ConfigurationBackupRetentionPolicy']:
        """
        A `retention_policy` block as defined below.
        """
        return pulumi.get(self, "retention_policy")

    @property
    @pulumi.getter(name="schedulePolicy")
    def schedule_policy(self) -> Optional['outputs.ConfigurationBackupSchedulePolicy']:
        """
        A `schedule_policy` block as defined below.
        """
        return pulumi.get(self, "schedule_policy")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[str]:
        """
        The timezone of the backup policy. Defaults to `UTC`.
        """
        return pulumi.get(self, "time_zone")


@pulumi.output_type
class ConfigurationBackupRetentionPolicy(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dailySchedule":
            suggest = "daily_schedule"
        elif key == "retentionPolicyType":
            suggest = "retention_policy_type"
        elif key == "weeklySchedule":
            suggest = "weekly_schedule"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationBackupRetentionPolicy. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationBackupRetentionPolicy.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationBackupRetentionPolicy.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 daily_schedule: Optional['outputs.ConfigurationBackupRetentionPolicyDailySchedule'] = None,
                 retention_policy_type: Optional[str] = None,
                 weekly_schedule: Optional['outputs.ConfigurationBackupRetentionPolicyWeeklySchedule'] = None):
        """
        :param 'ConfigurationBackupRetentionPolicyDailyScheduleArgs' daily_schedule: A `daily_schedule` block as defined below.
        :param str retention_policy_type: The retention policy type of the backup policy. Possible value is `LongTermRetentionPolicy`.
        :param 'ConfigurationBackupRetentionPolicyWeeklyScheduleArgs' weekly_schedule: A `weekly_schedule` block as defined below.
        """
        ConfigurationBackupRetentionPolicy._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            daily_schedule=daily_schedule,
            retention_policy_type=retention_policy_type,
            weekly_schedule=weekly_schedule,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             daily_schedule: Optional['outputs.ConfigurationBackupRetentionPolicyDailySchedule'] = None,
             retention_policy_type: Optional[str] = None,
             weekly_schedule: Optional['outputs.ConfigurationBackupRetentionPolicyWeeklySchedule'] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'dailySchedule' in kwargs:
            daily_schedule = kwargs['dailySchedule']
        if 'retentionPolicyType' in kwargs:
            retention_policy_type = kwargs['retentionPolicyType']
        if 'weeklySchedule' in kwargs:
            weekly_schedule = kwargs['weeklySchedule']

        if daily_schedule is not None:
            _setter("daily_schedule", daily_schedule)
        if retention_policy_type is not None:
            _setter("retention_policy_type", retention_policy_type)
        if weekly_schedule is not None:
            _setter("weekly_schedule", weekly_schedule)

    @property
    @pulumi.getter(name="dailySchedule")
    def daily_schedule(self) -> Optional['outputs.ConfigurationBackupRetentionPolicyDailySchedule']:
        """
        A `daily_schedule` block as defined below.
        """
        return pulumi.get(self, "daily_schedule")

    @property
    @pulumi.getter(name="retentionPolicyType")
    def retention_policy_type(self) -> Optional[str]:
        """
        The retention policy type of the backup policy. Possible value is `LongTermRetentionPolicy`.
        """
        return pulumi.get(self, "retention_policy_type")

    @property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(self) -> Optional['outputs.ConfigurationBackupRetentionPolicyWeeklySchedule']:
        """
        A `weekly_schedule` block as defined below.
        """
        return pulumi.get(self, "weekly_schedule")


@pulumi.output_type
class ConfigurationBackupRetentionPolicyDailySchedule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "retentionDuration":
            suggest = "retention_duration"
        elif key == "retentionTimes":
            suggest = "retention_times"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationBackupRetentionPolicyDailySchedule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationBackupRetentionPolicyDailySchedule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationBackupRetentionPolicyDailySchedule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 retention_duration: Optional['outputs.ConfigurationBackupRetentionPolicyDailyScheduleRetentionDuration'] = None,
                 retention_times: Optional[Sequence[str]] = None):
        """
        :param 'ConfigurationBackupRetentionPolicyDailyScheduleRetentionDurationArgs' retention_duration: A `retention_duration` block as defined below.
        :param Sequence[str] retention_times: The retention times of the backup policy.
        """
        ConfigurationBackupRetentionPolicyDailySchedule._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            retention_duration=retention_duration,
            retention_times=retention_times,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             retention_duration: Optional['outputs.ConfigurationBackupRetentionPolicyDailyScheduleRetentionDuration'] = None,
             retention_times: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'retentionDuration' in kwargs:
            retention_duration = kwargs['retentionDuration']
        if 'retentionTimes' in kwargs:
            retention_times = kwargs['retentionTimes']

        if retention_duration is not None:
            _setter("retention_duration", retention_duration)
        if retention_times is not None:
            _setter("retention_times", retention_times)

    @property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional['outputs.ConfigurationBackupRetentionPolicyDailyScheduleRetentionDuration']:
        """
        A `retention_duration` block as defined below.
        """
        return pulumi.get(self, "retention_duration")

    @property
    @pulumi.getter(name="retentionTimes")
    def retention_times(self) -> Optional[Sequence[str]]:
        """
        The retention times of the backup policy.
        """
        return pulumi.get(self, "retention_times")


@pulumi.output_type
class ConfigurationBackupRetentionPolicyDailyScheduleRetentionDuration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "durationType":
            suggest = "duration_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationBackupRetentionPolicyDailyScheduleRetentionDuration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationBackupRetentionPolicyDailyScheduleRetentionDuration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationBackupRetentionPolicyDailyScheduleRetentionDuration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 count: Optional[int] = None,
                 duration_type: Optional[str] = None):
        """
        :param int count: The count of the retention duration of the backup policy. Valid value inside `daily_schedule` is `7` to `9999` and inside `weekly_schedule` is `1` to `5163`.
        :param str duration_type: The duration type of the retention duration of the backup policy. Valid value inside `daily_schedule` is `Days` and inside `weekly_schedule` is `Weeks`.
        """
        ConfigurationBackupRetentionPolicyDailyScheduleRetentionDuration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            count=count,
            duration_type=duration_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             count: Optional[int] = None,
             duration_type: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'durationType' in kwargs:
            duration_type = kwargs['durationType']

        if count is not None:
            _setter("count", count)
        if duration_type is not None:
            _setter("duration_type", duration_type)

    @property
    @pulumi.getter
    def count(self) -> Optional[int]:
        """
        The count of the retention duration of the backup policy. Valid value inside `daily_schedule` is `7` to `9999` and inside `weekly_schedule` is `1` to `5163`.
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter(name="durationType")
    def duration_type(self) -> Optional[str]:
        """
        The duration type of the retention duration of the backup policy. Valid value inside `daily_schedule` is `Days` and inside `weekly_schedule` is `Weeks`.
        """
        return pulumi.get(self, "duration_type")


@pulumi.output_type
class ConfigurationBackupRetentionPolicyWeeklySchedule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "retentionDuration":
            suggest = "retention_duration"
        elif key == "retentionTimes":
            suggest = "retention_times"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationBackupRetentionPolicyWeeklySchedule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationBackupRetentionPolicyWeeklySchedule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationBackupRetentionPolicyWeeklySchedule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 retention_duration: Optional['outputs.ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDuration'] = None,
                 retention_times: Optional[Sequence[str]] = None):
        """
        :param 'ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDurationArgs' retention_duration: A `retention_duration` block as defined below.
        :param Sequence[str] retention_times: The retention times of the backup policy.
        """
        ConfigurationBackupRetentionPolicyWeeklySchedule._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            retention_duration=retention_duration,
            retention_times=retention_times,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             retention_duration: Optional['outputs.ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDuration'] = None,
             retention_times: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'retentionDuration' in kwargs:
            retention_duration = kwargs['retentionDuration']
        if 'retentionTimes' in kwargs:
            retention_times = kwargs['retentionTimes']

        if retention_duration is not None:
            _setter("retention_duration", retention_duration)
        if retention_times is not None:
            _setter("retention_times", retention_times)

    @property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional['outputs.ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDuration']:
        """
        A `retention_duration` block as defined below.
        """
        return pulumi.get(self, "retention_duration")

    @property
    @pulumi.getter(name="retentionTimes")
    def retention_times(self) -> Optional[Sequence[str]]:
        """
        The retention times of the backup policy.
        """
        return pulumi.get(self, "retention_times")


@pulumi.output_type
class ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDuration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "durationType":
            suggest = "duration_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDuration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDuration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDuration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 count: Optional[int] = None,
                 duration_type: Optional[str] = None):
        """
        :param int count: The count of the retention duration of the backup policy. Valid value inside `daily_schedule` is `7` to `9999` and inside `weekly_schedule` is `1` to `5163`.
        :param str duration_type: The duration type of the retention duration of the backup policy. Valid value inside `daily_schedule` is `Days` and inside `weekly_schedule` is `Weeks`.
        """
        ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDuration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            count=count,
            duration_type=duration_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             count: Optional[int] = None,
             duration_type: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'durationType' in kwargs:
            duration_type = kwargs['durationType']

        if count is not None:
            _setter("count", count)
        if duration_type is not None:
            _setter("duration_type", duration_type)

    @property
    @pulumi.getter
    def count(self) -> Optional[int]:
        """
        The count of the retention duration of the backup policy. Valid value inside `daily_schedule` is `7` to `9999` and inside `weekly_schedule` is `1` to `5163`.
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter(name="durationType")
    def duration_type(self) -> Optional[str]:
        """
        The duration type of the retention duration of the backup policy. Valid value inside `daily_schedule` is `Days` and inside `weekly_schedule` is `Weeks`.
        """
        return pulumi.get(self, "duration_type")


@pulumi.output_type
class ConfigurationBackupSchedulePolicy(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "schedulePolicyType":
            suggest = "schedule_policy_type"
        elif key == "scheduleRunDays":
            suggest = "schedule_run_days"
        elif key == "scheduleRunFrequency":
            suggest = "schedule_run_frequency"
        elif key == "scheduleRunTimes":
            suggest = "schedule_run_times"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationBackupSchedulePolicy. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationBackupSchedulePolicy.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationBackupSchedulePolicy.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 schedule_policy_type: Optional[str] = None,
                 schedule_run_days: Optional[Sequence[str]] = None,
                 schedule_run_frequency: Optional[str] = None,
                 schedule_run_times: Optional[Sequence[str]] = None):
        """
        :param str schedule_policy_type: The schedule policy type of the backup policy. Possible value is `SimpleSchedulePolicy`.
        :param Sequence[str] schedule_run_days: The schedule run days of the backup policy. Possible values are `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` and `Saturday`.
        :param str schedule_run_frequency: The schedule run frequency of the backup policy. Possible values are `Daily` and `Weekly`. Defaults to `Daily`.
        :param Sequence[str] schedule_run_times: The schedule run times of the backup policy.
        """
        ConfigurationBackupSchedulePolicy._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            schedule_policy_type=schedule_policy_type,
            schedule_run_days=schedule_run_days,
            schedule_run_frequency=schedule_run_frequency,
            schedule_run_times=schedule_run_times,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             schedule_policy_type: Optional[str] = None,
             schedule_run_days: Optional[Sequence[str]] = None,
             schedule_run_frequency: Optional[str] = None,
             schedule_run_times: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'schedulePolicyType' in kwargs:
            schedule_policy_type = kwargs['schedulePolicyType']
        if 'scheduleRunDays' in kwargs:
            schedule_run_days = kwargs['scheduleRunDays']
        if 'scheduleRunFrequency' in kwargs:
            schedule_run_frequency = kwargs['scheduleRunFrequency']
        if 'scheduleRunTimes' in kwargs:
            schedule_run_times = kwargs['scheduleRunTimes']

        if schedule_policy_type is not None:
            _setter("schedule_policy_type", schedule_policy_type)
        if schedule_run_days is not None:
            _setter("schedule_run_days", schedule_run_days)
        if schedule_run_frequency is not None:
            _setter("schedule_run_frequency", schedule_run_frequency)
        if schedule_run_times is not None:
            _setter("schedule_run_times", schedule_run_times)

    @property
    @pulumi.getter(name="schedulePolicyType")
    def schedule_policy_type(self) -> Optional[str]:
        """
        The schedule policy type of the backup policy. Possible value is `SimpleSchedulePolicy`.
        """
        return pulumi.get(self, "schedule_policy_type")

    @property
    @pulumi.getter(name="scheduleRunDays")
    def schedule_run_days(self) -> Optional[Sequence[str]]:
        """
        The schedule run days of the backup policy. Possible values are `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` and `Saturday`.
        """
        return pulumi.get(self, "schedule_run_days")

    @property
    @pulumi.getter(name="scheduleRunFrequency")
    def schedule_run_frequency(self) -> Optional[str]:
        """
        The schedule run frequency of the backup policy. Possible values are `Daily` and `Weekly`. Defaults to `Daily`.
        """
        return pulumi.get(self, "schedule_run_frequency")

    @property
    @pulumi.getter(name="scheduleRunTimes")
    def schedule_run_times(self) -> Optional[Sequence[str]]:
        """
        The schedule run times of the backup policy.
        """
        return pulumi.get(self, "schedule_run_times")



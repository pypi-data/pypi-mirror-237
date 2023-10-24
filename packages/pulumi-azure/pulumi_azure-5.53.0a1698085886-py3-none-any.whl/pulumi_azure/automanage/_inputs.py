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
    'ConfigurationAntimalwareArgs',
    'ConfigurationAntimalwareExclusionsArgs',
    'ConfigurationAzureSecurityBaselineArgs',
    'ConfigurationBackupArgs',
    'ConfigurationBackupRetentionPolicyArgs',
    'ConfigurationBackupRetentionPolicyDailyScheduleArgs',
    'ConfigurationBackupRetentionPolicyDailyScheduleRetentionDurationArgs',
    'ConfigurationBackupRetentionPolicyWeeklyScheduleArgs',
    'ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDurationArgs',
    'ConfigurationBackupSchedulePolicyArgs',
]

@pulumi.input_type
class ConfigurationAntimalwareArgs:
    def __init__(__self__, *,
                 exclusions: Optional[pulumi.Input['ConfigurationAntimalwareExclusionsArgs']] = None,
                 real_time_protection_enabled: Optional[pulumi.Input[bool]] = None,
                 scheduled_scan_day: Optional[pulumi.Input[int]] = None,
                 scheduled_scan_enabled: Optional[pulumi.Input[bool]] = None,
                 scheduled_scan_time_in_minutes: Optional[pulumi.Input[int]] = None,
                 scheduled_scan_type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input['ConfigurationAntimalwareExclusionsArgs'] exclusions: A `exclusions` block as defined below.
        :param pulumi.Input[bool] real_time_protection_enabled: Whether the real time protection is enabled. Defaults to `false`.
        :param pulumi.Input[int] scheduled_scan_day: The day of the scheduled scan. Possible values are `0` to `8` where `0` is daily, `1` to `7` are the days of the week and `8` is Disabled. Defaults to `8`.
        :param pulumi.Input[bool] scheduled_scan_enabled: Whether the scheduled scan is enabled. Defaults to `false`.
        :param pulumi.Input[int] scheduled_scan_time_in_minutes: The time of the scheduled scan in minutes. Possible values are `0` to `1439` where `0` is 12:00 AM and `1439` is 11:59 PM.
        :param pulumi.Input[str] scheduled_scan_type: The type of the scheduled scan. Possible values are `Quick` and `Full`. Defaults to `Quick`.
        """
        ConfigurationAntimalwareArgs._configure(
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
             exclusions: Optional[pulumi.Input['ConfigurationAntimalwareExclusionsArgs']] = None,
             real_time_protection_enabled: Optional[pulumi.Input[bool]] = None,
             scheduled_scan_day: Optional[pulumi.Input[int]] = None,
             scheduled_scan_enabled: Optional[pulumi.Input[bool]] = None,
             scheduled_scan_time_in_minutes: Optional[pulumi.Input[int]] = None,
             scheduled_scan_type: Optional[pulumi.Input[str]] = None,
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
    def exclusions(self) -> Optional[pulumi.Input['ConfigurationAntimalwareExclusionsArgs']]:
        """
        A `exclusions` block as defined below.
        """
        return pulumi.get(self, "exclusions")

    @exclusions.setter
    def exclusions(self, value: Optional[pulumi.Input['ConfigurationAntimalwareExclusionsArgs']]):
        pulumi.set(self, "exclusions", value)

    @property
    @pulumi.getter(name="realTimeProtectionEnabled")
    def real_time_protection_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the real time protection is enabled. Defaults to `false`.
        """
        return pulumi.get(self, "real_time_protection_enabled")

    @real_time_protection_enabled.setter
    def real_time_protection_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "real_time_protection_enabled", value)

    @property
    @pulumi.getter(name="scheduledScanDay")
    def scheduled_scan_day(self) -> Optional[pulumi.Input[int]]:
        """
        The day of the scheduled scan. Possible values are `0` to `8` where `0` is daily, `1` to `7` are the days of the week and `8` is Disabled. Defaults to `8`.
        """
        return pulumi.get(self, "scheduled_scan_day")

    @scheduled_scan_day.setter
    def scheduled_scan_day(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "scheduled_scan_day", value)

    @property
    @pulumi.getter(name="scheduledScanEnabled")
    def scheduled_scan_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the scheduled scan is enabled. Defaults to `false`.
        """
        return pulumi.get(self, "scheduled_scan_enabled")

    @scheduled_scan_enabled.setter
    def scheduled_scan_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "scheduled_scan_enabled", value)

    @property
    @pulumi.getter(name="scheduledScanTimeInMinutes")
    def scheduled_scan_time_in_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        The time of the scheduled scan in minutes. Possible values are `0` to `1439` where `0` is 12:00 AM and `1439` is 11:59 PM.
        """
        return pulumi.get(self, "scheduled_scan_time_in_minutes")

    @scheduled_scan_time_in_minutes.setter
    def scheduled_scan_time_in_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "scheduled_scan_time_in_minutes", value)

    @property
    @pulumi.getter(name="scheduledScanType")
    def scheduled_scan_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the scheduled scan. Possible values are `Quick` and `Full`. Defaults to `Quick`.
        """
        return pulumi.get(self, "scheduled_scan_type")

    @scheduled_scan_type.setter
    def scheduled_scan_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scheduled_scan_type", value)


@pulumi.input_type
class ConfigurationAntimalwareExclusionsArgs:
    def __init__(__self__, *,
                 extensions: Optional[pulumi.Input[str]] = None,
                 paths: Optional[pulumi.Input[str]] = None,
                 processes: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] extensions: The extensions to exclude from the antimalware scan, separated by `;`. For example `.ext1;.ext2`.
        :param pulumi.Input[str] paths: The paths to exclude from the antimalware scan, separated by `;`. For example `C:\\\\Windows\\\\Temp;D:\\\\Temp`.
        :param pulumi.Input[str] processes: The processes to exclude from the antimalware scan, separated by `;`. For example `svchost.exe;notepad.exe`.
        """
        ConfigurationAntimalwareExclusionsArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            extensions=extensions,
            paths=paths,
            processes=processes,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             extensions: Optional[pulumi.Input[str]] = None,
             paths: Optional[pulumi.Input[str]] = None,
             processes: Optional[pulumi.Input[str]] = None,
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
    def extensions(self) -> Optional[pulumi.Input[str]]:
        """
        The extensions to exclude from the antimalware scan, separated by `;`. For example `.ext1;.ext2`.
        """
        return pulumi.get(self, "extensions")

    @extensions.setter
    def extensions(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "extensions", value)

    @property
    @pulumi.getter
    def paths(self) -> Optional[pulumi.Input[str]]:
        """
        The paths to exclude from the antimalware scan, separated by `;`. For example `C:\\\\Windows\\\\Temp;D:\\\\Temp`.
        """
        return pulumi.get(self, "paths")

    @paths.setter
    def paths(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "paths", value)

    @property
    @pulumi.getter
    def processes(self) -> Optional[pulumi.Input[str]]:
        """
        The processes to exclude from the antimalware scan, separated by `;`. For example `svchost.exe;notepad.exe`.
        """
        return pulumi.get(self, "processes")

    @processes.setter
    def processes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "processes", value)


@pulumi.input_type
class ConfigurationAzureSecurityBaselineArgs:
    def __init__(__self__, *,
                 assignment_type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] assignment_type: The assignment type of the azure security baseline. Possible values are `ApplyAndAutoCorrect`, `ApplyAndMonitor`, `Audit` and `DeployAndAutoCorrect`. Defaults to `ApplyAndAutoCorrect`.
        """
        ConfigurationAzureSecurityBaselineArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            assignment_type=assignment_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             assignment_type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'assignmentType' in kwargs:
            assignment_type = kwargs['assignmentType']

        if assignment_type is not None:
            _setter("assignment_type", assignment_type)

    @property
    @pulumi.getter(name="assignmentType")
    def assignment_type(self) -> Optional[pulumi.Input[str]]:
        """
        The assignment type of the azure security baseline. Possible values are `ApplyAndAutoCorrect`, `ApplyAndMonitor`, `Audit` and `DeployAndAutoCorrect`. Defaults to `ApplyAndAutoCorrect`.
        """
        return pulumi.get(self, "assignment_type")

    @assignment_type.setter
    def assignment_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assignment_type", value)


@pulumi.input_type
class ConfigurationBackupArgs:
    def __init__(__self__, *,
                 instant_rp_retention_range_in_days: Optional[pulumi.Input[int]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 retention_policy: Optional[pulumi.Input['ConfigurationBackupRetentionPolicyArgs']] = None,
                 schedule_policy: Optional[pulumi.Input['ConfigurationBackupSchedulePolicyArgs']] = None,
                 time_zone: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[int] instant_rp_retention_range_in_days: The retention range in days of the backup policy. Defaults to `5`.
        :param pulumi.Input[str] policy_name: The name of the backup policy.
        :param pulumi.Input['ConfigurationBackupRetentionPolicyArgs'] retention_policy: A `retention_policy` block as defined below.
        :param pulumi.Input['ConfigurationBackupSchedulePolicyArgs'] schedule_policy: A `schedule_policy` block as defined below.
        :param pulumi.Input[str] time_zone: The timezone of the backup policy. Defaults to `UTC`.
        """
        ConfigurationBackupArgs._configure(
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
             instant_rp_retention_range_in_days: Optional[pulumi.Input[int]] = None,
             policy_name: Optional[pulumi.Input[str]] = None,
             retention_policy: Optional[pulumi.Input['ConfigurationBackupRetentionPolicyArgs']] = None,
             schedule_policy: Optional[pulumi.Input['ConfigurationBackupSchedulePolicyArgs']] = None,
             time_zone: Optional[pulumi.Input[str]] = None,
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
    def instant_rp_retention_range_in_days(self) -> Optional[pulumi.Input[int]]:
        """
        The retention range in days of the backup policy. Defaults to `5`.
        """
        return pulumi.get(self, "instant_rp_retention_range_in_days")

    @instant_rp_retention_range_in_days.setter
    def instant_rp_retention_range_in_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "instant_rp_retention_range_in_days", value)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the backup policy.
        """
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_name", value)

    @property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[pulumi.Input['ConfigurationBackupRetentionPolicyArgs']]:
        """
        A `retention_policy` block as defined below.
        """
        return pulumi.get(self, "retention_policy")

    @retention_policy.setter
    def retention_policy(self, value: Optional[pulumi.Input['ConfigurationBackupRetentionPolicyArgs']]):
        pulumi.set(self, "retention_policy", value)

    @property
    @pulumi.getter(name="schedulePolicy")
    def schedule_policy(self) -> Optional[pulumi.Input['ConfigurationBackupSchedulePolicyArgs']]:
        """
        A `schedule_policy` block as defined below.
        """
        return pulumi.get(self, "schedule_policy")

    @schedule_policy.setter
    def schedule_policy(self, value: Optional[pulumi.Input['ConfigurationBackupSchedulePolicyArgs']]):
        pulumi.set(self, "schedule_policy", value)

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[str]]:
        """
        The timezone of the backup policy. Defaults to `UTC`.
        """
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_zone", value)


@pulumi.input_type
class ConfigurationBackupRetentionPolicyArgs:
    def __init__(__self__, *,
                 daily_schedule: Optional[pulumi.Input['ConfigurationBackupRetentionPolicyDailyScheduleArgs']] = None,
                 retention_policy_type: Optional[pulumi.Input[str]] = None,
                 weekly_schedule: Optional[pulumi.Input['ConfigurationBackupRetentionPolicyWeeklyScheduleArgs']] = None):
        """
        :param pulumi.Input['ConfigurationBackupRetentionPolicyDailyScheduleArgs'] daily_schedule: A `daily_schedule` block as defined below.
        :param pulumi.Input[str] retention_policy_type: The retention policy type of the backup policy. Possible value is `LongTermRetentionPolicy`.
        :param pulumi.Input['ConfigurationBackupRetentionPolicyWeeklyScheduleArgs'] weekly_schedule: A `weekly_schedule` block as defined below.
        """
        ConfigurationBackupRetentionPolicyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            daily_schedule=daily_schedule,
            retention_policy_type=retention_policy_type,
            weekly_schedule=weekly_schedule,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             daily_schedule: Optional[pulumi.Input['ConfigurationBackupRetentionPolicyDailyScheduleArgs']] = None,
             retention_policy_type: Optional[pulumi.Input[str]] = None,
             weekly_schedule: Optional[pulumi.Input['ConfigurationBackupRetentionPolicyWeeklyScheduleArgs']] = None,
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
    def daily_schedule(self) -> Optional[pulumi.Input['ConfigurationBackupRetentionPolicyDailyScheduleArgs']]:
        """
        A `daily_schedule` block as defined below.
        """
        return pulumi.get(self, "daily_schedule")

    @daily_schedule.setter
    def daily_schedule(self, value: Optional[pulumi.Input['ConfigurationBackupRetentionPolicyDailyScheduleArgs']]):
        pulumi.set(self, "daily_schedule", value)

    @property
    @pulumi.getter(name="retentionPolicyType")
    def retention_policy_type(self) -> Optional[pulumi.Input[str]]:
        """
        The retention policy type of the backup policy. Possible value is `LongTermRetentionPolicy`.
        """
        return pulumi.get(self, "retention_policy_type")

    @retention_policy_type.setter
    def retention_policy_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "retention_policy_type", value)

    @property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(self) -> Optional[pulumi.Input['ConfigurationBackupRetentionPolicyWeeklyScheduleArgs']]:
        """
        A `weekly_schedule` block as defined below.
        """
        return pulumi.get(self, "weekly_schedule")

    @weekly_schedule.setter
    def weekly_schedule(self, value: Optional[pulumi.Input['ConfigurationBackupRetentionPolicyWeeklyScheduleArgs']]):
        pulumi.set(self, "weekly_schedule", value)


@pulumi.input_type
class ConfigurationBackupRetentionPolicyDailyScheduleArgs:
    def __init__(__self__, *,
                 retention_duration: Optional[pulumi.Input['ConfigurationBackupRetentionPolicyDailyScheduleRetentionDurationArgs']] = None,
                 retention_times: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input['ConfigurationBackupRetentionPolicyDailyScheduleRetentionDurationArgs'] retention_duration: A `retention_duration` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] retention_times: The retention times of the backup policy.
        """
        ConfigurationBackupRetentionPolicyDailyScheduleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            retention_duration=retention_duration,
            retention_times=retention_times,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             retention_duration: Optional[pulumi.Input['ConfigurationBackupRetentionPolicyDailyScheduleRetentionDurationArgs']] = None,
             retention_times: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
    def retention_duration(self) -> Optional[pulumi.Input['ConfigurationBackupRetentionPolicyDailyScheduleRetentionDurationArgs']]:
        """
        A `retention_duration` block as defined below.
        """
        return pulumi.get(self, "retention_duration")

    @retention_duration.setter
    def retention_duration(self, value: Optional[pulumi.Input['ConfigurationBackupRetentionPolicyDailyScheduleRetentionDurationArgs']]):
        pulumi.set(self, "retention_duration", value)

    @property
    @pulumi.getter(name="retentionTimes")
    def retention_times(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The retention times of the backup policy.
        """
        return pulumi.get(self, "retention_times")

    @retention_times.setter
    def retention_times(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "retention_times", value)


@pulumi.input_type
class ConfigurationBackupRetentionPolicyDailyScheduleRetentionDurationArgs:
    def __init__(__self__, *,
                 count: Optional[pulumi.Input[int]] = None,
                 duration_type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[int] count: The count of the retention duration of the backup policy. Valid value inside `daily_schedule` is `7` to `9999` and inside `weekly_schedule` is `1` to `5163`.
        :param pulumi.Input[str] duration_type: The duration type of the retention duration of the backup policy. Valid value inside `daily_schedule` is `Days` and inside `weekly_schedule` is `Weeks`.
        """
        ConfigurationBackupRetentionPolicyDailyScheduleRetentionDurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            count=count,
            duration_type=duration_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             count: Optional[pulumi.Input[int]] = None,
             duration_type: Optional[pulumi.Input[str]] = None,
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
    def count(self) -> Optional[pulumi.Input[int]]:
        """
        The count of the retention duration of the backup policy. Valid value inside `daily_schedule` is `7` to `9999` and inside `weekly_schedule` is `1` to `5163`.
        """
        return pulumi.get(self, "count")

    @count.setter
    def count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "count", value)

    @property
    @pulumi.getter(name="durationType")
    def duration_type(self) -> Optional[pulumi.Input[str]]:
        """
        The duration type of the retention duration of the backup policy. Valid value inside `daily_schedule` is `Days` and inside `weekly_schedule` is `Weeks`.
        """
        return pulumi.get(self, "duration_type")

    @duration_type.setter
    def duration_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "duration_type", value)


@pulumi.input_type
class ConfigurationBackupRetentionPolicyWeeklyScheduleArgs:
    def __init__(__self__, *,
                 retention_duration: Optional[pulumi.Input['ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDurationArgs']] = None,
                 retention_times: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input['ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDurationArgs'] retention_duration: A `retention_duration` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] retention_times: The retention times of the backup policy.
        """
        ConfigurationBackupRetentionPolicyWeeklyScheduleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            retention_duration=retention_duration,
            retention_times=retention_times,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             retention_duration: Optional[pulumi.Input['ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDurationArgs']] = None,
             retention_times: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
    def retention_duration(self) -> Optional[pulumi.Input['ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDurationArgs']]:
        """
        A `retention_duration` block as defined below.
        """
        return pulumi.get(self, "retention_duration")

    @retention_duration.setter
    def retention_duration(self, value: Optional[pulumi.Input['ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDurationArgs']]):
        pulumi.set(self, "retention_duration", value)

    @property
    @pulumi.getter(name="retentionTimes")
    def retention_times(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The retention times of the backup policy.
        """
        return pulumi.get(self, "retention_times")

    @retention_times.setter
    def retention_times(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "retention_times", value)


@pulumi.input_type
class ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDurationArgs:
    def __init__(__self__, *,
                 count: Optional[pulumi.Input[int]] = None,
                 duration_type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[int] count: The count of the retention duration of the backup policy. Valid value inside `daily_schedule` is `7` to `9999` and inside `weekly_schedule` is `1` to `5163`.
        :param pulumi.Input[str] duration_type: The duration type of the retention duration of the backup policy. Valid value inside `daily_schedule` is `Days` and inside `weekly_schedule` is `Weeks`.
        """
        ConfigurationBackupRetentionPolicyWeeklyScheduleRetentionDurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            count=count,
            duration_type=duration_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             count: Optional[pulumi.Input[int]] = None,
             duration_type: Optional[pulumi.Input[str]] = None,
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
    def count(self) -> Optional[pulumi.Input[int]]:
        """
        The count of the retention duration of the backup policy. Valid value inside `daily_schedule` is `7` to `9999` and inside `weekly_schedule` is `1` to `5163`.
        """
        return pulumi.get(self, "count")

    @count.setter
    def count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "count", value)

    @property
    @pulumi.getter(name="durationType")
    def duration_type(self) -> Optional[pulumi.Input[str]]:
        """
        The duration type of the retention duration of the backup policy. Valid value inside `daily_schedule` is `Days` and inside `weekly_schedule` is `Weeks`.
        """
        return pulumi.get(self, "duration_type")

    @duration_type.setter
    def duration_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "duration_type", value)


@pulumi.input_type
class ConfigurationBackupSchedulePolicyArgs:
    def __init__(__self__, *,
                 schedule_policy_type: Optional[pulumi.Input[str]] = None,
                 schedule_run_days: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 schedule_run_frequency: Optional[pulumi.Input[str]] = None,
                 schedule_run_times: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] schedule_policy_type: The schedule policy type of the backup policy. Possible value is `SimpleSchedulePolicy`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] schedule_run_days: The schedule run days of the backup policy. Possible values are `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` and `Saturday`.
        :param pulumi.Input[str] schedule_run_frequency: The schedule run frequency of the backup policy. Possible values are `Daily` and `Weekly`. Defaults to `Daily`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] schedule_run_times: The schedule run times of the backup policy.
        """
        ConfigurationBackupSchedulePolicyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            schedule_policy_type=schedule_policy_type,
            schedule_run_days=schedule_run_days,
            schedule_run_frequency=schedule_run_frequency,
            schedule_run_times=schedule_run_times,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             schedule_policy_type: Optional[pulumi.Input[str]] = None,
             schedule_run_days: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             schedule_run_frequency: Optional[pulumi.Input[str]] = None,
             schedule_run_times: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
    def schedule_policy_type(self) -> Optional[pulumi.Input[str]]:
        """
        The schedule policy type of the backup policy. Possible value is `SimpleSchedulePolicy`.
        """
        return pulumi.get(self, "schedule_policy_type")

    @schedule_policy_type.setter
    def schedule_policy_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schedule_policy_type", value)

    @property
    @pulumi.getter(name="scheduleRunDays")
    def schedule_run_days(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The schedule run days of the backup policy. Possible values are `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` and `Saturday`.
        """
        return pulumi.get(self, "schedule_run_days")

    @schedule_run_days.setter
    def schedule_run_days(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "schedule_run_days", value)

    @property
    @pulumi.getter(name="scheduleRunFrequency")
    def schedule_run_frequency(self) -> Optional[pulumi.Input[str]]:
        """
        The schedule run frequency of the backup policy. Possible values are `Daily` and `Weekly`. Defaults to `Daily`.
        """
        return pulumi.get(self, "schedule_run_frequency")

    @schedule_run_frequency.setter
    def schedule_run_frequency(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schedule_run_frequency", value)

    @property
    @pulumi.getter(name="scheduleRunTimes")
    def schedule_run_times(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The schedule run times of the backup policy.
        """
        return pulumi.get(self, "schedule_run_times")

    @schedule_run_times.setter
    def schedule_run_times(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "schedule_run_times", value)



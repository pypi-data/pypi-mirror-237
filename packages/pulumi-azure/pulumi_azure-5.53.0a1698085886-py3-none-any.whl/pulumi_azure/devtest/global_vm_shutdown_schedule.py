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
from ._inputs import *

__all__ = ['GlobalVMShutdownScheduleArgs', 'GlobalVMShutdownSchedule']

@pulumi.input_type
class GlobalVMShutdownScheduleArgs:
    def __init__(__self__, *,
                 daily_recurrence_time: pulumi.Input[str],
                 notification_settings: pulumi.Input['GlobalVMShutdownScheduleNotificationSettingsArgs'],
                 timezone: pulumi.Input[str],
                 virtual_machine_id: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a GlobalVMShutdownSchedule resource.
        :param pulumi.Input[str] daily_recurrence_time: The time each day when the schedule takes effect. Must match the format HHmm where HH is 00-23 and mm is 00-59 (e.g. 0930, 2300, etc.)
        :param pulumi.Input['GlobalVMShutdownScheduleNotificationSettingsArgs'] notification_settings: The notification setting of a schedule. A `notification_settings` as defined below.
        :param pulumi.Input[str] timezone: The time zone ID (e.g. Pacific Standard time). Refer to this guide for a [full list of accepted time zone names](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
        :param pulumi.Input[str] virtual_machine_id: The resource ID of the target ARM-based Virtual Machine. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] enabled: Whether to enable the schedule. Possible values are `true` and `false`. Defaults to `true`.
        :param pulumi.Input[str] location: The location where the schedule is created. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        GlobalVMShutdownScheduleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            daily_recurrence_time=daily_recurrence_time,
            notification_settings=notification_settings,
            timezone=timezone,
            virtual_machine_id=virtual_machine_id,
            enabled=enabled,
            location=location,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             daily_recurrence_time: pulumi.Input[str],
             notification_settings: pulumi.Input['GlobalVMShutdownScheduleNotificationSettingsArgs'],
             timezone: pulumi.Input[str],
             virtual_machine_id: pulumi.Input[str],
             enabled: Optional[pulumi.Input[bool]] = None,
             location: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'dailyRecurrenceTime' in kwargs:
            daily_recurrence_time = kwargs['dailyRecurrenceTime']
        if 'notificationSettings' in kwargs:
            notification_settings = kwargs['notificationSettings']
        if 'virtualMachineId' in kwargs:
            virtual_machine_id = kwargs['virtualMachineId']

        _setter("daily_recurrence_time", daily_recurrence_time)
        _setter("notification_settings", notification_settings)
        _setter("timezone", timezone)
        _setter("virtual_machine_id", virtual_machine_id)
        if enabled is not None:
            _setter("enabled", enabled)
        if location is not None:
            _setter("location", location)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="dailyRecurrenceTime")
    def daily_recurrence_time(self) -> pulumi.Input[str]:
        """
        The time each day when the schedule takes effect. Must match the format HHmm where HH is 00-23 and mm is 00-59 (e.g. 0930, 2300, etc.)
        """
        return pulumi.get(self, "daily_recurrence_time")

    @daily_recurrence_time.setter
    def daily_recurrence_time(self, value: pulumi.Input[str]):
        pulumi.set(self, "daily_recurrence_time", value)

    @property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(self) -> pulumi.Input['GlobalVMShutdownScheduleNotificationSettingsArgs']:
        """
        The notification setting of a schedule. A `notification_settings` as defined below.
        """
        return pulumi.get(self, "notification_settings")

    @notification_settings.setter
    def notification_settings(self, value: pulumi.Input['GlobalVMShutdownScheduleNotificationSettingsArgs']):
        pulumi.set(self, "notification_settings", value)

    @property
    @pulumi.getter
    def timezone(self) -> pulumi.Input[str]:
        """
        The time zone ID (e.g. Pacific Standard time). Refer to this guide for a [full list of accepted time zone names](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
        """
        return pulumi.get(self, "timezone")

    @timezone.setter
    def timezone(self, value: pulumi.Input[str]):
        pulumi.set(self, "timezone", value)

    @property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the target ARM-based Virtual Machine. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "virtual_machine_id")

    @virtual_machine_id.setter
    def virtual_machine_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_machine_id", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable the schedule. Possible values are `true` and `false`. Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location where the schedule is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _GlobalVMShutdownScheduleState:
    def __init__(__self__, *,
                 daily_recurrence_time: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 notification_settings: Optional[pulumi.Input['GlobalVMShutdownScheduleNotificationSettingsArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
                 virtual_machine_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GlobalVMShutdownSchedule resources.
        :param pulumi.Input[str] daily_recurrence_time: The time each day when the schedule takes effect. Must match the format HHmm where HH is 00-23 and mm is 00-59 (e.g. 0930, 2300, etc.)
        :param pulumi.Input[bool] enabled: Whether to enable the schedule. Possible values are `true` and `false`. Defaults to `true`.
        :param pulumi.Input[str] location: The location where the schedule is created. Changing this forces a new resource to be created.
        :param pulumi.Input['GlobalVMShutdownScheduleNotificationSettingsArgs'] notification_settings: The notification setting of a schedule. A `notification_settings` as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] timezone: The time zone ID (e.g. Pacific Standard time). Refer to this guide for a [full list of accepted time zone names](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
        :param pulumi.Input[str] virtual_machine_id: The resource ID of the target ARM-based Virtual Machine. Changing this forces a new resource to be created.
        """
        _GlobalVMShutdownScheduleState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            daily_recurrence_time=daily_recurrence_time,
            enabled=enabled,
            location=location,
            notification_settings=notification_settings,
            tags=tags,
            timezone=timezone,
            virtual_machine_id=virtual_machine_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             daily_recurrence_time: Optional[pulumi.Input[str]] = None,
             enabled: Optional[pulumi.Input[bool]] = None,
             location: Optional[pulumi.Input[str]] = None,
             notification_settings: Optional[pulumi.Input['GlobalVMShutdownScheduleNotificationSettingsArgs']] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             timezone: Optional[pulumi.Input[str]] = None,
             virtual_machine_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'dailyRecurrenceTime' in kwargs:
            daily_recurrence_time = kwargs['dailyRecurrenceTime']
        if 'notificationSettings' in kwargs:
            notification_settings = kwargs['notificationSettings']
        if 'virtualMachineId' in kwargs:
            virtual_machine_id = kwargs['virtualMachineId']

        if daily_recurrence_time is not None:
            _setter("daily_recurrence_time", daily_recurrence_time)
        if enabled is not None:
            _setter("enabled", enabled)
        if location is not None:
            _setter("location", location)
        if notification_settings is not None:
            _setter("notification_settings", notification_settings)
        if tags is not None:
            _setter("tags", tags)
        if timezone is not None:
            _setter("timezone", timezone)
        if virtual_machine_id is not None:
            _setter("virtual_machine_id", virtual_machine_id)

    @property
    @pulumi.getter(name="dailyRecurrenceTime")
    def daily_recurrence_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time each day when the schedule takes effect. Must match the format HHmm where HH is 00-23 and mm is 00-59 (e.g. 0930, 2300, etc.)
        """
        return pulumi.get(self, "daily_recurrence_time")

    @daily_recurrence_time.setter
    def daily_recurrence_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "daily_recurrence_time", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable the schedule. Possible values are `true` and `false`. Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location where the schedule is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(self) -> Optional[pulumi.Input['GlobalVMShutdownScheduleNotificationSettingsArgs']]:
        """
        The notification setting of a schedule. A `notification_settings` as defined below.
        """
        return pulumi.get(self, "notification_settings")

    @notification_settings.setter
    def notification_settings(self, value: Optional[pulumi.Input['GlobalVMShutdownScheduleNotificationSettingsArgs']]):
        pulumi.set(self, "notification_settings", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[str]]:
        """
        The time zone ID (e.g. Pacific Standard time). Refer to this guide for a [full list of accepted time zone names](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
        """
        return pulumi.get(self, "timezone")

    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timezone", value)

    @property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the target ARM-based Virtual Machine. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "virtual_machine_id")

    @virtual_machine_id.setter
    def virtual_machine_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_machine_id", value)


class GlobalVMShutdownSchedule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 daily_recurrence_time: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 notification_settings: Optional[pulumi.Input[pulumi.InputType['GlobalVMShutdownScheduleNotificationSettingsArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
                 virtual_machine_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages automated shutdown schedules for Azure VMs that are not within an Azure DevTest Lab. While this is part of the DevTest Labs service in Azure,
        this resource applies only to standard VMs, not DevTest Lab VMs. To manage automated shutdown schedules for DevTest Lab VMs, reference the
        `devtest.Schedule` resource

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            address_spaces=["10.0.0.0/16"],
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_subnet = azure.network.Subnet("exampleSubnet",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.0.2.0/24"])
        example_network_interface = azure.network.NetworkInterface("exampleNetworkInterface",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            ip_configurations=[azure.network.NetworkInterfaceIpConfigurationArgs(
                name="testconfiguration1",
                subnet_id=example_subnet.id,
                private_ip_address_allocation="Dynamic",
            )])
        example_linux_virtual_machine = azure.compute.LinuxVirtualMachine("exampleLinuxVirtualMachine",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            network_interface_ids=[example_network_interface.id],
            size="Standard_B2s",
            source_image_reference=azure.compute.LinuxVirtualMachineSourceImageReferenceArgs(
                publisher="Canonical",
                offer="0001-com-ubuntu-server-focal",
                sku="20_04-lts",
                version="latest",
            ),
            os_disk=azure.compute.LinuxVirtualMachineOsDiskArgs(
                name="myosdisk-example",
                caching="ReadWrite",
                storage_account_type="Standard_LRS",
            ),
            admin_username="testadmin",
            admin_password="Password1234!",
            disable_password_authentication=False)
        example_global_vm_shutdown_schedule = azure.devtest.GlobalVMShutdownSchedule("exampleGlobalVMShutdownSchedule",
            virtual_machine_id=example_linux_virtual_machine.id,
            location=example_resource_group.location,
            enabled=True,
            daily_recurrence_time="1100",
            timezone="Pacific Standard Time",
            notification_settings=azure.devtest.GlobalVMShutdownScheduleNotificationSettingsArgs(
                enabled=True,
                time_in_minutes=60,
                webhook_url="https://sample-webhook-url.example.com",
            ))
        ```

        ## Import

        An existing Dev Test Global Shutdown Schedule can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:devtest/globalVMShutdownSchedule:GlobalVMShutdownSchedule example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/sample-rg/providers/Microsoft.DevTestLab/schedules/shutdown-computevm-SampleVM
        ```

         The name of the resource within the `resource id` will always follow the format `shutdown-computevm-<VM Name>` where `<VM Name>` is replaced by the name of the target Virtual Machine

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] daily_recurrence_time: The time each day when the schedule takes effect. Must match the format HHmm where HH is 00-23 and mm is 00-59 (e.g. 0930, 2300, etc.)
        :param pulumi.Input[bool] enabled: Whether to enable the schedule. Possible values are `true` and `false`. Defaults to `true`.
        :param pulumi.Input[str] location: The location where the schedule is created. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['GlobalVMShutdownScheduleNotificationSettingsArgs']] notification_settings: The notification setting of a schedule. A `notification_settings` as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] timezone: The time zone ID (e.g. Pacific Standard time). Refer to this guide for a [full list of accepted time zone names](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
        :param pulumi.Input[str] virtual_machine_id: The resource ID of the target ARM-based Virtual Machine. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GlobalVMShutdownScheduleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages automated shutdown schedules for Azure VMs that are not within an Azure DevTest Lab. While this is part of the DevTest Labs service in Azure,
        this resource applies only to standard VMs, not DevTest Lab VMs. To manage automated shutdown schedules for DevTest Lab VMs, reference the
        `devtest.Schedule` resource

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            address_spaces=["10.0.0.0/16"],
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_subnet = azure.network.Subnet("exampleSubnet",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.0.2.0/24"])
        example_network_interface = azure.network.NetworkInterface("exampleNetworkInterface",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            ip_configurations=[azure.network.NetworkInterfaceIpConfigurationArgs(
                name="testconfiguration1",
                subnet_id=example_subnet.id,
                private_ip_address_allocation="Dynamic",
            )])
        example_linux_virtual_machine = azure.compute.LinuxVirtualMachine("exampleLinuxVirtualMachine",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            network_interface_ids=[example_network_interface.id],
            size="Standard_B2s",
            source_image_reference=azure.compute.LinuxVirtualMachineSourceImageReferenceArgs(
                publisher="Canonical",
                offer="0001-com-ubuntu-server-focal",
                sku="20_04-lts",
                version="latest",
            ),
            os_disk=azure.compute.LinuxVirtualMachineOsDiskArgs(
                name="myosdisk-example",
                caching="ReadWrite",
                storage_account_type="Standard_LRS",
            ),
            admin_username="testadmin",
            admin_password="Password1234!",
            disable_password_authentication=False)
        example_global_vm_shutdown_schedule = azure.devtest.GlobalVMShutdownSchedule("exampleGlobalVMShutdownSchedule",
            virtual_machine_id=example_linux_virtual_machine.id,
            location=example_resource_group.location,
            enabled=True,
            daily_recurrence_time="1100",
            timezone="Pacific Standard Time",
            notification_settings=azure.devtest.GlobalVMShutdownScheduleNotificationSettingsArgs(
                enabled=True,
                time_in_minutes=60,
                webhook_url="https://sample-webhook-url.example.com",
            ))
        ```

        ## Import

        An existing Dev Test Global Shutdown Schedule can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:devtest/globalVMShutdownSchedule:GlobalVMShutdownSchedule example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/sample-rg/providers/Microsoft.DevTestLab/schedules/shutdown-computevm-SampleVM
        ```

         The name of the resource within the `resource id` will always follow the format `shutdown-computevm-<VM Name>` where `<VM Name>` is replaced by the name of the target Virtual Machine

        :param str resource_name: The name of the resource.
        :param GlobalVMShutdownScheduleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GlobalVMShutdownScheduleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            GlobalVMShutdownScheduleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 daily_recurrence_time: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 notification_settings: Optional[pulumi.Input[pulumi.InputType['GlobalVMShutdownScheduleNotificationSettingsArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
                 virtual_machine_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GlobalVMShutdownScheduleArgs.__new__(GlobalVMShutdownScheduleArgs)

            if daily_recurrence_time is None and not opts.urn:
                raise TypeError("Missing required property 'daily_recurrence_time'")
            __props__.__dict__["daily_recurrence_time"] = daily_recurrence_time
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["location"] = location
            if notification_settings is not None and not isinstance(notification_settings, GlobalVMShutdownScheduleNotificationSettingsArgs):
                notification_settings = notification_settings or {}
                def _setter(key, value):
                    notification_settings[key] = value
                GlobalVMShutdownScheduleNotificationSettingsArgs._configure(_setter, **notification_settings)
            if notification_settings is None and not opts.urn:
                raise TypeError("Missing required property 'notification_settings'")
            __props__.__dict__["notification_settings"] = notification_settings
            __props__.__dict__["tags"] = tags
            if timezone is None and not opts.urn:
                raise TypeError("Missing required property 'timezone'")
            __props__.__dict__["timezone"] = timezone
            if virtual_machine_id is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_machine_id'")
            __props__.__dict__["virtual_machine_id"] = virtual_machine_id
        super(GlobalVMShutdownSchedule, __self__).__init__(
            'azure:devtest/globalVMShutdownSchedule:GlobalVMShutdownSchedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            daily_recurrence_time: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            location: Optional[pulumi.Input[str]] = None,
            notification_settings: Optional[pulumi.Input[pulumi.InputType['GlobalVMShutdownScheduleNotificationSettingsArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            timezone: Optional[pulumi.Input[str]] = None,
            virtual_machine_id: Optional[pulumi.Input[str]] = None) -> 'GlobalVMShutdownSchedule':
        """
        Get an existing GlobalVMShutdownSchedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] daily_recurrence_time: The time each day when the schedule takes effect. Must match the format HHmm where HH is 00-23 and mm is 00-59 (e.g. 0930, 2300, etc.)
        :param pulumi.Input[bool] enabled: Whether to enable the schedule. Possible values are `true` and `false`. Defaults to `true`.
        :param pulumi.Input[str] location: The location where the schedule is created. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['GlobalVMShutdownScheduleNotificationSettingsArgs']] notification_settings: The notification setting of a schedule. A `notification_settings` as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] timezone: The time zone ID (e.g. Pacific Standard time). Refer to this guide for a [full list of accepted time zone names](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
        :param pulumi.Input[str] virtual_machine_id: The resource ID of the target ARM-based Virtual Machine. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GlobalVMShutdownScheduleState.__new__(_GlobalVMShutdownScheduleState)

        __props__.__dict__["daily_recurrence_time"] = daily_recurrence_time
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["location"] = location
        __props__.__dict__["notification_settings"] = notification_settings
        __props__.__dict__["tags"] = tags
        __props__.__dict__["timezone"] = timezone
        __props__.__dict__["virtual_machine_id"] = virtual_machine_id
        return GlobalVMShutdownSchedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dailyRecurrenceTime")
    def daily_recurrence_time(self) -> pulumi.Output[str]:
        """
        The time each day when the schedule takes effect. Must match the format HHmm where HH is 00-23 and mm is 00-59 (e.g. 0930, 2300, etc.)
        """
        return pulumi.get(self, "daily_recurrence_time")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to enable the schedule. Possible values are `true` and `false`. Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location where the schedule is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(self) -> pulumi.Output['outputs.GlobalVMShutdownScheduleNotificationSettings']:
        """
        The notification setting of a schedule. A `notification_settings` as defined below.
        """
        return pulumi.get(self, "notification_settings")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def timezone(self) -> pulumi.Output[str]:
        """
        The time zone ID (e.g. Pacific Standard time). Refer to this guide for a [full list of accepted time zone names](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
        """
        return pulumi.get(self, "timezone")

    @property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the target ARM-based Virtual Machine. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "virtual_machine_id")


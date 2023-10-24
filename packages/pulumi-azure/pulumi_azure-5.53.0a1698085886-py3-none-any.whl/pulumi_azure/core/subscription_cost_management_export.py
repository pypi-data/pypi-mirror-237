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

__all__ = ['SubscriptionCostManagementExportArgs', 'SubscriptionCostManagementExport']

@pulumi.input_type
class SubscriptionCostManagementExportArgs:
    def __init__(__self__, *,
                 export_data_options: pulumi.Input['SubscriptionCostManagementExportExportDataOptionsArgs'],
                 export_data_storage_location: pulumi.Input['SubscriptionCostManagementExportExportDataStorageLocationArgs'],
                 recurrence_period_end_date: pulumi.Input[str],
                 recurrence_period_start_date: pulumi.Input[str],
                 recurrence_type: pulumi.Input[str],
                 subscription_id: pulumi.Input[str],
                 active: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SubscriptionCostManagementExport resource.
        :param pulumi.Input['SubscriptionCostManagementExportExportDataOptionsArgs'] export_data_options: A `export_data_options` block as defined below.
        :param pulumi.Input['SubscriptionCostManagementExportExportDataStorageLocationArgs'] export_data_storage_location: A `export_data_storage_location` block as defined below.
        :param pulumi.Input[str] recurrence_period_end_date: The date the export will stop capturing information.
        :param pulumi.Input[str] recurrence_period_start_date: The date the export will start capturing information.
        :param pulumi.Input[str] recurrence_type: How often the requested information will be exported. Valid values include `Annually`, `Daily`, `Monthly`, `Weekly`.
        :param pulumi.Input[str] subscription_id: The id of the subscription on which to create an export. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] active: Is the cost management export active? Default is `true`.
        :param pulumi.Input[str] name: Specifies the name of the Cost Management Export. Changing this forces a new resource to be created.
        """
        SubscriptionCostManagementExportArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            export_data_options=export_data_options,
            export_data_storage_location=export_data_storage_location,
            recurrence_period_end_date=recurrence_period_end_date,
            recurrence_period_start_date=recurrence_period_start_date,
            recurrence_type=recurrence_type,
            subscription_id=subscription_id,
            active=active,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             export_data_options: pulumi.Input['SubscriptionCostManagementExportExportDataOptionsArgs'],
             export_data_storage_location: pulumi.Input['SubscriptionCostManagementExportExportDataStorageLocationArgs'],
             recurrence_period_end_date: pulumi.Input[str],
             recurrence_period_start_date: pulumi.Input[str],
             recurrence_type: pulumi.Input[str],
             subscription_id: pulumi.Input[str],
             active: Optional[pulumi.Input[bool]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'exportDataOptions' in kwargs:
            export_data_options = kwargs['exportDataOptions']
        if 'exportDataStorageLocation' in kwargs:
            export_data_storage_location = kwargs['exportDataStorageLocation']
        if 'recurrencePeriodEndDate' in kwargs:
            recurrence_period_end_date = kwargs['recurrencePeriodEndDate']
        if 'recurrencePeriodStartDate' in kwargs:
            recurrence_period_start_date = kwargs['recurrencePeriodStartDate']
        if 'recurrenceType' in kwargs:
            recurrence_type = kwargs['recurrenceType']
        if 'subscriptionId' in kwargs:
            subscription_id = kwargs['subscriptionId']

        _setter("export_data_options", export_data_options)
        _setter("export_data_storage_location", export_data_storage_location)
        _setter("recurrence_period_end_date", recurrence_period_end_date)
        _setter("recurrence_period_start_date", recurrence_period_start_date)
        _setter("recurrence_type", recurrence_type)
        _setter("subscription_id", subscription_id)
        if active is not None:
            _setter("active", active)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="exportDataOptions")
    def export_data_options(self) -> pulumi.Input['SubscriptionCostManagementExportExportDataOptionsArgs']:
        """
        A `export_data_options` block as defined below.
        """
        return pulumi.get(self, "export_data_options")

    @export_data_options.setter
    def export_data_options(self, value: pulumi.Input['SubscriptionCostManagementExportExportDataOptionsArgs']):
        pulumi.set(self, "export_data_options", value)

    @property
    @pulumi.getter(name="exportDataStorageLocation")
    def export_data_storage_location(self) -> pulumi.Input['SubscriptionCostManagementExportExportDataStorageLocationArgs']:
        """
        A `export_data_storage_location` block as defined below.
        """
        return pulumi.get(self, "export_data_storage_location")

    @export_data_storage_location.setter
    def export_data_storage_location(self, value: pulumi.Input['SubscriptionCostManagementExportExportDataStorageLocationArgs']):
        pulumi.set(self, "export_data_storage_location", value)

    @property
    @pulumi.getter(name="recurrencePeriodEndDate")
    def recurrence_period_end_date(self) -> pulumi.Input[str]:
        """
        The date the export will stop capturing information.
        """
        return pulumi.get(self, "recurrence_period_end_date")

    @recurrence_period_end_date.setter
    def recurrence_period_end_date(self, value: pulumi.Input[str]):
        pulumi.set(self, "recurrence_period_end_date", value)

    @property
    @pulumi.getter(name="recurrencePeriodStartDate")
    def recurrence_period_start_date(self) -> pulumi.Input[str]:
        """
        The date the export will start capturing information.
        """
        return pulumi.get(self, "recurrence_period_start_date")

    @recurrence_period_start_date.setter
    def recurrence_period_start_date(self, value: pulumi.Input[str]):
        pulumi.set(self, "recurrence_period_start_date", value)

    @property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> pulumi.Input[str]:
        """
        How often the requested information will be exported. Valid values include `Annually`, `Daily`, `Monthly`, `Weekly`.
        """
        return pulumi.get(self, "recurrence_type")

    @recurrence_type.setter
    def recurrence_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "recurrence_type", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Input[str]:
        """
        The id of the subscription on which to create an export. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subscription_id", value)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        """
        Is the cost management export active? Default is `true`.
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Cost Management Export. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _SubscriptionCostManagementExportState:
    def __init__(__self__, *,
                 active: Optional[pulumi.Input[bool]] = None,
                 export_data_options: Optional[pulumi.Input['SubscriptionCostManagementExportExportDataOptionsArgs']] = None,
                 export_data_storage_location: Optional[pulumi.Input['SubscriptionCostManagementExportExportDataStorageLocationArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recurrence_period_end_date: Optional[pulumi.Input[str]] = None,
                 recurrence_period_start_date: Optional[pulumi.Input[str]] = None,
                 recurrence_type: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SubscriptionCostManagementExport resources.
        :param pulumi.Input[bool] active: Is the cost management export active? Default is `true`.
        :param pulumi.Input['SubscriptionCostManagementExportExportDataOptionsArgs'] export_data_options: A `export_data_options` block as defined below.
        :param pulumi.Input['SubscriptionCostManagementExportExportDataStorageLocationArgs'] export_data_storage_location: A `export_data_storage_location` block as defined below.
        :param pulumi.Input[str] name: Specifies the name of the Cost Management Export. Changing this forces a new resource to be created.
        :param pulumi.Input[str] recurrence_period_end_date: The date the export will stop capturing information.
        :param pulumi.Input[str] recurrence_period_start_date: The date the export will start capturing information.
        :param pulumi.Input[str] recurrence_type: How often the requested information will be exported. Valid values include `Annually`, `Daily`, `Monthly`, `Weekly`.
        :param pulumi.Input[str] subscription_id: The id of the subscription on which to create an export. Changing this forces a new resource to be created.
        """
        _SubscriptionCostManagementExportState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            active=active,
            export_data_options=export_data_options,
            export_data_storage_location=export_data_storage_location,
            name=name,
            recurrence_period_end_date=recurrence_period_end_date,
            recurrence_period_start_date=recurrence_period_start_date,
            recurrence_type=recurrence_type,
            subscription_id=subscription_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             active: Optional[pulumi.Input[bool]] = None,
             export_data_options: Optional[pulumi.Input['SubscriptionCostManagementExportExportDataOptionsArgs']] = None,
             export_data_storage_location: Optional[pulumi.Input['SubscriptionCostManagementExportExportDataStorageLocationArgs']] = None,
             name: Optional[pulumi.Input[str]] = None,
             recurrence_period_end_date: Optional[pulumi.Input[str]] = None,
             recurrence_period_start_date: Optional[pulumi.Input[str]] = None,
             recurrence_type: Optional[pulumi.Input[str]] = None,
             subscription_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'exportDataOptions' in kwargs:
            export_data_options = kwargs['exportDataOptions']
        if 'exportDataStorageLocation' in kwargs:
            export_data_storage_location = kwargs['exportDataStorageLocation']
        if 'recurrencePeriodEndDate' in kwargs:
            recurrence_period_end_date = kwargs['recurrencePeriodEndDate']
        if 'recurrencePeriodStartDate' in kwargs:
            recurrence_period_start_date = kwargs['recurrencePeriodStartDate']
        if 'recurrenceType' in kwargs:
            recurrence_type = kwargs['recurrenceType']
        if 'subscriptionId' in kwargs:
            subscription_id = kwargs['subscriptionId']

        if active is not None:
            _setter("active", active)
        if export_data_options is not None:
            _setter("export_data_options", export_data_options)
        if export_data_storage_location is not None:
            _setter("export_data_storage_location", export_data_storage_location)
        if name is not None:
            _setter("name", name)
        if recurrence_period_end_date is not None:
            _setter("recurrence_period_end_date", recurrence_period_end_date)
        if recurrence_period_start_date is not None:
            _setter("recurrence_period_start_date", recurrence_period_start_date)
        if recurrence_type is not None:
            _setter("recurrence_type", recurrence_type)
        if subscription_id is not None:
            _setter("subscription_id", subscription_id)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        """
        Is the cost management export active? Default is `true`.
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter(name="exportDataOptions")
    def export_data_options(self) -> Optional[pulumi.Input['SubscriptionCostManagementExportExportDataOptionsArgs']]:
        """
        A `export_data_options` block as defined below.
        """
        return pulumi.get(self, "export_data_options")

    @export_data_options.setter
    def export_data_options(self, value: Optional[pulumi.Input['SubscriptionCostManagementExportExportDataOptionsArgs']]):
        pulumi.set(self, "export_data_options", value)

    @property
    @pulumi.getter(name="exportDataStorageLocation")
    def export_data_storage_location(self) -> Optional[pulumi.Input['SubscriptionCostManagementExportExportDataStorageLocationArgs']]:
        """
        A `export_data_storage_location` block as defined below.
        """
        return pulumi.get(self, "export_data_storage_location")

    @export_data_storage_location.setter
    def export_data_storage_location(self, value: Optional[pulumi.Input['SubscriptionCostManagementExportExportDataStorageLocationArgs']]):
        pulumi.set(self, "export_data_storage_location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Cost Management Export. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="recurrencePeriodEndDate")
    def recurrence_period_end_date(self) -> Optional[pulumi.Input[str]]:
        """
        The date the export will stop capturing information.
        """
        return pulumi.get(self, "recurrence_period_end_date")

    @recurrence_period_end_date.setter
    def recurrence_period_end_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recurrence_period_end_date", value)

    @property
    @pulumi.getter(name="recurrencePeriodStartDate")
    def recurrence_period_start_date(self) -> Optional[pulumi.Input[str]]:
        """
        The date the export will start capturing information.
        """
        return pulumi.get(self, "recurrence_period_start_date")

    @recurrence_period_start_date.setter
    def recurrence_period_start_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recurrence_period_start_date", value)

    @property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> Optional[pulumi.Input[str]]:
        """
        How often the requested information will be exported. Valid values include `Annually`, `Daily`, `Monthly`, `Weekly`.
        """
        return pulumi.get(self, "recurrence_type")

    @recurrence_type.setter
    def recurrence_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recurrence_type", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the subscription on which to create an export. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)


class SubscriptionCostManagementExport(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 export_data_options: Optional[pulumi.Input[pulumi.InputType['SubscriptionCostManagementExportExportDataOptionsArgs']]] = None,
                 export_data_storage_location: Optional[pulumi.Input[pulumi.InputType['SubscriptionCostManagementExportExportDataStorageLocationArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recurrence_period_end_date: Optional[pulumi.Input[str]] = None,
                 recurrence_period_start_date: Optional[pulumi.Input[str]] = None,
                 recurrence_type: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Cost Management Export for a Subscription.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_subscription = azure.core.get_subscription()
        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_container = azure.storage.Container("exampleContainer", storage_account_name=example_account.name)
        example_subscription_cost_management_export = azure.core.SubscriptionCostManagementExport("exampleSubscriptionCostManagementExport",
            subscription_id=example_subscription.id,
            recurrence_type="Monthly",
            recurrence_period_start_date="2020-08-18T00:00:00Z",
            recurrence_period_end_date="2020-09-18T00:00:00Z",
            export_data_storage_location=azure.core.SubscriptionCostManagementExportExportDataStorageLocationArgs(
                container_id=example_container.resource_manager_id,
                root_folder_path="/root/updated",
            ),
            export_data_options=azure.core.SubscriptionCostManagementExportExportDataOptionsArgs(
                type="Usage",
                time_frame="WeekToDate",
            ))
        ```

        ## Import

        Subscription Cost Management Exports can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:core/subscriptionCostManagementExport:SubscriptionCostManagementExport example /subscriptions/12345678-1234-9876-4563-123456789012/providers/Microsoft.CostManagement/exports/export1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: Is the cost management export active? Default is `true`.
        :param pulumi.Input[pulumi.InputType['SubscriptionCostManagementExportExportDataOptionsArgs']] export_data_options: A `export_data_options` block as defined below.
        :param pulumi.Input[pulumi.InputType['SubscriptionCostManagementExportExportDataStorageLocationArgs']] export_data_storage_location: A `export_data_storage_location` block as defined below.
        :param pulumi.Input[str] name: Specifies the name of the Cost Management Export. Changing this forces a new resource to be created.
        :param pulumi.Input[str] recurrence_period_end_date: The date the export will stop capturing information.
        :param pulumi.Input[str] recurrence_period_start_date: The date the export will start capturing information.
        :param pulumi.Input[str] recurrence_type: How often the requested information will be exported. Valid values include `Annually`, `Daily`, `Monthly`, `Weekly`.
        :param pulumi.Input[str] subscription_id: The id of the subscription on which to create an export. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubscriptionCostManagementExportArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Cost Management Export for a Subscription.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_subscription = azure.core.get_subscription()
        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_container = azure.storage.Container("exampleContainer", storage_account_name=example_account.name)
        example_subscription_cost_management_export = azure.core.SubscriptionCostManagementExport("exampleSubscriptionCostManagementExport",
            subscription_id=example_subscription.id,
            recurrence_type="Monthly",
            recurrence_period_start_date="2020-08-18T00:00:00Z",
            recurrence_period_end_date="2020-09-18T00:00:00Z",
            export_data_storage_location=azure.core.SubscriptionCostManagementExportExportDataStorageLocationArgs(
                container_id=example_container.resource_manager_id,
                root_folder_path="/root/updated",
            ),
            export_data_options=azure.core.SubscriptionCostManagementExportExportDataOptionsArgs(
                type="Usage",
                time_frame="WeekToDate",
            ))
        ```

        ## Import

        Subscription Cost Management Exports can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:core/subscriptionCostManagementExport:SubscriptionCostManagementExport example /subscriptions/12345678-1234-9876-4563-123456789012/providers/Microsoft.CostManagement/exports/export1
        ```

        :param str resource_name: The name of the resource.
        :param SubscriptionCostManagementExportArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubscriptionCostManagementExportArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SubscriptionCostManagementExportArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 export_data_options: Optional[pulumi.Input[pulumi.InputType['SubscriptionCostManagementExportExportDataOptionsArgs']]] = None,
                 export_data_storage_location: Optional[pulumi.Input[pulumi.InputType['SubscriptionCostManagementExportExportDataStorageLocationArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recurrence_period_end_date: Optional[pulumi.Input[str]] = None,
                 recurrence_period_start_date: Optional[pulumi.Input[str]] = None,
                 recurrence_type: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SubscriptionCostManagementExportArgs.__new__(SubscriptionCostManagementExportArgs)

            __props__.__dict__["active"] = active
            if export_data_options is not None and not isinstance(export_data_options, SubscriptionCostManagementExportExportDataOptionsArgs):
                export_data_options = export_data_options or {}
                def _setter(key, value):
                    export_data_options[key] = value
                SubscriptionCostManagementExportExportDataOptionsArgs._configure(_setter, **export_data_options)
            if export_data_options is None and not opts.urn:
                raise TypeError("Missing required property 'export_data_options'")
            __props__.__dict__["export_data_options"] = export_data_options
            if export_data_storage_location is not None and not isinstance(export_data_storage_location, SubscriptionCostManagementExportExportDataStorageLocationArgs):
                export_data_storage_location = export_data_storage_location or {}
                def _setter(key, value):
                    export_data_storage_location[key] = value
                SubscriptionCostManagementExportExportDataStorageLocationArgs._configure(_setter, **export_data_storage_location)
            if export_data_storage_location is None and not opts.urn:
                raise TypeError("Missing required property 'export_data_storage_location'")
            __props__.__dict__["export_data_storage_location"] = export_data_storage_location
            __props__.__dict__["name"] = name
            if recurrence_period_end_date is None and not opts.urn:
                raise TypeError("Missing required property 'recurrence_period_end_date'")
            __props__.__dict__["recurrence_period_end_date"] = recurrence_period_end_date
            if recurrence_period_start_date is None and not opts.urn:
                raise TypeError("Missing required property 'recurrence_period_start_date'")
            __props__.__dict__["recurrence_period_start_date"] = recurrence_period_start_date
            if recurrence_type is None and not opts.urn:
                raise TypeError("Missing required property 'recurrence_type'")
            __props__.__dict__["recurrence_type"] = recurrence_type
            if subscription_id is None and not opts.urn:
                raise TypeError("Missing required property 'subscription_id'")
            __props__.__dict__["subscription_id"] = subscription_id
        super(SubscriptionCostManagementExport, __self__).__init__(
            'azure:core/subscriptionCostManagementExport:SubscriptionCostManagementExport',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            active: Optional[pulumi.Input[bool]] = None,
            export_data_options: Optional[pulumi.Input[pulumi.InputType['SubscriptionCostManagementExportExportDataOptionsArgs']]] = None,
            export_data_storage_location: Optional[pulumi.Input[pulumi.InputType['SubscriptionCostManagementExportExportDataStorageLocationArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            recurrence_period_end_date: Optional[pulumi.Input[str]] = None,
            recurrence_period_start_date: Optional[pulumi.Input[str]] = None,
            recurrence_type: Optional[pulumi.Input[str]] = None,
            subscription_id: Optional[pulumi.Input[str]] = None) -> 'SubscriptionCostManagementExport':
        """
        Get an existing SubscriptionCostManagementExport resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: Is the cost management export active? Default is `true`.
        :param pulumi.Input[pulumi.InputType['SubscriptionCostManagementExportExportDataOptionsArgs']] export_data_options: A `export_data_options` block as defined below.
        :param pulumi.Input[pulumi.InputType['SubscriptionCostManagementExportExportDataStorageLocationArgs']] export_data_storage_location: A `export_data_storage_location` block as defined below.
        :param pulumi.Input[str] name: Specifies the name of the Cost Management Export. Changing this forces a new resource to be created.
        :param pulumi.Input[str] recurrence_period_end_date: The date the export will stop capturing information.
        :param pulumi.Input[str] recurrence_period_start_date: The date the export will start capturing information.
        :param pulumi.Input[str] recurrence_type: How often the requested information will be exported. Valid values include `Annually`, `Daily`, `Monthly`, `Weekly`.
        :param pulumi.Input[str] subscription_id: The id of the subscription on which to create an export. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SubscriptionCostManagementExportState.__new__(_SubscriptionCostManagementExportState)

        __props__.__dict__["active"] = active
        __props__.__dict__["export_data_options"] = export_data_options
        __props__.__dict__["export_data_storage_location"] = export_data_storage_location
        __props__.__dict__["name"] = name
        __props__.__dict__["recurrence_period_end_date"] = recurrence_period_end_date
        __props__.__dict__["recurrence_period_start_date"] = recurrence_period_start_date
        __props__.__dict__["recurrence_type"] = recurrence_type
        __props__.__dict__["subscription_id"] = subscription_id
        return SubscriptionCostManagementExport(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Output[Optional[bool]]:
        """
        Is the cost management export active? Default is `true`.
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter(name="exportDataOptions")
    def export_data_options(self) -> pulumi.Output['outputs.SubscriptionCostManagementExportExportDataOptions']:
        """
        A `export_data_options` block as defined below.
        """
        return pulumi.get(self, "export_data_options")

    @property
    @pulumi.getter(name="exportDataStorageLocation")
    def export_data_storage_location(self) -> pulumi.Output['outputs.SubscriptionCostManagementExportExportDataStorageLocation']:
        """
        A `export_data_storage_location` block as defined below.
        """
        return pulumi.get(self, "export_data_storage_location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Cost Management Export. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recurrencePeriodEndDate")
    def recurrence_period_end_date(self) -> pulumi.Output[str]:
        """
        The date the export will stop capturing information.
        """
        return pulumi.get(self, "recurrence_period_end_date")

    @property
    @pulumi.getter(name="recurrencePeriodStartDate")
    def recurrence_period_start_date(self) -> pulumi.Output[str]:
        """
        The date the export will start capturing information.
        """
        return pulumi.get(self, "recurrence_period_start_date")

    @property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> pulumi.Output[str]:
        """
        How often the requested information will be exported. Valid values include `Annually`, `Daily`, `Monthly`, `Weekly`.
        """
        return pulumi.get(self, "recurrence_type")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Output[str]:
        """
        The id of the subscription on which to create an export. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "subscription_id")


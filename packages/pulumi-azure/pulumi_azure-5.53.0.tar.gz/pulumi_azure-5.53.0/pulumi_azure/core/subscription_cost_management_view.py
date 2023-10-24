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

__all__ = ['SubscriptionCostManagementViewArgs', 'SubscriptionCostManagementView']

@pulumi.input_type
class SubscriptionCostManagementViewArgs:
    def __init__(__self__, *,
                 accumulated: pulumi.Input[bool],
                 chart_type: pulumi.Input[str],
                 dataset: pulumi.Input['SubscriptionCostManagementViewDatasetArgs'],
                 display_name: pulumi.Input[str],
                 report_type: pulumi.Input[str],
                 subscription_id: pulumi.Input[str],
                 timeframe: pulumi.Input[str],
                 kpis: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewKpiArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pivots: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewPivotArgs']]]] = None):
        """
        The set of arguments for constructing a SubscriptionCostManagementView resource.
        :param pulumi.Input[bool] accumulated: Whether the costs data in the Cost Management View are accumulated over time. Changing this forces a new Cost Management View for a Subscription to be created.
        :param pulumi.Input[str] chart_type: Chart type of the main view in Cost Analysis. Possible values are `Area`, `GroupedColumn`, `Line`, `StackedColumn` and `Table`.
        :param pulumi.Input['SubscriptionCostManagementViewDatasetArgs'] dataset: A `dataset` block as defined below.
        :param pulumi.Input[str] display_name: User visible input name of the Cost Management View.
        :param pulumi.Input[str] report_type: The type of the report. The only possible value is `Usage`.
        :param pulumi.Input[str] subscription_id: The ID of the Subscription this View is scoped to. Changing this forces a new Cost Management View for a Subscription to be created.
        :param pulumi.Input[str] timeframe: The time frame for pulling data for the report. Possible values are `Custom`, `MonthToDate`, `WeekToDate` and `YearToDate`.
        :param pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewKpiArgs']]] kpis: One or more `kpi` blocks as defined below, to show in Cost Analysis UI.
        :param pulumi.Input[str] name: The name which should be used for this Cost Management View for a Subscription. Changing this forces a new Cost Management View for a Subscription to be created.
        :param pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewPivotArgs']]] pivots: One or more `pivot` blocks as defined below, containing the configuration of 3 sub-views in the Cost Analysis UI. Non table views should have three pivots.
        """
        SubscriptionCostManagementViewArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            accumulated=accumulated,
            chart_type=chart_type,
            dataset=dataset,
            display_name=display_name,
            report_type=report_type,
            subscription_id=subscription_id,
            timeframe=timeframe,
            kpis=kpis,
            name=name,
            pivots=pivots,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             accumulated: pulumi.Input[bool],
             chart_type: pulumi.Input[str],
             dataset: pulumi.Input['SubscriptionCostManagementViewDatasetArgs'],
             display_name: pulumi.Input[str],
             report_type: pulumi.Input[str],
             subscription_id: pulumi.Input[str],
             timeframe: pulumi.Input[str],
             kpis: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewKpiArgs']]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             pivots: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewPivotArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'chartType' in kwargs:
            chart_type = kwargs['chartType']
        if 'displayName' in kwargs:
            display_name = kwargs['displayName']
        if 'reportType' in kwargs:
            report_type = kwargs['reportType']
        if 'subscriptionId' in kwargs:
            subscription_id = kwargs['subscriptionId']

        _setter("accumulated", accumulated)
        _setter("chart_type", chart_type)
        _setter("dataset", dataset)
        _setter("display_name", display_name)
        _setter("report_type", report_type)
        _setter("subscription_id", subscription_id)
        _setter("timeframe", timeframe)
        if kpis is not None:
            _setter("kpis", kpis)
        if name is not None:
            _setter("name", name)
        if pivots is not None:
            _setter("pivots", pivots)

    @property
    @pulumi.getter
    def accumulated(self) -> pulumi.Input[bool]:
        """
        Whether the costs data in the Cost Management View are accumulated over time. Changing this forces a new Cost Management View for a Subscription to be created.
        """
        return pulumi.get(self, "accumulated")

    @accumulated.setter
    def accumulated(self, value: pulumi.Input[bool]):
        pulumi.set(self, "accumulated", value)

    @property
    @pulumi.getter(name="chartType")
    def chart_type(self) -> pulumi.Input[str]:
        """
        Chart type of the main view in Cost Analysis. Possible values are `Area`, `GroupedColumn`, `Line`, `StackedColumn` and `Table`.
        """
        return pulumi.get(self, "chart_type")

    @chart_type.setter
    def chart_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "chart_type", value)

    @property
    @pulumi.getter
    def dataset(self) -> pulumi.Input['SubscriptionCostManagementViewDatasetArgs']:
        """
        A `dataset` block as defined below.
        """
        return pulumi.get(self, "dataset")

    @dataset.setter
    def dataset(self, value: pulumi.Input['SubscriptionCostManagementViewDatasetArgs']):
        pulumi.set(self, "dataset", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        User visible input name of the Cost Management View.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="reportType")
    def report_type(self) -> pulumi.Input[str]:
        """
        The type of the report. The only possible value is `Usage`.
        """
        return pulumi.get(self, "report_type")

    @report_type.setter
    def report_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "report_type", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Input[str]:
        """
        The ID of the Subscription this View is scoped to. Changing this forces a new Cost Management View for a Subscription to be created.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subscription_id", value)

    @property
    @pulumi.getter
    def timeframe(self) -> pulumi.Input[str]:
        """
        The time frame for pulling data for the report. Possible values are `Custom`, `MonthToDate`, `WeekToDate` and `YearToDate`.
        """
        return pulumi.get(self, "timeframe")

    @timeframe.setter
    def timeframe(self, value: pulumi.Input[str]):
        pulumi.set(self, "timeframe", value)

    @property
    @pulumi.getter
    def kpis(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewKpiArgs']]]]:
        """
        One or more `kpi` blocks as defined below, to show in Cost Analysis UI.
        """
        return pulumi.get(self, "kpis")

    @kpis.setter
    def kpis(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewKpiArgs']]]]):
        pulumi.set(self, "kpis", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Cost Management View for a Subscription. Changing this forces a new Cost Management View for a Subscription to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def pivots(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewPivotArgs']]]]:
        """
        One or more `pivot` blocks as defined below, containing the configuration of 3 sub-views in the Cost Analysis UI. Non table views should have three pivots.
        """
        return pulumi.get(self, "pivots")

    @pivots.setter
    def pivots(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewPivotArgs']]]]):
        pulumi.set(self, "pivots", value)


@pulumi.input_type
class _SubscriptionCostManagementViewState:
    def __init__(__self__, *,
                 accumulated: Optional[pulumi.Input[bool]] = None,
                 chart_type: Optional[pulumi.Input[str]] = None,
                 dataset: Optional[pulumi.Input['SubscriptionCostManagementViewDatasetArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 kpis: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewKpiArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pivots: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewPivotArgs']]]] = None,
                 report_type: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 timeframe: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SubscriptionCostManagementView resources.
        :param pulumi.Input[bool] accumulated: Whether the costs data in the Cost Management View are accumulated over time. Changing this forces a new Cost Management View for a Subscription to be created.
        :param pulumi.Input[str] chart_type: Chart type of the main view in Cost Analysis. Possible values are `Area`, `GroupedColumn`, `Line`, `StackedColumn` and `Table`.
        :param pulumi.Input['SubscriptionCostManagementViewDatasetArgs'] dataset: A `dataset` block as defined below.
        :param pulumi.Input[str] display_name: User visible input name of the Cost Management View.
        :param pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewKpiArgs']]] kpis: One or more `kpi` blocks as defined below, to show in Cost Analysis UI.
        :param pulumi.Input[str] name: The name which should be used for this Cost Management View for a Subscription. Changing this forces a new Cost Management View for a Subscription to be created.
        :param pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewPivotArgs']]] pivots: One or more `pivot` blocks as defined below, containing the configuration of 3 sub-views in the Cost Analysis UI. Non table views should have three pivots.
        :param pulumi.Input[str] report_type: The type of the report. The only possible value is `Usage`.
        :param pulumi.Input[str] subscription_id: The ID of the Subscription this View is scoped to. Changing this forces a new Cost Management View for a Subscription to be created.
        :param pulumi.Input[str] timeframe: The time frame for pulling data for the report. Possible values are `Custom`, `MonthToDate`, `WeekToDate` and `YearToDate`.
        """
        _SubscriptionCostManagementViewState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            accumulated=accumulated,
            chart_type=chart_type,
            dataset=dataset,
            display_name=display_name,
            kpis=kpis,
            name=name,
            pivots=pivots,
            report_type=report_type,
            subscription_id=subscription_id,
            timeframe=timeframe,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             accumulated: Optional[pulumi.Input[bool]] = None,
             chart_type: Optional[pulumi.Input[str]] = None,
             dataset: Optional[pulumi.Input['SubscriptionCostManagementViewDatasetArgs']] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             kpis: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewKpiArgs']]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             pivots: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewPivotArgs']]]] = None,
             report_type: Optional[pulumi.Input[str]] = None,
             subscription_id: Optional[pulumi.Input[str]] = None,
             timeframe: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'chartType' in kwargs:
            chart_type = kwargs['chartType']
        if 'displayName' in kwargs:
            display_name = kwargs['displayName']
        if 'reportType' in kwargs:
            report_type = kwargs['reportType']
        if 'subscriptionId' in kwargs:
            subscription_id = kwargs['subscriptionId']

        if accumulated is not None:
            _setter("accumulated", accumulated)
        if chart_type is not None:
            _setter("chart_type", chart_type)
        if dataset is not None:
            _setter("dataset", dataset)
        if display_name is not None:
            _setter("display_name", display_name)
        if kpis is not None:
            _setter("kpis", kpis)
        if name is not None:
            _setter("name", name)
        if pivots is not None:
            _setter("pivots", pivots)
        if report_type is not None:
            _setter("report_type", report_type)
        if subscription_id is not None:
            _setter("subscription_id", subscription_id)
        if timeframe is not None:
            _setter("timeframe", timeframe)

    @property
    @pulumi.getter
    def accumulated(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the costs data in the Cost Management View are accumulated over time. Changing this forces a new Cost Management View for a Subscription to be created.
        """
        return pulumi.get(self, "accumulated")

    @accumulated.setter
    def accumulated(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "accumulated", value)

    @property
    @pulumi.getter(name="chartType")
    def chart_type(self) -> Optional[pulumi.Input[str]]:
        """
        Chart type of the main view in Cost Analysis. Possible values are `Area`, `GroupedColumn`, `Line`, `StackedColumn` and `Table`.
        """
        return pulumi.get(self, "chart_type")

    @chart_type.setter
    def chart_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "chart_type", value)

    @property
    @pulumi.getter
    def dataset(self) -> Optional[pulumi.Input['SubscriptionCostManagementViewDatasetArgs']]:
        """
        A `dataset` block as defined below.
        """
        return pulumi.get(self, "dataset")

    @dataset.setter
    def dataset(self, value: Optional[pulumi.Input['SubscriptionCostManagementViewDatasetArgs']]):
        pulumi.set(self, "dataset", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        User visible input name of the Cost Management View.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def kpis(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewKpiArgs']]]]:
        """
        One or more `kpi` blocks as defined below, to show in Cost Analysis UI.
        """
        return pulumi.get(self, "kpis")

    @kpis.setter
    def kpis(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewKpiArgs']]]]):
        pulumi.set(self, "kpis", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Cost Management View for a Subscription. Changing this forces a new Cost Management View for a Subscription to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def pivots(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewPivotArgs']]]]:
        """
        One or more `pivot` blocks as defined below, containing the configuration of 3 sub-views in the Cost Analysis UI. Non table views should have three pivots.
        """
        return pulumi.get(self, "pivots")

    @pivots.setter
    def pivots(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriptionCostManagementViewPivotArgs']]]]):
        pulumi.set(self, "pivots", value)

    @property
    @pulumi.getter(name="reportType")
    def report_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the report. The only possible value is `Usage`.
        """
        return pulumi.get(self, "report_type")

    @report_type.setter
    def report_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "report_type", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Subscription this View is scoped to. Changing this forces a new Cost Management View for a Subscription to be created.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)

    @property
    @pulumi.getter
    def timeframe(self) -> Optional[pulumi.Input[str]]:
        """
        The time frame for pulling data for the report. Possible values are `Custom`, `MonthToDate`, `WeekToDate` and `YearToDate`.
        """
        return pulumi.get(self, "timeframe")

    @timeframe.setter
    def timeframe(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timeframe", value)


class SubscriptionCostManagementView(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accumulated: Optional[pulumi.Input[bool]] = None,
                 chart_type: Optional[pulumi.Input[str]] = None,
                 dataset: Optional[pulumi.Input[pulumi.InputType['SubscriptionCostManagementViewDatasetArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 kpis: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriptionCostManagementViewKpiArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pivots: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriptionCostManagementViewPivotArgs']]]]] = None,
                 report_type: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 timeframe: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an Azure Cost Management View for a Subscription.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.SubscriptionCostManagementView("example",
            accumulated=False,
            chart_type="StackedColumn",
            dataset=azure.core.SubscriptionCostManagementViewDatasetArgs(
                aggregations=[azure.core.SubscriptionCostManagementViewDatasetAggregationArgs(
                    column_name="Cost",
                    name="totalCost",
                )],
                granularity="Monthly",
            ),
            display_name="Cost View per Month",
            report_type="Usage",
            subscription_id="/subscription/00000000-0000-0000-0000-000000000000",
            timeframe="MonthToDate")
        ```

        ## Import

        Cost Management View for a Subscriptions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:core/subscriptionCostManagementView:SubscriptionCostManagementView example /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.CostManagement/views/costmanagementview
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] accumulated: Whether the costs data in the Cost Management View are accumulated over time. Changing this forces a new Cost Management View for a Subscription to be created.
        :param pulumi.Input[str] chart_type: Chart type of the main view in Cost Analysis. Possible values are `Area`, `GroupedColumn`, `Line`, `StackedColumn` and `Table`.
        :param pulumi.Input[pulumi.InputType['SubscriptionCostManagementViewDatasetArgs']] dataset: A `dataset` block as defined below.
        :param pulumi.Input[str] display_name: User visible input name of the Cost Management View.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriptionCostManagementViewKpiArgs']]]] kpis: One or more `kpi` blocks as defined below, to show in Cost Analysis UI.
        :param pulumi.Input[str] name: The name which should be used for this Cost Management View for a Subscription. Changing this forces a new Cost Management View for a Subscription to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriptionCostManagementViewPivotArgs']]]] pivots: One or more `pivot` blocks as defined below, containing the configuration of 3 sub-views in the Cost Analysis UI. Non table views should have three pivots.
        :param pulumi.Input[str] report_type: The type of the report. The only possible value is `Usage`.
        :param pulumi.Input[str] subscription_id: The ID of the Subscription this View is scoped to. Changing this forces a new Cost Management View for a Subscription to be created.
        :param pulumi.Input[str] timeframe: The time frame for pulling data for the report. Possible values are `Custom`, `MonthToDate`, `WeekToDate` and `YearToDate`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubscriptionCostManagementViewArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Azure Cost Management View for a Subscription.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.SubscriptionCostManagementView("example",
            accumulated=False,
            chart_type="StackedColumn",
            dataset=azure.core.SubscriptionCostManagementViewDatasetArgs(
                aggregations=[azure.core.SubscriptionCostManagementViewDatasetAggregationArgs(
                    column_name="Cost",
                    name="totalCost",
                )],
                granularity="Monthly",
            ),
            display_name="Cost View per Month",
            report_type="Usage",
            subscription_id="/subscription/00000000-0000-0000-0000-000000000000",
            timeframe="MonthToDate")
        ```

        ## Import

        Cost Management View for a Subscriptions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:core/subscriptionCostManagementView:SubscriptionCostManagementView example /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.CostManagement/views/costmanagementview
        ```

        :param str resource_name: The name of the resource.
        :param SubscriptionCostManagementViewArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubscriptionCostManagementViewArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SubscriptionCostManagementViewArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accumulated: Optional[pulumi.Input[bool]] = None,
                 chart_type: Optional[pulumi.Input[str]] = None,
                 dataset: Optional[pulumi.Input[pulumi.InputType['SubscriptionCostManagementViewDatasetArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 kpis: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriptionCostManagementViewKpiArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pivots: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriptionCostManagementViewPivotArgs']]]]] = None,
                 report_type: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 timeframe: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SubscriptionCostManagementViewArgs.__new__(SubscriptionCostManagementViewArgs)

            if accumulated is None and not opts.urn:
                raise TypeError("Missing required property 'accumulated'")
            __props__.__dict__["accumulated"] = accumulated
            if chart_type is None and not opts.urn:
                raise TypeError("Missing required property 'chart_type'")
            __props__.__dict__["chart_type"] = chart_type
            if dataset is not None and not isinstance(dataset, SubscriptionCostManagementViewDatasetArgs):
                dataset = dataset or {}
                def _setter(key, value):
                    dataset[key] = value
                SubscriptionCostManagementViewDatasetArgs._configure(_setter, **dataset)
            if dataset is None and not opts.urn:
                raise TypeError("Missing required property 'dataset'")
            __props__.__dict__["dataset"] = dataset
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["kpis"] = kpis
            __props__.__dict__["name"] = name
            __props__.__dict__["pivots"] = pivots
            if report_type is None and not opts.urn:
                raise TypeError("Missing required property 'report_type'")
            __props__.__dict__["report_type"] = report_type
            if subscription_id is None and not opts.urn:
                raise TypeError("Missing required property 'subscription_id'")
            __props__.__dict__["subscription_id"] = subscription_id
            if timeframe is None and not opts.urn:
                raise TypeError("Missing required property 'timeframe'")
            __props__.__dict__["timeframe"] = timeframe
        super(SubscriptionCostManagementView, __self__).__init__(
            'azure:core/subscriptionCostManagementView:SubscriptionCostManagementView',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accumulated: Optional[pulumi.Input[bool]] = None,
            chart_type: Optional[pulumi.Input[str]] = None,
            dataset: Optional[pulumi.Input[pulumi.InputType['SubscriptionCostManagementViewDatasetArgs']]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            kpis: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriptionCostManagementViewKpiArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            pivots: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriptionCostManagementViewPivotArgs']]]]] = None,
            report_type: Optional[pulumi.Input[str]] = None,
            subscription_id: Optional[pulumi.Input[str]] = None,
            timeframe: Optional[pulumi.Input[str]] = None) -> 'SubscriptionCostManagementView':
        """
        Get an existing SubscriptionCostManagementView resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] accumulated: Whether the costs data in the Cost Management View are accumulated over time. Changing this forces a new Cost Management View for a Subscription to be created.
        :param pulumi.Input[str] chart_type: Chart type of the main view in Cost Analysis. Possible values are `Area`, `GroupedColumn`, `Line`, `StackedColumn` and `Table`.
        :param pulumi.Input[pulumi.InputType['SubscriptionCostManagementViewDatasetArgs']] dataset: A `dataset` block as defined below.
        :param pulumi.Input[str] display_name: User visible input name of the Cost Management View.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriptionCostManagementViewKpiArgs']]]] kpis: One or more `kpi` blocks as defined below, to show in Cost Analysis UI.
        :param pulumi.Input[str] name: The name which should be used for this Cost Management View for a Subscription. Changing this forces a new Cost Management View for a Subscription to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriptionCostManagementViewPivotArgs']]]] pivots: One or more `pivot` blocks as defined below, containing the configuration of 3 sub-views in the Cost Analysis UI. Non table views should have three pivots.
        :param pulumi.Input[str] report_type: The type of the report. The only possible value is `Usage`.
        :param pulumi.Input[str] subscription_id: The ID of the Subscription this View is scoped to. Changing this forces a new Cost Management View for a Subscription to be created.
        :param pulumi.Input[str] timeframe: The time frame for pulling data for the report. Possible values are `Custom`, `MonthToDate`, `WeekToDate` and `YearToDate`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SubscriptionCostManagementViewState.__new__(_SubscriptionCostManagementViewState)

        __props__.__dict__["accumulated"] = accumulated
        __props__.__dict__["chart_type"] = chart_type
        __props__.__dict__["dataset"] = dataset
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["kpis"] = kpis
        __props__.__dict__["name"] = name
        __props__.__dict__["pivots"] = pivots
        __props__.__dict__["report_type"] = report_type
        __props__.__dict__["subscription_id"] = subscription_id
        __props__.__dict__["timeframe"] = timeframe
        return SubscriptionCostManagementView(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def accumulated(self) -> pulumi.Output[bool]:
        """
        Whether the costs data in the Cost Management View are accumulated over time. Changing this forces a new Cost Management View for a Subscription to be created.
        """
        return pulumi.get(self, "accumulated")

    @property
    @pulumi.getter(name="chartType")
    def chart_type(self) -> pulumi.Output[str]:
        """
        Chart type of the main view in Cost Analysis. Possible values are `Area`, `GroupedColumn`, `Line`, `StackedColumn` and `Table`.
        """
        return pulumi.get(self, "chart_type")

    @property
    @pulumi.getter
    def dataset(self) -> pulumi.Output['outputs.SubscriptionCostManagementViewDataset']:
        """
        A `dataset` block as defined below.
        """
        return pulumi.get(self, "dataset")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        User visible input name of the Cost Management View.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def kpis(self) -> pulumi.Output[Optional[Sequence['outputs.SubscriptionCostManagementViewKpi']]]:
        """
        One or more `kpi` blocks as defined below, to show in Cost Analysis UI.
        """
        return pulumi.get(self, "kpis")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Cost Management View for a Subscription. Changing this forces a new Cost Management View for a Subscription to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def pivots(self) -> pulumi.Output[Optional[Sequence['outputs.SubscriptionCostManagementViewPivot']]]:
        """
        One or more `pivot` blocks as defined below, containing the configuration of 3 sub-views in the Cost Analysis UI. Non table views should have three pivots.
        """
        return pulumi.get(self, "pivots")

    @property
    @pulumi.getter(name="reportType")
    def report_type(self) -> pulumi.Output[str]:
        """
        The type of the report. The only possible value is `Usage`.
        """
        return pulumi.get(self, "report_type")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Output[str]:
        """
        The ID of the Subscription this View is scoped to. Changing this forces a new Cost Management View for a Subscription to be created.
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter
    def timeframe(self) -> pulumi.Output[str]:
        """
        The time frame for pulling data for the report. Possible values are `Custom`, `MonthToDate`, `WeekToDate` and `YearToDate`.
        """
        return pulumi.get(self, "timeframe")


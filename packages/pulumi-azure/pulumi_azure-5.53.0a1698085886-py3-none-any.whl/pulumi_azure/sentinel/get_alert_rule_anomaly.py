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
    'GetAlertRuleAnomalyResult',
    'AwaitableGetAlertRuleAnomalyResult',
    'get_alert_rule_anomaly',
    'get_alert_rule_anomaly_output',
]

@pulumi.output_type
class GetAlertRuleAnomalyResult:
    """
    A collection of values returned by getAlertRuleAnomaly.
    """
    def __init__(__self__, anomaly_settings_version=None, anomaly_version=None, description=None, display_name=None, enabled=None, frequency=None, id=None, log_analytics_workspace_id=None, mode=None, multi_select_observations=None, name=None, prioritized_exclude_observations=None, required_data_connectors=None, settings_definition_id=None, single_select_observations=None, tactics=None, techniques=None, threshold_observations=None):
        if anomaly_settings_version and not isinstance(anomaly_settings_version, int):
            raise TypeError("Expected argument 'anomaly_settings_version' to be a int")
        pulumi.set(__self__, "anomaly_settings_version", anomaly_settings_version)
        if anomaly_version and not isinstance(anomaly_version, str):
            raise TypeError("Expected argument 'anomaly_version' to be a str")
        pulumi.set(__self__, "anomaly_version", anomaly_version)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if frequency and not isinstance(frequency, str):
            raise TypeError("Expected argument 'frequency' to be a str")
        pulumi.set(__self__, "frequency", frequency)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if log_analytics_workspace_id and not isinstance(log_analytics_workspace_id, str):
            raise TypeError("Expected argument 'log_analytics_workspace_id' to be a str")
        pulumi.set(__self__, "log_analytics_workspace_id", log_analytics_workspace_id)
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        pulumi.set(__self__, "mode", mode)
        if multi_select_observations and not isinstance(multi_select_observations, list):
            raise TypeError("Expected argument 'multi_select_observations' to be a list")
        pulumi.set(__self__, "multi_select_observations", multi_select_observations)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if prioritized_exclude_observations and not isinstance(prioritized_exclude_observations, list):
            raise TypeError("Expected argument 'prioritized_exclude_observations' to be a list")
        pulumi.set(__self__, "prioritized_exclude_observations", prioritized_exclude_observations)
        if required_data_connectors and not isinstance(required_data_connectors, list):
            raise TypeError("Expected argument 'required_data_connectors' to be a list")
        pulumi.set(__self__, "required_data_connectors", required_data_connectors)
        if settings_definition_id and not isinstance(settings_definition_id, str):
            raise TypeError("Expected argument 'settings_definition_id' to be a str")
        pulumi.set(__self__, "settings_definition_id", settings_definition_id)
        if single_select_observations and not isinstance(single_select_observations, list):
            raise TypeError("Expected argument 'single_select_observations' to be a list")
        pulumi.set(__self__, "single_select_observations", single_select_observations)
        if tactics and not isinstance(tactics, list):
            raise TypeError("Expected argument 'tactics' to be a list")
        pulumi.set(__self__, "tactics", tactics)
        if techniques and not isinstance(techniques, list):
            raise TypeError("Expected argument 'techniques' to be a list")
        pulumi.set(__self__, "techniques", techniques)
        if threshold_observations and not isinstance(threshold_observations, list):
            raise TypeError("Expected argument 'threshold_observations' to be a list")
        pulumi.set(__self__, "threshold_observations", threshold_observations)

    @property
    @pulumi.getter(name="anomalySettingsVersion")
    def anomaly_settings_version(self) -> int:
        """
        The version of the Anomaly Security ML Analytics Settings.
        """
        return pulumi.get(self, "anomaly_settings_version")

    @property
    @pulumi.getter(name="anomalyVersion")
    def anomaly_version(self) -> str:
        """
        The anomaly version of the Anomaly Alert Rule.
        """
        return pulumi.get(self, "anomaly_version")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the threshold observation.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Is the Anomaly Alert Rule enabled?
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def frequency(self) -> str:
        """
        The frequency the Anomaly Alert Rule will be run.
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> str:
        return pulumi.get(self, "log_analytics_workspace_id")

    @property
    @pulumi.getter
    def mode(self) -> str:
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter(name="multiSelectObservations")
    def multi_select_observations(self) -> Sequence['outputs.GetAlertRuleAnomalyMultiSelectObservationResult']:
        """
        A list of `multi_select_observation` blocks as defined below.
        """
        return pulumi.get(self, "multi_select_observations")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the threshold observation.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="prioritizedExcludeObservations")
    def prioritized_exclude_observations(self) -> Sequence['outputs.GetAlertRuleAnomalyPrioritizedExcludeObservationResult']:
        """
        A list of `prioritized_exclude_observation` blocks as defined below.
        """
        return pulumi.get(self, "prioritized_exclude_observations")

    @property
    @pulumi.getter(name="requiredDataConnectors")
    def required_data_connectors(self) -> Sequence['outputs.GetAlertRuleAnomalyRequiredDataConnectorResult']:
        """
        A `required_data_connector` block as defined below.
        """
        return pulumi.get(self, "required_data_connectors")

    @property
    @pulumi.getter(name="settingsDefinitionId")
    def settings_definition_id(self) -> str:
        """
        The ID of the anomaly settings definition Id.
        """
        return pulumi.get(self, "settings_definition_id")

    @property
    @pulumi.getter(name="singleSelectObservations")
    def single_select_observations(self) -> Sequence['outputs.GetAlertRuleAnomalySingleSelectObservationResult']:
        """
        A list of `single_select_observation` blocks as defined below.
        """
        return pulumi.get(self, "single_select_observations")

    @property
    @pulumi.getter
    def tactics(self) -> Sequence[str]:
        """
        A list of categories of attacks by which to classify the rule.
        """
        return pulumi.get(self, "tactics")

    @property
    @pulumi.getter
    def techniques(self) -> Sequence[str]:
        """
        A list of techniques of attacks by which to classify the rule.
        """
        return pulumi.get(self, "techniques")

    @property
    @pulumi.getter(name="thresholdObservations")
    def threshold_observations(self) -> Sequence['outputs.GetAlertRuleAnomalyThresholdObservationResult']:
        """
        A list of `threshold_observation` blocks as defined below.
        """
        return pulumi.get(self, "threshold_observations")


class AwaitableGetAlertRuleAnomalyResult(GetAlertRuleAnomalyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAlertRuleAnomalyResult(
            anomaly_settings_version=self.anomaly_settings_version,
            anomaly_version=self.anomaly_version,
            description=self.description,
            display_name=self.display_name,
            enabled=self.enabled,
            frequency=self.frequency,
            id=self.id,
            log_analytics_workspace_id=self.log_analytics_workspace_id,
            mode=self.mode,
            multi_select_observations=self.multi_select_observations,
            name=self.name,
            prioritized_exclude_observations=self.prioritized_exclude_observations,
            required_data_connectors=self.required_data_connectors,
            settings_definition_id=self.settings_definition_id,
            single_select_observations=self.single_select_observations,
            tactics=self.tactics,
            techniques=self.techniques,
            threshold_observations=self.threshold_observations)


def get_alert_rule_anomaly(display_name: Optional[str] = None,
                           log_analytics_workspace_id: Optional[str] = None,
                           name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAlertRuleAnomalyResult:
    """
    Use this data source to access information about an existing Anomaly Alert Rule.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
    example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace",
        location=example_resource_group.location,
        resource_group_name=example_resource_group.name,
        sku="PerGB2018")
    example_log_analytics_workspace_onboarding = azure.sentinel.LogAnalyticsWorkspaceOnboarding("exampleLogAnalyticsWorkspaceOnboarding",
        workspace_id=example_analytics_workspace.id,
        customer_managed_key_enabled=False)
    example_alert_rule_anomaly = azure.sentinel.get_alert_rule_anomaly_output(log_analytics_workspace_id=example_log_analytics_workspace_onboarding.workspace_id,
        display_name="Potential data staging")
    pulumi.export("id", example_alert_rule_anomaly.id)
    ```


    :param str display_name: The display name of this Sentinel Alert Rule Template. Either `display_name` or `name` have to be specified.
           
           > **NOTE** One of `name` or `display_name` must be specified.
    :param str log_analytics_workspace_id: The ID of the Log Analytics Workspace.
    :param str name: The guid of this Sentinel Alert Rule Template. Either `display_name` or `name` have to be specified.
    """
    __args__ = dict()
    __args__['displayName'] = display_name
    __args__['logAnalyticsWorkspaceId'] = log_analytics_workspace_id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:sentinel/getAlertRuleAnomaly:getAlertRuleAnomaly', __args__, opts=opts, typ=GetAlertRuleAnomalyResult).value

    return AwaitableGetAlertRuleAnomalyResult(
        anomaly_settings_version=pulumi.get(__ret__, 'anomaly_settings_version'),
        anomaly_version=pulumi.get(__ret__, 'anomaly_version'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        enabled=pulumi.get(__ret__, 'enabled'),
        frequency=pulumi.get(__ret__, 'frequency'),
        id=pulumi.get(__ret__, 'id'),
        log_analytics_workspace_id=pulumi.get(__ret__, 'log_analytics_workspace_id'),
        mode=pulumi.get(__ret__, 'mode'),
        multi_select_observations=pulumi.get(__ret__, 'multi_select_observations'),
        name=pulumi.get(__ret__, 'name'),
        prioritized_exclude_observations=pulumi.get(__ret__, 'prioritized_exclude_observations'),
        required_data_connectors=pulumi.get(__ret__, 'required_data_connectors'),
        settings_definition_id=pulumi.get(__ret__, 'settings_definition_id'),
        single_select_observations=pulumi.get(__ret__, 'single_select_observations'),
        tactics=pulumi.get(__ret__, 'tactics'),
        techniques=pulumi.get(__ret__, 'techniques'),
        threshold_observations=pulumi.get(__ret__, 'threshold_observations'))


@_utilities.lift_output_func(get_alert_rule_anomaly)
def get_alert_rule_anomaly_output(display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                  log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
                                  name: Optional[pulumi.Input[Optional[str]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAlertRuleAnomalyResult]:
    """
    Use this data source to access information about an existing Anomaly Alert Rule.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
    example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace",
        location=example_resource_group.location,
        resource_group_name=example_resource_group.name,
        sku="PerGB2018")
    example_log_analytics_workspace_onboarding = azure.sentinel.LogAnalyticsWorkspaceOnboarding("exampleLogAnalyticsWorkspaceOnboarding",
        workspace_id=example_analytics_workspace.id,
        customer_managed_key_enabled=False)
    example_alert_rule_anomaly = azure.sentinel.get_alert_rule_anomaly_output(log_analytics_workspace_id=example_log_analytics_workspace_onboarding.workspace_id,
        display_name="Potential data staging")
    pulumi.export("id", example_alert_rule_anomaly.id)
    ```


    :param str display_name: The display name of this Sentinel Alert Rule Template. Either `display_name` or `name` have to be specified.
           
           > **NOTE** One of `name` or `display_name` must be specified.
    :param str log_analytics_workspace_id: The ID of the Log Analytics Workspace.
    :param str name: The guid of this Sentinel Alert Rule Template. Either `display_name` or `name` have to be specified.
    """
    ...

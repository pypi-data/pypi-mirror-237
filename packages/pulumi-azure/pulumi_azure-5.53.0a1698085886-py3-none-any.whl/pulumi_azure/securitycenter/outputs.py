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
    'AssessmentStatus',
    'AutomationAction',
    'AutomationSource',
    'AutomationSourceRuleSet',
    'AutomationSourceRuleSetRule',
    'SubscriptionPricingExtension',
]

@pulumi.output_type
class AssessmentStatus(dict):
    def __init__(__self__, *,
                 code: str,
                 cause: Optional[str] = None,
                 description: Optional[str] = None):
        """
        :param str code: Specifies the programmatic code of the assessment status. Possible values are `Healthy`, `Unhealthy` and `NotApplicable`.
        :param str cause: Specifies the cause of the assessment status.
        :param str description: Specifies the human readable description of the assessment status.
        """
        AssessmentStatus._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            code=code,
            cause=cause,
            description=description,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             code: str,
             cause: Optional[str] = None,
             description: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        _setter("code", code)
        if cause is not None:
            _setter("cause", cause)
        if description is not None:
            _setter("description", description)

    @property
    @pulumi.getter
    def code(self) -> str:
        """
        Specifies the programmatic code of the assessment status. Possible values are `Healthy`, `Unhealthy` and `NotApplicable`.
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter
    def cause(self) -> Optional[str]:
        """
        Specifies the cause of the assessment status.
        """
        return pulumi.get(self, "cause")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Specifies the human readable description of the assessment status.
        """
        return pulumi.get(self, "description")


@pulumi.output_type
class AutomationAction(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "resourceId":
            suggest = "resource_id"
        elif key == "connectionString":
            suggest = "connection_string"
        elif key == "triggerUrl":
            suggest = "trigger_url"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AutomationAction. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AutomationAction.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AutomationAction.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 resource_id: str,
                 type: str,
                 connection_string: Optional[str] = None,
                 trigger_url: Optional[str] = None):
        """
        :param str resource_id: The resource id of the target Logic App, Event Hub namespace or Log Analytics workspace.
        :param str type: Type of Azure resource to send data to. Must be set to one of: `LogicApp`, `EventHub` or `LogAnalytics`.
        :param str connection_string: (Optional, but required when `type` is `EventHub`) A connection string to send data to the target Event Hub namespace, this should include a key with send permissions.
        :param str trigger_url: (Optional, but required when `type` is `LogicApp`) The callback URL to trigger the Logic App that will receive and process data sent by this automation. This can be found in the Azure Portal under "See trigger history"
        """
        AutomationAction._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            resource_id=resource_id,
            type=type,
            connection_string=connection_string,
            trigger_url=trigger_url,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             resource_id: str,
             type: str,
             connection_string: Optional[str] = None,
             trigger_url: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'resourceId' in kwargs:
            resource_id = kwargs['resourceId']
        if 'connectionString' in kwargs:
            connection_string = kwargs['connectionString']
        if 'triggerUrl' in kwargs:
            trigger_url = kwargs['triggerUrl']

        _setter("resource_id", resource_id)
        _setter("type", type)
        if connection_string is not None:
            _setter("connection_string", connection_string)
        if trigger_url is not None:
            _setter("trigger_url", trigger_url)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> str:
        """
        The resource id of the target Logic App, Event Hub namespace or Log Analytics workspace.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of Azure resource to send data to. Must be set to one of: `LogicApp`, `EventHub` or `LogAnalytics`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[str]:
        """
        (Optional, but required when `type` is `EventHub`) A connection string to send data to the target Event Hub namespace, this should include a key with send permissions.
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter(name="triggerUrl")
    def trigger_url(self) -> Optional[str]:
        """
        (Optional, but required when `type` is `LogicApp`) The callback URL to trigger the Logic App that will receive and process data sent by this automation. This can be found in the Azure Portal under "See trigger history"
        """
        return pulumi.get(self, "trigger_url")


@pulumi.output_type
class AutomationSource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "eventSource":
            suggest = "event_source"
        elif key == "ruleSets":
            suggest = "rule_sets"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AutomationSource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AutomationSource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AutomationSource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 event_source: str,
                 rule_sets: Optional[Sequence['outputs.AutomationSourceRuleSet']] = None):
        """
        :param str event_source: Type of data that will trigger this automation. Must be one of `Alerts`, `Assessments`, `AssessmentsSnapshot`, `RegulatoryComplianceAssessment`, `RegulatoryComplianceAssessmentSnapshot`, `SecureScoreControls`, `SecureScoreControlsSnapshot`, `SecureScores`, `SecureScoresSnapshot`, `SubAssessments` or `SubAssessmentsSnapshot`. Note. assessments are also referred to as recommendations
        :param Sequence['AutomationSourceRuleSetArgs'] rule_sets: A set of rules which evaluate upon event and data interception. This is defined in one or more `rule_set` blocks as defined below.
               
               > **NOTE:** When multiple `rule_set` block are provided, a logical 'OR' is applied to the evaluation of them.
        """
        AutomationSource._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            event_source=event_source,
            rule_sets=rule_sets,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             event_source: str,
             rule_sets: Optional[Sequence['outputs.AutomationSourceRuleSet']] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'eventSource' in kwargs:
            event_source = kwargs['eventSource']
        if 'ruleSets' in kwargs:
            rule_sets = kwargs['ruleSets']

        _setter("event_source", event_source)
        if rule_sets is not None:
            _setter("rule_sets", rule_sets)

    @property
    @pulumi.getter(name="eventSource")
    def event_source(self) -> str:
        """
        Type of data that will trigger this automation. Must be one of `Alerts`, `Assessments`, `AssessmentsSnapshot`, `RegulatoryComplianceAssessment`, `RegulatoryComplianceAssessmentSnapshot`, `SecureScoreControls`, `SecureScoreControlsSnapshot`, `SecureScores`, `SecureScoresSnapshot`, `SubAssessments` or `SubAssessmentsSnapshot`. Note. assessments are also referred to as recommendations
        """
        return pulumi.get(self, "event_source")

    @property
    @pulumi.getter(name="ruleSets")
    def rule_sets(self) -> Optional[Sequence['outputs.AutomationSourceRuleSet']]:
        """
        A set of rules which evaluate upon event and data interception. This is defined in one or more `rule_set` blocks as defined below.

        > **NOTE:** When multiple `rule_set` block are provided, a logical 'OR' is applied to the evaluation of them.
        """
        return pulumi.get(self, "rule_sets")


@pulumi.output_type
class AutomationSourceRuleSet(dict):
    def __init__(__self__, *,
                 rules: Sequence['outputs.AutomationSourceRuleSetRule']):
        """
        :param Sequence['AutomationSourceRuleSetRuleArgs'] rules: One or more `rule` blocks as defined below.
               
               > **NOTE:** This automation will trigger when all of the `rule`s in this `rule_set` are evaluated as 'true'. This is equivalent to a logical 'AND'.
        """
        AutomationSourceRuleSet._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            rules=rules,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             rules: Sequence['outputs.AutomationSourceRuleSetRule'],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        _setter("rules", rules)

    @property
    @pulumi.getter
    def rules(self) -> Sequence['outputs.AutomationSourceRuleSetRule']:
        """
        One or more `rule` blocks as defined below.

        > **NOTE:** This automation will trigger when all of the `rule`s in this `rule_set` are evaluated as 'true'. This is equivalent to a logical 'AND'.
        """
        return pulumi.get(self, "rules")


@pulumi.output_type
class AutomationSourceRuleSetRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "expectedValue":
            suggest = "expected_value"
        elif key == "propertyPath":
            suggest = "property_path"
        elif key == "propertyType":
            suggest = "property_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AutomationSourceRuleSetRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AutomationSourceRuleSetRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AutomationSourceRuleSetRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 expected_value: str,
                 operator: str,
                 property_path: str,
                 property_type: str):
        """
        :param str expected_value: A value that will be compared with the value in `property_path`.
        :param str operator: The comparison operator to use, must be one of: `Contains`, `EndsWith`, `Equals`, `GreaterThan`, `GreaterThanOrEqualTo`, `LesserThan`, `LesserThanOrEqualTo`, `NotEquals`, `StartsWith`
        :param str property_path: The JPath of the entity model property that should be checked.
        :param str property_type: The data type of the compared operands, must be one of: `Integer`, `String`, `Boolean` or `Number`.
               
               > **NOTE:** The schema for Security Center alerts (when `event_source` is "Alerts") [can be found here](https://docs.microsoft.com/azure/security-center/alerts-schemas?tabs=schema-continuousexport)
        """
        AutomationSourceRuleSetRule._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            expected_value=expected_value,
            operator=operator,
            property_path=property_path,
            property_type=property_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             expected_value: str,
             operator: str,
             property_path: str,
             property_type: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'expectedValue' in kwargs:
            expected_value = kwargs['expectedValue']
        if 'propertyPath' in kwargs:
            property_path = kwargs['propertyPath']
        if 'propertyType' in kwargs:
            property_type = kwargs['propertyType']

        _setter("expected_value", expected_value)
        _setter("operator", operator)
        _setter("property_path", property_path)
        _setter("property_type", property_type)

    @property
    @pulumi.getter(name="expectedValue")
    def expected_value(self) -> str:
        """
        A value that will be compared with the value in `property_path`.
        """
        return pulumi.get(self, "expected_value")

    @property
    @pulumi.getter
    def operator(self) -> str:
        """
        The comparison operator to use, must be one of: `Contains`, `EndsWith`, `Equals`, `GreaterThan`, `GreaterThanOrEqualTo`, `LesserThan`, `LesserThanOrEqualTo`, `NotEquals`, `StartsWith`
        """
        return pulumi.get(self, "operator")

    @property
    @pulumi.getter(name="propertyPath")
    def property_path(self) -> str:
        """
        The JPath of the entity model property that should be checked.
        """
        return pulumi.get(self, "property_path")

    @property
    @pulumi.getter(name="propertyType")
    def property_type(self) -> str:
        """
        The data type of the compared operands, must be one of: `Integer`, `String`, `Boolean` or `Number`.

        > **NOTE:** The schema for Security Center alerts (when `event_source` is "Alerts") [can be found here](https://docs.microsoft.com/azure/security-center/alerts-schemas?tabs=schema-continuousexport)
        """
        return pulumi.get(self, "property_type")


@pulumi.output_type
class SubscriptionPricingExtension(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "additionalExtensionProperties":
            suggest = "additional_extension_properties"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SubscriptionPricingExtension. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SubscriptionPricingExtension.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SubscriptionPricingExtension.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 additional_extension_properties: Optional[Mapping[str, str]] = None):
        """
        :param str name: The name of extension.
        :param Mapping[str, str] additional_extension_properties: Key/Value pairs that are required for some extensions.
               
               > **NOTE:** If an extension is not defined, it will not be enabled.
               
               > **NOTE:** Changing the pricing tier to `Standard` affects all resources of the given type in the subscription and could be quite costly.
        """
        SubscriptionPricingExtension._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            additional_extension_properties=additional_extension_properties,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: str,
             additional_extension_properties: Optional[Mapping[str, str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'additionalExtensionProperties' in kwargs:
            additional_extension_properties = kwargs['additionalExtensionProperties']

        _setter("name", name)
        if additional_extension_properties is not None:
            _setter("additional_extension_properties", additional_extension_properties)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of extension.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="additionalExtensionProperties")
    def additional_extension_properties(self) -> Optional[Mapping[str, str]]:
        """
        Key/Value pairs that are required for some extensions.

        > **NOTE:** If an extension is not defined, it will not be enabled.

        > **NOTE:** Changing the pricing tier to `Standard` affects all resources of the given type in the subscription and could be quite costly.
        """
        return pulumi.get(self, "additional_extension_properties")



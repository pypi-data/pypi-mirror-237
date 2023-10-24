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

__all__ = ['LogzSubAccountTagRuleArgs', 'LogzSubAccountTagRule']

@pulumi.input_type
class LogzSubAccountTagRuleArgs:
    def __init__(__self__, *,
                 logz_sub_account_id: pulumi.Input[str],
                 send_aad_logs: Optional[pulumi.Input[bool]] = None,
                 send_activity_logs: Optional[pulumi.Input[bool]] = None,
                 send_subscription_logs: Optional[pulumi.Input[bool]] = None,
                 tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input['LogzSubAccountTagRuleTagFilterArgs']]]] = None):
        """
        The set of arguments for constructing a LogzSubAccountTagRule resource.
        :param pulumi.Input[str] logz_sub_account_id: The ID of the Logz Sub Account. Changing this forces a new Logz Sub Account Tag Rule to be created.
        :param pulumi.Input[bool] send_aad_logs: Whether AAD logs should be sent to the Monitor resource?
        :param pulumi.Input[bool] send_activity_logs: Whether activity logs from this Logz Sub Account Tag Rule should be sent to the Monitor resource?
        :param pulumi.Input[bool] send_subscription_logs: Whether subscription logs should be sent to the Monitor resource?
        :param pulumi.Input[Sequence[pulumi.Input['LogzSubAccountTagRuleTagFilterArgs']]] tag_filters: One or more (up to 10) `tag_filter` blocks as defined below.
        """
        LogzSubAccountTagRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            logz_sub_account_id=logz_sub_account_id,
            send_aad_logs=send_aad_logs,
            send_activity_logs=send_activity_logs,
            send_subscription_logs=send_subscription_logs,
            tag_filters=tag_filters,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             logz_sub_account_id: pulumi.Input[str],
             send_aad_logs: Optional[pulumi.Input[bool]] = None,
             send_activity_logs: Optional[pulumi.Input[bool]] = None,
             send_subscription_logs: Optional[pulumi.Input[bool]] = None,
             tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input['LogzSubAccountTagRuleTagFilterArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'logzSubAccountId' in kwargs:
            logz_sub_account_id = kwargs['logzSubAccountId']
        if 'sendAadLogs' in kwargs:
            send_aad_logs = kwargs['sendAadLogs']
        if 'sendActivityLogs' in kwargs:
            send_activity_logs = kwargs['sendActivityLogs']
        if 'sendSubscriptionLogs' in kwargs:
            send_subscription_logs = kwargs['sendSubscriptionLogs']
        if 'tagFilters' in kwargs:
            tag_filters = kwargs['tagFilters']

        _setter("logz_sub_account_id", logz_sub_account_id)
        if send_aad_logs is not None:
            _setter("send_aad_logs", send_aad_logs)
        if send_activity_logs is not None:
            _setter("send_activity_logs", send_activity_logs)
        if send_subscription_logs is not None:
            _setter("send_subscription_logs", send_subscription_logs)
        if tag_filters is not None:
            _setter("tag_filters", tag_filters)

    @property
    @pulumi.getter(name="logzSubAccountId")
    def logz_sub_account_id(self) -> pulumi.Input[str]:
        """
        The ID of the Logz Sub Account. Changing this forces a new Logz Sub Account Tag Rule to be created.
        """
        return pulumi.get(self, "logz_sub_account_id")

    @logz_sub_account_id.setter
    def logz_sub_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "logz_sub_account_id", value)

    @property
    @pulumi.getter(name="sendAadLogs")
    def send_aad_logs(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether AAD logs should be sent to the Monitor resource?
        """
        return pulumi.get(self, "send_aad_logs")

    @send_aad_logs.setter
    def send_aad_logs(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "send_aad_logs", value)

    @property
    @pulumi.getter(name="sendActivityLogs")
    def send_activity_logs(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether activity logs from this Logz Sub Account Tag Rule should be sent to the Monitor resource?
        """
        return pulumi.get(self, "send_activity_logs")

    @send_activity_logs.setter
    def send_activity_logs(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "send_activity_logs", value)

    @property
    @pulumi.getter(name="sendSubscriptionLogs")
    def send_subscription_logs(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether subscription logs should be sent to the Monitor resource?
        """
        return pulumi.get(self, "send_subscription_logs")

    @send_subscription_logs.setter
    def send_subscription_logs(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "send_subscription_logs", value)

    @property
    @pulumi.getter(name="tagFilters")
    def tag_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LogzSubAccountTagRuleTagFilterArgs']]]]:
        """
        One or more (up to 10) `tag_filter` blocks as defined below.
        """
        return pulumi.get(self, "tag_filters")

    @tag_filters.setter
    def tag_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LogzSubAccountTagRuleTagFilterArgs']]]]):
        pulumi.set(self, "tag_filters", value)


@pulumi.input_type
class _LogzSubAccountTagRuleState:
    def __init__(__self__, *,
                 logz_sub_account_id: Optional[pulumi.Input[str]] = None,
                 send_aad_logs: Optional[pulumi.Input[bool]] = None,
                 send_activity_logs: Optional[pulumi.Input[bool]] = None,
                 send_subscription_logs: Optional[pulumi.Input[bool]] = None,
                 tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input['LogzSubAccountTagRuleTagFilterArgs']]]] = None):
        """
        Input properties used for looking up and filtering LogzSubAccountTagRule resources.
        :param pulumi.Input[str] logz_sub_account_id: The ID of the Logz Sub Account. Changing this forces a new Logz Sub Account Tag Rule to be created.
        :param pulumi.Input[bool] send_aad_logs: Whether AAD logs should be sent to the Monitor resource?
        :param pulumi.Input[bool] send_activity_logs: Whether activity logs from this Logz Sub Account Tag Rule should be sent to the Monitor resource?
        :param pulumi.Input[bool] send_subscription_logs: Whether subscription logs should be sent to the Monitor resource?
        :param pulumi.Input[Sequence[pulumi.Input['LogzSubAccountTagRuleTagFilterArgs']]] tag_filters: One or more (up to 10) `tag_filter` blocks as defined below.
        """
        _LogzSubAccountTagRuleState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            logz_sub_account_id=logz_sub_account_id,
            send_aad_logs=send_aad_logs,
            send_activity_logs=send_activity_logs,
            send_subscription_logs=send_subscription_logs,
            tag_filters=tag_filters,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             logz_sub_account_id: Optional[pulumi.Input[str]] = None,
             send_aad_logs: Optional[pulumi.Input[bool]] = None,
             send_activity_logs: Optional[pulumi.Input[bool]] = None,
             send_subscription_logs: Optional[pulumi.Input[bool]] = None,
             tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input['LogzSubAccountTagRuleTagFilterArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'logzSubAccountId' in kwargs:
            logz_sub_account_id = kwargs['logzSubAccountId']
        if 'sendAadLogs' in kwargs:
            send_aad_logs = kwargs['sendAadLogs']
        if 'sendActivityLogs' in kwargs:
            send_activity_logs = kwargs['sendActivityLogs']
        if 'sendSubscriptionLogs' in kwargs:
            send_subscription_logs = kwargs['sendSubscriptionLogs']
        if 'tagFilters' in kwargs:
            tag_filters = kwargs['tagFilters']

        if logz_sub_account_id is not None:
            _setter("logz_sub_account_id", logz_sub_account_id)
        if send_aad_logs is not None:
            _setter("send_aad_logs", send_aad_logs)
        if send_activity_logs is not None:
            _setter("send_activity_logs", send_activity_logs)
        if send_subscription_logs is not None:
            _setter("send_subscription_logs", send_subscription_logs)
        if tag_filters is not None:
            _setter("tag_filters", tag_filters)

    @property
    @pulumi.getter(name="logzSubAccountId")
    def logz_sub_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Logz Sub Account. Changing this forces a new Logz Sub Account Tag Rule to be created.
        """
        return pulumi.get(self, "logz_sub_account_id")

    @logz_sub_account_id.setter
    def logz_sub_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logz_sub_account_id", value)

    @property
    @pulumi.getter(name="sendAadLogs")
    def send_aad_logs(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether AAD logs should be sent to the Monitor resource?
        """
        return pulumi.get(self, "send_aad_logs")

    @send_aad_logs.setter
    def send_aad_logs(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "send_aad_logs", value)

    @property
    @pulumi.getter(name="sendActivityLogs")
    def send_activity_logs(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether activity logs from this Logz Sub Account Tag Rule should be sent to the Monitor resource?
        """
        return pulumi.get(self, "send_activity_logs")

    @send_activity_logs.setter
    def send_activity_logs(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "send_activity_logs", value)

    @property
    @pulumi.getter(name="sendSubscriptionLogs")
    def send_subscription_logs(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether subscription logs should be sent to the Monitor resource?
        """
        return pulumi.get(self, "send_subscription_logs")

    @send_subscription_logs.setter
    def send_subscription_logs(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "send_subscription_logs", value)

    @property
    @pulumi.getter(name="tagFilters")
    def tag_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LogzSubAccountTagRuleTagFilterArgs']]]]:
        """
        One or more (up to 10) `tag_filter` blocks as defined below.
        """
        return pulumi.get(self, "tag_filters")

    @tag_filters.setter
    def tag_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LogzSubAccountTagRuleTagFilterArgs']]]]):
        pulumi.set(self, "tag_filters", value)


class LogzSubAccountTagRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 logz_sub_account_id: Optional[pulumi.Input[str]] = None,
                 send_aad_logs: Optional[pulumi.Input[bool]] = None,
                 send_activity_logs: Optional[pulumi.Input[bool]] = None,
                 send_subscription_logs: Optional[pulumi.Input[bool]] = None,
                 tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LogzSubAccountTagRuleTagFilterArgs']]]]] = None,
                 __props__=None):
        """
        Manages a Logz Sub Account Tag Rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_logz_monitor = azure.monitoring.LogzMonitor("exampleLogzMonitor",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            plan=azure.monitoring.LogzMonitorPlanArgs(
                billing_cycle="MONTHLY",
                effective_date="2022-06-06T00:00:00Z",
                usage_type="COMMITTED",
            ),
            user=azure.monitoring.LogzMonitorUserArgs(
                email="user@example.com",
                first_name="Example",
                last_name="User",
                phone_number="+12313803556",
            ))
        example_logz_sub_account = azure.monitoring.LogzSubAccount("exampleLogzSubAccount",
            logz_monitor_id=example_logz_monitor.id,
            user=azure.monitoring.LogzSubAccountUserArgs(
                email=example_logz_monitor.user.email,
                first_name=example_logz_monitor.user.first_name,
                last_name=example_logz_monitor.user.last_name,
                phone_number=example_logz_monitor.user.phone_number,
            ))
        example_logz_sub_account_tag_rule = azure.monitoring.LogzSubAccountTagRule("exampleLogzSubAccountTagRule",
            logz_sub_account_id=example_logz_sub_account.id,
            send_aad_logs=True,
            send_activity_logs=True,
            send_subscription_logs=True,
            tag_filters=[
                azure.monitoring.LogzSubAccountTagRuleTagFilterArgs(
                    name="name1",
                    action="Include",
                    value="value1",
                ),
                azure.monitoring.LogzSubAccountTagRuleTagFilterArgs(
                    name="name2",
                    action="Exclude",
                    value="value2",
                ),
            ])
        ```

        ## Import

        Logz Sub Account Tag Rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:monitoring/logzSubAccountTagRule:LogzSubAccountTagRule example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Logz/monitors/monitor1/accounts/subAccount1/tagRules/ruleSet1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] logz_sub_account_id: The ID of the Logz Sub Account. Changing this forces a new Logz Sub Account Tag Rule to be created.
        :param pulumi.Input[bool] send_aad_logs: Whether AAD logs should be sent to the Monitor resource?
        :param pulumi.Input[bool] send_activity_logs: Whether activity logs from this Logz Sub Account Tag Rule should be sent to the Monitor resource?
        :param pulumi.Input[bool] send_subscription_logs: Whether subscription logs should be sent to the Monitor resource?
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LogzSubAccountTagRuleTagFilterArgs']]]] tag_filters: One or more (up to 10) `tag_filter` blocks as defined below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LogzSubAccountTagRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Logz Sub Account Tag Rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_logz_monitor = azure.monitoring.LogzMonitor("exampleLogzMonitor",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            plan=azure.monitoring.LogzMonitorPlanArgs(
                billing_cycle="MONTHLY",
                effective_date="2022-06-06T00:00:00Z",
                usage_type="COMMITTED",
            ),
            user=azure.monitoring.LogzMonitorUserArgs(
                email="user@example.com",
                first_name="Example",
                last_name="User",
                phone_number="+12313803556",
            ))
        example_logz_sub_account = azure.monitoring.LogzSubAccount("exampleLogzSubAccount",
            logz_monitor_id=example_logz_monitor.id,
            user=azure.monitoring.LogzSubAccountUserArgs(
                email=example_logz_monitor.user.email,
                first_name=example_logz_monitor.user.first_name,
                last_name=example_logz_monitor.user.last_name,
                phone_number=example_logz_monitor.user.phone_number,
            ))
        example_logz_sub_account_tag_rule = azure.monitoring.LogzSubAccountTagRule("exampleLogzSubAccountTagRule",
            logz_sub_account_id=example_logz_sub_account.id,
            send_aad_logs=True,
            send_activity_logs=True,
            send_subscription_logs=True,
            tag_filters=[
                azure.monitoring.LogzSubAccountTagRuleTagFilterArgs(
                    name="name1",
                    action="Include",
                    value="value1",
                ),
                azure.monitoring.LogzSubAccountTagRuleTagFilterArgs(
                    name="name2",
                    action="Exclude",
                    value="value2",
                ),
            ])
        ```

        ## Import

        Logz Sub Account Tag Rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:monitoring/logzSubAccountTagRule:LogzSubAccountTagRule example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Logz/monitors/monitor1/accounts/subAccount1/tagRules/ruleSet1
        ```

        :param str resource_name: The name of the resource.
        :param LogzSubAccountTagRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LogzSubAccountTagRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            LogzSubAccountTagRuleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 logz_sub_account_id: Optional[pulumi.Input[str]] = None,
                 send_aad_logs: Optional[pulumi.Input[bool]] = None,
                 send_activity_logs: Optional[pulumi.Input[bool]] = None,
                 send_subscription_logs: Optional[pulumi.Input[bool]] = None,
                 tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LogzSubAccountTagRuleTagFilterArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LogzSubAccountTagRuleArgs.__new__(LogzSubAccountTagRuleArgs)

            if logz_sub_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'logz_sub_account_id'")
            __props__.__dict__["logz_sub_account_id"] = logz_sub_account_id
            __props__.__dict__["send_aad_logs"] = send_aad_logs
            __props__.__dict__["send_activity_logs"] = send_activity_logs
            __props__.__dict__["send_subscription_logs"] = send_subscription_logs
            __props__.__dict__["tag_filters"] = tag_filters
        super(LogzSubAccountTagRule, __self__).__init__(
            'azure:monitoring/logzSubAccountTagRule:LogzSubAccountTagRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            logz_sub_account_id: Optional[pulumi.Input[str]] = None,
            send_aad_logs: Optional[pulumi.Input[bool]] = None,
            send_activity_logs: Optional[pulumi.Input[bool]] = None,
            send_subscription_logs: Optional[pulumi.Input[bool]] = None,
            tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LogzSubAccountTagRuleTagFilterArgs']]]]] = None) -> 'LogzSubAccountTagRule':
        """
        Get an existing LogzSubAccountTagRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] logz_sub_account_id: The ID of the Logz Sub Account. Changing this forces a new Logz Sub Account Tag Rule to be created.
        :param pulumi.Input[bool] send_aad_logs: Whether AAD logs should be sent to the Monitor resource?
        :param pulumi.Input[bool] send_activity_logs: Whether activity logs from this Logz Sub Account Tag Rule should be sent to the Monitor resource?
        :param pulumi.Input[bool] send_subscription_logs: Whether subscription logs should be sent to the Monitor resource?
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LogzSubAccountTagRuleTagFilterArgs']]]] tag_filters: One or more (up to 10) `tag_filter` blocks as defined below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LogzSubAccountTagRuleState.__new__(_LogzSubAccountTagRuleState)

        __props__.__dict__["logz_sub_account_id"] = logz_sub_account_id
        __props__.__dict__["send_aad_logs"] = send_aad_logs
        __props__.__dict__["send_activity_logs"] = send_activity_logs
        __props__.__dict__["send_subscription_logs"] = send_subscription_logs
        __props__.__dict__["tag_filters"] = tag_filters
        return LogzSubAccountTagRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="logzSubAccountId")
    def logz_sub_account_id(self) -> pulumi.Output[str]:
        """
        The ID of the Logz Sub Account. Changing this forces a new Logz Sub Account Tag Rule to be created.
        """
        return pulumi.get(self, "logz_sub_account_id")

    @property
    @pulumi.getter(name="sendAadLogs")
    def send_aad_logs(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether AAD logs should be sent to the Monitor resource?
        """
        return pulumi.get(self, "send_aad_logs")

    @property
    @pulumi.getter(name="sendActivityLogs")
    def send_activity_logs(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether activity logs from this Logz Sub Account Tag Rule should be sent to the Monitor resource?
        """
        return pulumi.get(self, "send_activity_logs")

    @property
    @pulumi.getter(name="sendSubscriptionLogs")
    def send_subscription_logs(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether subscription logs should be sent to the Monitor resource?
        """
        return pulumi.get(self, "send_subscription_logs")

    @property
    @pulumi.getter(name="tagFilters")
    def tag_filters(self) -> pulumi.Output[Optional[Sequence['outputs.LogzSubAccountTagRuleTagFilter']]]:
        """
        One or more (up to 10) `tag_filter` blocks as defined below.
        """
        return pulumi.get(self, "tag_filters")


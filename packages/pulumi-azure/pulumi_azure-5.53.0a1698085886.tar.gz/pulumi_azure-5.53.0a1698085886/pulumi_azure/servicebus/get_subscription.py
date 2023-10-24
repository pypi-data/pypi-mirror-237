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
    'GetSubscriptionResult',
    'AwaitableGetSubscriptionResult',
    'get_subscription',
    'get_subscription_output',
]

@pulumi.output_type
class GetSubscriptionResult:
    """
    A collection of values returned by getSubscription.
    """
    def __init__(__self__, auto_delete_on_idle=None, dead_lettering_on_filter_evaluation_error=None, dead_lettering_on_message_expiration=None, default_message_ttl=None, enable_batched_operations=None, forward_dead_lettered_messages_to=None, forward_to=None, id=None, lock_duration=None, max_delivery_count=None, name=None, namespace_name=None, requires_session=None, resource_group_name=None, topic_id=None, topic_name=None):
        if auto_delete_on_idle and not isinstance(auto_delete_on_idle, str):
            raise TypeError("Expected argument 'auto_delete_on_idle' to be a str")
        pulumi.set(__self__, "auto_delete_on_idle", auto_delete_on_idle)
        if dead_lettering_on_filter_evaluation_error and not isinstance(dead_lettering_on_filter_evaluation_error, bool):
            raise TypeError("Expected argument 'dead_lettering_on_filter_evaluation_error' to be a bool")
        pulumi.set(__self__, "dead_lettering_on_filter_evaluation_error", dead_lettering_on_filter_evaluation_error)
        if dead_lettering_on_message_expiration and not isinstance(dead_lettering_on_message_expiration, bool):
            raise TypeError("Expected argument 'dead_lettering_on_message_expiration' to be a bool")
        pulumi.set(__self__, "dead_lettering_on_message_expiration", dead_lettering_on_message_expiration)
        if default_message_ttl and not isinstance(default_message_ttl, str):
            raise TypeError("Expected argument 'default_message_ttl' to be a str")
        pulumi.set(__self__, "default_message_ttl", default_message_ttl)
        if enable_batched_operations and not isinstance(enable_batched_operations, bool):
            raise TypeError("Expected argument 'enable_batched_operations' to be a bool")
        pulumi.set(__self__, "enable_batched_operations", enable_batched_operations)
        if forward_dead_lettered_messages_to and not isinstance(forward_dead_lettered_messages_to, str):
            raise TypeError("Expected argument 'forward_dead_lettered_messages_to' to be a str")
        pulumi.set(__self__, "forward_dead_lettered_messages_to", forward_dead_lettered_messages_to)
        if forward_to and not isinstance(forward_to, str):
            raise TypeError("Expected argument 'forward_to' to be a str")
        pulumi.set(__self__, "forward_to", forward_to)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lock_duration and not isinstance(lock_duration, str):
            raise TypeError("Expected argument 'lock_duration' to be a str")
        pulumi.set(__self__, "lock_duration", lock_duration)
        if max_delivery_count and not isinstance(max_delivery_count, int):
            raise TypeError("Expected argument 'max_delivery_count' to be a int")
        pulumi.set(__self__, "max_delivery_count", max_delivery_count)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if namespace_name and not isinstance(namespace_name, str):
            raise TypeError("Expected argument 'namespace_name' to be a str")
        pulumi.set(__self__, "namespace_name", namespace_name)
        if requires_session and not isinstance(requires_session, bool):
            raise TypeError("Expected argument 'requires_session' to be a bool")
        pulumi.set(__self__, "requires_session", requires_session)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if topic_id and not isinstance(topic_id, str):
            raise TypeError("Expected argument 'topic_id' to be a str")
        pulumi.set(__self__, "topic_id", topic_id)
        if topic_name and not isinstance(topic_name, str):
            raise TypeError("Expected argument 'topic_name' to be a str")
        pulumi.set(__self__, "topic_name", topic_name)

    @property
    @pulumi.getter(name="autoDeleteOnIdle")
    def auto_delete_on_idle(self) -> str:
        """
        The idle interval after which the topic is automatically deleted.
        """
        return pulumi.get(self, "auto_delete_on_idle")

    @property
    @pulumi.getter(name="deadLetteringOnFilterEvaluationError")
    def dead_lettering_on_filter_evaluation_error(self) -> bool:
        """
        Does the ServiceBus Subscription have dead letter support on filter evaluation exceptions?
        """
        return pulumi.get(self, "dead_lettering_on_filter_evaluation_error")

    @property
    @pulumi.getter(name="deadLetteringOnMessageExpiration")
    def dead_lettering_on_message_expiration(self) -> bool:
        """
        Does the Service Bus Subscription have dead letter support when a message expires?
        """
        return pulumi.get(self, "dead_lettering_on_message_expiration")

    @property
    @pulumi.getter(name="defaultMessageTtl")
    def default_message_ttl(self) -> str:
        """
        The Default message timespan to live. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
        """
        return pulumi.get(self, "default_message_ttl")

    @property
    @pulumi.getter(name="enableBatchedOperations")
    def enable_batched_operations(self) -> bool:
        """
        Are batched operations enabled on this ServiceBus Subscription?
        """
        return pulumi.get(self, "enable_batched_operations")

    @property
    @pulumi.getter(name="forwardDeadLetteredMessagesTo")
    def forward_dead_lettered_messages_to(self) -> str:
        """
        The name of a Queue or Topic to automatically forward Dead Letter messages to.
        """
        return pulumi.get(self, "forward_dead_lettered_messages_to")

    @property
    @pulumi.getter(name="forwardTo")
    def forward_to(self) -> str:
        """
        The name of a ServiceBus Queue or ServiceBus Topic where messages are automatically forwarded.
        """
        return pulumi.get(self, "forward_to")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lockDuration")
    def lock_duration(self) -> str:
        """
        The lock duration for the subscription.
        """
        return pulumi.get(self, "lock_duration")

    @property
    @pulumi.getter(name="maxDeliveryCount")
    def max_delivery_count(self) -> int:
        """
        The maximum number of deliveries.
        """
        return pulumi.get(self, "max_delivery_count")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[str]:
        warnings.warn("""`namespace_name` will be removed in favour of the property `topic_id` in version 4.0 of the AzureRM Provider.""", DeprecationWarning)
        pulumi.log.warn("""namespace_name is deprecated: `namespace_name` will be removed in favour of the property `topic_id` in version 4.0 of the AzureRM Provider.""")

        return pulumi.get(self, "namespace_name")

    @property
    @pulumi.getter(name="requiresSession")
    def requires_session(self) -> bool:
        """
        Whether or not this ServiceBus Subscription supports session.
        """
        return pulumi.get(self, "requires_session")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[str]:
        warnings.warn("""`resource_group_name` will be removed in favour of the property `topic_id` in version 4.0 of the AzureRM Provider.""", DeprecationWarning)
        pulumi.log.warn("""resource_group_name is deprecated: `resource_group_name` will be removed in favour of the property `topic_id` in version 4.0 of the AzureRM Provider.""")

        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="topicId")
    def topic_id(self) -> Optional[str]:
        return pulumi.get(self, "topic_id")

    @property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> Optional[str]:
        warnings.warn("""`topic_name` will be removed in favour of the property `topic_id` in version 4.0 of the AzureRM Provider.""", DeprecationWarning)
        pulumi.log.warn("""topic_name is deprecated: `topic_name` will be removed in favour of the property `topic_id` in version 4.0 of the AzureRM Provider.""")

        return pulumi.get(self, "topic_name")


class AwaitableGetSubscriptionResult(GetSubscriptionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSubscriptionResult(
            auto_delete_on_idle=self.auto_delete_on_idle,
            dead_lettering_on_filter_evaluation_error=self.dead_lettering_on_filter_evaluation_error,
            dead_lettering_on_message_expiration=self.dead_lettering_on_message_expiration,
            default_message_ttl=self.default_message_ttl,
            enable_batched_operations=self.enable_batched_operations,
            forward_dead_lettered_messages_to=self.forward_dead_lettered_messages_to,
            forward_to=self.forward_to,
            id=self.id,
            lock_duration=self.lock_duration,
            max_delivery_count=self.max_delivery_count,
            name=self.name,
            namespace_name=self.namespace_name,
            requires_session=self.requires_session,
            resource_group_name=self.resource_group_name,
            topic_id=self.topic_id,
            topic_name=self.topic_name)


def get_subscription(name: Optional[str] = None,
                     namespace_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     topic_id: Optional[str] = None,
                     topic_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSubscriptionResult:
    """
    Use this data source to access information about an existing ServiceBus Subscription.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.servicebus.get_subscription(name="examplesubscription",
        topic_id="exampletopic")
    pulumi.export("servicebusSubscription", data["azurerm_servicebus_namespace"]["example"])
    ```


    :param str name: Specifies the name of the ServiceBus Subscription.
    :param str namespace_name: The name of the ServiceBus Namespace.
    :param str resource_group_name: Specifies the name of the Resource Group where the ServiceBus Namespace exists.
    :param str topic_id: The ID of the ServiceBus Topic where the Service Bus Subscription exists.
    :param str topic_name: The name of the ServiceBus Topic.
           
           > **Note:** `namespace_name`，`resource_group_name` and `topic_name` has been deprecated and will be removed in version 4.0 of the provider in favour of `topic_id`.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['topicId'] = topic_id
    __args__['topicName'] = topic_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:servicebus/getSubscription:getSubscription', __args__, opts=opts, typ=GetSubscriptionResult).value

    return AwaitableGetSubscriptionResult(
        auto_delete_on_idle=pulumi.get(__ret__, 'auto_delete_on_idle'),
        dead_lettering_on_filter_evaluation_error=pulumi.get(__ret__, 'dead_lettering_on_filter_evaluation_error'),
        dead_lettering_on_message_expiration=pulumi.get(__ret__, 'dead_lettering_on_message_expiration'),
        default_message_ttl=pulumi.get(__ret__, 'default_message_ttl'),
        enable_batched_operations=pulumi.get(__ret__, 'enable_batched_operations'),
        forward_dead_lettered_messages_to=pulumi.get(__ret__, 'forward_dead_lettered_messages_to'),
        forward_to=pulumi.get(__ret__, 'forward_to'),
        id=pulumi.get(__ret__, 'id'),
        lock_duration=pulumi.get(__ret__, 'lock_duration'),
        max_delivery_count=pulumi.get(__ret__, 'max_delivery_count'),
        name=pulumi.get(__ret__, 'name'),
        namespace_name=pulumi.get(__ret__, 'namespace_name'),
        requires_session=pulumi.get(__ret__, 'requires_session'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        topic_id=pulumi.get(__ret__, 'topic_id'),
        topic_name=pulumi.get(__ret__, 'topic_name'))


@_utilities.lift_output_func(get_subscription)
def get_subscription_output(name: Optional[pulumi.Input[str]] = None,
                            namespace_name: Optional[pulumi.Input[Optional[str]]] = None,
                            resource_group_name: Optional[pulumi.Input[Optional[str]]] = None,
                            topic_id: Optional[pulumi.Input[Optional[str]]] = None,
                            topic_name: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSubscriptionResult]:
    """
    Use this data source to access information about an existing ServiceBus Subscription.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.servicebus.get_subscription(name="examplesubscription",
        topic_id="exampletopic")
    pulumi.export("servicebusSubscription", data["azurerm_servicebus_namespace"]["example"])
    ```


    :param str name: Specifies the name of the ServiceBus Subscription.
    :param str namespace_name: The name of the ServiceBus Namespace.
    :param str resource_group_name: Specifies the name of the Resource Group where the ServiceBus Namespace exists.
    :param str topic_id: The ID of the ServiceBus Topic where the Service Bus Subscription exists.
    :param str topic_name: The name of the ServiceBus Topic.
           
           > **Note:** `namespace_name`，`resource_group_name` and `topic_name` has been deprecated and will be removed in version 4.0 of the provider in favour of `topic_id`.
    """
    ...

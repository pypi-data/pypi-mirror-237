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

__all__ = ['EventHubArgs', 'EventHub']

@pulumi.input_type
class EventHubArgs:
    def __init__(__self__, *,
                 message_retention: pulumi.Input[int],
                 namespace_name: pulumi.Input[str],
                 partition_count: pulumi.Input[int],
                 resource_group_name: pulumi.Input[str],
                 capture_description: Optional[pulumi.Input['EventHubCaptureDescriptionArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EventHub resource.
        :param pulumi.Input[int] message_retention: Specifies the number of days to retain the events for this Event Hub.
               
               > **Note:** When using a dedicated Event Hubs cluster, maximum value of `message_retention` is 90 days. When using a shared parent EventHub Namespace, maximum value is 7 days; or 1 day when using a Basic SKU for the shared parent EventHub Namespace.
        :param pulumi.Input[str] namespace_name: Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[int] partition_count: Specifies the current number of shards on the Event Hub.
               
               > **Note:** `partition_count` cannot be changed unless Eventhub Namespace SKU is `Premium` and cannot be decreased.
               
               > **Note:** When using a dedicated Event Hubs cluster, maximum value of `partition_count` is 1024. When using a shared parent EventHub Namespace, maximum value is 32.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the EventHub's parent Namespace exists. Changing this forces a new resource to be created.
        :param pulumi.Input['EventHubCaptureDescriptionArgs'] capture_description: A `capture_description` block as defined below.
        :param pulumi.Input[str] name: Specifies the name of the EventHub resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] status: Specifies the status of the Event Hub resource. Possible values are `Active`, `Disabled` and `SendDisabled`. Defaults to `Active`.
        """
        EventHubArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            message_retention=message_retention,
            namespace_name=namespace_name,
            partition_count=partition_count,
            resource_group_name=resource_group_name,
            capture_description=capture_description,
            name=name,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             message_retention: pulumi.Input[int],
             namespace_name: pulumi.Input[str],
             partition_count: pulumi.Input[int],
             resource_group_name: pulumi.Input[str],
             capture_description: Optional[pulumi.Input['EventHubCaptureDescriptionArgs']] = None,
             name: Optional[pulumi.Input[str]] = None,
             status: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'messageRetention' in kwargs:
            message_retention = kwargs['messageRetention']
        if 'namespaceName' in kwargs:
            namespace_name = kwargs['namespaceName']
        if 'partitionCount' in kwargs:
            partition_count = kwargs['partitionCount']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'captureDescription' in kwargs:
            capture_description = kwargs['captureDescription']

        _setter("message_retention", message_retention)
        _setter("namespace_name", namespace_name)
        _setter("partition_count", partition_count)
        _setter("resource_group_name", resource_group_name)
        if capture_description is not None:
            _setter("capture_description", capture_description)
        if name is not None:
            _setter("name", name)
        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter(name="messageRetention")
    def message_retention(self) -> pulumi.Input[int]:
        """
        Specifies the number of days to retain the events for this Event Hub.

        > **Note:** When using a dedicated Event Hubs cluster, maximum value of `message_retention` is 90 days. When using a shared parent EventHub Namespace, maximum value is 7 days; or 1 day when using a Basic SKU for the shared parent EventHub Namespace.
        """
        return pulumi.get(self, "message_retention")

    @message_retention.setter
    def message_retention(self, value: pulumi.Input[int]):
        pulumi.set(self, "message_retention", value)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[str]:
        """
        Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="partitionCount")
    def partition_count(self) -> pulumi.Input[int]:
        """
        Specifies the current number of shards on the Event Hub.

        > **Note:** `partition_count` cannot be changed unless Eventhub Namespace SKU is `Premium` and cannot be decreased.

        > **Note:** When using a dedicated Event Hubs cluster, maximum value of `partition_count` is 1024. When using a shared parent EventHub Namespace, maximum value is 32.
        """
        return pulumi.get(self, "partition_count")

    @partition_count.setter
    def partition_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "partition_count", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group in which the EventHub's parent Namespace exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="captureDescription")
    def capture_description(self) -> Optional[pulumi.Input['EventHubCaptureDescriptionArgs']]:
        """
        A `capture_description` block as defined below.
        """
        return pulumi.get(self, "capture_description")

    @capture_description.setter
    def capture_description(self, value: Optional[pulumi.Input['EventHubCaptureDescriptionArgs']]):
        pulumi.set(self, "capture_description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the EventHub resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the status of the Event Hub resource. Possible values are `Active`, `Disabled` and `SendDisabled`. Defaults to `Active`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class _EventHubState:
    def __init__(__self__, *,
                 capture_description: Optional[pulumi.Input['EventHubCaptureDescriptionArgs']] = None,
                 message_retention: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 partition_count: Optional[pulumi.Input[int]] = None,
                 partition_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering EventHub resources.
        :param pulumi.Input['EventHubCaptureDescriptionArgs'] capture_description: A `capture_description` block as defined below.
        :param pulumi.Input[int] message_retention: Specifies the number of days to retain the events for this Event Hub.
               
               > **Note:** When using a dedicated Event Hubs cluster, maximum value of `message_retention` is 90 days. When using a shared parent EventHub Namespace, maximum value is 7 days; or 1 day when using a Basic SKU for the shared parent EventHub Namespace.
        :param pulumi.Input[str] name: Specifies the name of the EventHub resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] namespace_name: Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[int] partition_count: Specifies the current number of shards on the Event Hub.
               
               > **Note:** `partition_count` cannot be changed unless Eventhub Namespace SKU is `Premium` and cannot be decreased.
               
               > **Note:** When using a dedicated Event Hubs cluster, maximum value of `partition_count` is 1024. When using a shared parent EventHub Namespace, maximum value is 32.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] partition_ids: The identifiers for partitions created for Event Hubs.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the EventHub's parent Namespace exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] status: Specifies the status of the Event Hub resource. Possible values are `Active`, `Disabled` and `SendDisabled`. Defaults to `Active`.
        """
        _EventHubState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            capture_description=capture_description,
            message_retention=message_retention,
            name=name,
            namespace_name=namespace_name,
            partition_count=partition_count,
            partition_ids=partition_ids,
            resource_group_name=resource_group_name,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             capture_description: Optional[pulumi.Input['EventHubCaptureDescriptionArgs']] = None,
             message_retention: Optional[pulumi.Input[int]] = None,
             name: Optional[pulumi.Input[str]] = None,
             namespace_name: Optional[pulumi.Input[str]] = None,
             partition_count: Optional[pulumi.Input[int]] = None,
             partition_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             status: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'captureDescription' in kwargs:
            capture_description = kwargs['captureDescription']
        if 'messageRetention' in kwargs:
            message_retention = kwargs['messageRetention']
        if 'namespaceName' in kwargs:
            namespace_name = kwargs['namespaceName']
        if 'partitionCount' in kwargs:
            partition_count = kwargs['partitionCount']
        if 'partitionIds' in kwargs:
            partition_ids = kwargs['partitionIds']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']

        if capture_description is not None:
            _setter("capture_description", capture_description)
        if message_retention is not None:
            _setter("message_retention", message_retention)
        if name is not None:
            _setter("name", name)
        if namespace_name is not None:
            _setter("namespace_name", namespace_name)
        if partition_count is not None:
            _setter("partition_count", partition_count)
        if partition_ids is not None:
            _setter("partition_ids", partition_ids)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter(name="captureDescription")
    def capture_description(self) -> Optional[pulumi.Input['EventHubCaptureDescriptionArgs']]:
        """
        A `capture_description` block as defined below.
        """
        return pulumi.get(self, "capture_description")

    @capture_description.setter
    def capture_description(self, value: Optional[pulumi.Input['EventHubCaptureDescriptionArgs']]):
        pulumi.set(self, "capture_description", value)

    @property
    @pulumi.getter(name="messageRetention")
    def message_retention(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the number of days to retain the events for this Event Hub.

        > **Note:** When using a dedicated Event Hubs cluster, maximum value of `message_retention` is 90 days. When using a shared parent EventHub Namespace, maximum value is 7 days; or 1 day when using a Basic SKU for the shared parent EventHub Namespace.
        """
        return pulumi.get(self, "message_retention")

    @message_retention.setter
    def message_retention(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "message_retention", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the EventHub resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="partitionCount")
    def partition_count(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the current number of shards on the Event Hub.

        > **Note:** `partition_count` cannot be changed unless Eventhub Namespace SKU is `Premium` and cannot be decreased.

        > **Note:** When using a dedicated Event Hubs cluster, maximum value of `partition_count` is 1024. When using a shared parent EventHub Namespace, maximum value is 32.
        """
        return pulumi.get(self, "partition_count")

    @partition_count.setter
    def partition_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "partition_count", value)

    @property
    @pulumi.getter(name="partitionIds")
    def partition_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The identifiers for partitions created for Event Hubs.
        """
        return pulumi.get(self, "partition_ids")

    @partition_ids.setter
    def partition_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "partition_ids", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group in which the EventHub's parent Namespace exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the status of the Event Hub resource. Possible values are `Active`, `Disabled` and `SendDisabled`. Defaults to `Active`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class EventHub(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capture_description: Optional[pulumi.Input[pulumi.InputType['EventHubCaptureDescriptionArgs']]] = None,
                 message_retention: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 partition_count: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Event Hubs as a nested resource within a Event Hubs namespace.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_event_hub_namespace = azure.eventhub.EventHubNamespace("exampleEventHubNamespace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="Standard",
            capacity=1,
            tags={
                "environment": "Production",
            })
        example_event_hub = azure.eventhub.EventHub("exampleEventHub",
            namespace_name=example_event_hub_namespace.name,
            resource_group_name=example_resource_group.name,
            partition_count=2,
            message_retention=1)
        ```

        ## Import

        EventHubs can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:eventhub/eventHub:EventHub eventhub1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.EventHub/namespaces/namespace1/eventhubs/eventhub1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['EventHubCaptureDescriptionArgs']] capture_description: A `capture_description` block as defined below.
        :param pulumi.Input[int] message_retention: Specifies the number of days to retain the events for this Event Hub.
               
               > **Note:** When using a dedicated Event Hubs cluster, maximum value of `message_retention` is 90 days. When using a shared parent EventHub Namespace, maximum value is 7 days; or 1 day when using a Basic SKU for the shared parent EventHub Namespace.
        :param pulumi.Input[str] name: Specifies the name of the EventHub resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] namespace_name: Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[int] partition_count: Specifies the current number of shards on the Event Hub.
               
               > **Note:** `partition_count` cannot be changed unless Eventhub Namespace SKU is `Premium` and cannot be decreased.
               
               > **Note:** When using a dedicated Event Hubs cluster, maximum value of `partition_count` is 1024. When using a shared parent EventHub Namespace, maximum value is 32.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the EventHub's parent Namespace exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] status: Specifies the status of the Event Hub resource. Possible values are `Active`, `Disabled` and `SendDisabled`. Defaults to `Active`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EventHubArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Event Hubs as a nested resource within a Event Hubs namespace.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_event_hub_namespace = azure.eventhub.EventHubNamespace("exampleEventHubNamespace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="Standard",
            capacity=1,
            tags={
                "environment": "Production",
            })
        example_event_hub = azure.eventhub.EventHub("exampleEventHub",
            namespace_name=example_event_hub_namespace.name,
            resource_group_name=example_resource_group.name,
            partition_count=2,
            message_retention=1)
        ```

        ## Import

        EventHubs can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:eventhub/eventHub:EventHub eventhub1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.EventHub/namespaces/namespace1/eventhubs/eventhub1
        ```

        :param str resource_name: The name of the resource.
        :param EventHubArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EventHubArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            EventHubArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capture_description: Optional[pulumi.Input[pulumi.InputType['EventHubCaptureDescriptionArgs']]] = None,
                 message_retention: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 partition_count: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EventHubArgs.__new__(EventHubArgs)

            if capture_description is not None and not isinstance(capture_description, EventHubCaptureDescriptionArgs):
                capture_description = capture_description or {}
                def _setter(key, value):
                    capture_description[key] = value
                EventHubCaptureDescriptionArgs._configure(_setter, **capture_description)
            __props__.__dict__["capture_description"] = capture_description
            if message_retention is None and not opts.urn:
                raise TypeError("Missing required property 'message_retention'")
            __props__.__dict__["message_retention"] = message_retention
            __props__.__dict__["name"] = name
            if namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_name'")
            __props__.__dict__["namespace_name"] = namespace_name
            if partition_count is None and not opts.urn:
                raise TypeError("Missing required property 'partition_count'")
            __props__.__dict__["partition_count"] = partition_count
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["status"] = status
            __props__.__dict__["partition_ids"] = None
        super(EventHub, __self__).__init__(
            'azure:eventhub/eventHub:EventHub',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            capture_description: Optional[pulumi.Input[pulumi.InputType['EventHubCaptureDescriptionArgs']]] = None,
            message_retention: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace_name: Optional[pulumi.Input[str]] = None,
            partition_count: Optional[pulumi.Input[int]] = None,
            partition_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'EventHub':
        """
        Get an existing EventHub resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['EventHubCaptureDescriptionArgs']] capture_description: A `capture_description` block as defined below.
        :param pulumi.Input[int] message_retention: Specifies the number of days to retain the events for this Event Hub.
               
               > **Note:** When using a dedicated Event Hubs cluster, maximum value of `message_retention` is 90 days. When using a shared parent EventHub Namespace, maximum value is 7 days; or 1 day when using a Basic SKU for the shared parent EventHub Namespace.
        :param pulumi.Input[str] name: Specifies the name of the EventHub resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] namespace_name: Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[int] partition_count: Specifies the current number of shards on the Event Hub.
               
               > **Note:** `partition_count` cannot be changed unless Eventhub Namespace SKU is `Premium` and cannot be decreased.
               
               > **Note:** When using a dedicated Event Hubs cluster, maximum value of `partition_count` is 1024. When using a shared parent EventHub Namespace, maximum value is 32.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] partition_ids: The identifiers for partitions created for Event Hubs.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the EventHub's parent Namespace exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] status: Specifies the status of the Event Hub resource. Possible values are `Active`, `Disabled` and `SendDisabled`. Defaults to `Active`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EventHubState.__new__(_EventHubState)

        __props__.__dict__["capture_description"] = capture_description
        __props__.__dict__["message_retention"] = message_retention
        __props__.__dict__["name"] = name
        __props__.__dict__["namespace_name"] = namespace_name
        __props__.__dict__["partition_count"] = partition_count
        __props__.__dict__["partition_ids"] = partition_ids
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["status"] = status
        return EventHub(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="captureDescription")
    def capture_description(self) -> pulumi.Output[Optional['outputs.EventHubCaptureDescription']]:
        """
        A `capture_description` block as defined below.
        """
        return pulumi.get(self, "capture_description")

    @property
    @pulumi.getter(name="messageRetention")
    def message_retention(self) -> pulumi.Output[int]:
        """
        Specifies the number of days to retain the events for this Event Hub.

        > **Note:** When using a dedicated Event Hubs cluster, maximum value of `message_retention` is 90 days. When using a shared parent EventHub Namespace, maximum value is 7 days; or 1 day when using a Basic SKU for the shared parent EventHub Namespace.
        """
        return pulumi.get(self, "message_retention")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the EventHub resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "namespace_name")

    @property
    @pulumi.getter(name="partitionCount")
    def partition_count(self) -> pulumi.Output[int]:
        """
        Specifies the current number of shards on the Event Hub.

        > **Note:** `partition_count` cannot be changed unless Eventhub Namespace SKU is `Premium` and cannot be decreased.

        > **Note:** When using a dedicated Event Hubs cluster, maximum value of `partition_count` is 1024. When using a shared parent EventHub Namespace, maximum value is 32.
        """
        return pulumi.get(self, "partition_count")

    @property
    @pulumi.getter(name="partitionIds")
    def partition_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The identifiers for partitions created for Event Hubs.
        """
        return pulumi.get(self, "partition_ids")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which the EventHub's parent Namespace exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the status of the Event Hub resource. Possible values are `Active`, `Disabled` and `SendDisabled`. Defaults to `Active`.
        """
        return pulumi.get(self, "status")


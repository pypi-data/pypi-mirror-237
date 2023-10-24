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

__all__ = ['MedtechServiceArgs', 'MedtechService']

@pulumi.input_type
class MedtechServiceArgs:
    def __init__(__self__, *,
                 device_mapping_json: pulumi.Input[str],
                 eventhub_consumer_group_name: pulumi.Input[str],
                 eventhub_name: pulumi.Input[str],
                 eventhub_namespace_name: pulumi.Input[str],
                 workspace_id: pulumi.Input[str],
                 identity: Optional[pulumi.Input['MedtechServiceIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a MedtechService resource.
        :param pulumi.Input[str] device_mapping_json: Specifies the Device Mappings of the Med Tech Service.
        :param pulumi.Input[str] eventhub_consumer_group_name: Specifies the Consumer Group of the Event Hub to connect to.
        :param pulumi.Input[str] eventhub_name: Specifies the name of the Event Hub to connect to.
        :param pulumi.Input[str] eventhub_namespace_name: Specifies the namespace name of the Event Hub to connect to.
        :param pulumi.Input[str] workspace_id: Specifies the id of the Healthcare Workspace where the Healthcare Med Tech Service should exist. Changing this forces a new Healthcare Med Tech Service to be created.
        :param pulumi.Input['MedtechServiceIdentityArgs'] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Healthcare Med Tech Service should be created. Changing this forces a new Healthcare Med Tech Service to be created.
        :param pulumi.Input[str] name: Specifies the name of the Healthcare Med Tech Service. Changing this forces a new Healthcare Med Tech Service to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the Healthcare Med Tech Service.
        """
        MedtechServiceArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            device_mapping_json=device_mapping_json,
            eventhub_consumer_group_name=eventhub_consumer_group_name,
            eventhub_name=eventhub_name,
            eventhub_namespace_name=eventhub_namespace_name,
            workspace_id=workspace_id,
            identity=identity,
            location=location,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             device_mapping_json: pulumi.Input[str],
             eventhub_consumer_group_name: pulumi.Input[str],
             eventhub_name: pulumi.Input[str],
             eventhub_namespace_name: pulumi.Input[str],
             workspace_id: pulumi.Input[str],
             identity: Optional[pulumi.Input['MedtechServiceIdentityArgs']] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'deviceMappingJson' in kwargs:
            device_mapping_json = kwargs['deviceMappingJson']
        if 'eventhubConsumerGroupName' in kwargs:
            eventhub_consumer_group_name = kwargs['eventhubConsumerGroupName']
        if 'eventhubName' in kwargs:
            eventhub_name = kwargs['eventhubName']
        if 'eventhubNamespaceName' in kwargs:
            eventhub_namespace_name = kwargs['eventhubNamespaceName']
        if 'workspaceId' in kwargs:
            workspace_id = kwargs['workspaceId']

        _setter("device_mapping_json", device_mapping_json)
        _setter("eventhub_consumer_group_name", eventhub_consumer_group_name)
        _setter("eventhub_name", eventhub_name)
        _setter("eventhub_namespace_name", eventhub_namespace_name)
        _setter("workspace_id", workspace_id)
        if identity is not None:
            _setter("identity", identity)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="deviceMappingJson")
    def device_mapping_json(self) -> pulumi.Input[str]:
        """
        Specifies the Device Mappings of the Med Tech Service.
        """
        return pulumi.get(self, "device_mapping_json")

    @device_mapping_json.setter
    def device_mapping_json(self, value: pulumi.Input[str]):
        pulumi.set(self, "device_mapping_json", value)

    @property
    @pulumi.getter(name="eventhubConsumerGroupName")
    def eventhub_consumer_group_name(self) -> pulumi.Input[str]:
        """
        Specifies the Consumer Group of the Event Hub to connect to.
        """
        return pulumi.get(self, "eventhub_consumer_group_name")

    @eventhub_consumer_group_name.setter
    def eventhub_consumer_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "eventhub_consumer_group_name", value)

    @property
    @pulumi.getter(name="eventhubName")
    def eventhub_name(self) -> pulumi.Input[str]:
        """
        Specifies the name of the Event Hub to connect to.
        """
        return pulumi.get(self, "eventhub_name")

    @eventhub_name.setter
    def eventhub_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "eventhub_name", value)

    @property
    @pulumi.getter(name="eventhubNamespaceName")
    def eventhub_namespace_name(self) -> pulumi.Input[str]:
        """
        Specifies the namespace name of the Event Hub to connect to.
        """
        return pulumi.get(self, "eventhub_namespace_name")

    @eventhub_namespace_name.setter
    def eventhub_namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "eventhub_namespace_name", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[str]:
        """
        Specifies the id of the Healthcare Workspace where the Healthcare Med Tech Service should exist. Changing this forces a new Healthcare Med Tech Service to be created.
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_id", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['MedtechServiceIdentityArgs']]:
        """
        An `identity` block as defined below.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['MedtechServiceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Azure Region where the Healthcare Med Tech Service should be created. Changing this forces a new Healthcare Med Tech Service to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Healthcare Med Tech Service. Changing this forces a new Healthcare Med Tech Service to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the Healthcare Med Tech Service.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _MedtechServiceState:
    def __init__(__self__, *,
                 device_mapping_json: Optional[pulumi.Input[str]] = None,
                 eventhub_consumer_group_name: Optional[pulumi.Input[str]] = None,
                 eventhub_name: Optional[pulumi.Input[str]] = None,
                 eventhub_namespace_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['MedtechServiceIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MedtechService resources.
        :param pulumi.Input[str] device_mapping_json: Specifies the Device Mappings of the Med Tech Service.
        :param pulumi.Input[str] eventhub_consumer_group_name: Specifies the Consumer Group of the Event Hub to connect to.
        :param pulumi.Input[str] eventhub_name: Specifies the name of the Event Hub to connect to.
        :param pulumi.Input[str] eventhub_namespace_name: Specifies the namespace name of the Event Hub to connect to.
        :param pulumi.Input['MedtechServiceIdentityArgs'] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Healthcare Med Tech Service should be created. Changing this forces a new Healthcare Med Tech Service to be created.
        :param pulumi.Input[str] name: Specifies the name of the Healthcare Med Tech Service. Changing this forces a new Healthcare Med Tech Service to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the Healthcare Med Tech Service.
        :param pulumi.Input[str] workspace_id: Specifies the id of the Healthcare Workspace where the Healthcare Med Tech Service should exist. Changing this forces a new Healthcare Med Tech Service to be created.
        """
        _MedtechServiceState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            device_mapping_json=device_mapping_json,
            eventhub_consumer_group_name=eventhub_consumer_group_name,
            eventhub_name=eventhub_name,
            eventhub_namespace_name=eventhub_namespace_name,
            identity=identity,
            location=location,
            name=name,
            tags=tags,
            workspace_id=workspace_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             device_mapping_json: Optional[pulumi.Input[str]] = None,
             eventhub_consumer_group_name: Optional[pulumi.Input[str]] = None,
             eventhub_name: Optional[pulumi.Input[str]] = None,
             eventhub_namespace_name: Optional[pulumi.Input[str]] = None,
             identity: Optional[pulumi.Input['MedtechServiceIdentityArgs']] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             workspace_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'deviceMappingJson' in kwargs:
            device_mapping_json = kwargs['deviceMappingJson']
        if 'eventhubConsumerGroupName' in kwargs:
            eventhub_consumer_group_name = kwargs['eventhubConsumerGroupName']
        if 'eventhubName' in kwargs:
            eventhub_name = kwargs['eventhubName']
        if 'eventhubNamespaceName' in kwargs:
            eventhub_namespace_name = kwargs['eventhubNamespaceName']
        if 'workspaceId' in kwargs:
            workspace_id = kwargs['workspaceId']

        if device_mapping_json is not None:
            _setter("device_mapping_json", device_mapping_json)
        if eventhub_consumer_group_name is not None:
            _setter("eventhub_consumer_group_name", eventhub_consumer_group_name)
        if eventhub_name is not None:
            _setter("eventhub_name", eventhub_name)
        if eventhub_namespace_name is not None:
            _setter("eventhub_namespace_name", eventhub_namespace_name)
        if identity is not None:
            _setter("identity", identity)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)
        if workspace_id is not None:
            _setter("workspace_id", workspace_id)

    @property
    @pulumi.getter(name="deviceMappingJson")
    def device_mapping_json(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Device Mappings of the Med Tech Service.
        """
        return pulumi.get(self, "device_mapping_json")

    @device_mapping_json.setter
    def device_mapping_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device_mapping_json", value)

    @property
    @pulumi.getter(name="eventhubConsumerGroupName")
    def eventhub_consumer_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Consumer Group of the Event Hub to connect to.
        """
        return pulumi.get(self, "eventhub_consumer_group_name")

    @eventhub_consumer_group_name.setter
    def eventhub_consumer_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "eventhub_consumer_group_name", value)

    @property
    @pulumi.getter(name="eventhubName")
    def eventhub_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Event Hub to connect to.
        """
        return pulumi.get(self, "eventhub_name")

    @eventhub_name.setter
    def eventhub_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "eventhub_name", value)

    @property
    @pulumi.getter(name="eventhubNamespaceName")
    def eventhub_namespace_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the namespace name of the Event Hub to connect to.
        """
        return pulumi.get(self, "eventhub_namespace_name")

    @eventhub_namespace_name.setter
    def eventhub_namespace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "eventhub_namespace_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['MedtechServiceIdentityArgs']]:
        """
        An `identity` block as defined below.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['MedtechServiceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Azure Region where the Healthcare Med Tech Service should be created. Changing this forces a new Healthcare Med Tech Service to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Healthcare Med Tech Service. Changing this forces a new Healthcare Med Tech Service to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the Healthcare Med Tech Service.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the id of the Healthcare Workspace where the Healthcare Med Tech Service should exist. Changing this forces a new Healthcare Med Tech Service to be created.
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_id", value)


class MedtechService(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 device_mapping_json: Optional[pulumi.Input[str]] = None,
                 eventhub_consumer_group_name: Optional[pulumi.Input[str]] = None,
                 eventhub_name: Optional[pulumi.Input[str]] = None,
                 eventhub_namespace_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['MedtechServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Healthcare Med Tech Service.

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="east us")
        example_workspace = azure.healthcare.Workspace("exampleWorkspace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_medtech_service = azure.healthcare.MedtechService("exampleMedtechService",
            workspace_id=example_workspace.id,
            location="east us",
            identity=azure.healthcare.MedtechServiceIdentityArgs(
                type="SystemAssigned",
            ),
            eventhub_namespace_name="example-eventhub-namespace",
            eventhub_name="example-eventhub",
            eventhub_consumer_group_name="$Default",
            device_mapping_json=json.dumps({
                "templateType": "CollectionContent",
                "template": [{
                    "templateType": "JsonPathContent",
                    "template": {
                        "typeName": "heartrate",
                        "typeMatchExpression": "$..[?(@heartrate)]",
                        "deviceIdExpression": "$.deviceid",
                        "timestampExpression": "$.measurementdatetime",
                        "values": [{
                            "required": "true",
                            "valueExpression": "$.heartrate",
                            "valueName": "hr",
                        }],
                    },
                }],
            }))
        ```

        ## Import

        Healthcare Med Tech Service can be imported using the resource`id`, e.g.

        ```sh
         $ pulumi import azure:healthcare/medtechService:MedtechService example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/group1/providers/Microsoft.HealthcareApis/workspaces/workspace1/iotConnectors/iotconnector1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] device_mapping_json: Specifies the Device Mappings of the Med Tech Service.
        :param pulumi.Input[str] eventhub_consumer_group_name: Specifies the Consumer Group of the Event Hub to connect to.
        :param pulumi.Input[str] eventhub_name: Specifies the name of the Event Hub to connect to.
        :param pulumi.Input[str] eventhub_namespace_name: Specifies the namespace name of the Event Hub to connect to.
        :param pulumi.Input[pulumi.InputType['MedtechServiceIdentityArgs']] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Healthcare Med Tech Service should be created. Changing this forces a new Healthcare Med Tech Service to be created.
        :param pulumi.Input[str] name: Specifies the name of the Healthcare Med Tech Service. Changing this forces a new Healthcare Med Tech Service to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the Healthcare Med Tech Service.
        :param pulumi.Input[str] workspace_id: Specifies the id of the Healthcare Workspace where the Healthcare Med Tech Service should exist. Changing this forces a new Healthcare Med Tech Service to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MedtechServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Healthcare Med Tech Service.

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="east us")
        example_workspace = azure.healthcare.Workspace("exampleWorkspace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_medtech_service = azure.healthcare.MedtechService("exampleMedtechService",
            workspace_id=example_workspace.id,
            location="east us",
            identity=azure.healthcare.MedtechServiceIdentityArgs(
                type="SystemAssigned",
            ),
            eventhub_namespace_name="example-eventhub-namespace",
            eventhub_name="example-eventhub",
            eventhub_consumer_group_name="$Default",
            device_mapping_json=json.dumps({
                "templateType": "CollectionContent",
                "template": [{
                    "templateType": "JsonPathContent",
                    "template": {
                        "typeName": "heartrate",
                        "typeMatchExpression": "$..[?(@heartrate)]",
                        "deviceIdExpression": "$.deviceid",
                        "timestampExpression": "$.measurementdatetime",
                        "values": [{
                            "required": "true",
                            "valueExpression": "$.heartrate",
                            "valueName": "hr",
                        }],
                    },
                }],
            }))
        ```

        ## Import

        Healthcare Med Tech Service can be imported using the resource`id`, e.g.

        ```sh
         $ pulumi import azure:healthcare/medtechService:MedtechService example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/group1/providers/Microsoft.HealthcareApis/workspaces/workspace1/iotConnectors/iotconnector1
        ```

        :param str resource_name: The name of the resource.
        :param MedtechServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MedtechServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            MedtechServiceArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 device_mapping_json: Optional[pulumi.Input[str]] = None,
                 eventhub_consumer_group_name: Optional[pulumi.Input[str]] = None,
                 eventhub_name: Optional[pulumi.Input[str]] = None,
                 eventhub_namespace_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['MedtechServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MedtechServiceArgs.__new__(MedtechServiceArgs)

            if device_mapping_json is None and not opts.urn:
                raise TypeError("Missing required property 'device_mapping_json'")
            __props__.__dict__["device_mapping_json"] = device_mapping_json
            if eventhub_consumer_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'eventhub_consumer_group_name'")
            __props__.__dict__["eventhub_consumer_group_name"] = eventhub_consumer_group_name
            if eventhub_name is None and not opts.urn:
                raise TypeError("Missing required property 'eventhub_name'")
            __props__.__dict__["eventhub_name"] = eventhub_name
            if eventhub_namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'eventhub_namespace_name'")
            __props__.__dict__["eventhub_namespace_name"] = eventhub_namespace_name
            if identity is not None and not isinstance(identity, MedtechServiceIdentityArgs):
                identity = identity or {}
                def _setter(key, value):
                    identity[key] = value
                MedtechServiceIdentityArgs._configure(_setter, **identity)
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            if workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_id'")
            __props__.__dict__["workspace_id"] = workspace_id
        super(MedtechService, __self__).__init__(
            'azure:healthcare/medtechService:MedtechService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            device_mapping_json: Optional[pulumi.Input[str]] = None,
            eventhub_consumer_group_name: Optional[pulumi.Input[str]] = None,
            eventhub_name: Optional[pulumi.Input[str]] = None,
            eventhub_namespace_name: Optional[pulumi.Input[str]] = None,
            identity: Optional[pulumi.Input[pulumi.InputType['MedtechServiceIdentityArgs']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            workspace_id: Optional[pulumi.Input[str]] = None) -> 'MedtechService':
        """
        Get an existing MedtechService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] device_mapping_json: Specifies the Device Mappings of the Med Tech Service.
        :param pulumi.Input[str] eventhub_consumer_group_name: Specifies the Consumer Group of the Event Hub to connect to.
        :param pulumi.Input[str] eventhub_name: Specifies the name of the Event Hub to connect to.
        :param pulumi.Input[str] eventhub_namespace_name: Specifies the namespace name of the Event Hub to connect to.
        :param pulumi.Input[pulumi.InputType['MedtechServiceIdentityArgs']] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Healthcare Med Tech Service should be created. Changing this forces a new Healthcare Med Tech Service to be created.
        :param pulumi.Input[str] name: Specifies the name of the Healthcare Med Tech Service. Changing this forces a new Healthcare Med Tech Service to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the Healthcare Med Tech Service.
        :param pulumi.Input[str] workspace_id: Specifies the id of the Healthcare Workspace where the Healthcare Med Tech Service should exist. Changing this forces a new Healthcare Med Tech Service to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MedtechServiceState.__new__(_MedtechServiceState)

        __props__.__dict__["device_mapping_json"] = device_mapping_json
        __props__.__dict__["eventhub_consumer_group_name"] = eventhub_consumer_group_name
        __props__.__dict__["eventhub_name"] = eventhub_name
        __props__.__dict__["eventhub_namespace_name"] = eventhub_namespace_name
        __props__.__dict__["identity"] = identity
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["tags"] = tags
        __props__.__dict__["workspace_id"] = workspace_id
        return MedtechService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deviceMappingJson")
    def device_mapping_json(self) -> pulumi.Output[str]:
        """
        Specifies the Device Mappings of the Med Tech Service.
        """
        return pulumi.get(self, "device_mapping_json")

    @property
    @pulumi.getter(name="eventhubConsumerGroupName")
    def eventhub_consumer_group_name(self) -> pulumi.Output[str]:
        """
        Specifies the Consumer Group of the Event Hub to connect to.
        """
        return pulumi.get(self, "eventhub_consumer_group_name")

    @property
    @pulumi.getter(name="eventhubName")
    def eventhub_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Event Hub to connect to.
        """
        return pulumi.get(self, "eventhub_name")

    @property
    @pulumi.getter(name="eventhubNamespaceName")
    def eventhub_namespace_name(self) -> pulumi.Output[str]:
        """
        Specifies the namespace name of the Event Hub to connect to.
        """
        return pulumi.get(self, "eventhub_namespace_name")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.MedtechServiceIdentity']]:
        """
        An `identity` block as defined below.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the Azure Region where the Healthcare Med Tech Service should be created. Changing this forces a new Healthcare Med Tech Service to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Healthcare Med Tech Service. Changing this forces a new Healthcare Med Tech Service to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the Healthcare Med Tech Service.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[str]:
        """
        Specifies the id of the Healthcare Workspace where the Healthcare Med Tech Service should exist. Changing this forces a new Healthcare Med Tech Service to be created.
        """
        return pulumi.get(self, "workspace_id")


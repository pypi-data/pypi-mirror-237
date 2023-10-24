# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['NamespaceSchemaGroupArgs', 'NamespaceSchemaGroup']

@pulumi.input_type
class NamespaceSchemaGroupArgs:
    def __init__(__self__, *,
                 namespace_id: pulumi.Input[str],
                 schema_compatibility: pulumi.Input[str],
                 schema_type: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NamespaceSchemaGroup resource.
        :param pulumi.Input[str] namespace_id: Specifies the ID of the EventHub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] schema_compatibility: Specifies the compatibility of this schema group. Possible values are `None`, `Backward`, `Forward`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] schema_type: Specifies the Type of this schema group. Possible values are `Avro`, `Unknown`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of this schema group. Changing this forces a new resource to be created.
        """
        NamespaceSchemaGroupArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            namespace_id=namespace_id,
            schema_compatibility=schema_compatibility,
            schema_type=schema_type,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             namespace_id: pulumi.Input[str],
             schema_compatibility: pulumi.Input[str],
             schema_type: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'namespaceId' in kwargs:
            namespace_id = kwargs['namespaceId']
        if 'schemaCompatibility' in kwargs:
            schema_compatibility = kwargs['schemaCompatibility']
        if 'schemaType' in kwargs:
            schema_type = kwargs['schemaType']

        _setter("namespace_id", namespace_id)
        _setter("schema_compatibility", schema_compatibility)
        _setter("schema_type", schema_type)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> pulumi.Input[str]:
        """
        Specifies the ID of the EventHub Namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "namespace_id")

    @namespace_id.setter
    def namespace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_id", value)

    @property
    @pulumi.getter(name="schemaCompatibility")
    def schema_compatibility(self) -> pulumi.Input[str]:
        """
        Specifies the compatibility of this schema group. Possible values are `None`, `Backward`, `Forward`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "schema_compatibility")

    @schema_compatibility.setter
    def schema_compatibility(self, value: pulumi.Input[str]):
        pulumi.set(self, "schema_compatibility", value)

    @property
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> pulumi.Input[str]:
        """
        Specifies the Type of this schema group. Possible values are `Avro`, `Unknown`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "schema_type")

    @schema_type.setter
    def schema_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "schema_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of this schema group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _NamespaceSchemaGroupState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 schema_compatibility: Optional[pulumi.Input[str]] = None,
                 schema_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering NamespaceSchemaGroup resources.
        :param pulumi.Input[str] name: Specifies the name of this schema group. Changing this forces a new resource to be created.
        :param pulumi.Input[str] namespace_id: Specifies the ID of the EventHub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] schema_compatibility: Specifies the compatibility of this schema group. Possible values are `None`, `Backward`, `Forward`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] schema_type: Specifies the Type of this schema group. Possible values are `Avro`, `Unknown`. Changing this forces a new resource to be created.
        """
        _NamespaceSchemaGroupState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            namespace_id=namespace_id,
            schema_compatibility=schema_compatibility,
            schema_type=schema_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             namespace_id: Optional[pulumi.Input[str]] = None,
             schema_compatibility: Optional[pulumi.Input[str]] = None,
             schema_type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'namespaceId' in kwargs:
            namespace_id = kwargs['namespaceId']
        if 'schemaCompatibility' in kwargs:
            schema_compatibility = kwargs['schemaCompatibility']
        if 'schemaType' in kwargs:
            schema_type = kwargs['schemaType']

        if name is not None:
            _setter("name", name)
        if namespace_id is not None:
            _setter("namespace_id", namespace_id)
        if schema_compatibility is not None:
            _setter("schema_compatibility", schema_compatibility)
        if schema_type is not None:
            _setter("schema_type", schema_type)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of this schema group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the ID of the EventHub Namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "namespace_id")

    @namespace_id.setter
    def namespace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_id", value)

    @property
    @pulumi.getter(name="schemaCompatibility")
    def schema_compatibility(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the compatibility of this schema group. Possible values are `None`, `Backward`, `Forward`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "schema_compatibility")

    @schema_compatibility.setter
    def schema_compatibility(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema_compatibility", value)

    @property
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Type of this schema group. Possible values are `Avro`, `Unknown`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "schema_type")

    @schema_type.setter
    def schema_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema_type", value)


class NamespaceSchemaGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 schema_compatibility: Optional[pulumi.Input[str]] = None,
                 schema_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example", location="East US")
        test_event_hub_namespace = azure.eventhub.EventHubNamespace("testEventHubNamespace",
            location=azurerm_resource_group["test"]["location"],
            resource_group_name=azurerm_resource_group["test"]["name"],
            sku="Standard")
        test_namespace_schema_group = azure.eventhub.NamespaceSchemaGroup("testNamespaceSchemaGroup",
            namespace_id=test_event_hub_namespace.id,
            schema_compatibility="Forward",
            schema_type="Avro")
        ```

        ## Import

        Schema Group for a EventHub Namespace can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:eventhub/namespaceSchemaGroup:NamespaceSchemaGroup example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.EventHub/namespaces/namespace1/schemaGroups/group1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Specifies the name of this schema group. Changing this forces a new resource to be created.
        :param pulumi.Input[str] namespace_id: Specifies the ID of the EventHub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] schema_compatibility: Specifies the compatibility of this schema group. Possible values are `None`, `Backward`, `Forward`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] schema_type: Specifies the Type of this schema group. Possible values are `Avro`, `Unknown`. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamespaceSchemaGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example", location="East US")
        test_event_hub_namespace = azure.eventhub.EventHubNamespace("testEventHubNamespace",
            location=azurerm_resource_group["test"]["location"],
            resource_group_name=azurerm_resource_group["test"]["name"],
            sku="Standard")
        test_namespace_schema_group = azure.eventhub.NamespaceSchemaGroup("testNamespaceSchemaGroup",
            namespace_id=test_event_hub_namespace.id,
            schema_compatibility="Forward",
            schema_type="Avro")
        ```

        ## Import

        Schema Group for a EventHub Namespace can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:eventhub/namespaceSchemaGroup:NamespaceSchemaGroup example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.EventHub/namespaces/namespace1/schemaGroups/group1
        ```

        :param str resource_name: The name of the resource.
        :param NamespaceSchemaGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamespaceSchemaGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            NamespaceSchemaGroupArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 schema_compatibility: Optional[pulumi.Input[str]] = None,
                 schema_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NamespaceSchemaGroupArgs.__new__(NamespaceSchemaGroupArgs)

            __props__.__dict__["name"] = name
            if namespace_id is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_id'")
            __props__.__dict__["namespace_id"] = namespace_id
            if schema_compatibility is None and not opts.urn:
                raise TypeError("Missing required property 'schema_compatibility'")
            __props__.__dict__["schema_compatibility"] = schema_compatibility
            if schema_type is None and not opts.urn:
                raise TypeError("Missing required property 'schema_type'")
            __props__.__dict__["schema_type"] = schema_type
        super(NamespaceSchemaGroup, __self__).__init__(
            'azure:eventhub/namespaceSchemaGroup:NamespaceSchemaGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace_id: Optional[pulumi.Input[str]] = None,
            schema_compatibility: Optional[pulumi.Input[str]] = None,
            schema_type: Optional[pulumi.Input[str]] = None) -> 'NamespaceSchemaGroup':
        """
        Get an existing NamespaceSchemaGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Specifies the name of this schema group. Changing this forces a new resource to be created.
        :param pulumi.Input[str] namespace_id: Specifies the ID of the EventHub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] schema_compatibility: Specifies the compatibility of this schema group. Possible values are `None`, `Backward`, `Forward`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] schema_type: Specifies the Type of this schema group. Possible values are `Avro`, `Unknown`. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NamespaceSchemaGroupState.__new__(_NamespaceSchemaGroupState)

        __props__.__dict__["name"] = name
        __props__.__dict__["namespace_id"] = namespace_id
        __props__.__dict__["schema_compatibility"] = schema_compatibility
        __props__.__dict__["schema_type"] = schema_type
        return NamespaceSchemaGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of this schema group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> pulumi.Output[str]:
        """
        Specifies the ID of the EventHub Namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "namespace_id")

    @property
    @pulumi.getter(name="schemaCompatibility")
    def schema_compatibility(self) -> pulumi.Output[str]:
        """
        Specifies the compatibility of this schema group. Possible values are `None`, `Backward`, `Forward`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "schema_compatibility")

    @property
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> pulumi.Output[str]:
        """
        Specifies the Type of this schema group. Possible values are `Avro`, `Unknown`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "schema_type")


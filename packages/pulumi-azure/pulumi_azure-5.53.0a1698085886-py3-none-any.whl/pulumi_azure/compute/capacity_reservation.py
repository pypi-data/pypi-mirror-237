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

__all__ = ['CapacityReservationArgs', 'CapacityReservation']

@pulumi.input_type
class CapacityReservationArgs:
    def __init__(__self__, *,
                 capacity_reservation_group_id: pulumi.Input[str],
                 sku: pulumi.Input['CapacityReservationSkuArgs'],
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CapacityReservation resource.
        :param pulumi.Input[str] capacity_reservation_group_id: The ID of the Capacity Reservation Group where the Capacity Reservation exists. Changing this forces a new resource to be created.
        :param pulumi.Input['CapacityReservationSkuArgs'] sku: A `sku` block as defined below.
        :param pulumi.Input[str] name: Specifies the name of this Capacity Reservation. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] zone: Specifies the Availability Zone for this Capacity Reservation. Changing this forces a new resource to be created.
        """
        CapacityReservationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            capacity_reservation_group_id=capacity_reservation_group_id,
            sku=sku,
            name=name,
            tags=tags,
            zone=zone,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             capacity_reservation_group_id: pulumi.Input[str],
             sku: pulumi.Input['CapacityReservationSkuArgs'],
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             zone: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'capacityReservationGroupId' in kwargs:
            capacity_reservation_group_id = kwargs['capacityReservationGroupId']

        _setter("capacity_reservation_group_id", capacity_reservation_group_id)
        _setter("sku", sku)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)
        if zone is not None:
            _setter("zone", zone)

    @property
    @pulumi.getter(name="capacityReservationGroupId")
    def capacity_reservation_group_id(self) -> pulumi.Input[str]:
        """
        The ID of the Capacity Reservation Group where the Capacity Reservation exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "capacity_reservation_group_id")

    @capacity_reservation_group_id.setter
    def capacity_reservation_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "capacity_reservation_group_id", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input['CapacityReservationSkuArgs']:
        """
        A `sku` block as defined below.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['CapacityReservationSkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of this Capacity Reservation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Availability Zone for this Capacity Reservation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


@pulumi.input_type
class _CapacityReservationState:
    def __init__(__self__, *,
                 capacity_reservation_group_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['CapacityReservationSkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CapacityReservation resources.
        :param pulumi.Input[str] capacity_reservation_group_id: The ID of the Capacity Reservation Group where the Capacity Reservation exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of this Capacity Reservation. Changing this forces a new resource to be created.
        :param pulumi.Input['CapacityReservationSkuArgs'] sku: A `sku` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] zone: Specifies the Availability Zone for this Capacity Reservation. Changing this forces a new resource to be created.
        """
        _CapacityReservationState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            capacity_reservation_group_id=capacity_reservation_group_id,
            name=name,
            sku=sku,
            tags=tags,
            zone=zone,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             capacity_reservation_group_id: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             sku: Optional[pulumi.Input['CapacityReservationSkuArgs']] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             zone: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'capacityReservationGroupId' in kwargs:
            capacity_reservation_group_id = kwargs['capacityReservationGroupId']

        if capacity_reservation_group_id is not None:
            _setter("capacity_reservation_group_id", capacity_reservation_group_id)
        if name is not None:
            _setter("name", name)
        if sku is not None:
            _setter("sku", sku)
        if tags is not None:
            _setter("tags", tags)
        if zone is not None:
            _setter("zone", zone)

    @property
    @pulumi.getter(name="capacityReservationGroupId")
    def capacity_reservation_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Capacity Reservation Group where the Capacity Reservation exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "capacity_reservation_group_id")

    @capacity_reservation_group_id.setter
    def capacity_reservation_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "capacity_reservation_group_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of this Capacity Reservation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['CapacityReservationSkuArgs']]:
        """
        A `sku` block as defined below.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['CapacityReservationSkuArgs']]):
        pulumi.set(self, "sku", value)

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
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Availability Zone for this Capacity Reservation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class CapacityReservation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capacity_reservation_group_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['CapacityReservationSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Capacity Reservation within a Capacity Reservation Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_capacity_reservation_group = azure.compute.CapacityReservationGroup("exampleCapacityReservationGroup",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_capacity_reservation = azure.compute.CapacityReservation("exampleCapacityReservation",
            capacity_reservation_group_id=example_capacity_reservation_group.id,
            sku=azure.compute.CapacityReservationSkuArgs(
                name="Standard_D2s_v3",
                capacity=1,
            ))
        ```

        ## Import

        Capacity Reservations can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:compute/capacityReservation:CapacityReservation example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Compute/capacityReservationGroups/capacityReservationGroup1/capacityReservations/capacityReservation1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] capacity_reservation_group_id: The ID of the Capacity Reservation Group where the Capacity Reservation exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of this Capacity Reservation. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['CapacityReservationSkuArgs']] sku: A `sku` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] zone: Specifies the Availability Zone for this Capacity Reservation. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CapacityReservationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Capacity Reservation within a Capacity Reservation Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_capacity_reservation_group = azure.compute.CapacityReservationGroup("exampleCapacityReservationGroup",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_capacity_reservation = azure.compute.CapacityReservation("exampleCapacityReservation",
            capacity_reservation_group_id=example_capacity_reservation_group.id,
            sku=azure.compute.CapacityReservationSkuArgs(
                name="Standard_D2s_v3",
                capacity=1,
            ))
        ```

        ## Import

        Capacity Reservations can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:compute/capacityReservation:CapacityReservation example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Compute/capacityReservationGroups/capacityReservationGroup1/capacityReservations/capacityReservation1
        ```

        :param str resource_name: The name of the resource.
        :param CapacityReservationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CapacityReservationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CapacityReservationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capacity_reservation_group_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['CapacityReservationSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CapacityReservationArgs.__new__(CapacityReservationArgs)

            if capacity_reservation_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'capacity_reservation_group_id'")
            __props__.__dict__["capacity_reservation_group_id"] = capacity_reservation_group_id
            __props__.__dict__["name"] = name
            if sku is not None and not isinstance(sku, CapacityReservationSkuArgs):
                sku = sku or {}
                def _setter(key, value):
                    sku[key] = value
                CapacityReservationSkuArgs._configure(_setter, **sku)
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zone"] = zone
        super(CapacityReservation, __self__).__init__(
            'azure:compute/capacityReservation:CapacityReservation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            capacity_reservation_group_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            sku: Optional[pulumi.Input[pulumi.InputType['CapacityReservationSkuArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'CapacityReservation':
        """
        Get an existing CapacityReservation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] capacity_reservation_group_id: The ID of the Capacity Reservation Group where the Capacity Reservation exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of this Capacity Reservation. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['CapacityReservationSkuArgs']] sku: A `sku` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] zone: Specifies the Availability Zone for this Capacity Reservation. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CapacityReservationState.__new__(_CapacityReservationState)

        __props__.__dict__["capacity_reservation_group_id"] = capacity_reservation_group_id
        __props__.__dict__["name"] = name
        __props__.__dict__["sku"] = sku
        __props__.__dict__["tags"] = tags
        __props__.__dict__["zone"] = zone
        return CapacityReservation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="capacityReservationGroupId")
    def capacity_reservation_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the Capacity Reservation Group where the Capacity Reservation exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "capacity_reservation_group_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of this Capacity Reservation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.CapacityReservationSku']:
        """
        A `sku` block as defined below.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the Availability Zone for this Capacity Reservation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")


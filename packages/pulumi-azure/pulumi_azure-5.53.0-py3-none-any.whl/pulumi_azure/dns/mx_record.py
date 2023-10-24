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

__all__ = ['MxRecordArgs', 'MxRecord']

@pulumi.input_type
class MxRecordArgs:
    def __init__(__self__, *,
                 records: pulumi.Input[Sequence[pulumi.Input['MxRecordRecordArgs']]],
                 resource_group_name: pulumi.Input[str],
                 ttl: pulumi.Input[int],
                 zone_name: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a MxRecord resource.
        :param pulumi.Input[Sequence[pulumi.Input['MxRecordRecordArgs']]] records: A list of values that make up the MX record. Each `record` block supports fields documented below.
        :param pulumi.Input[str] resource_group_name: Specifies the resource group where the DNS Zone (parent resource) exists. Changing this forces a new resource to be created.
        :param pulumi.Input[int] ttl: The Time To Live (TTL) of the DNS record in seconds.
        :param pulumi.Input[str] zone_name: Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the DNS MX Record. Defaults to `@` (root). Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        MxRecordArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            records=records,
            resource_group_name=resource_group_name,
            ttl=ttl,
            zone_name=zone_name,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             records: pulumi.Input[Sequence[pulumi.Input['MxRecordRecordArgs']]],
             resource_group_name: pulumi.Input[str],
             ttl: pulumi.Input[int],
             zone_name: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'zoneName' in kwargs:
            zone_name = kwargs['zoneName']

        _setter("records", records)
        _setter("resource_group_name", resource_group_name)
        _setter("ttl", ttl)
        _setter("zone_name", zone_name)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter
    def records(self) -> pulumi.Input[Sequence[pulumi.Input['MxRecordRecordArgs']]]:
        """
        A list of values that make up the MX record. Each `record` block supports fields documented below.
        """
        return pulumi.get(self, "records")

    @records.setter
    def records(self, value: pulumi.Input[Sequence[pulumi.Input['MxRecordRecordArgs']]]):
        pulumi.set(self, "records", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Specifies the resource group where the DNS Zone (parent resource) exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Input[int]:
        """
        The Time To Live (TTL) of the DNS record in seconds.
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: pulumi.Input[int]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> pulumi.Input[str]:
        """
        Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone_name")

    @zone_name.setter
    def zone_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the DNS MX Record. Defaults to `@` (root). Changing this forces a new resource to be created.
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


@pulumi.input_type
class _MxRecordState:
    def __init__(__self__, *,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 records: Optional[pulumi.Input[Sequence[pulumi.Input['MxRecordRecordArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MxRecord resources.
        :param pulumi.Input[str] fqdn: The FQDN of the DNS MX Record.
        :param pulumi.Input[str] name: The name of the DNS MX Record. Defaults to `@` (root). Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input['MxRecordRecordArgs']]] records: A list of values that make up the MX record. Each `record` block supports fields documented below.
        :param pulumi.Input[str] resource_group_name: Specifies the resource group where the DNS Zone (parent resource) exists. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[int] ttl: The Time To Live (TTL) of the DNS record in seconds.
        :param pulumi.Input[str] zone_name: Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.
        """
        _MxRecordState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            fqdn=fqdn,
            name=name,
            records=records,
            resource_group_name=resource_group_name,
            tags=tags,
            ttl=ttl,
            zone_name=zone_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             fqdn: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             records: Optional[pulumi.Input[Sequence[pulumi.Input['MxRecordRecordArgs']]]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             ttl: Optional[pulumi.Input[int]] = None,
             zone_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'zoneName' in kwargs:
            zone_name = kwargs['zoneName']

        if fqdn is not None:
            _setter("fqdn", fqdn)
        if name is not None:
            _setter("name", name)
        if records is not None:
            _setter("records", records)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if tags is not None:
            _setter("tags", tags)
        if ttl is not None:
            _setter("ttl", ttl)
        if zone_name is not None:
            _setter("zone_name", zone_name)

    @property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[str]]:
        """
        The FQDN of the DNS MX Record.
        """
        return pulumi.get(self, "fqdn")

    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fqdn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the DNS MX Record. Defaults to `@` (root). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MxRecordRecordArgs']]]]:
        """
        A list of values that make up the MX record. Each `record` block supports fields documented below.
        """
        return pulumi.get(self, "records")

    @records.setter
    def records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MxRecordRecordArgs']]]]):
        pulumi.set(self, "records", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the resource group where the DNS Zone (parent resource) exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

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
    def ttl(self) -> Optional[pulumi.Input[int]]:
        """
        The Time To Live (TTL) of the DNS record in seconds.
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone_name")

    @zone_name.setter
    def zone_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_name", value)


class MxRecord(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MxRecordRecordArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_zone = azure.dns.Zone("exampleZone", resource_group_name=example_resource_group.name)
        example_mx_record = azure.dns.MxRecord("exampleMxRecord",
            zone_name=example_zone.name,
            resource_group_name=example_resource_group.name,
            ttl=300,
            records=[
                azure.dns.MxRecordRecordArgs(
                    preference="10",
                    exchange="mail1.contoso.com",
                ),
                azure.dns.MxRecordRecordArgs(
                    preference="20",
                    exchange="mail2.contoso.com",
                ),
            ],
            tags={
                "Environment": "Production",
            })
        ```

        ## Import

        MX records can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:dns/mxRecord:MxRecord example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/dnsZones/zone1/MX/myrecord1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the DNS MX Record. Defaults to `@` (root). Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MxRecordRecordArgs']]]] records: A list of values that make up the MX record. Each `record` block supports fields documented below.
        :param pulumi.Input[str] resource_group_name: Specifies the resource group where the DNS Zone (parent resource) exists. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[int] ttl: The Time To Live (TTL) of the DNS record in seconds.
        :param pulumi.Input[str] zone_name: Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MxRecordArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_zone = azure.dns.Zone("exampleZone", resource_group_name=example_resource_group.name)
        example_mx_record = azure.dns.MxRecord("exampleMxRecord",
            zone_name=example_zone.name,
            resource_group_name=example_resource_group.name,
            ttl=300,
            records=[
                azure.dns.MxRecordRecordArgs(
                    preference="10",
                    exchange="mail1.contoso.com",
                ),
                azure.dns.MxRecordRecordArgs(
                    preference="20",
                    exchange="mail2.contoso.com",
                ),
            ],
            tags={
                "Environment": "Production",
            })
        ```

        ## Import

        MX records can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:dns/mxRecord:MxRecord example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/dnsZones/zone1/MX/myrecord1
        ```

        :param str resource_name: The name of the resource.
        :param MxRecordArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MxRecordArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            MxRecordArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MxRecordRecordArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MxRecordArgs.__new__(MxRecordArgs)

            __props__.__dict__["name"] = name
            if records is None and not opts.urn:
                raise TypeError("Missing required property 'records'")
            __props__.__dict__["records"] = records
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            if ttl is None and not opts.urn:
                raise TypeError("Missing required property 'ttl'")
            __props__.__dict__["ttl"] = ttl
            if zone_name is None and not opts.urn:
                raise TypeError("Missing required property 'zone_name'")
            __props__.__dict__["zone_name"] = zone_name
            __props__.__dict__["fqdn"] = None
        super(MxRecord, __self__).__init__(
            'azure:dns/mxRecord:MxRecord',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            fqdn: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MxRecordRecordArgs']]]]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            ttl: Optional[pulumi.Input[int]] = None,
            zone_name: Optional[pulumi.Input[str]] = None) -> 'MxRecord':
        """
        Get an existing MxRecord resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] fqdn: The FQDN of the DNS MX Record.
        :param pulumi.Input[str] name: The name of the DNS MX Record. Defaults to `@` (root). Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MxRecordRecordArgs']]]] records: A list of values that make up the MX record. Each `record` block supports fields documented below.
        :param pulumi.Input[str] resource_group_name: Specifies the resource group where the DNS Zone (parent resource) exists. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[int] ttl: The Time To Live (TTL) of the DNS record in seconds.
        :param pulumi.Input[str] zone_name: Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MxRecordState.__new__(_MxRecordState)

        __props__.__dict__["fqdn"] = fqdn
        __props__.__dict__["name"] = name
        __props__.__dict__["records"] = records
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["tags"] = tags
        __props__.__dict__["ttl"] = ttl
        __props__.__dict__["zone_name"] = zone_name
        return MxRecord(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[str]:
        """
        The FQDN of the DNS MX Record.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the DNS MX Record. Defaults to `@` (root). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def records(self) -> pulumi.Output[Sequence['outputs.MxRecordRecord']]:
        """
        A list of values that make up the MX record. Each `record` block supports fields documented below.
        """
        return pulumi.get(self, "records")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        Specifies the resource group where the DNS Zone (parent resource) exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[int]:
        """
        The Time To Live (TTL) of the DNS record in seconds.
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> pulumi.Output[str]:
        """
        Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone_name")


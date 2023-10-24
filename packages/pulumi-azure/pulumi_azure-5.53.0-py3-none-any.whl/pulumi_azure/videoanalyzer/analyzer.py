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

__all__ = ['AnalyzerArgs', 'Analyzer']

@pulumi.input_type
class AnalyzerArgs:
    def __init__(__self__, *,
                 identity: pulumi.Input['AnalyzerIdentityArgs'],
                 resource_group_name: pulumi.Input[str],
                 storage_account: pulumi.Input['AnalyzerStorageAccountArgs'],
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Analyzer resource.
        :param pulumi.Input['AnalyzerIdentityArgs'] identity: An `identity` block as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Video Analyzer. Changing this forces a new resource to be created.
        :param pulumi.Input['AnalyzerStorageAccountArgs'] storage_account: A `storage_account` block as defined below.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Video Analyzer. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags assigned to the resource.
        """
        AnalyzerArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            identity=identity,
            resource_group_name=resource_group_name,
            storage_account=storage_account,
            location=location,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             identity: pulumi.Input['AnalyzerIdentityArgs'],
             resource_group_name: pulumi.Input[str],
             storage_account: pulumi.Input['AnalyzerStorageAccountArgs'],
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'storageAccount' in kwargs:
            storage_account = kwargs['storageAccount']

        _setter("identity", identity)
        _setter("resource_group_name", resource_group_name)
        _setter("storage_account", storage_account)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Input['AnalyzerIdentityArgs']:
        """
        An `identity` block as defined below.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: pulumi.Input['AnalyzerIdentityArgs']):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group in which to create the Video Analyzer. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> pulumi.Input['AnalyzerStorageAccountArgs']:
        """
        A `storage_account` block as defined below.
        """
        return pulumi.get(self, "storage_account")

    @storage_account.setter
    def storage_account(self, value: pulumi.Input['AnalyzerStorageAccountArgs']):
        pulumi.set(self, "storage_account", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Video Analyzer. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags assigned to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _AnalyzerState:
    def __init__(__self__, *,
                 identity: Optional[pulumi.Input['AnalyzerIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account: Optional[pulumi.Input['AnalyzerStorageAccountArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Analyzer resources.
        :param pulumi.Input['AnalyzerIdentityArgs'] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Video Analyzer. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Video Analyzer. Changing this forces a new resource to be created.
        :param pulumi.Input['AnalyzerStorageAccountArgs'] storage_account: A `storage_account` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags assigned to the resource.
        """
        _AnalyzerState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            identity=identity,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            storage_account=storage_account,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             identity: Optional[pulumi.Input['AnalyzerIdentityArgs']] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             storage_account: Optional[pulumi.Input['AnalyzerStorageAccountArgs']] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'storageAccount' in kwargs:
            storage_account = kwargs['storageAccount']

        if identity is not None:
            _setter("identity", identity)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if storage_account is not None:
            _setter("storage_account", storage_account)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['AnalyzerIdentityArgs']]:
        """
        An `identity` block as defined below.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['AnalyzerIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Video Analyzer. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group in which to create the Video Analyzer. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> Optional[pulumi.Input['AnalyzerStorageAccountArgs']]:
        """
        A `storage_account` block as defined below.
        """
        return pulumi.get(self, "storage_account")

    @storage_account.setter
    def storage_account(self, value: Optional[pulumi.Input['AnalyzerStorageAccountArgs']]):
        pulumi.set(self, "storage_account", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags assigned to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Analyzer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['AnalyzerIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account: Optional[pulumi.Input[pulumi.InputType['AnalyzerStorageAccountArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages a Video Analyzer.

        !> Video Analyzer (Preview) is now Deprecated and will be Retired on 2022-11-30 - as such the `videoanalyzer.Analyzer` resource is deprecated and will be removed in v4.0 of the AzureRM Provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="GRS")
        example_user_assigned_identity = azure.authorization.UserAssignedIdentity("exampleUserAssignedIdentity",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        contributor = azure.authorization.Assignment("contributor",
            scope=example_account.id,
            role_definition_name="Storage Blob Data Contributor",
            principal_id=example_user_assigned_identity.principal_id)
        reader = azure.authorization.Assignment("reader",
            scope=example_account.id,
            role_definition_name="Reader",
            principal_id=example_user_assigned_identity.principal_id)
        example_analyzer = azure.videoanalyzer.Analyzer("exampleAnalyzer",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            storage_account=azure.videoanalyzer.AnalyzerStorageAccountArgs(
                id=example_account.id,
                user_assigned_identity_id=example_user_assigned_identity.id,
            ),
            identity=azure.videoanalyzer.AnalyzerIdentityArgs(
                type="UserAssigned",
                identity_ids=[example_user_assigned_identity.id],
            ),
            tags={
                "environment": "staging",
            },
            opts=pulumi.ResourceOptions(depends_on=[
                    contributor,
                    reader,
                ]))
        ```

        ## Import

        Video Analyzer can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:videoanalyzer/analyzer:Analyzer analyzer /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Media/videoAnalyzers/analyzer1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AnalyzerIdentityArgs']] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Video Analyzer. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Video Analyzer. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['AnalyzerStorageAccountArgs']] storage_account: A `storage_account` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags assigned to the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AnalyzerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Video Analyzer.

        !> Video Analyzer (Preview) is now Deprecated and will be Retired on 2022-11-30 - as such the `videoanalyzer.Analyzer` resource is deprecated and will be removed in v4.0 of the AzureRM Provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="GRS")
        example_user_assigned_identity = azure.authorization.UserAssignedIdentity("exampleUserAssignedIdentity",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        contributor = azure.authorization.Assignment("contributor",
            scope=example_account.id,
            role_definition_name="Storage Blob Data Contributor",
            principal_id=example_user_assigned_identity.principal_id)
        reader = azure.authorization.Assignment("reader",
            scope=example_account.id,
            role_definition_name="Reader",
            principal_id=example_user_assigned_identity.principal_id)
        example_analyzer = azure.videoanalyzer.Analyzer("exampleAnalyzer",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            storage_account=azure.videoanalyzer.AnalyzerStorageAccountArgs(
                id=example_account.id,
                user_assigned_identity_id=example_user_assigned_identity.id,
            ),
            identity=azure.videoanalyzer.AnalyzerIdentityArgs(
                type="UserAssigned",
                identity_ids=[example_user_assigned_identity.id],
            ),
            tags={
                "environment": "staging",
            },
            opts=pulumi.ResourceOptions(depends_on=[
                    contributor,
                    reader,
                ]))
        ```

        ## Import

        Video Analyzer can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:videoanalyzer/analyzer:Analyzer analyzer /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Media/videoAnalyzers/analyzer1
        ```

        :param str resource_name: The name of the resource.
        :param AnalyzerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AnalyzerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AnalyzerArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['AnalyzerIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account: Optional[pulumi.Input[pulumi.InputType['AnalyzerStorageAccountArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AnalyzerArgs.__new__(AnalyzerArgs)

            if identity is not None and not isinstance(identity, AnalyzerIdentityArgs):
                identity = identity or {}
                def _setter(key, value):
                    identity[key] = value
                AnalyzerIdentityArgs._configure(_setter, **identity)
            if identity is None and not opts.urn:
                raise TypeError("Missing required property 'identity'")
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if storage_account is not None and not isinstance(storage_account, AnalyzerStorageAccountArgs):
                storage_account = storage_account or {}
                def _setter(key, value):
                    storage_account[key] = value
                AnalyzerStorageAccountArgs._configure(_setter, **storage_account)
            if storage_account is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account'")
            __props__.__dict__["storage_account"] = storage_account
            __props__.__dict__["tags"] = tags
        super(Analyzer, __self__).__init__(
            'azure:videoanalyzer/analyzer:Analyzer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            identity: Optional[pulumi.Input[pulumi.InputType['AnalyzerIdentityArgs']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            storage_account: Optional[pulumi.Input[pulumi.InputType['AnalyzerStorageAccountArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Analyzer':
        """
        Get an existing Analyzer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AnalyzerIdentityArgs']] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Video Analyzer. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Video Analyzer. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['AnalyzerStorageAccountArgs']] storage_account: A `storage_account` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags assigned to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AnalyzerState.__new__(_AnalyzerState)

        __props__.__dict__["identity"] = identity
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["storage_account"] = storage_account
        __props__.__dict__["tags"] = tags
        return Analyzer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output['outputs.AnalyzerIdentity']:
        """
        An `identity` block as defined below.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Video Analyzer. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the Video Analyzer. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> pulumi.Output['outputs.AnalyzerStorageAccount']:
        """
        A `storage_account` block as defined below.
        """
        return pulumi.get(self, "storage_account")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags assigned to the resource.
        """
        return pulumi.get(self, "tags")


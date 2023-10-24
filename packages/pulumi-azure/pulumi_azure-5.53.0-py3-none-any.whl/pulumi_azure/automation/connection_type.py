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

__all__ = ['ConnectionTypeArgs', 'ConnectionType']

@pulumi.input_type
class ConnectionTypeArgs:
    def __init__(__self__, *,
                 automation_account_name: pulumi.Input[str],
                 fields: pulumi.Input[Sequence[pulumi.Input['ConnectionTypeFieldArgs']]],
                 resource_group_name: pulumi.Input[str],
                 is_global: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ConnectionType resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account in which the Connection is created. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input['ConnectionTypeFieldArgs']]] fields: One or more `field` blocks as defined below. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        :param pulumi.Input[bool] is_global: Whether the connection type is global. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] name: The name which should be used for this Automation Connection Type. Changing this forces a new Automation to be created.
        """
        ConnectionTypeArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            automation_account_name=automation_account_name,
            fields=fields,
            resource_group_name=resource_group_name,
            is_global=is_global,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             automation_account_name: pulumi.Input[str],
             fields: pulumi.Input[Sequence[pulumi.Input['ConnectionTypeFieldArgs']]],
             resource_group_name: pulumi.Input[str],
             is_global: Optional[pulumi.Input[bool]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'automationAccountName' in kwargs:
            automation_account_name = kwargs['automationAccountName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'isGlobal' in kwargs:
            is_global = kwargs['isGlobal']

        _setter("automation_account_name", automation_account_name)
        _setter("fields", fields)
        _setter("resource_group_name", resource_group_name)
        if is_global is not None:
            _setter("is_global", is_global)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[str]:
        """
        The name of the automation account in which the Connection is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "automation_account_name")

    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "automation_account_name", value)

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input['ConnectionTypeFieldArgs']]]:
        """
        One or more `field` blocks as defined below. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input['ConnectionTypeFieldArgs']]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="isGlobal")
    def is_global(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the connection type is global. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "is_global")

    @is_global.setter
    def is_global(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_global", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Automation Connection Type. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ConnectionTypeState:
    def __init__(__self__, *,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionTypeFieldArgs']]]] = None,
                 is_global: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ConnectionType resources.
        :param pulumi.Input[str] automation_account_name: The name of the automation account in which the Connection is created. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input['ConnectionTypeFieldArgs']]] fields: One or more `field` blocks as defined below. Changing this forces a new Automation to be created.
        :param pulumi.Input[bool] is_global: Whether the connection type is global. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] name: The name which should be used for this Automation Connection Type. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        """
        _ConnectionTypeState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            automation_account_name=automation_account_name,
            fields=fields,
            is_global=is_global,
            name=name,
            resource_group_name=resource_group_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             automation_account_name: Optional[pulumi.Input[str]] = None,
             fields: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionTypeFieldArgs']]]] = None,
             is_global: Optional[pulumi.Input[bool]] = None,
             name: Optional[pulumi.Input[str]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'automationAccountName' in kwargs:
            automation_account_name = kwargs['automationAccountName']
        if 'isGlobal' in kwargs:
            is_global = kwargs['isGlobal']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']

        if automation_account_name is not None:
            _setter("automation_account_name", automation_account_name)
        if fields is not None:
            _setter("fields", fields)
        if is_global is not None:
            _setter("is_global", is_global)
        if name is not None:
            _setter("name", name)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the automation account in which the Connection is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "automation_account_name")

    @automation_account_name.setter
    def automation_account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "automation_account_name", value)

    @property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionTypeFieldArgs']]]]:
        """
        One or more `field` blocks as defined below. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionTypeFieldArgs']]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter(name="isGlobal")
    def is_global(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the connection type is global. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "is_global")

    @is_global.setter
    def is_global(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_global", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Automation Connection Type. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)


class ConnectionType(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionTypeFieldArgs']]]]] = None,
                 is_global: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages anAutomation Connection Type.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_client_config = azure.core.get_client_config()
        example_account = azure.automation.Account("exampleAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="Basic")
        example_connection_type = azure.automation.ConnectionType("exampleConnectionType",
            resource_group_name=example_resource_group.name,
            automation_account_name=example_account.name,
            fields=[azure.automation.ConnectionTypeFieldArgs(
                name="example",
                type="string",
            )])
        ```

        ## Import

        Automations can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:automation/connectionType:ConnectionType example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/group1/providers/Microsoft.Automation/automationAccounts/account1/connectionTypes/type1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account in which the Connection is created. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionTypeFieldArgs']]]] fields: One or more `field` blocks as defined below. Changing this forces a new Automation to be created.
        :param pulumi.Input[bool] is_global: Whether the connection type is global. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] name: The name which should be used for this Automation Connection Type. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectionTypeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages anAutomation Connection Type.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_client_config = azure.core.get_client_config()
        example_account = azure.automation.Account("exampleAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="Basic")
        example_connection_type = azure.automation.ConnectionType("exampleConnectionType",
            resource_group_name=example_resource_group.name,
            automation_account_name=example_account.name,
            fields=[azure.automation.ConnectionTypeFieldArgs(
                name="example",
                type="string",
            )])
        ```

        ## Import

        Automations can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:automation/connectionType:ConnectionType example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/group1/providers/Microsoft.Automation/automationAccounts/account1/connectionTypes/type1
        ```

        :param str resource_name: The name of the resource.
        :param ConnectionTypeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectionTypeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ConnectionTypeArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionTypeFieldArgs']]]]] = None,
                 is_global: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectionTypeArgs.__new__(ConnectionTypeArgs)

            if automation_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'automation_account_name'")
            __props__.__dict__["automation_account_name"] = automation_account_name
            if fields is None and not opts.urn:
                raise TypeError("Missing required property 'fields'")
            __props__.__dict__["fields"] = fields
            __props__.__dict__["is_global"] = is_global
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
        super(ConnectionType, __self__).__init__(
            'azure:automation/connectionType:ConnectionType',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            automation_account_name: Optional[pulumi.Input[str]] = None,
            fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionTypeFieldArgs']]]]] = None,
            is_global: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None) -> 'ConnectionType':
        """
        Get an existing ConnectionType resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account in which the Connection is created. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionTypeFieldArgs']]]] fields: One or more `field` blocks as defined below. Changing this forces a new Automation to be created.
        :param pulumi.Input[bool] is_global: Whether the connection type is global. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] name: The name which should be used for this Automation Connection Type. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConnectionTypeState.__new__(_ConnectionTypeState)

        __props__.__dict__["automation_account_name"] = automation_account_name
        __props__.__dict__["fields"] = fields
        __props__.__dict__["is_global"] = is_global
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        return ConnectionType(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Output[str]:
        """
        The name of the automation account in which the Connection is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "automation_account_name")

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Sequence['outputs.ConnectionTypeField']]:
        """
        One or more `field` blocks as defined below. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter(name="isGlobal")
    def is_global(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the connection type is global. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "is_global")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Automation Connection Type. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "resource_group_name")


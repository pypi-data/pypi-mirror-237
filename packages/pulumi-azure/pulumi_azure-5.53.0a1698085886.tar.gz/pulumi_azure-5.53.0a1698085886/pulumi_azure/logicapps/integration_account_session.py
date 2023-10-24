# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['IntegrationAccountSessionArgs', 'IntegrationAccountSession']

@pulumi.input_type
class IntegrationAccountSessionArgs:
    def __init__(__self__, *,
                 content: pulumi.Input[str],
                 integration_account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IntegrationAccountSession resource.
        :param pulumi.Input[str] content: The content of the Logic App Integration Account Session.
        :param pulumi.Input[str] integration_account_name: The name of the Logic App Integration Account. Changing this forces a new Logic App Integration Account Session to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Logic App Integration Account Session should exist. Changing this forces a new Logic App Integration Account Session to be created.
        :param pulumi.Input[str] name: The name which should be used for this Logic App Integration Account Session. Changing this forces a new Logic App Integration Account Session to be created.
        """
        IntegrationAccountSessionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            content=content,
            integration_account_name=integration_account_name,
            resource_group_name=resource_group_name,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             content: pulumi.Input[str],
             integration_account_name: pulumi.Input[str],
             resource_group_name: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'integrationAccountName' in kwargs:
            integration_account_name = kwargs['integrationAccountName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']

        _setter("content", content)
        _setter("integration_account_name", integration_account_name)
        _setter("resource_group_name", resource_group_name)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[str]:
        """
        The content of the Logic App Integration Account Session.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="integrationAccountName")
    def integration_account_name(self) -> pulumi.Input[str]:
        """
        The name of the Logic App Integration Account. Changing this forces a new Logic App Integration Account Session to be created.
        """
        return pulumi.get(self, "integration_account_name")

    @integration_account_name.setter
    def integration_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "integration_account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group where the Logic App Integration Account Session should exist. Changing this forces a new Logic App Integration Account Session to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Logic App Integration Account Session. Changing this forces a new Logic App Integration Account Session to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _IntegrationAccountSessionState:
    def __init__(__self__, *,
                 content: Optional[pulumi.Input[str]] = None,
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IntegrationAccountSession resources.
        :param pulumi.Input[str] content: The content of the Logic App Integration Account Session.
        :param pulumi.Input[str] integration_account_name: The name of the Logic App Integration Account. Changing this forces a new Logic App Integration Account Session to be created.
        :param pulumi.Input[str] name: The name which should be used for this Logic App Integration Account Session. Changing this forces a new Logic App Integration Account Session to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Logic App Integration Account Session should exist. Changing this forces a new Logic App Integration Account Session to be created.
        """
        _IntegrationAccountSessionState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            content=content,
            integration_account_name=integration_account_name,
            name=name,
            resource_group_name=resource_group_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             content: Optional[pulumi.Input[str]] = None,
             integration_account_name: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'integrationAccountName' in kwargs:
            integration_account_name = kwargs['integrationAccountName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']

        if content is not None:
            _setter("content", content)
        if integration_account_name is not None:
            _setter("integration_account_name", integration_account_name)
        if name is not None:
            _setter("name", name)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[str]]:
        """
        The content of the Logic App Integration Account Session.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="integrationAccountName")
    def integration_account_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Logic App Integration Account. Changing this forces a new Logic App Integration Account Session to be created.
        """
        return pulumi.get(self, "integration_account_name")

    @integration_account_name.setter
    def integration_account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "integration_account_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Logic App Integration Account Session. Changing this forces a new Logic App Integration Account Session to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group where the Logic App Integration Account Session should exist. Changing this forces a new Logic App Integration Account Session to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)


class IntegrationAccountSession(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Logic App Integration Account Session.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_integration_account = azure.logicapps.IntegrationAccount("exampleIntegrationAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="Basic")
        example_integration_account_session = azure.logicapps.IntegrationAccountSession("exampleIntegrationAccountSession",
            resource_group_name=example_resource_group.name,
            integration_account_name=example_integration_account.name,
            content=\"\"\" {
               "controlNumber": "1234"
            }
        \"\"\")
        ```

        ## Import

        Logic App Integration Account Sessions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:logicapps/integrationAccountSession:IntegrationAccountSession example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Logic/integrationAccounts/account1/sessions/session1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content: The content of the Logic App Integration Account Session.
        :param pulumi.Input[str] integration_account_name: The name of the Logic App Integration Account. Changing this forces a new Logic App Integration Account Session to be created.
        :param pulumi.Input[str] name: The name which should be used for this Logic App Integration Account Session. Changing this forces a new Logic App Integration Account Session to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Logic App Integration Account Session should exist. Changing this forces a new Logic App Integration Account Session to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationAccountSessionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Logic App Integration Account Session.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_integration_account = azure.logicapps.IntegrationAccount("exampleIntegrationAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="Basic")
        example_integration_account_session = azure.logicapps.IntegrationAccountSession("exampleIntegrationAccountSession",
            resource_group_name=example_resource_group.name,
            integration_account_name=example_integration_account.name,
            content=\"\"\" {
               "controlNumber": "1234"
            }
        \"\"\")
        ```

        ## Import

        Logic App Integration Account Sessions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:logicapps/integrationAccountSession:IntegrationAccountSession example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Logic/integrationAccounts/account1/sessions/session1
        ```

        :param str resource_name: The name of the resource.
        :param IntegrationAccountSessionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationAccountSessionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            IntegrationAccountSessionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IntegrationAccountSessionArgs.__new__(IntegrationAccountSessionArgs)

            if content is None and not opts.urn:
                raise TypeError("Missing required property 'content'")
            __props__.__dict__["content"] = content
            if integration_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'integration_account_name'")
            __props__.__dict__["integration_account_name"] = integration_account_name
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
        super(IntegrationAccountSession, __self__).__init__(
            'azure:logicapps/integrationAccountSession:IntegrationAccountSession',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            content: Optional[pulumi.Input[str]] = None,
            integration_account_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None) -> 'IntegrationAccountSession':
        """
        Get an existing IntegrationAccountSession resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content: The content of the Logic App Integration Account Session.
        :param pulumi.Input[str] integration_account_name: The name of the Logic App Integration Account. Changing this forces a new Logic App Integration Account Session to be created.
        :param pulumi.Input[str] name: The name which should be used for this Logic App Integration Account Session. Changing this forces a new Logic App Integration Account Session to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Logic App Integration Account Session should exist. Changing this forces a new Logic App Integration Account Session to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IntegrationAccountSessionState.__new__(_IntegrationAccountSessionState)

        __props__.__dict__["content"] = content
        __props__.__dict__["integration_account_name"] = integration_account_name
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        return IntegrationAccountSession(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[str]:
        """
        The content of the Logic App Integration Account Session.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="integrationAccountName")
    def integration_account_name(self) -> pulumi.Output[str]:
        """
        The name of the Logic App Integration Account. Changing this forces a new Logic App Integration Account Session to be created.
        """
        return pulumi.get(self, "integration_account_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Logic App Integration Account Session. Changing this forces a new Logic App Integration Account Session to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Logic App Integration Account Session should exist. Changing this forces a new Logic App Integration Account Session to be created.
        """
        return pulumi.get(self, "resource_group_name")


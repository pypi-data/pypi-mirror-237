# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ConnectionClassicCertificateArgs', 'ConnectionClassicCertificate']

@pulumi.input_type
class ConnectionClassicCertificateArgs:
    def __init__(__self__, *,
                 automation_account_name: pulumi.Input[str],
                 certificate_asset_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 subscription_id: pulumi.Input[str],
                 subscription_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ConnectionClassicCertificate resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account in which the Connection is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] certificate_asset_name: The name of the certificate asset.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Connection is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subscription_id: The id of subscription.
        :param pulumi.Input[str] subscription_name: The name of subscription.
        :param pulumi.Input[str] description: A description for this Connection.
        :param pulumi.Input[str] name: Specifies the name of the Connection. Changing this forces a new resource to be created.
        """
        ConnectionClassicCertificateArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            automation_account_name=automation_account_name,
            certificate_asset_name=certificate_asset_name,
            resource_group_name=resource_group_name,
            subscription_id=subscription_id,
            subscription_name=subscription_name,
            description=description,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             automation_account_name: pulumi.Input[str],
             certificate_asset_name: pulumi.Input[str],
             resource_group_name: pulumi.Input[str],
             subscription_id: pulumi.Input[str],
             subscription_name: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'automationAccountName' in kwargs:
            automation_account_name = kwargs['automationAccountName']
        if 'certificateAssetName' in kwargs:
            certificate_asset_name = kwargs['certificateAssetName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'subscriptionId' in kwargs:
            subscription_id = kwargs['subscriptionId']
        if 'subscriptionName' in kwargs:
            subscription_name = kwargs['subscriptionName']

        _setter("automation_account_name", automation_account_name)
        _setter("certificate_asset_name", certificate_asset_name)
        _setter("resource_group_name", resource_group_name)
        _setter("subscription_id", subscription_id)
        _setter("subscription_name", subscription_name)
        if description is not None:
            _setter("description", description)
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
    @pulumi.getter(name="certificateAssetName")
    def certificate_asset_name(self) -> pulumi.Input[str]:
        """
        The name of the certificate asset.
        """
        return pulumi.get(self, "certificate_asset_name")

    @certificate_asset_name.setter
    def certificate_asset_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "certificate_asset_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group in which the Connection is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Input[str]:
        """
        The id of subscription.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subscription_id", value)

    @property
    @pulumi.getter(name="subscriptionName")
    def subscription_name(self) -> pulumi.Input[str]:
        """
        The name of subscription.
        """
        return pulumi.get(self, "subscription_name")

    @subscription_name.setter
    def subscription_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "subscription_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for this Connection.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Connection. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ConnectionClassicCertificateState:
    def __init__(__self__, *,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 certificate_asset_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 subscription_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ConnectionClassicCertificate resources.
        :param pulumi.Input[str] automation_account_name: The name of the automation account in which the Connection is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] certificate_asset_name: The name of the certificate asset.
        :param pulumi.Input[str] description: A description for this Connection.
        :param pulumi.Input[str] name: Specifies the name of the Connection. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Connection is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subscription_id: The id of subscription.
        :param pulumi.Input[str] subscription_name: The name of subscription.
        """
        _ConnectionClassicCertificateState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            automation_account_name=automation_account_name,
            certificate_asset_name=certificate_asset_name,
            description=description,
            name=name,
            resource_group_name=resource_group_name,
            subscription_id=subscription_id,
            subscription_name=subscription_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             automation_account_name: Optional[pulumi.Input[str]] = None,
             certificate_asset_name: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             subscription_id: Optional[pulumi.Input[str]] = None,
             subscription_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'automationAccountName' in kwargs:
            automation_account_name = kwargs['automationAccountName']
        if 'certificateAssetName' in kwargs:
            certificate_asset_name = kwargs['certificateAssetName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'subscriptionId' in kwargs:
            subscription_id = kwargs['subscriptionId']
        if 'subscriptionName' in kwargs:
            subscription_name = kwargs['subscriptionName']

        if automation_account_name is not None:
            _setter("automation_account_name", automation_account_name)
        if certificate_asset_name is not None:
            _setter("certificate_asset_name", certificate_asset_name)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if subscription_id is not None:
            _setter("subscription_id", subscription_id)
        if subscription_name is not None:
            _setter("subscription_name", subscription_name)

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
    @pulumi.getter(name="certificateAssetName")
    def certificate_asset_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the certificate asset.
        """
        return pulumi.get(self, "certificate_asset_name")

    @certificate_asset_name.setter
    def certificate_asset_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_asset_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for this Connection.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Connection. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group in which the Connection is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of subscription.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)

    @property
    @pulumi.getter(name="subscriptionName")
    def subscription_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of subscription.
        """
        return pulumi.get(self, "subscription_name")

    @subscription_name.setter
    def subscription_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_name", value)


class ConnectionClassicCertificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 certificate_asset_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 subscription_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an Automation Connection with type `AzureClassicCertificate`.

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
        example_connection_classic_certificate = azure.automation.ConnectionClassicCertificate("exampleConnectionClassicCertificate",
            resource_group_name=example_resource_group.name,
            automation_account_name=example_account.name,
            certificate_asset_name="cert1",
            subscription_name="subs1",
            subscription_id=example_client_config.subscription_id)
        ```

        ## Import

        Automation Connection can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:automation/connectionClassicCertificate:ConnectionClassicCertificate conn1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Automation/automationAccounts/account1/connections/conn1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account in which the Connection is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] certificate_asset_name: The name of the certificate asset.
        :param pulumi.Input[str] description: A description for this Connection.
        :param pulumi.Input[str] name: Specifies the name of the Connection. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Connection is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subscription_id: The id of subscription.
        :param pulumi.Input[str] subscription_name: The name of subscription.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectionClassicCertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Automation Connection with type `AzureClassicCertificate`.

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
        example_connection_classic_certificate = azure.automation.ConnectionClassicCertificate("exampleConnectionClassicCertificate",
            resource_group_name=example_resource_group.name,
            automation_account_name=example_account.name,
            certificate_asset_name="cert1",
            subscription_name="subs1",
            subscription_id=example_client_config.subscription_id)
        ```

        ## Import

        Automation Connection can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:automation/connectionClassicCertificate:ConnectionClassicCertificate conn1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Automation/automationAccounts/account1/connections/conn1
        ```

        :param str resource_name: The name of the resource.
        :param ConnectionClassicCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectionClassicCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ConnectionClassicCertificateArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 certificate_asset_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 subscription_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectionClassicCertificateArgs.__new__(ConnectionClassicCertificateArgs)

            if automation_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'automation_account_name'")
            __props__.__dict__["automation_account_name"] = automation_account_name
            if certificate_asset_name is None and not opts.urn:
                raise TypeError("Missing required property 'certificate_asset_name'")
            __props__.__dict__["certificate_asset_name"] = certificate_asset_name
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if subscription_id is None and not opts.urn:
                raise TypeError("Missing required property 'subscription_id'")
            __props__.__dict__["subscription_id"] = subscription_id
            if subscription_name is None and not opts.urn:
                raise TypeError("Missing required property 'subscription_name'")
            __props__.__dict__["subscription_name"] = subscription_name
        super(ConnectionClassicCertificate, __self__).__init__(
            'azure:automation/connectionClassicCertificate:ConnectionClassicCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            automation_account_name: Optional[pulumi.Input[str]] = None,
            certificate_asset_name: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            subscription_id: Optional[pulumi.Input[str]] = None,
            subscription_name: Optional[pulumi.Input[str]] = None) -> 'ConnectionClassicCertificate':
        """
        Get an existing ConnectionClassicCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account in which the Connection is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] certificate_asset_name: The name of the certificate asset.
        :param pulumi.Input[str] description: A description for this Connection.
        :param pulumi.Input[str] name: Specifies the name of the Connection. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Connection is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subscription_id: The id of subscription.
        :param pulumi.Input[str] subscription_name: The name of subscription.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConnectionClassicCertificateState.__new__(_ConnectionClassicCertificateState)

        __props__.__dict__["automation_account_name"] = automation_account_name
        __props__.__dict__["certificate_asset_name"] = certificate_asset_name
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["subscription_id"] = subscription_id
        __props__.__dict__["subscription_name"] = subscription_name
        return ConnectionClassicCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Output[str]:
        """
        The name of the automation account in which the Connection is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "automation_account_name")

    @property
    @pulumi.getter(name="certificateAssetName")
    def certificate_asset_name(self) -> pulumi.Output[str]:
        """
        The name of the certificate asset.
        """
        return pulumi.get(self, "certificate_asset_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for this Connection.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Connection. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which the Connection is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Output[str]:
        """
        The id of subscription.
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter(name="subscriptionName")
    def subscription_name(self) -> pulumi.Output[str]:
        """
        The name of subscription.
        """
        return pulumi.get(self, "subscription_name")


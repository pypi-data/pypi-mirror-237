# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['GroupSubscriptionAssociationArgs', 'GroupSubscriptionAssociation']

@pulumi.input_type
class GroupSubscriptionAssociationArgs:
    def __init__(__self__, *,
                 management_group_id: pulumi.Input[str],
                 subscription_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a GroupSubscriptionAssociation resource.
        :param pulumi.Input[str] management_group_id: The ID of the Management Group to associate the Subscription with. Changing this forces a new Management to be created.
        :param pulumi.Input[str] subscription_id: The ID of the Subscription to be associated with the Management Group. Changing this forces a new Management to be created.
        """
        GroupSubscriptionAssociationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            management_group_id=management_group_id,
            subscription_id=subscription_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             management_group_id: pulumi.Input[str],
             subscription_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'managementGroupId' in kwargs:
            management_group_id = kwargs['managementGroupId']
        if 'subscriptionId' in kwargs:
            subscription_id = kwargs['subscriptionId']

        _setter("management_group_id", management_group_id)
        _setter("subscription_id", subscription_id)

    @property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> pulumi.Input[str]:
        """
        The ID of the Management Group to associate the Subscription with. Changing this forces a new Management to be created.
        """
        return pulumi.get(self, "management_group_id")

    @management_group_id.setter
    def management_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "management_group_id", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Input[str]:
        """
        The ID of the Subscription to be associated with the Management Group. Changing this forces a new Management to be created.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subscription_id", value)


@pulumi.input_type
class _GroupSubscriptionAssociationState:
    def __init__(__self__, *,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GroupSubscriptionAssociation resources.
        :param pulumi.Input[str] management_group_id: The ID of the Management Group to associate the Subscription with. Changing this forces a new Management to be created.
        :param pulumi.Input[str] subscription_id: The ID of the Subscription to be associated with the Management Group. Changing this forces a new Management to be created.
        """
        _GroupSubscriptionAssociationState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            management_group_id=management_group_id,
            subscription_id=subscription_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             management_group_id: Optional[pulumi.Input[str]] = None,
             subscription_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'managementGroupId' in kwargs:
            management_group_id = kwargs['managementGroupId']
        if 'subscriptionId' in kwargs:
            subscription_id = kwargs['subscriptionId']

        if management_group_id is not None:
            _setter("management_group_id", management_group_id)
        if subscription_id is not None:
            _setter("subscription_id", subscription_id)

    @property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Management Group to associate the Subscription with. Changing this forces a new Management to be created.
        """
        return pulumi.get(self, "management_group_id")

    @management_group_id.setter
    def management_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "management_group_id", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Subscription to be associated with the Management Group. Changing this forces a new Management to be created.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)


class GroupSubscriptionAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Management Group Subscription Association.

        !> **Note:** When using this resource, configuring `subscription_ids` on the `management.Group` resource is not supported.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_group = azure.management.get_group(name="exampleManagementGroup")
        example_subscription = azure.core.get_subscription(subscription_id="12345678-1234-1234-1234-123456789012")
        example_group_subscription_association = azure.management.GroupSubscriptionAssociation("exampleGroupSubscriptionAssociation",
            management_group_id=example_group.id,
            subscription_id=example_subscription.id)
        ```

        ## Import

        Managements can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:management/groupSubscriptionAssociation:GroupSubscriptionAssociation example /managementGroup/MyManagementGroup/subscription/12345678-1234-1234-1234-123456789012
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] management_group_id: The ID of the Management Group to associate the Subscription with. Changing this forces a new Management to be created.
        :param pulumi.Input[str] subscription_id: The ID of the Subscription to be associated with the Management Group. Changing this forces a new Management to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GroupSubscriptionAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Management Group Subscription Association.

        !> **Note:** When using this resource, configuring `subscription_ids` on the `management.Group` resource is not supported.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_group = azure.management.get_group(name="exampleManagementGroup")
        example_subscription = azure.core.get_subscription(subscription_id="12345678-1234-1234-1234-123456789012")
        example_group_subscription_association = azure.management.GroupSubscriptionAssociation("exampleGroupSubscriptionAssociation",
            management_group_id=example_group.id,
            subscription_id=example_subscription.id)
        ```

        ## Import

        Managements can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:management/groupSubscriptionAssociation:GroupSubscriptionAssociation example /managementGroup/MyManagementGroup/subscription/12345678-1234-1234-1234-123456789012
        ```

        :param str resource_name: The name of the resource.
        :param GroupSubscriptionAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupSubscriptionAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            GroupSubscriptionAssociationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GroupSubscriptionAssociationArgs.__new__(GroupSubscriptionAssociationArgs)

            if management_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'management_group_id'")
            __props__.__dict__["management_group_id"] = management_group_id
            if subscription_id is None and not opts.urn:
                raise TypeError("Missing required property 'subscription_id'")
            __props__.__dict__["subscription_id"] = subscription_id
        super(GroupSubscriptionAssociation, __self__).__init__(
            'azure:management/groupSubscriptionAssociation:GroupSubscriptionAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            management_group_id: Optional[pulumi.Input[str]] = None,
            subscription_id: Optional[pulumi.Input[str]] = None) -> 'GroupSubscriptionAssociation':
        """
        Get an existing GroupSubscriptionAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] management_group_id: The ID of the Management Group to associate the Subscription with. Changing this forces a new Management to be created.
        :param pulumi.Input[str] subscription_id: The ID of the Subscription to be associated with the Management Group. Changing this forces a new Management to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GroupSubscriptionAssociationState.__new__(_GroupSubscriptionAssociationState)

        __props__.__dict__["management_group_id"] = management_group_id
        __props__.__dict__["subscription_id"] = subscription_id
        return GroupSubscriptionAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the Management Group to associate the Subscription with. Changing this forces a new Management to be created.
        """
        return pulumi.get(self, "management_group_id")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Output[str]:
        """
        The ID of the Subscription to be associated with the Management Group. Changing this forces a new Management to be created.
        """
        return pulumi.get(self, "subscription_id")


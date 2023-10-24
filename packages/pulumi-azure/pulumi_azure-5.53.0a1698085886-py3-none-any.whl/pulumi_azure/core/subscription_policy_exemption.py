# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SubscriptionPolicyExemptionArgs', 'SubscriptionPolicyExemption']

@pulumi.input_type
class SubscriptionPolicyExemptionArgs:
    def __init__(__self__, *,
                 exemption_category: pulumi.Input[str],
                 policy_assignment_id: pulumi.Input[str],
                 subscription_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 expires_on: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a SubscriptionPolicyExemption resource.
        :param pulumi.Input[str] exemption_category: The category of this policy exemption. Possible values are `Waiver` and `Mitigated`.
        :param pulumi.Input[str] policy_assignment_id: The ID of the Policy Assignment to be exempted at the specified Scope. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subscription_id: The Subscription ID where the Policy Exemption should be applied. Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: A description to use for this Policy Exemption.
        :param pulumi.Input[str] display_name: A friendly display name to use for this Policy Exemption.
        :param pulumi.Input[str] expires_on: The expiration date and time in UTC ISO 8601 format of this policy exemption.
        :param pulumi.Input[str] metadata: The metadata for this policy exemption. This is a JSON string representing additional metadata that should be stored with the policy exemption.
        :param pulumi.Input[str] name: The name of the Policy Exemption. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policy_definition_reference_ids: The policy definition reference ID list when the associated policy assignment is an assignment of a policy set definition.
        """
        SubscriptionPolicyExemptionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            exemption_category=exemption_category,
            policy_assignment_id=policy_assignment_id,
            subscription_id=subscription_id,
            description=description,
            display_name=display_name,
            expires_on=expires_on,
            metadata=metadata,
            name=name,
            policy_definition_reference_ids=policy_definition_reference_ids,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             exemption_category: pulumi.Input[str],
             policy_assignment_id: pulumi.Input[str],
             subscription_id: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             expires_on: Optional[pulumi.Input[str]] = None,
             metadata: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             policy_definition_reference_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'exemptionCategory' in kwargs:
            exemption_category = kwargs['exemptionCategory']
        if 'policyAssignmentId' in kwargs:
            policy_assignment_id = kwargs['policyAssignmentId']
        if 'subscriptionId' in kwargs:
            subscription_id = kwargs['subscriptionId']
        if 'displayName' in kwargs:
            display_name = kwargs['displayName']
        if 'expiresOn' in kwargs:
            expires_on = kwargs['expiresOn']
        if 'policyDefinitionReferenceIds' in kwargs:
            policy_definition_reference_ids = kwargs['policyDefinitionReferenceIds']

        _setter("exemption_category", exemption_category)
        _setter("policy_assignment_id", policy_assignment_id)
        _setter("subscription_id", subscription_id)
        if description is not None:
            _setter("description", description)
        if display_name is not None:
            _setter("display_name", display_name)
        if expires_on is not None:
            _setter("expires_on", expires_on)
        if metadata is not None:
            _setter("metadata", metadata)
        if name is not None:
            _setter("name", name)
        if policy_definition_reference_ids is not None:
            _setter("policy_definition_reference_ids", policy_definition_reference_ids)

    @property
    @pulumi.getter(name="exemptionCategory")
    def exemption_category(self) -> pulumi.Input[str]:
        """
        The category of this policy exemption. Possible values are `Waiver` and `Mitigated`.
        """
        return pulumi.get(self, "exemption_category")

    @exemption_category.setter
    def exemption_category(self, value: pulumi.Input[str]):
        pulumi.set(self, "exemption_category", value)

    @property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> pulumi.Input[str]:
        """
        The ID of the Policy Assignment to be exempted at the specified Scope. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "policy_assignment_id")

    @policy_assignment_id.setter
    def policy_assignment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_assignment_id", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Input[str]:
        """
        The Subscription ID where the Policy Exemption should be applied. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subscription_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description to use for this Policy Exemption.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        A friendly display name to use for this Policy Exemption.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> Optional[pulumi.Input[str]]:
        """
        The expiration date and time in UTC ISO 8601 format of this policy exemption.
        """
        return pulumi.get(self, "expires_on")

    @expires_on.setter
    def expires_on(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires_on", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[str]]:
        """
        The metadata for this policy exemption. This is a JSON string representing additional metadata that should be stored with the policy exemption.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Policy Exemption. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="policyDefinitionReferenceIds")
    def policy_definition_reference_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The policy definition reference ID list when the associated policy assignment is an assignment of a policy set definition.
        """
        return pulumi.get(self, "policy_definition_reference_ids")

    @policy_definition_reference_ids.setter
    def policy_definition_reference_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "policy_definition_reference_ids", value)


@pulumi.input_type
class _SubscriptionPolicyExemptionState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 exemption_category: Optional[pulumi.Input[str]] = None,
                 expires_on: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_assignment_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SubscriptionPolicyExemption resources.
        :param pulumi.Input[str] description: A description to use for this Policy Exemption.
        :param pulumi.Input[str] display_name: A friendly display name to use for this Policy Exemption.
        :param pulumi.Input[str] exemption_category: The category of this policy exemption. Possible values are `Waiver` and `Mitigated`.
        :param pulumi.Input[str] expires_on: The expiration date and time in UTC ISO 8601 format of this policy exemption.
        :param pulumi.Input[str] metadata: The metadata for this policy exemption. This is a JSON string representing additional metadata that should be stored with the policy exemption.
        :param pulumi.Input[str] name: The name of the Policy Exemption. Changing this forces a new resource to be created.
        :param pulumi.Input[str] policy_assignment_id: The ID of the Policy Assignment to be exempted at the specified Scope. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policy_definition_reference_ids: The policy definition reference ID list when the associated policy assignment is an assignment of a policy set definition.
        :param pulumi.Input[str] subscription_id: The Subscription ID where the Policy Exemption should be applied. Changing this forces a new resource to be created.
        """
        _SubscriptionPolicyExemptionState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            display_name=display_name,
            exemption_category=exemption_category,
            expires_on=expires_on,
            metadata=metadata,
            name=name,
            policy_assignment_id=policy_assignment_id,
            policy_definition_reference_ids=policy_definition_reference_ids,
            subscription_id=subscription_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: Optional[pulumi.Input[str]] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             exemption_category: Optional[pulumi.Input[str]] = None,
             expires_on: Optional[pulumi.Input[str]] = None,
             metadata: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             policy_assignment_id: Optional[pulumi.Input[str]] = None,
             policy_definition_reference_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             subscription_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'displayName' in kwargs:
            display_name = kwargs['displayName']
        if 'exemptionCategory' in kwargs:
            exemption_category = kwargs['exemptionCategory']
        if 'expiresOn' in kwargs:
            expires_on = kwargs['expiresOn']
        if 'policyAssignmentId' in kwargs:
            policy_assignment_id = kwargs['policyAssignmentId']
        if 'policyDefinitionReferenceIds' in kwargs:
            policy_definition_reference_ids = kwargs['policyDefinitionReferenceIds']
        if 'subscriptionId' in kwargs:
            subscription_id = kwargs['subscriptionId']

        if description is not None:
            _setter("description", description)
        if display_name is not None:
            _setter("display_name", display_name)
        if exemption_category is not None:
            _setter("exemption_category", exemption_category)
        if expires_on is not None:
            _setter("expires_on", expires_on)
        if metadata is not None:
            _setter("metadata", metadata)
        if name is not None:
            _setter("name", name)
        if policy_assignment_id is not None:
            _setter("policy_assignment_id", policy_assignment_id)
        if policy_definition_reference_ids is not None:
            _setter("policy_definition_reference_ids", policy_definition_reference_ids)
        if subscription_id is not None:
            _setter("subscription_id", subscription_id)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description to use for this Policy Exemption.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        A friendly display name to use for this Policy Exemption.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="exemptionCategory")
    def exemption_category(self) -> Optional[pulumi.Input[str]]:
        """
        The category of this policy exemption. Possible values are `Waiver` and `Mitigated`.
        """
        return pulumi.get(self, "exemption_category")

    @exemption_category.setter
    def exemption_category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "exemption_category", value)

    @property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> Optional[pulumi.Input[str]]:
        """
        The expiration date and time in UTC ISO 8601 format of this policy exemption.
        """
        return pulumi.get(self, "expires_on")

    @expires_on.setter
    def expires_on(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires_on", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[str]]:
        """
        The metadata for this policy exemption. This is a JSON string representing additional metadata that should be stored with the policy exemption.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Policy Exemption. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Policy Assignment to be exempted at the specified Scope. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "policy_assignment_id")

    @policy_assignment_id.setter
    def policy_assignment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_assignment_id", value)

    @property
    @pulumi.getter(name="policyDefinitionReferenceIds")
    def policy_definition_reference_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The policy definition reference ID list when the associated policy assignment is an assignment of a policy set definition.
        """
        return pulumi.get(self, "policy_definition_reference_ids")

    @policy_definition_reference_ids.setter
    def policy_definition_reference_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "policy_definition_reference_ids", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Subscription ID where the Policy Exemption should be applied. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)


class SubscriptionPolicyExemption(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 exemption_category: Optional[pulumi.Input[str]] = None,
                 expires_on: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_assignment_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Subscription Policy Exemption.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_subscription = azure.core.get_subscription()
        example_policy_set_definition = azure.policy.get_policy_set_definition(display_name="Audit machines with insecure password security settings")
        example_subscription_policy_assignment = azure.core.SubscriptionPolicyAssignment("exampleSubscriptionPolicyAssignment",
            subscription_id=example_subscription.id,
            policy_definition_id=example_policy_set_definition.id,
            location="westus",
            identity=azure.core.SubscriptionPolicyAssignmentIdentityArgs(
                type="SystemAssigned",
            ))
        example_subscription_policy_exemption = azure.core.SubscriptionPolicyExemption("exampleSubscriptionPolicyExemption",
            subscription_id=example_subscription.id,
            policy_assignment_id=example_subscription_policy_assignment.id,
            exemption_category="Mitigated")
        ```

        ## Import

        Policy Exemptions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:core/subscriptionPolicyExemption:SubscriptionPolicyExemption exemption1 /subscriptions/00000000-0000-0000-000000000000/providers/Microsoft.Authorization/policyExemptions/exemption1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description to use for this Policy Exemption.
        :param pulumi.Input[str] display_name: A friendly display name to use for this Policy Exemption.
        :param pulumi.Input[str] exemption_category: The category of this policy exemption. Possible values are `Waiver` and `Mitigated`.
        :param pulumi.Input[str] expires_on: The expiration date and time in UTC ISO 8601 format of this policy exemption.
        :param pulumi.Input[str] metadata: The metadata for this policy exemption. This is a JSON string representing additional metadata that should be stored with the policy exemption.
        :param pulumi.Input[str] name: The name of the Policy Exemption. Changing this forces a new resource to be created.
        :param pulumi.Input[str] policy_assignment_id: The ID of the Policy Assignment to be exempted at the specified Scope. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policy_definition_reference_ids: The policy definition reference ID list when the associated policy assignment is an assignment of a policy set definition.
        :param pulumi.Input[str] subscription_id: The Subscription ID where the Policy Exemption should be applied. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubscriptionPolicyExemptionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Subscription Policy Exemption.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_subscription = azure.core.get_subscription()
        example_policy_set_definition = azure.policy.get_policy_set_definition(display_name="Audit machines with insecure password security settings")
        example_subscription_policy_assignment = azure.core.SubscriptionPolicyAssignment("exampleSubscriptionPolicyAssignment",
            subscription_id=example_subscription.id,
            policy_definition_id=example_policy_set_definition.id,
            location="westus",
            identity=azure.core.SubscriptionPolicyAssignmentIdentityArgs(
                type="SystemAssigned",
            ))
        example_subscription_policy_exemption = azure.core.SubscriptionPolicyExemption("exampleSubscriptionPolicyExemption",
            subscription_id=example_subscription.id,
            policy_assignment_id=example_subscription_policy_assignment.id,
            exemption_category="Mitigated")
        ```

        ## Import

        Policy Exemptions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:core/subscriptionPolicyExemption:SubscriptionPolicyExemption exemption1 /subscriptions/00000000-0000-0000-000000000000/providers/Microsoft.Authorization/policyExemptions/exemption1
        ```

        :param str resource_name: The name of the resource.
        :param SubscriptionPolicyExemptionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubscriptionPolicyExemptionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SubscriptionPolicyExemptionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 exemption_category: Optional[pulumi.Input[str]] = None,
                 expires_on: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_assignment_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SubscriptionPolicyExemptionArgs.__new__(SubscriptionPolicyExemptionArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            if exemption_category is None and not opts.urn:
                raise TypeError("Missing required property 'exemption_category'")
            __props__.__dict__["exemption_category"] = exemption_category
            __props__.__dict__["expires_on"] = expires_on
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            if policy_assignment_id is None and not opts.urn:
                raise TypeError("Missing required property 'policy_assignment_id'")
            __props__.__dict__["policy_assignment_id"] = policy_assignment_id
            __props__.__dict__["policy_definition_reference_ids"] = policy_definition_reference_ids
            if subscription_id is None and not opts.urn:
                raise TypeError("Missing required property 'subscription_id'")
            __props__.__dict__["subscription_id"] = subscription_id
        super(SubscriptionPolicyExemption, __self__).__init__(
            'azure:core/subscriptionPolicyExemption:SubscriptionPolicyExemption',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            exemption_category: Optional[pulumi.Input[str]] = None,
            expires_on: Optional[pulumi.Input[str]] = None,
            metadata: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            policy_assignment_id: Optional[pulumi.Input[str]] = None,
            policy_definition_reference_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            subscription_id: Optional[pulumi.Input[str]] = None) -> 'SubscriptionPolicyExemption':
        """
        Get an existing SubscriptionPolicyExemption resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description to use for this Policy Exemption.
        :param pulumi.Input[str] display_name: A friendly display name to use for this Policy Exemption.
        :param pulumi.Input[str] exemption_category: The category of this policy exemption. Possible values are `Waiver` and `Mitigated`.
        :param pulumi.Input[str] expires_on: The expiration date and time in UTC ISO 8601 format of this policy exemption.
        :param pulumi.Input[str] metadata: The metadata for this policy exemption. This is a JSON string representing additional metadata that should be stored with the policy exemption.
        :param pulumi.Input[str] name: The name of the Policy Exemption. Changing this forces a new resource to be created.
        :param pulumi.Input[str] policy_assignment_id: The ID of the Policy Assignment to be exempted at the specified Scope. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policy_definition_reference_ids: The policy definition reference ID list when the associated policy assignment is an assignment of a policy set definition.
        :param pulumi.Input[str] subscription_id: The Subscription ID where the Policy Exemption should be applied. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SubscriptionPolicyExemptionState.__new__(_SubscriptionPolicyExemptionState)

        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["exemption_category"] = exemption_category
        __props__.__dict__["expires_on"] = expires_on
        __props__.__dict__["metadata"] = metadata
        __props__.__dict__["name"] = name
        __props__.__dict__["policy_assignment_id"] = policy_assignment_id
        __props__.__dict__["policy_definition_reference_ids"] = policy_definition_reference_ids
        __props__.__dict__["subscription_id"] = subscription_id
        return SubscriptionPolicyExemption(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description to use for this Policy Exemption.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        A friendly display name to use for this Policy Exemption.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="exemptionCategory")
    def exemption_category(self) -> pulumi.Output[str]:
        """
        The category of this policy exemption. Possible values are `Waiver` and `Mitigated`.
        """
        return pulumi.get(self, "exemption_category")

    @property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> pulumi.Output[Optional[str]]:
        """
        The expiration date and time in UTC ISO 8601 format of this policy exemption.
        """
        return pulumi.get(self, "expires_on")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[str]:
        """
        The metadata for this policy exemption. This is a JSON string representing additional metadata that should be stored with the policy exemption.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Policy Exemption. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> pulumi.Output[str]:
        """
        The ID of the Policy Assignment to be exempted at the specified Scope. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "policy_assignment_id")

    @property
    @pulumi.getter(name="policyDefinitionReferenceIds")
    def policy_definition_reference_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The policy definition reference ID list when the associated policy assignment is an assignment of a policy set definition.
        """
        return pulumi.get(self, "policy_definition_reference_ids")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Output[str]:
        """
        The Subscription ID where the Policy Exemption should be applied. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "subscription_id")


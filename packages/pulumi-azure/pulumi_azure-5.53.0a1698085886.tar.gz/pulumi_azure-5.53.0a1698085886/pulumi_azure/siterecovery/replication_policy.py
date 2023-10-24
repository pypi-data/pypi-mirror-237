# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ReplicationPolicyArgs', 'ReplicationPolicy']

@pulumi.input_type
class ReplicationPolicyArgs:
    def __init__(__self__, *,
                 application_consistent_snapshot_frequency_in_minutes: pulumi.Input[int],
                 recovery_point_retention_in_minutes: pulumi.Input[int],
                 recovery_vault_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ReplicationPolicy resource.
        :param pulumi.Input[int] application_consistent_snapshot_frequency_in_minutes: Specifies the frequency(in minutes) at which to create application consistent recovery points.
               
               > **Note:** The value of `application_consistent_snapshot_frequency_in_minutes` must be less than or equal to the value of `recovery_point_retention_in_minutes`.
        :param pulumi.Input[int] recovery_point_retention_in_minutes: The duration in minutes for which the recovery points need to be stored.
        :param pulumi.Input[str] recovery_vault_name: The name of the vault that should be updated. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Name of the resource group where the vault that should be updated is located. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the replication policy. Changing this forces a new resource to be created.
        """
        ReplicationPolicyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            application_consistent_snapshot_frequency_in_minutes=application_consistent_snapshot_frequency_in_minutes,
            recovery_point_retention_in_minutes=recovery_point_retention_in_minutes,
            recovery_vault_name=recovery_vault_name,
            resource_group_name=resource_group_name,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             application_consistent_snapshot_frequency_in_minutes: pulumi.Input[int],
             recovery_point_retention_in_minutes: pulumi.Input[int],
             recovery_vault_name: pulumi.Input[str],
             resource_group_name: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'applicationConsistentSnapshotFrequencyInMinutes' in kwargs:
            application_consistent_snapshot_frequency_in_minutes = kwargs['applicationConsistentSnapshotFrequencyInMinutes']
        if 'recoveryPointRetentionInMinutes' in kwargs:
            recovery_point_retention_in_minutes = kwargs['recoveryPointRetentionInMinutes']
        if 'recoveryVaultName' in kwargs:
            recovery_vault_name = kwargs['recoveryVaultName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']

        _setter("application_consistent_snapshot_frequency_in_minutes", application_consistent_snapshot_frequency_in_minutes)
        _setter("recovery_point_retention_in_minutes", recovery_point_retention_in_minutes)
        _setter("recovery_vault_name", recovery_vault_name)
        _setter("resource_group_name", resource_group_name)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="applicationConsistentSnapshotFrequencyInMinutes")
    def application_consistent_snapshot_frequency_in_minutes(self) -> pulumi.Input[int]:
        """
        Specifies the frequency(in minutes) at which to create application consistent recovery points.

        > **Note:** The value of `application_consistent_snapshot_frequency_in_minutes` must be less than or equal to the value of `recovery_point_retention_in_minutes`.
        """
        return pulumi.get(self, "application_consistent_snapshot_frequency_in_minutes")

    @application_consistent_snapshot_frequency_in_minutes.setter
    def application_consistent_snapshot_frequency_in_minutes(self, value: pulumi.Input[int]):
        pulumi.set(self, "application_consistent_snapshot_frequency_in_minutes", value)

    @property
    @pulumi.getter(name="recoveryPointRetentionInMinutes")
    def recovery_point_retention_in_minutes(self) -> pulumi.Input[int]:
        """
        The duration in minutes for which the recovery points need to be stored.
        """
        return pulumi.get(self, "recovery_point_retention_in_minutes")

    @recovery_point_retention_in_minutes.setter
    def recovery_point_retention_in_minutes(self, value: pulumi.Input[int]):
        pulumi.set(self, "recovery_point_retention_in_minutes", value)

    @property
    @pulumi.getter(name="recoveryVaultName")
    def recovery_vault_name(self) -> pulumi.Input[str]:
        """
        The name of the vault that should be updated. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "recovery_vault_name")

    @recovery_vault_name.setter
    def recovery_vault_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "recovery_vault_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group where the vault that should be updated is located. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the replication policy. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ReplicationPolicyState:
    def __init__(__self__, *,
                 application_consistent_snapshot_frequency_in_minutes: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recovery_point_retention_in_minutes: Optional[pulumi.Input[int]] = None,
                 recovery_vault_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ReplicationPolicy resources.
        :param pulumi.Input[int] application_consistent_snapshot_frequency_in_minutes: Specifies the frequency(in minutes) at which to create application consistent recovery points.
               
               > **Note:** The value of `application_consistent_snapshot_frequency_in_minutes` must be less than or equal to the value of `recovery_point_retention_in_minutes`.
        :param pulumi.Input[str] name: The name of the replication policy. Changing this forces a new resource to be created.
        :param pulumi.Input[int] recovery_point_retention_in_minutes: The duration in minutes for which the recovery points need to be stored.
        :param pulumi.Input[str] recovery_vault_name: The name of the vault that should be updated. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Name of the resource group where the vault that should be updated is located. Changing this forces a new resource to be created.
        """
        _ReplicationPolicyState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            application_consistent_snapshot_frequency_in_minutes=application_consistent_snapshot_frequency_in_minutes,
            name=name,
            recovery_point_retention_in_minutes=recovery_point_retention_in_minutes,
            recovery_vault_name=recovery_vault_name,
            resource_group_name=resource_group_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             application_consistent_snapshot_frequency_in_minutes: Optional[pulumi.Input[int]] = None,
             name: Optional[pulumi.Input[str]] = None,
             recovery_point_retention_in_minutes: Optional[pulumi.Input[int]] = None,
             recovery_vault_name: Optional[pulumi.Input[str]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'applicationConsistentSnapshotFrequencyInMinutes' in kwargs:
            application_consistent_snapshot_frequency_in_minutes = kwargs['applicationConsistentSnapshotFrequencyInMinutes']
        if 'recoveryPointRetentionInMinutes' in kwargs:
            recovery_point_retention_in_minutes = kwargs['recoveryPointRetentionInMinutes']
        if 'recoveryVaultName' in kwargs:
            recovery_vault_name = kwargs['recoveryVaultName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']

        if application_consistent_snapshot_frequency_in_minutes is not None:
            _setter("application_consistent_snapshot_frequency_in_minutes", application_consistent_snapshot_frequency_in_minutes)
        if name is not None:
            _setter("name", name)
        if recovery_point_retention_in_minutes is not None:
            _setter("recovery_point_retention_in_minutes", recovery_point_retention_in_minutes)
        if recovery_vault_name is not None:
            _setter("recovery_vault_name", recovery_vault_name)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)

    @property
    @pulumi.getter(name="applicationConsistentSnapshotFrequencyInMinutes")
    def application_consistent_snapshot_frequency_in_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the frequency(in minutes) at which to create application consistent recovery points.

        > **Note:** The value of `application_consistent_snapshot_frequency_in_minutes` must be less than or equal to the value of `recovery_point_retention_in_minutes`.
        """
        return pulumi.get(self, "application_consistent_snapshot_frequency_in_minutes")

    @application_consistent_snapshot_frequency_in_minutes.setter
    def application_consistent_snapshot_frequency_in_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "application_consistent_snapshot_frequency_in_minutes", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the replication policy. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="recoveryPointRetentionInMinutes")
    def recovery_point_retention_in_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        The duration in minutes for which the recovery points need to be stored.
        """
        return pulumi.get(self, "recovery_point_retention_in_minutes")

    @recovery_point_retention_in_minutes.setter
    def recovery_point_retention_in_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "recovery_point_retention_in_minutes", value)

    @property
    @pulumi.getter(name="recoveryVaultName")
    def recovery_vault_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the vault that should be updated. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "recovery_vault_name")

    @recovery_vault_name.setter
    def recovery_vault_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recovery_vault_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource group where the vault that should be updated is located. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)


class ReplicationPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_consistent_snapshot_frequency_in_minutes: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recovery_point_retention_in_minutes: Optional[pulumi.Input[int]] = None,
                 recovery_vault_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Azure Site Recovery replication policy within a recovery vault. Replication policies define the frequency at which recovery points are created and how long they are stored.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example", location="East US")
        vault = azure.recoveryservices.Vault("vault",
            location=example.location,
            resource_group_name=example.name,
            sku="Standard")
        policy = azure.siterecovery.ReplicationPolicy("policy",
            resource_group_name=example.name,
            recovery_vault_name=vault.name,
            recovery_point_retention_in_minutes=24 * 60,
            application_consistent_snapshot_frequency_in_minutes=4 * 60)
        ```

        ## Import

        Site Recovery Replication Policies can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:siterecovery/replicationPolicy:ReplicationPolicy mypolicy /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resource-group-name/providers/Microsoft.RecoveryServices/vaults/recovery-vault-name/replicationPolicies/policy-name
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] application_consistent_snapshot_frequency_in_minutes: Specifies the frequency(in minutes) at which to create application consistent recovery points.
               
               > **Note:** The value of `application_consistent_snapshot_frequency_in_minutes` must be less than or equal to the value of `recovery_point_retention_in_minutes`.
        :param pulumi.Input[str] name: The name of the replication policy. Changing this forces a new resource to be created.
        :param pulumi.Input[int] recovery_point_retention_in_minutes: The duration in minutes for which the recovery points need to be stored.
        :param pulumi.Input[str] recovery_vault_name: The name of the vault that should be updated. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Name of the resource group where the vault that should be updated is located. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReplicationPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Azure Site Recovery replication policy within a recovery vault. Replication policies define the frequency at which recovery points are created and how long they are stored.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example", location="East US")
        vault = azure.recoveryservices.Vault("vault",
            location=example.location,
            resource_group_name=example.name,
            sku="Standard")
        policy = azure.siterecovery.ReplicationPolicy("policy",
            resource_group_name=example.name,
            recovery_vault_name=vault.name,
            recovery_point_retention_in_minutes=24 * 60,
            application_consistent_snapshot_frequency_in_minutes=4 * 60)
        ```

        ## Import

        Site Recovery Replication Policies can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:siterecovery/replicationPolicy:ReplicationPolicy mypolicy /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resource-group-name/providers/Microsoft.RecoveryServices/vaults/recovery-vault-name/replicationPolicies/policy-name
        ```

        :param str resource_name: The name of the resource.
        :param ReplicationPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReplicationPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ReplicationPolicyArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_consistent_snapshot_frequency_in_minutes: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recovery_point_retention_in_minutes: Optional[pulumi.Input[int]] = None,
                 recovery_vault_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ReplicationPolicyArgs.__new__(ReplicationPolicyArgs)

            if application_consistent_snapshot_frequency_in_minutes is None and not opts.urn:
                raise TypeError("Missing required property 'application_consistent_snapshot_frequency_in_minutes'")
            __props__.__dict__["application_consistent_snapshot_frequency_in_minutes"] = application_consistent_snapshot_frequency_in_minutes
            __props__.__dict__["name"] = name
            if recovery_point_retention_in_minutes is None and not opts.urn:
                raise TypeError("Missing required property 'recovery_point_retention_in_minutes'")
            __props__.__dict__["recovery_point_retention_in_minutes"] = recovery_point_retention_in_minutes
            if recovery_vault_name is None and not opts.urn:
                raise TypeError("Missing required property 'recovery_vault_name'")
            __props__.__dict__["recovery_vault_name"] = recovery_vault_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
        super(ReplicationPolicy, __self__).__init__(
            'azure:siterecovery/replicationPolicy:ReplicationPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            application_consistent_snapshot_frequency_in_minutes: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            recovery_point_retention_in_minutes: Optional[pulumi.Input[int]] = None,
            recovery_vault_name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None) -> 'ReplicationPolicy':
        """
        Get an existing ReplicationPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] application_consistent_snapshot_frequency_in_minutes: Specifies the frequency(in minutes) at which to create application consistent recovery points.
               
               > **Note:** The value of `application_consistent_snapshot_frequency_in_minutes` must be less than or equal to the value of `recovery_point_retention_in_minutes`.
        :param pulumi.Input[str] name: The name of the replication policy. Changing this forces a new resource to be created.
        :param pulumi.Input[int] recovery_point_retention_in_minutes: The duration in minutes for which the recovery points need to be stored.
        :param pulumi.Input[str] recovery_vault_name: The name of the vault that should be updated. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Name of the resource group where the vault that should be updated is located. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ReplicationPolicyState.__new__(_ReplicationPolicyState)

        __props__.__dict__["application_consistent_snapshot_frequency_in_minutes"] = application_consistent_snapshot_frequency_in_minutes
        __props__.__dict__["name"] = name
        __props__.__dict__["recovery_point_retention_in_minutes"] = recovery_point_retention_in_minutes
        __props__.__dict__["recovery_vault_name"] = recovery_vault_name
        __props__.__dict__["resource_group_name"] = resource_group_name
        return ReplicationPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationConsistentSnapshotFrequencyInMinutes")
    def application_consistent_snapshot_frequency_in_minutes(self) -> pulumi.Output[int]:
        """
        Specifies the frequency(in minutes) at which to create application consistent recovery points.

        > **Note:** The value of `application_consistent_snapshot_frequency_in_minutes` must be less than or equal to the value of `recovery_point_retention_in_minutes`.
        """
        return pulumi.get(self, "application_consistent_snapshot_frequency_in_minutes")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the replication policy. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recoveryPointRetentionInMinutes")
    def recovery_point_retention_in_minutes(self) -> pulumi.Output[int]:
        """
        The duration in minutes for which the recovery points need to be stored.
        """
        return pulumi.get(self, "recovery_point_retention_in_minutes")

    @property
    @pulumi.getter(name="recoveryVaultName")
    def recovery_vault_name(self) -> pulumi.Output[str]:
        """
        The name of the vault that should be updated. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "recovery_vault_name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        Name of the resource group where the vault that should be updated is located. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")


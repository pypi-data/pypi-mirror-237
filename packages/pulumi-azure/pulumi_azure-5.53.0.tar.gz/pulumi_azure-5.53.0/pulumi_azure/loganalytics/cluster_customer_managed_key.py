# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ClusterCustomerManagedKeyArgs', 'ClusterCustomerManagedKey']

@pulumi.input_type
class ClusterCustomerManagedKeyArgs:
    def __init__(__self__, *,
                 key_vault_key_id: pulumi.Input[str],
                 log_analytics_cluster_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a ClusterCustomerManagedKey resource.
        :param pulumi.Input[str] key_vault_key_id: The ID of the Key Vault Key to use for encryption.
        :param pulumi.Input[str] log_analytics_cluster_id: The ID of the Log Analytics Cluster. Changing this forces a new Log Analytics Cluster Customer Managed Key to be created.
        """
        ClusterCustomerManagedKeyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key_vault_key_id=key_vault_key_id,
            log_analytics_cluster_id=log_analytics_cluster_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key_vault_key_id: pulumi.Input[str],
             log_analytics_cluster_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'keyVaultKeyId' in kwargs:
            key_vault_key_id = kwargs['keyVaultKeyId']
        if 'logAnalyticsClusterId' in kwargs:
            log_analytics_cluster_id = kwargs['logAnalyticsClusterId']

        _setter("key_vault_key_id", key_vault_key_id)
        _setter("log_analytics_cluster_id", log_analytics_cluster_id)

    @property
    @pulumi.getter(name="keyVaultKeyId")
    def key_vault_key_id(self) -> pulumi.Input[str]:
        """
        The ID of the Key Vault Key to use for encryption.
        """
        return pulumi.get(self, "key_vault_key_id")

    @key_vault_key_id.setter
    def key_vault_key_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_vault_key_id", value)

    @property
    @pulumi.getter(name="logAnalyticsClusterId")
    def log_analytics_cluster_id(self) -> pulumi.Input[str]:
        """
        The ID of the Log Analytics Cluster. Changing this forces a new Log Analytics Cluster Customer Managed Key to be created.
        """
        return pulumi.get(self, "log_analytics_cluster_id")

    @log_analytics_cluster_id.setter
    def log_analytics_cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "log_analytics_cluster_id", value)


@pulumi.input_type
class _ClusterCustomerManagedKeyState:
    def __init__(__self__, *,
                 key_vault_key_id: Optional[pulumi.Input[str]] = None,
                 log_analytics_cluster_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ClusterCustomerManagedKey resources.
        :param pulumi.Input[str] key_vault_key_id: The ID of the Key Vault Key to use for encryption.
        :param pulumi.Input[str] log_analytics_cluster_id: The ID of the Log Analytics Cluster. Changing this forces a new Log Analytics Cluster Customer Managed Key to be created.
        """
        _ClusterCustomerManagedKeyState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key_vault_key_id=key_vault_key_id,
            log_analytics_cluster_id=log_analytics_cluster_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key_vault_key_id: Optional[pulumi.Input[str]] = None,
             log_analytics_cluster_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'keyVaultKeyId' in kwargs:
            key_vault_key_id = kwargs['keyVaultKeyId']
        if 'logAnalyticsClusterId' in kwargs:
            log_analytics_cluster_id = kwargs['logAnalyticsClusterId']

        if key_vault_key_id is not None:
            _setter("key_vault_key_id", key_vault_key_id)
        if log_analytics_cluster_id is not None:
            _setter("log_analytics_cluster_id", log_analytics_cluster_id)

    @property
    @pulumi.getter(name="keyVaultKeyId")
    def key_vault_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Key Vault Key to use for encryption.
        """
        return pulumi.get(self, "key_vault_key_id")

    @key_vault_key_id.setter
    def key_vault_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_vault_key_id", value)

    @property
    @pulumi.getter(name="logAnalyticsClusterId")
    def log_analytics_cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Log Analytics Cluster. Changing this forces a new Log Analytics Cluster Customer Managed Key to be created.
        """
        return pulumi.get(self, "log_analytics_cluster_id")

    @log_analytics_cluster_id.setter
    def log_analytics_cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_analytics_cluster_id", value)


class ClusterCustomerManagedKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_vault_key_id: Optional[pulumi.Input[str]] = None,
                 log_analytics_cluster_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Log Analytics Cluster Customer Managed Key.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        current = azure.core.get_client_config()
        example_cluster = azure.loganalytics.Cluster("exampleCluster",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            identity=azure.loganalytics.ClusterIdentityArgs(
                type="SystemAssigned",
            ))
        example_key_vault = azure.keyvault.KeyVault("exampleKeyVault",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            tenant_id=current.tenant_id,
            sku_name="premium",
            access_policies=[
                azure.keyvault.KeyVaultAccessPolicyArgs(
                    tenant_id=current.tenant_id,
                    object_id=current.object_id,
                    key_permissions=[
                        "Create",
                        "Get",
                        "GetRotationPolicy",
                    ],
                    secret_permissions=["Set"],
                ),
                azure.keyvault.KeyVaultAccessPolicyArgs(
                    tenant_id=example_cluster.identity.tenant_id,
                    object_id=example_cluster.identity.principal_id,
                    key_permissions=[
                        "Get",
                        "Unwrapkey",
                        "Wrapkey",
                    ],
                ),
            ],
            tags={
                "environment": "Production",
            })
        example_key = azure.keyvault.Key("exampleKey",
            key_vault_id=example_key_vault.id,
            key_type="RSA",
            key_size=2048,
            key_opts=[
                "decrypt",
                "encrypt",
                "sign",
                "unwrapKey",
                "verify",
                "wrapKey",
            ])
        example_cluster_customer_managed_key = azure.loganalytics.ClusterCustomerManagedKey("exampleClusterCustomerManagedKey",
            log_analytics_cluster_id=example_cluster.id,
            key_vault_key_id=example_key.id)
        ```

        ## Import

        Log Analytics Cluster Customer Managed Keys can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:loganalytics/clusterCustomerManagedKey:ClusterCustomerManagedKey example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.OperationalInsights/clusters/cluster1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key_vault_key_id: The ID of the Key Vault Key to use for encryption.
        :param pulumi.Input[str] log_analytics_cluster_id: The ID of the Log Analytics Cluster. Changing this forces a new Log Analytics Cluster Customer Managed Key to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterCustomerManagedKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Log Analytics Cluster Customer Managed Key.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        current = azure.core.get_client_config()
        example_cluster = azure.loganalytics.Cluster("exampleCluster",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            identity=azure.loganalytics.ClusterIdentityArgs(
                type="SystemAssigned",
            ))
        example_key_vault = azure.keyvault.KeyVault("exampleKeyVault",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            tenant_id=current.tenant_id,
            sku_name="premium",
            access_policies=[
                azure.keyvault.KeyVaultAccessPolicyArgs(
                    tenant_id=current.tenant_id,
                    object_id=current.object_id,
                    key_permissions=[
                        "Create",
                        "Get",
                        "GetRotationPolicy",
                    ],
                    secret_permissions=["Set"],
                ),
                azure.keyvault.KeyVaultAccessPolicyArgs(
                    tenant_id=example_cluster.identity.tenant_id,
                    object_id=example_cluster.identity.principal_id,
                    key_permissions=[
                        "Get",
                        "Unwrapkey",
                        "Wrapkey",
                    ],
                ),
            ],
            tags={
                "environment": "Production",
            })
        example_key = azure.keyvault.Key("exampleKey",
            key_vault_id=example_key_vault.id,
            key_type="RSA",
            key_size=2048,
            key_opts=[
                "decrypt",
                "encrypt",
                "sign",
                "unwrapKey",
                "verify",
                "wrapKey",
            ])
        example_cluster_customer_managed_key = azure.loganalytics.ClusterCustomerManagedKey("exampleClusterCustomerManagedKey",
            log_analytics_cluster_id=example_cluster.id,
            key_vault_key_id=example_key.id)
        ```

        ## Import

        Log Analytics Cluster Customer Managed Keys can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:loganalytics/clusterCustomerManagedKey:ClusterCustomerManagedKey example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.OperationalInsights/clusters/cluster1
        ```

        :param str resource_name: The name of the resource.
        :param ClusterCustomerManagedKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterCustomerManagedKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ClusterCustomerManagedKeyArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_vault_key_id: Optional[pulumi.Input[str]] = None,
                 log_analytics_cluster_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterCustomerManagedKeyArgs.__new__(ClusterCustomerManagedKeyArgs)

            if key_vault_key_id is None and not opts.urn:
                raise TypeError("Missing required property 'key_vault_key_id'")
            __props__.__dict__["key_vault_key_id"] = key_vault_key_id
            if log_analytics_cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'log_analytics_cluster_id'")
            __props__.__dict__["log_analytics_cluster_id"] = log_analytics_cluster_id
        super(ClusterCustomerManagedKey, __self__).__init__(
            'azure:loganalytics/clusterCustomerManagedKey:ClusterCustomerManagedKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            key_vault_key_id: Optional[pulumi.Input[str]] = None,
            log_analytics_cluster_id: Optional[pulumi.Input[str]] = None) -> 'ClusterCustomerManagedKey':
        """
        Get an existing ClusterCustomerManagedKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key_vault_key_id: The ID of the Key Vault Key to use for encryption.
        :param pulumi.Input[str] log_analytics_cluster_id: The ID of the Log Analytics Cluster. Changing this forces a new Log Analytics Cluster Customer Managed Key to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ClusterCustomerManagedKeyState.__new__(_ClusterCustomerManagedKeyState)

        __props__.__dict__["key_vault_key_id"] = key_vault_key_id
        __props__.__dict__["log_analytics_cluster_id"] = log_analytics_cluster_id
        return ClusterCustomerManagedKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="keyVaultKeyId")
    def key_vault_key_id(self) -> pulumi.Output[str]:
        """
        The ID of the Key Vault Key to use for encryption.
        """
        return pulumi.get(self, "key_vault_key_id")

    @property
    @pulumi.getter(name="logAnalyticsClusterId")
    def log_analytics_cluster_id(self) -> pulumi.Output[str]:
        """
        The ID of the Log Analytics Cluster. Changing this forces a new Log Analytics Cluster Customer Managed Key to be created.
        """
        return pulumi.get(self, "log_analytics_cluster_id")


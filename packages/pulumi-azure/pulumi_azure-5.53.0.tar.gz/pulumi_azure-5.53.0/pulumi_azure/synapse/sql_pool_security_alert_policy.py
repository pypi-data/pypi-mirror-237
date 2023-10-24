# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SqlPoolSecurityAlertPolicyArgs', 'SqlPoolSecurityAlertPolicy']

@pulumi.input_type
class SqlPoolSecurityAlertPolicyArgs:
    def __init__(__self__, *,
                 policy_state: pulumi.Input[str],
                 sql_pool_id: pulumi.Input[str],
                 disabled_alerts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 email_account_admins_enabled: Optional[pulumi.Input[bool]] = None,
                 email_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 retention_days: Optional[pulumi.Input[int]] = None,
                 storage_account_access_key: Optional[pulumi.Input[str]] = None,
                 storage_endpoint: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SqlPoolSecurityAlertPolicy resource.
        :param pulumi.Input[str] policy_state: Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific SQL pool. Possible values are `Disabled`, `Enabled` and `New`.
        :param pulumi.Input[str] sql_pool_id: Specifies the ID of the Synapse SQL Pool. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] disabled_alerts: Specifies an array of alerts that are disabled. Allowed values are: `Sql_Injection`, `Sql_Injection_Vulnerability`, `Access_Anomaly`, `Data_Exfiltration`, `Unsafe_Action`.
        :param pulumi.Input[bool] email_account_admins_enabled: Boolean flag which specifies if the alert is sent to the account administrators or not. Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] email_addresses: Specifies an array of email addresses to which the alert is sent.
        :param pulumi.Input[int] retention_days: Specifies the number of days to keep in the Threat Detection audit logs. Defaults to `0`.
        :param pulumi.Input[str] storage_account_access_key: Specifies the identifier key of the Threat Detection audit storage account.
        :param pulumi.Input[str] storage_endpoint: Specifies the blob storage endpoint (e.g. <https://example.blob.core.windows.net>). This blob storage will hold all Threat Detection audit logs.
        """
        SqlPoolSecurityAlertPolicyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            policy_state=policy_state,
            sql_pool_id=sql_pool_id,
            disabled_alerts=disabled_alerts,
            email_account_admins_enabled=email_account_admins_enabled,
            email_addresses=email_addresses,
            retention_days=retention_days,
            storage_account_access_key=storage_account_access_key,
            storage_endpoint=storage_endpoint,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             policy_state: pulumi.Input[str],
             sql_pool_id: pulumi.Input[str],
             disabled_alerts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             email_account_admins_enabled: Optional[pulumi.Input[bool]] = None,
             email_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             retention_days: Optional[pulumi.Input[int]] = None,
             storage_account_access_key: Optional[pulumi.Input[str]] = None,
             storage_endpoint: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'policyState' in kwargs:
            policy_state = kwargs['policyState']
        if 'sqlPoolId' in kwargs:
            sql_pool_id = kwargs['sqlPoolId']
        if 'disabledAlerts' in kwargs:
            disabled_alerts = kwargs['disabledAlerts']
        if 'emailAccountAdminsEnabled' in kwargs:
            email_account_admins_enabled = kwargs['emailAccountAdminsEnabled']
        if 'emailAddresses' in kwargs:
            email_addresses = kwargs['emailAddresses']
        if 'retentionDays' in kwargs:
            retention_days = kwargs['retentionDays']
        if 'storageAccountAccessKey' in kwargs:
            storage_account_access_key = kwargs['storageAccountAccessKey']
        if 'storageEndpoint' in kwargs:
            storage_endpoint = kwargs['storageEndpoint']

        _setter("policy_state", policy_state)
        _setter("sql_pool_id", sql_pool_id)
        if disabled_alerts is not None:
            _setter("disabled_alerts", disabled_alerts)
        if email_account_admins_enabled is not None:
            _setter("email_account_admins_enabled", email_account_admins_enabled)
        if email_addresses is not None:
            _setter("email_addresses", email_addresses)
        if retention_days is not None:
            _setter("retention_days", retention_days)
        if storage_account_access_key is not None:
            _setter("storage_account_access_key", storage_account_access_key)
        if storage_endpoint is not None:
            _setter("storage_endpoint", storage_endpoint)

    @property
    @pulumi.getter(name="policyState")
    def policy_state(self) -> pulumi.Input[str]:
        """
        Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific SQL pool. Possible values are `Disabled`, `Enabled` and `New`.
        """
        return pulumi.get(self, "policy_state")

    @policy_state.setter
    def policy_state(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_state", value)

    @property
    @pulumi.getter(name="sqlPoolId")
    def sql_pool_id(self) -> pulumi.Input[str]:
        """
        Specifies the ID of the Synapse SQL Pool. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "sql_pool_id")

    @sql_pool_id.setter
    def sql_pool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "sql_pool_id", value)

    @property
    @pulumi.getter(name="disabledAlerts")
    def disabled_alerts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies an array of alerts that are disabled. Allowed values are: `Sql_Injection`, `Sql_Injection_Vulnerability`, `Access_Anomaly`, `Data_Exfiltration`, `Unsafe_Action`.
        """
        return pulumi.get(self, "disabled_alerts")

    @disabled_alerts.setter
    def disabled_alerts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "disabled_alerts", value)

    @property
    @pulumi.getter(name="emailAccountAdminsEnabled")
    def email_account_admins_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean flag which specifies if the alert is sent to the account administrators or not. Defaults to `false`.
        """
        return pulumi.get(self, "email_account_admins_enabled")

    @email_account_admins_enabled.setter
    def email_account_admins_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "email_account_admins_enabled", value)

    @property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies an array of email addresses to which the alert is sent.
        """
        return pulumi.get(self, "email_addresses")

    @email_addresses.setter
    def email_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "email_addresses", value)

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the number of days to keep in the Threat Detection audit logs. Defaults to `0`.
        """
        return pulumi.get(self, "retention_days")

    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_days", value)

    @property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the identifier key of the Threat Detection audit storage account.
        """
        return pulumi.get(self, "storage_account_access_key")

    @storage_account_access_key.setter
    def storage_account_access_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_access_key", value)

    @property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the blob storage endpoint (e.g. <https://example.blob.core.windows.net>). This blob storage will hold all Threat Detection audit logs.
        """
        return pulumi.get(self, "storage_endpoint")

    @storage_endpoint.setter
    def storage_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_endpoint", value)


@pulumi.input_type
class _SqlPoolSecurityAlertPolicyState:
    def __init__(__self__, *,
                 disabled_alerts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 email_account_admins_enabled: Optional[pulumi.Input[bool]] = None,
                 email_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 policy_state: Optional[pulumi.Input[str]] = None,
                 retention_days: Optional[pulumi.Input[int]] = None,
                 sql_pool_id: Optional[pulumi.Input[str]] = None,
                 storage_account_access_key: Optional[pulumi.Input[str]] = None,
                 storage_endpoint: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SqlPoolSecurityAlertPolicy resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] disabled_alerts: Specifies an array of alerts that are disabled. Allowed values are: `Sql_Injection`, `Sql_Injection_Vulnerability`, `Access_Anomaly`, `Data_Exfiltration`, `Unsafe_Action`.
        :param pulumi.Input[bool] email_account_admins_enabled: Boolean flag which specifies if the alert is sent to the account administrators or not. Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] email_addresses: Specifies an array of email addresses to which the alert is sent.
        :param pulumi.Input[str] policy_state: Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific SQL pool. Possible values are `Disabled`, `Enabled` and `New`.
        :param pulumi.Input[int] retention_days: Specifies the number of days to keep in the Threat Detection audit logs. Defaults to `0`.
        :param pulumi.Input[str] sql_pool_id: Specifies the ID of the Synapse SQL Pool. Changing this forces a new resource to be created.
        :param pulumi.Input[str] storage_account_access_key: Specifies the identifier key of the Threat Detection audit storage account.
        :param pulumi.Input[str] storage_endpoint: Specifies the blob storage endpoint (e.g. <https://example.blob.core.windows.net>). This blob storage will hold all Threat Detection audit logs.
        """
        _SqlPoolSecurityAlertPolicyState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            disabled_alerts=disabled_alerts,
            email_account_admins_enabled=email_account_admins_enabled,
            email_addresses=email_addresses,
            policy_state=policy_state,
            retention_days=retention_days,
            sql_pool_id=sql_pool_id,
            storage_account_access_key=storage_account_access_key,
            storage_endpoint=storage_endpoint,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             disabled_alerts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             email_account_admins_enabled: Optional[pulumi.Input[bool]] = None,
             email_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             policy_state: Optional[pulumi.Input[str]] = None,
             retention_days: Optional[pulumi.Input[int]] = None,
             sql_pool_id: Optional[pulumi.Input[str]] = None,
             storage_account_access_key: Optional[pulumi.Input[str]] = None,
             storage_endpoint: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'disabledAlerts' in kwargs:
            disabled_alerts = kwargs['disabledAlerts']
        if 'emailAccountAdminsEnabled' in kwargs:
            email_account_admins_enabled = kwargs['emailAccountAdminsEnabled']
        if 'emailAddresses' in kwargs:
            email_addresses = kwargs['emailAddresses']
        if 'policyState' in kwargs:
            policy_state = kwargs['policyState']
        if 'retentionDays' in kwargs:
            retention_days = kwargs['retentionDays']
        if 'sqlPoolId' in kwargs:
            sql_pool_id = kwargs['sqlPoolId']
        if 'storageAccountAccessKey' in kwargs:
            storage_account_access_key = kwargs['storageAccountAccessKey']
        if 'storageEndpoint' in kwargs:
            storage_endpoint = kwargs['storageEndpoint']

        if disabled_alerts is not None:
            _setter("disabled_alerts", disabled_alerts)
        if email_account_admins_enabled is not None:
            _setter("email_account_admins_enabled", email_account_admins_enabled)
        if email_addresses is not None:
            _setter("email_addresses", email_addresses)
        if policy_state is not None:
            _setter("policy_state", policy_state)
        if retention_days is not None:
            _setter("retention_days", retention_days)
        if sql_pool_id is not None:
            _setter("sql_pool_id", sql_pool_id)
        if storage_account_access_key is not None:
            _setter("storage_account_access_key", storage_account_access_key)
        if storage_endpoint is not None:
            _setter("storage_endpoint", storage_endpoint)

    @property
    @pulumi.getter(name="disabledAlerts")
    def disabled_alerts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies an array of alerts that are disabled. Allowed values are: `Sql_Injection`, `Sql_Injection_Vulnerability`, `Access_Anomaly`, `Data_Exfiltration`, `Unsafe_Action`.
        """
        return pulumi.get(self, "disabled_alerts")

    @disabled_alerts.setter
    def disabled_alerts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "disabled_alerts", value)

    @property
    @pulumi.getter(name="emailAccountAdminsEnabled")
    def email_account_admins_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean flag which specifies if the alert is sent to the account administrators or not. Defaults to `false`.
        """
        return pulumi.get(self, "email_account_admins_enabled")

    @email_account_admins_enabled.setter
    def email_account_admins_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "email_account_admins_enabled", value)

    @property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies an array of email addresses to which the alert is sent.
        """
        return pulumi.get(self, "email_addresses")

    @email_addresses.setter
    def email_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "email_addresses", value)

    @property
    @pulumi.getter(name="policyState")
    def policy_state(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific SQL pool. Possible values are `Disabled`, `Enabled` and `New`.
        """
        return pulumi.get(self, "policy_state")

    @policy_state.setter
    def policy_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_state", value)

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the number of days to keep in the Threat Detection audit logs. Defaults to `0`.
        """
        return pulumi.get(self, "retention_days")

    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_days", value)

    @property
    @pulumi.getter(name="sqlPoolId")
    def sql_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the ID of the Synapse SQL Pool. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "sql_pool_id")

    @sql_pool_id.setter
    def sql_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_pool_id", value)

    @property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the identifier key of the Threat Detection audit storage account.
        """
        return pulumi.get(self, "storage_account_access_key")

    @storage_account_access_key.setter
    def storage_account_access_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_access_key", value)

    @property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the blob storage endpoint (e.g. <https://example.blob.core.windows.net>). This blob storage will hold all Threat Detection audit logs.
        """
        return pulumi.get(self, "storage_endpoint")

    @storage_endpoint.setter
    def storage_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_endpoint", value)


class SqlPoolSecurityAlertPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disabled_alerts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 email_account_admins_enabled: Optional[pulumi.Input[bool]] = None,
                 email_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 policy_state: Optional[pulumi.Input[str]] = None,
                 retention_days: Optional[pulumi.Input[int]] = None,
                 sql_pool_id: Optional[pulumi.Input[str]] = None,
                 storage_account_access_key: Optional[pulumi.Input[str]] = None,
                 storage_endpoint: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Security Alert Policy for a Synapse SQL Pool.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS",
            account_kind="StorageV2",
            is_hns_enabled=True)
        example_data_lake_gen2_filesystem = azure.storage.DataLakeGen2Filesystem("exampleDataLakeGen2Filesystem", storage_account_id=example_account.id)
        example_workspace = azure.synapse.Workspace("exampleWorkspace",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            storage_data_lake_gen2_filesystem_id=example_data_lake_gen2_filesystem.id,
            sql_administrator_login="sqladminuser",
            sql_administrator_login_password="H@Sh1CoR3!",
            aad_admin=azure.synapse.WorkspaceAadAdminArgs(
                login="AzureAD Admin",
                object_id="00000000-0000-0000-0000-000000000000",
                tenant_id="00000000-0000-0000-0000-000000000000",
            ),
            identity=azure.synapse.WorkspaceIdentityArgs(
                type="SystemAssigned",
            ),
            tags={
                "Env": "production",
            })
        example_sql_pool = azure.synapse.SqlPool("exampleSqlPool",
            synapse_workspace_id=example_workspace.id,
            sku_name="DW100c",
            create_mode="Default")
        audit_logs = azure.storage.Account("auditLogs",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_sql_pool_security_alert_policy = azure.synapse.SqlPoolSecurityAlertPolicy("exampleSqlPoolSecurityAlertPolicy",
            sql_pool_id=example_sql_pool.id,
            policy_state="Enabled",
            storage_endpoint=audit_logs.primary_blob_endpoint,
            storage_account_access_key=audit_logs.primary_access_key,
            disabled_alerts=[
                "Sql_Injection",
                "Data_Exfiltration",
            ],
            retention_days=20)
        ```

        ## Import

        Synapse SQL Pool Security Alert Policies can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:synapse/sqlPoolSecurityAlertPolicy:SqlPoolSecurityAlertPolicy example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Synapse/workspaces/workspace1/sqlPools/sqlPool1/securityAlertPolicies/default
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] disabled_alerts: Specifies an array of alerts that are disabled. Allowed values are: `Sql_Injection`, `Sql_Injection_Vulnerability`, `Access_Anomaly`, `Data_Exfiltration`, `Unsafe_Action`.
        :param pulumi.Input[bool] email_account_admins_enabled: Boolean flag which specifies if the alert is sent to the account administrators or not. Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] email_addresses: Specifies an array of email addresses to which the alert is sent.
        :param pulumi.Input[str] policy_state: Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific SQL pool. Possible values are `Disabled`, `Enabled` and `New`.
        :param pulumi.Input[int] retention_days: Specifies the number of days to keep in the Threat Detection audit logs. Defaults to `0`.
        :param pulumi.Input[str] sql_pool_id: Specifies the ID of the Synapse SQL Pool. Changing this forces a new resource to be created.
        :param pulumi.Input[str] storage_account_access_key: Specifies the identifier key of the Threat Detection audit storage account.
        :param pulumi.Input[str] storage_endpoint: Specifies the blob storage endpoint (e.g. <https://example.blob.core.windows.net>). This blob storage will hold all Threat Detection audit logs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SqlPoolSecurityAlertPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Security Alert Policy for a Synapse SQL Pool.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS",
            account_kind="StorageV2",
            is_hns_enabled=True)
        example_data_lake_gen2_filesystem = azure.storage.DataLakeGen2Filesystem("exampleDataLakeGen2Filesystem", storage_account_id=example_account.id)
        example_workspace = azure.synapse.Workspace("exampleWorkspace",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            storage_data_lake_gen2_filesystem_id=example_data_lake_gen2_filesystem.id,
            sql_administrator_login="sqladminuser",
            sql_administrator_login_password="H@Sh1CoR3!",
            aad_admin=azure.synapse.WorkspaceAadAdminArgs(
                login="AzureAD Admin",
                object_id="00000000-0000-0000-0000-000000000000",
                tenant_id="00000000-0000-0000-0000-000000000000",
            ),
            identity=azure.synapse.WorkspaceIdentityArgs(
                type="SystemAssigned",
            ),
            tags={
                "Env": "production",
            })
        example_sql_pool = azure.synapse.SqlPool("exampleSqlPool",
            synapse_workspace_id=example_workspace.id,
            sku_name="DW100c",
            create_mode="Default")
        audit_logs = azure.storage.Account("auditLogs",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_sql_pool_security_alert_policy = azure.synapse.SqlPoolSecurityAlertPolicy("exampleSqlPoolSecurityAlertPolicy",
            sql_pool_id=example_sql_pool.id,
            policy_state="Enabled",
            storage_endpoint=audit_logs.primary_blob_endpoint,
            storage_account_access_key=audit_logs.primary_access_key,
            disabled_alerts=[
                "Sql_Injection",
                "Data_Exfiltration",
            ],
            retention_days=20)
        ```

        ## Import

        Synapse SQL Pool Security Alert Policies can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:synapse/sqlPoolSecurityAlertPolicy:SqlPoolSecurityAlertPolicy example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Synapse/workspaces/workspace1/sqlPools/sqlPool1/securityAlertPolicies/default
        ```

        :param str resource_name: The name of the resource.
        :param SqlPoolSecurityAlertPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SqlPoolSecurityAlertPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SqlPoolSecurityAlertPolicyArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disabled_alerts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 email_account_admins_enabled: Optional[pulumi.Input[bool]] = None,
                 email_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 policy_state: Optional[pulumi.Input[str]] = None,
                 retention_days: Optional[pulumi.Input[int]] = None,
                 sql_pool_id: Optional[pulumi.Input[str]] = None,
                 storage_account_access_key: Optional[pulumi.Input[str]] = None,
                 storage_endpoint: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SqlPoolSecurityAlertPolicyArgs.__new__(SqlPoolSecurityAlertPolicyArgs)

            __props__.__dict__["disabled_alerts"] = disabled_alerts
            __props__.__dict__["email_account_admins_enabled"] = email_account_admins_enabled
            __props__.__dict__["email_addresses"] = email_addresses
            if policy_state is None and not opts.urn:
                raise TypeError("Missing required property 'policy_state'")
            __props__.__dict__["policy_state"] = policy_state
            __props__.__dict__["retention_days"] = retention_days
            if sql_pool_id is None and not opts.urn:
                raise TypeError("Missing required property 'sql_pool_id'")
            __props__.__dict__["sql_pool_id"] = sql_pool_id
            __props__.__dict__["storage_account_access_key"] = None if storage_account_access_key is None else pulumi.Output.secret(storage_account_access_key)
            __props__.__dict__["storage_endpoint"] = storage_endpoint
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["storageAccountAccessKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(SqlPoolSecurityAlertPolicy, __self__).__init__(
            'azure:synapse/sqlPoolSecurityAlertPolicy:SqlPoolSecurityAlertPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            disabled_alerts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            email_account_admins_enabled: Optional[pulumi.Input[bool]] = None,
            email_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            policy_state: Optional[pulumi.Input[str]] = None,
            retention_days: Optional[pulumi.Input[int]] = None,
            sql_pool_id: Optional[pulumi.Input[str]] = None,
            storage_account_access_key: Optional[pulumi.Input[str]] = None,
            storage_endpoint: Optional[pulumi.Input[str]] = None) -> 'SqlPoolSecurityAlertPolicy':
        """
        Get an existing SqlPoolSecurityAlertPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] disabled_alerts: Specifies an array of alerts that are disabled. Allowed values are: `Sql_Injection`, `Sql_Injection_Vulnerability`, `Access_Anomaly`, `Data_Exfiltration`, `Unsafe_Action`.
        :param pulumi.Input[bool] email_account_admins_enabled: Boolean flag which specifies if the alert is sent to the account administrators or not. Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] email_addresses: Specifies an array of email addresses to which the alert is sent.
        :param pulumi.Input[str] policy_state: Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific SQL pool. Possible values are `Disabled`, `Enabled` and `New`.
        :param pulumi.Input[int] retention_days: Specifies the number of days to keep in the Threat Detection audit logs. Defaults to `0`.
        :param pulumi.Input[str] sql_pool_id: Specifies the ID of the Synapse SQL Pool. Changing this forces a new resource to be created.
        :param pulumi.Input[str] storage_account_access_key: Specifies the identifier key of the Threat Detection audit storage account.
        :param pulumi.Input[str] storage_endpoint: Specifies the blob storage endpoint (e.g. <https://example.blob.core.windows.net>). This blob storage will hold all Threat Detection audit logs.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SqlPoolSecurityAlertPolicyState.__new__(_SqlPoolSecurityAlertPolicyState)

        __props__.__dict__["disabled_alerts"] = disabled_alerts
        __props__.__dict__["email_account_admins_enabled"] = email_account_admins_enabled
        __props__.__dict__["email_addresses"] = email_addresses
        __props__.__dict__["policy_state"] = policy_state
        __props__.__dict__["retention_days"] = retention_days
        __props__.__dict__["sql_pool_id"] = sql_pool_id
        __props__.__dict__["storage_account_access_key"] = storage_account_access_key
        __props__.__dict__["storage_endpoint"] = storage_endpoint
        return SqlPoolSecurityAlertPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="disabledAlerts")
    def disabled_alerts(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Specifies an array of alerts that are disabled. Allowed values are: `Sql_Injection`, `Sql_Injection_Vulnerability`, `Access_Anomaly`, `Data_Exfiltration`, `Unsafe_Action`.
        """
        return pulumi.get(self, "disabled_alerts")

    @property
    @pulumi.getter(name="emailAccountAdminsEnabled")
    def email_account_admins_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean flag which specifies if the alert is sent to the account administrators or not. Defaults to `false`.
        """
        return pulumi.get(self, "email_account_admins_enabled")

    @property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Specifies an array of email addresses to which the alert is sent.
        """
        return pulumi.get(self, "email_addresses")

    @property
    @pulumi.getter(name="policyState")
    def policy_state(self) -> pulumi.Output[str]:
        """
        Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific SQL pool. Possible values are `Disabled`, `Enabled` and `New`.
        """
        return pulumi.get(self, "policy_state")

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> pulumi.Output[Optional[int]]:
        """
        Specifies the number of days to keep in the Threat Detection audit logs. Defaults to `0`.
        """
        return pulumi.get(self, "retention_days")

    @property
    @pulumi.getter(name="sqlPoolId")
    def sql_pool_id(self) -> pulumi.Output[str]:
        """
        Specifies the ID of the Synapse SQL Pool. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "sql_pool_id")

    @property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the identifier key of the Threat Detection audit storage account.
        """
        return pulumi.get(self, "storage_account_access_key")

    @property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the blob storage endpoint (e.g. <https://example.blob.core.windows.net>). This blob storage will hold all Threat Detection audit logs.
        """
        return pulumi.get(self, "storage_endpoint")


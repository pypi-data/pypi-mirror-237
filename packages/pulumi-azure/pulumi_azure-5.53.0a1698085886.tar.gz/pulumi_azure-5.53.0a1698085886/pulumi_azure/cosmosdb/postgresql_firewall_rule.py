# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['PostgresqlFirewallRuleArgs', 'PostgresqlFirewallRule']

@pulumi.input_type
class PostgresqlFirewallRuleArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 end_ip_address: pulumi.Input[str],
                 start_ip_address: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PostgresqlFirewallRule resource.
        :param pulumi.Input[str] cluster_id: The resource ID of the Azure Cosmos DB for PostgreSQL Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] end_ip_address: The end IP address of the Azure Cosmos DB for PostgreSQL Firewall Rule.
        :param pulumi.Input[str] start_ip_address: The start IP address of the Azure Cosmos DB for PostgreSQL Firewall Rule.
        :param pulumi.Input[str] name: The name which should be used for the Azure Cosmos DB for PostgreSQL Firewall Rule. Changing this forces a new resource to be created.
        """
        PostgresqlFirewallRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cluster_id=cluster_id,
            end_ip_address=end_ip_address,
            start_ip_address=start_ip_address,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cluster_id: pulumi.Input[str],
             end_ip_address: pulumi.Input[str],
             start_ip_address: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'clusterId' in kwargs:
            cluster_id = kwargs['clusterId']
        if 'endIpAddress' in kwargs:
            end_ip_address = kwargs['endIpAddress']
        if 'startIpAddress' in kwargs:
            start_ip_address = kwargs['startIpAddress']

        _setter("cluster_id", cluster_id)
        _setter("end_ip_address", end_ip_address)
        _setter("start_ip_address", start_ip_address)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the Azure Cosmos DB for PostgreSQL Cluster. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> pulumi.Input[str]:
        """
        The end IP address of the Azure Cosmos DB for PostgreSQL Firewall Rule.
        """
        return pulumi.get(self, "end_ip_address")

    @end_ip_address.setter
    def end_ip_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "end_ip_address", value)

    @property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> pulumi.Input[str]:
        """
        The start IP address of the Azure Cosmos DB for PostgreSQL Firewall Rule.
        """
        return pulumi.get(self, "start_ip_address")

    @start_ip_address.setter
    def start_ip_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "start_ip_address", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for the Azure Cosmos DB for PostgreSQL Firewall Rule. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _PostgresqlFirewallRuleState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 end_ip_address: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 start_ip_address: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PostgresqlFirewallRule resources.
        :param pulumi.Input[str] cluster_id: The resource ID of the Azure Cosmos DB for PostgreSQL Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] end_ip_address: The end IP address of the Azure Cosmos DB for PostgreSQL Firewall Rule.
        :param pulumi.Input[str] name: The name which should be used for the Azure Cosmos DB for PostgreSQL Firewall Rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] start_ip_address: The start IP address of the Azure Cosmos DB for PostgreSQL Firewall Rule.
        """
        _PostgresqlFirewallRuleState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cluster_id=cluster_id,
            end_ip_address=end_ip_address,
            name=name,
            start_ip_address=start_ip_address,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cluster_id: Optional[pulumi.Input[str]] = None,
             end_ip_address: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             start_ip_address: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'clusterId' in kwargs:
            cluster_id = kwargs['clusterId']
        if 'endIpAddress' in kwargs:
            end_ip_address = kwargs['endIpAddress']
        if 'startIpAddress' in kwargs:
            start_ip_address = kwargs['startIpAddress']

        if cluster_id is not None:
            _setter("cluster_id", cluster_id)
        if end_ip_address is not None:
            _setter("end_ip_address", end_ip_address)
        if name is not None:
            _setter("name", name)
        if start_ip_address is not None:
            _setter("start_ip_address", start_ip_address)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the Azure Cosmos DB for PostgreSQL Cluster. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The end IP address of the Azure Cosmos DB for PostgreSQL Firewall Rule.
        """
        return pulumi.get(self, "end_ip_address")

    @end_ip_address.setter
    def end_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_ip_address", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for the Azure Cosmos DB for PostgreSQL Firewall Rule. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The start IP address of the Azure Cosmos DB for PostgreSQL Firewall Rule.
        """
        return pulumi.get(self, "start_ip_address")

    @start_ip_address.setter
    def start_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_ip_address", value)


class PostgresqlFirewallRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 end_ip_address: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 start_ip_address: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an Azure Cosmos DB for PostgreSQL Firewall Rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_postgresql_cluster = azure.cosmosdb.PostgresqlCluster("examplePostgresqlCluster",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            administrator_login_password="H@Sh1CoR3!",
            coordinator_storage_quota_in_mb=131072,
            coordinator_vcore_count=2,
            node_count=0)
        example_postgresql_firewall_rule = azure.cosmosdb.PostgresqlFirewallRule("examplePostgresqlFirewallRule",
            cluster_id=example_postgresql_cluster.id,
            start_ip_address="10.0.17.62",
            end_ip_address="10.0.17.64")
        ```

        ## Import

        Azure Cosmos DB for PostgreSQL Firewall Rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:cosmosdb/postgresqlFirewallRule:PostgresqlFirewallRule example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resourceGroup1/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/cluster1/firewallRules/firewallRule1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The resource ID of the Azure Cosmos DB for PostgreSQL Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] end_ip_address: The end IP address of the Azure Cosmos DB for PostgreSQL Firewall Rule.
        :param pulumi.Input[str] name: The name which should be used for the Azure Cosmos DB for PostgreSQL Firewall Rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] start_ip_address: The start IP address of the Azure Cosmos DB for PostgreSQL Firewall Rule.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PostgresqlFirewallRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Azure Cosmos DB for PostgreSQL Firewall Rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_postgresql_cluster = azure.cosmosdb.PostgresqlCluster("examplePostgresqlCluster",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            administrator_login_password="H@Sh1CoR3!",
            coordinator_storage_quota_in_mb=131072,
            coordinator_vcore_count=2,
            node_count=0)
        example_postgresql_firewall_rule = azure.cosmosdb.PostgresqlFirewallRule("examplePostgresqlFirewallRule",
            cluster_id=example_postgresql_cluster.id,
            start_ip_address="10.0.17.62",
            end_ip_address="10.0.17.64")
        ```

        ## Import

        Azure Cosmos DB for PostgreSQL Firewall Rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:cosmosdb/postgresqlFirewallRule:PostgresqlFirewallRule example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resourceGroup1/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/cluster1/firewallRules/firewallRule1
        ```

        :param str resource_name: The name of the resource.
        :param PostgresqlFirewallRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PostgresqlFirewallRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            PostgresqlFirewallRuleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 end_ip_address: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 start_ip_address: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PostgresqlFirewallRuleArgs.__new__(PostgresqlFirewallRuleArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            if end_ip_address is None and not opts.urn:
                raise TypeError("Missing required property 'end_ip_address'")
            __props__.__dict__["end_ip_address"] = end_ip_address
            __props__.__dict__["name"] = name
            if start_ip_address is None and not opts.urn:
                raise TypeError("Missing required property 'start_ip_address'")
            __props__.__dict__["start_ip_address"] = start_ip_address
        super(PostgresqlFirewallRule, __self__).__init__(
            'azure:cosmosdb/postgresqlFirewallRule:PostgresqlFirewallRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            end_ip_address: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            start_ip_address: Optional[pulumi.Input[str]] = None) -> 'PostgresqlFirewallRule':
        """
        Get an existing PostgresqlFirewallRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The resource ID of the Azure Cosmos DB for PostgreSQL Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] end_ip_address: The end IP address of the Azure Cosmos DB for PostgreSQL Firewall Rule.
        :param pulumi.Input[str] name: The name which should be used for the Azure Cosmos DB for PostgreSQL Firewall Rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] start_ip_address: The start IP address of the Azure Cosmos DB for PostgreSQL Firewall Rule.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PostgresqlFirewallRuleState.__new__(_PostgresqlFirewallRuleState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["end_ip_address"] = end_ip_address
        __props__.__dict__["name"] = name
        __props__.__dict__["start_ip_address"] = start_ip_address
        return PostgresqlFirewallRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the Azure Cosmos DB for PostgreSQL Cluster. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> pulumi.Output[str]:
        """
        The end IP address of the Azure Cosmos DB for PostgreSQL Firewall Rule.
        """
        return pulumi.get(self, "end_ip_address")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for the Azure Cosmos DB for PostgreSQL Firewall Rule. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> pulumi.Output[str]:
        """
        The start IP address of the Azure Cosmos DB for PostgreSQL Firewall Rule.
        """
        return pulumi.get(self, "start_ip_address")


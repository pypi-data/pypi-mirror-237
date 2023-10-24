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

__all__ = ['FailoverGroupArgs', 'FailoverGroup']

@pulumi.input_type
class FailoverGroupArgs:
    def __init__(__self__, *,
                 partner_servers: pulumi.Input[Sequence[pulumi.Input['FailoverGroupPartnerServerArgs']]],
                 read_write_endpoint_failover_policy: pulumi.Input['FailoverGroupReadWriteEndpointFailoverPolicyArgs'],
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 databases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 readonly_endpoint_failover_policy: Optional[pulumi.Input['FailoverGroupReadonlyEndpointFailoverPolicyArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a FailoverGroup resource.
        :param pulumi.Input[Sequence[pulumi.Input['FailoverGroupPartnerServerArgs']]] partner_servers: A list of secondary servers as documented below
        :param pulumi.Input['FailoverGroupReadWriteEndpointFailoverPolicyArgs'] read_write_endpoint_failover_policy: A read/write policy as documented below
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the SQL server Changing this forces a new resource to be created.
        :param pulumi.Input[str] server_name: The name of the primary SQL server. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] databases: A list of database ids to add to the failover group
               
               > **NOTE:** The failover group will create a secondary database for each database listed in `databases`. If the secondary databases need to be managed through this provider, they should be defined as resources and a dependency added to the failover group to ensure the secondary databases are created first.
        :param pulumi.Input[str] name: The name of the failover group. Changing this forces a new resource to be created.
        :param pulumi.Input['FailoverGroupReadonlyEndpointFailoverPolicyArgs'] readonly_endpoint_failover_policy: a read-only policy as documented below
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        FailoverGroupArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            partner_servers=partner_servers,
            read_write_endpoint_failover_policy=read_write_endpoint_failover_policy,
            resource_group_name=resource_group_name,
            server_name=server_name,
            databases=databases,
            name=name,
            readonly_endpoint_failover_policy=readonly_endpoint_failover_policy,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             partner_servers: pulumi.Input[Sequence[pulumi.Input['FailoverGroupPartnerServerArgs']]],
             read_write_endpoint_failover_policy: pulumi.Input['FailoverGroupReadWriteEndpointFailoverPolicyArgs'],
             resource_group_name: pulumi.Input[str],
             server_name: pulumi.Input[str],
             databases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             readonly_endpoint_failover_policy: Optional[pulumi.Input['FailoverGroupReadonlyEndpointFailoverPolicyArgs']] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'partnerServers' in kwargs:
            partner_servers = kwargs['partnerServers']
        if 'readWriteEndpointFailoverPolicy' in kwargs:
            read_write_endpoint_failover_policy = kwargs['readWriteEndpointFailoverPolicy']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'serverName' in kwargs:
            server_name = kwargs['serverName']
        if 'readonlyEndpointFailoverPolicy' in kwargs:
            readonly_endpoint_failover_policy = kwargs['readonlyEndpointFailoverPolicy']

        _setter("partner_servers", partner_servers)
        _setter("read_write_endpoint_failover_policy", read_write_endpoint_failover_policy)
        _setter("resource_group_name", resource_group_name)
        _setter("server_name", server_name)
        if databases is not None:
            _setter("databases", databases)
        if name is not None:
            _setter("name", name)
        if readonly_endpoint_failover_policy is not None:
            _setter("readonly_endpoint_failover_policy", readonly_endpoint_failover_policy)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="partnerServers")
    def partner_servers(self) -> pulumi.Input[Sequence[pulumi.Input['FailoverGroupPartnerServerArgs']]]:
        """
        A list of secondary servers as documented below
        """
        return pulumi.get(self, "partner_servers")

    @partner_servers.setter
    def partner_servers(self, value: pulumi.Input[Sequence[pulumi.Input['FailoverGroupPartnerServerArgs']]]):
        pulumi.set(self, "partner_servers", value)

    @property
    @pulumi.getter(name="readWriteEndpointFailoverPolicy")
    def read_write_endpoint_failover_policy(self) -> pulumi.Input['FailoverGroupReadWriteEndpointFailoverPolicyArgs']:
        """
        A read/write policy as documented below
        """
        return pulumi.get(self, "read_write_endpoint_failover_policy")

    @read_write_endpoint_failover_policy.setter
    def read_write_endpoint_failover_policy(self, value: pulumi.Input['FailoverGroupReadWriteEndpointFailoverPolicyArgs']):
        pulumi.set(self, "read_write_endpoint_failover_policy", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group containing the SQL server Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        The name of the primary SQL server. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter
    def databases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of database ids to add to the failover group

        > **NOTE:** The failover group will create a secondary database for each database listed in `databases`. If the secondary databases need to be managed through this provider, they should be defined as resources and a dependency added to the failover group to ensure the secondary databases are created first.
        """
        return pulumi.get(self, "databases")

    @databases.setter
    def databases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "databases", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the failover group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="readonlyEndpointFailoverPolicy")
    def readonly_endpoint_failover_policy(self) -> Optional[pulumi.Input['FailoverGroupReadonlyEndpointFailoverPolicyArgs']]:
        """
        a read-only policy as documented below
        """
        return pulumi.get(self, "readonly_endpoint_failover_policy")

    @readonly_endpoint_failover_policy.setter
    def readonly_endpoint_failover_policy(self, value: Optional[pulumi.Input['FailoverGroupReadonlyEndpointFailoverPolicyArgs']]):
        pulumi.set(self, "readonly_endpoint_failover_policy", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _FailoverGroupState:
    def __init__(__self__, *,
                 databases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 partner_servers: Optional[pulumi.Input[Sequence[pulumi.Input['FailoverGroupPartnerServerArgs']]]] = None,
                 read_write_endpoint_failover_policy: Optional[pulumi.Input['FailoverGroupReadWriteEndpointFailoverPolicyArgs']] = None,
                 readonly_endpoint_failover_policy: Optional[pulumi.Input['FailoverGroupReadonlyEndpointFailoverPolicyArgs']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering FailoverGroup resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] databases: A list of database ids to add to the failover group
               
               > **NOTE:** The failover group will create a secondary database for each database listed in `databases`. If the secondary databases need to be managed through this provider, they should be defined as resources and a dependency added to the failover group to ensure the secondary databases are created first.
        :param pulumi.Input[str] location: the location of the failover group.
        :param pulumi.Input[str] name: The name of the failover group. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input['FailoverGroupPartnerServerArgs']]] partner_servers: A list of secondary servers as documented below
        :param pulumi.Input['FailoverGroupReadWriteEndpointFailoverPolicyArgs'] read_write_endpoint_failover_policy: A read/write policy as documented below
        :param pulumi.Input['FailoverGroupReadonlyEndpointFailoverPolicyArgs'] readonly_endpoint_failover_policy: a read-only policy as documented below
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the SQL server Changing this forces a new resource to be created.
        :param pulumi.Input[str] role: local replication role of the failover group instance.
        :param pulumi.Input[str] server_name: The name of the primary SQL server. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        _FailoverGroupState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            databases=databases,
            location=location,
            name=name,
            partner_servers=partner_servers,
            read_write_endpoint_failover_policy=read_write_endpoint_failover_policy,
            readonly_endpoint_failover_policy=readonly_endpoint_failover_policy,
            resource_group_name=resource_group_name,
            role=role,
            server_name=server_name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             databases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             partner_servers: Optional[pulumi.Input[Sequence[pulumi.Input['FailoverGroupPartnerServerArgs']]]] = None,
             read_write_endpoint_failover_policy: Optional[pulumi.Input['FailoverGroupReadWriteEndpointFailoverPolicyArgs']] = None,
             readonly_endpoint_failover_policy: Optional[pulumi.Input['FailoverGroupReadonlyEndpointFailoverPolicyArgs']] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             role: Optional[pulumi.Input[str]] = None,
             server_name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'partnerServers' in kwargs:
            partner_servers = kwargs['partnerServers']
        if 'readWriteEndpointFailoverPolicy' in kwargs:
            read_write_endpoint_failover_policy = kwargs['readWriteEndpointFailoverPolicy']
        if 'readonlyEndpointFailoverPolicy' in kwargs:
            readonly_endpoint_failover_policy = kwargs['readonlyEndpointFailoverPolicy']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'serverName' in kwargs:
            server_name = kwargs['serverName']

        if databases is not None:
            _setter("databases", databases)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if partner_servers is not None:
            _setter("partner_servers", partner_servers)
        if read_write_endpoint_failover_policy is not None:
            _setter("read_write_endpoint_failover_policy", read_write_endpoint_failover_policy)
        if readonly_endpoint_failover_policy is not None:
            _setter("readonly_endpoint_failover_policy", readonly_endpoint_failover_policy)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if role is not None:
            _setter("role", role)
        if server_name is not None:
            _setter("server_name", server_name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter
    def databases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of database ids to add to the failover group

        > **NOTE:** The failover group will create a secondary database for each database listed in `databases`. If the secondary databases need to be managed through this provider, they should be defined as resources and a dependency added to the failover group to ensure the secondary databases are created first.
        """
        return pulumi.get(self, "databases")

    @databases.setter
    def databases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "databases", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        the location of the failover group.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the failover group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="partnerServers")
    def partner_servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FailoverGroupPartnerServerArgs']]]]:
        """
        A list of secondary servers as documented below
        """
        return pulumi.get(self, "partner_servers")

    @partner_servers.setter
    def partner_servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FailoverGroupPartnerServerArgs']]]]):
        pulumi.set(self, "partner_servers", value)

    @property
    @pulumi.getter(name="readWriteEndpointFailoverPolicy")
    def read_write_endpoint_failover_policy(self) -> Optional[pulumi.Input['FailoverGroupReadWriteEndpointFailoverPolicyArgs']]:
        """
        A read/write policy as documented below
        """
        return pulumi.get(self, "read_write_endpoint_failover_policy")

    @read_write_endpoint_failover_policy.setter
    def read_write_endpoint_failover_policy(self, value: Optional[pulumi.Input['FailoverGroupReadWriteEndpointFailoverPolicyArgs']]):
        pulumi.set(self, "read_write_endpoint_failover_policy", value)

    @property
    @pulumi.getter(name="readonlyEndpointFailoverPolicy")
    def readonly_endpoint_failover_policy(self) -> Optional[pulumi.Input['FailoverGroupReadonlyEndpointFailoverPolicyArgs']]:
        """
        a read-only policy as documented below
        """
        return pulumi.get(self, "readonly_endpoint_failover_policy")

    @readonly_endpoint_failover_policy.setter
    def readonly_endpoint_failover_policy(self, value: Optional[pulumi.Input['FailoverGroupReadonlyEndpointFailoverPolicyArgs']]):
        pulumi.set(self, "readonly_endpoint_failover_policy", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group containing the SQL server Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        local replication role of the failover group instance.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the primary SQL server. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class FailoverGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 databases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 partner_servers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FailoverGroupPartnerServerArgs']]]]] = None,
                 read_write_endpoint_failover_policy: Optional[pulumi.Input[pulumi.InputType['FailoverGroupReadWriteEndpointFailoverPolicyArgs']]] = None,
                 readonly_endpoint_failover_policy: Optional[pulumi.Input[pulumi.InputType['FailoverGroupReadonlyEndpointFailoverPolicyArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a failover group of databases on a collection of Azure SQL servers.

        > **Note:** The `sql.FailoverGroup` resource is deprecated in version 3.0 of the AzureRM provider and will be removed in version 4.0. Please use the `mssql.FailoverGroup` resource instead.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        primary = azure.sql.SqlServer("primary",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            version="12.0",
            administrator_login="sqladmin",
            administrator_login_password="pa$$w0rd")
        secondary = azure.sql.SqlServer("secondary",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            version="12.0",
            administrator_login="sqladmin",
            administrator_login_password="pa$$w0rd")
        db1 = azure.sql.Database("db1",
            resource_group_name=primary.resource_group_name,
            location=primary.location,
            server_name=primary.name)
        example_failover_group = azure.sql.FailoverGroup("exampleFailoverGroup",
            resource_group_name=primary.resource_group_name,
            server_name=primary.name,
            databases=[db1.id],
            partner_servers=[azure.sql.FailoverGroupPartnerServerArgs(
                id=secondary.id,
            )],
            read_write_endpoint_failover_policy=azure.sql.FailoverGroupReadWriteEndpointFailoverPolicyArgs(
                mode="Automatic",
                grace_minutes=60,
            ))
        ```

        ## Import

        SQL Failover Groups can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:sql/failoverGroup:FailoverGroup example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myresourcegroup/providers/Microsoft.Sql/servers/myserver/failoverGroups/group1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] databases: A list of database ids to add to the failover group
               
               > **NOTE:** The failover group will create a secondary database for each database listed in `databases`. If the secondary databases need to be managed through this provider, they should be defined as resources and a dependency added to the failover group to ensure the secondary databases are created first.
        :param pulumi.Input[str] name: The name of the failover group. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FailoverGroupPartnerServerArgs']]]] partner_servers: A list of secondary servers as documented below
        :param pulumi.Input[pulumi.InputType['FailoverGroupReadWriteEndpointFailoverPolicyArgs']] read_write_endpoint_failover_policy: A read/write policy as documented below
        :param pulumi.Input[pulumi.InputType['FailoverGroupReadonlyEndpointFailoverPolicyArgs']] readonly_endpoint_failover_policy: a read-only policy as documented below
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the SQL server Changing this forces a new resource to be created.
        :param pulumi.Input[str] server_name: The name of the primary SQL server. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FailoverGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a failover group of databases on a collection of Azure SQL servers.

        > **Note:** The `sql.FailoverGroup` resource is deprecated in version 3.0 of the AzureRM provider and will be removed in version 4.0. Please use the `mssql.FailoverGroup` resource instead.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        primary = azure.sql.SqlServer("primary",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            version="12.0",
            administrator_login="sqladmin",
            administrator_login_password="pa$$w0rd")
        secondary = azure.sql.SqlServer("secondary",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            version="12.0",
            administrator_login="sqladmin",
            administrator_login_password="pa$$w0rd")
        db1 = azure.sql.Database("db1",
            resource_group_name=primary.resource_group_name,
            location=primary.location,
            server_name=primary.name)
        example_failover_group = azure.sql.FailoverGroup("exampleFailoverGroup",
            resource_group_name=primary.resource_group_name,
            server_name=primary.name,
            databases=[db1.id],
            partner_servers=[azure.sql.FailoverGroupPartnerServerArgs(
                id=secondary.id,
            )],
            read_write_endpoint_failover_policy=azure.sql.FailoverGroupReadWriteEndpointFailoverPolicyArgs(
                mode="Automatic",
                grace_minutes=60,
            ))
        ```

        ## Import

        SQL Failover Groups can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:sql/failoverGroup:FailoverGroup example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myresourcegroup/providers/Microsoft.Sql/servers/myserver/failoverGroups/group1
        ```

        :param str resource_name: The name of the resource.
        :param FailoverGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FailoverGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            FailoverGroupArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 databases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 partner_servers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FailoverGroupPartnerServerArgs']]]]] = None,
                 read_write_endpoint_failover_policy: Optional[pulumi.Input[pulumi.InputType['FailoverGroupReadWriteEndpointFailoverPolicyArgs']]] = None,
                 readonly_endpoint_failover_policy: Optional[pulumi.Input[pulumi.InputType['FailoverGroupReadonlyEndpointFailoverPolicyArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FailoverGroupArgs.__new__(FailoverGroupArgs)

            __props__.__dict__["databases"] = databases
            __props__.__dict__["name"] = name
            if partner_servers is None and not opts.urn:
                raise TypeError("Missing required property 'partner_servers'")
            __props__.__dict__["partner_servers"] = partner_servers
            if read_write_endpoint_failover_policy is not None and not isinstance(read_write_endpoint_failover_policy, FailoverGroupReadWriteEndpointFailoverPolicyArgs):
                read_write_endpoint_failover_policy = read_write_endpoint_failover_policy or {}
                def _setter(key, value):
                    read_write_endpoint_failover_policy[key] = value
                FailoverGroupReadWriteEndpointFailoverPolicyArgs._configure(_setter, **read_write_endpoint_failover_policy)
            if read_write_endpoint_failover_policy is None and not opts.urn:
                raise TypeError("Missing required property 'read_write_endpoint_failover_policy'")
            __props__.__dict__["read_write_endpoint_failover_policy"] = read_write_endpoint_failover_policy
            if readonly_endpoint_failover_policy is not None and not isinstance(readonly_endpoint_failover_policy, FailoverGroupReadonlyEndpointFailoverPolicyArgs):
                readonly_endpoint_failover_policy = readonly_endpoint_failover_policy or {}
                def _setter(key, value):
                    readonly_endpoint_failover_policy[key] = value
                FailoverGroupReadonlyEndpointFailoverPolicyArgs._configure(_setter, **readonly_endpoint_failover_policy)
            __props__.__dict__["readonly_endpoint_failover_policy"] = readonly_endpoint_failover_policy
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["location"] = None
            __props__.__dict__["role"] = None
        super(FailoverGroup, __self__).__init__(
            'azure:sql/failoverGroup:FailoverGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            databases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            partner_servers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FailoverGroupPartnerServerArgs']]]]] = None,
            read_write_endpoint_failover_policy: Optional[pulumi.Input[pulumi.InputType['FailoverGroupReadWriteEndpointFailoverPolicyArgs']]] = None,
            readonly_endpoint_failover_policy: Optional[pulumi.Input[pulumi.InputType['FailoverGroupReadonlyEndpointFailoverPolicyArgs']]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[str]] = None,
            server_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'FailoverGroup':
        """
        Get an existing FailoverGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] databases: A list of database ids to add to the failover group
               
               > **NOTE:** The failover group will create a secondary database for each database listed in `databases`. If the secondary databases need to be managed through this provider, they should be defined as resources and a dependency added to the failover group to ensure the secondary databases are created first.
        :param pulumi.Input[str] location: the location of the failover group.
        :param pulumi.Input[str] name: The name of the failover group. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FailoverGroupPartnerServerArgs']]]] partner_servers: A list of secondary servers as documented below
        :param pulumi.Input[pulumi.InputType['FailoverGroupReadWriteEndpointFailoverPolicyArgs']] read_write_endpoint_failover_policy: A read/write policy as documented below
        :param pulumi.Input[pulumi.InputType['FailoverGroupReadonlyEndpointFailoverPolicyArgs']] readonly_endpoint_failover_policy: a read-only policy as documented below
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the SQL server Changing this forces a new resource to be created.
        :param pulumi.Input[str] role: local replication role of the failover group instance.
        :param pulumi.Input[str] server_name: The name of the primary SQL server. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FailoverGroupState.__new__(_FailoverGroupState)

        __props__.__dict__["databases"] = databases
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["partner_servers"] = partner_servers
        __props__.__dict__["read_write_endpoint_failover_policy"] = read_write_endpoint_failover_policy
        __props__.__dict__["readonly_endpoint_failover_policy"] = readonly_endpoint_failover_policy
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["role"] = role
        __props__.__dict__["server_name"] = server_name
        __props__.__dict__["tags"] = tags
        return FailoverGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def databases(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of database ids to add to the failover group

        > **NOTE:** The failover group will create a secondary database for each database listed in `databases`. If the secondary databases need to be managed through this provider, they should be defined as resources and a dependency added to the failover group to ensure the secondary databases are created first.
        """
        return pulumi.get(self, "databases")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        the location of the failover group.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the failover group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerServers")
    def partner_servers(self) -> pulumi.Output[Sequence['outputs.FailoverGroupPartnerServer']]:
        """
        A list of secondary servers as documented below
        """
        return pulumi.get(self, "partner_servers")

    @property
    @pulumi.getter(name="readWriteEndpointFailoverPolicy")
    def read_write_endpoint_failover_policy(self) -> pulumi.Output['outputs.FailoverGroupReadWriteEndpointFailoverPolicy']:
        """
        A read/write policy as documented below
        """
        return pulumi.get(self, "read_write_endpoint_failover_policy")

    @property
    @pulumi.getter(name="readonlyEndpointFailoverPolicy")
    def readonly_endpoint_failover_policy(self) -> pulumi.Output['outputs.FailoverGroupReadonlyEndpointFailoverPolicy']:
        """
        a read-only policy as documented below
        """
        return pulumi.get(self, "readonly_endpoint_failover_policy")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group containing the SQL server Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        local replication role of the failover group instance.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Output[str]:
        """
        The name of the primary SQL server. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "server_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")


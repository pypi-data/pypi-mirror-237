# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['MongoUserDefinitionArgs', 'MongoUserDefinition']

@pulumi.input_type
class MongoUserDefinitionArgs:
    def __init__(__self__, *,
                 cosmos_mongo_database_id: pulumi.Input[str],
                 password: pulumi.Input[str],
                 username: pulumi.Input[str],
                 inherited_role_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a MongoUserDefinition resource.
        :param pulumi.Input[str] cosmos_mongo_database_id: The resource ID of the Mongo DB. Changing this forces a new resource to be created.
        :param pulumi.Input[str] password: The password for the Mongo User Definition.
        :param pulumi.Input[str] username: The username for the Mongo User Definition. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] inherited_role_names: A list of Mongo Roles that are inherited to the Mongo User Definition.
               
               > **Note:** The role that needs to be inherited should exist in the Mongo DB of `cosmos_mongo_database_id`.
        """
        MongoUserDefinitionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cosmos_mongo_database_id=cosmos_mongo_database_id,
            password=password,
            username=username,
            inherited_role_names=inherited_role_names,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cosmos_mongo_database_id: pulumi.Input[str],
             password: pulumi.Input[str],
             username: pulumi.Input[str],
             inherited_role_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'cosmosMongoDatabaseId' in kwargs:
            cosmos_mongo_database_id = kwargs['cosmosMongoDatabaseId']
        if 'inheritedRoleNames' in kwargs:
            inherited_role_names = kwargs['inheritedRoleNames']

        _setter("cosmos_mongo_database_id", cosmos_mongo_database_id)
        _setter("password", password)
        _setter("username", username)
        if inherited_role_names is not None:
            _setter("inherited_role_names", inherited_role_names)

    @property
    @pulumi.getter(name="cosmosMongoDatabaseId")
    def cosmos_mongo_database_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the Mongo DB. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cosmos_mongo_database_id")

    @cosmos_mongo_database_id.setter
    def cosmos_mongo_database_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cosmos_mongo_database_id", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        The password for the Mongo User Definition.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        The username for the Mongo User Definition. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter(name="inheritedRoleNames")
    def inherited_role_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of Mongo Roles that are inherited to the Mongo User Definition.

        > **Note:** The role that needs to be inherited should exist in the Mongo DB of `cosmos_mongo_database_id`.
        """
        return pulumi.get(self, "inherited_role_names")

    @inherited_role_names.setter
    def inherited_role_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "inherited_role_names", value)


@pulumi.input_type
class _MongoUserDefinitionState:
    def __init__(__self__, *,
                 cosmos_mongo_database_id: Optional[pulumi.Input[str]] = None,
                 inherited_role_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MongoUserDefinition resources.
        :param pulumi.Input[str] cosmos_mongo_database_id: The resource ID of the Mongo DB. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] inherited_role_names: A list of Mongo Roles that are inherited to the Mongo User Definition.
               
               > **Note:** The role that needs to be inherited should exist in the Mongo DB of `cosmos_mongo_database_id`.
        :param pulumi.Input[str] password: The password for the Mongo User Definition.
        :param pulumi.Input[str] username: The username for the Mongo User Definition. Changing this forces a new resource to be created.
        """
        _MongoUserDefinitionState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cosmos_mongo_database_id=cosmos_mongo_database_id,
            inherited_role_names=inherited_role_names,
            password=password,
            username=username,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cosmos_mongo_database_id: Optional[pulumi.Input[str]] = None,
             inherited_role_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             password: Optional[pulumi.Input[str]] = None,
             username: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'cosmosMongoDatabaseId' in kwargs:
            cosmos_mongo_database_id = kwargs['cosmosMongoDatabaseId']
        if 'inheritedRoleNames' in kwargs:
            inherited_role_names = kwargs['inheritedRoleNames']

        if cosmos_mongo_database_id is not None:
            _setter("cosmos_mongo_database_id", cosmos_mongo_database_id)
        if inherited_role_names is not None:
            _setter("inherited_role_names", inherited_role_names)
        if password is not None:
            _setter("password", password)
        if username is not None:
            _setter("username", username)

    @property
    @pulumi.getter(name="cosmosMongoDatabaseId")
    def cosmos_mongo_database_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the Mongo DB. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cosmos_mongo_database_id")

    @cosmos_mongo_database_id.setter
    def cosmos_mongo_database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cosmos_mongo_database_id", value)

    @property
    @pulumi.getter(name="inheritedRoleNames")
    def inherited_role_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of Mongo Roles that are inherited to the Mongo User Definition.

        > **Note:** The role that needs to be inherited should exist in the Mongo DB of `cosmos_mongo_database_id`.
        """
        return pulumi.get(self, "inherited_role_names")

    @inherited_role_names.setter
    def inherited_role_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "inherited_role_names", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password for the Mongo User Definition.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        The username for the Mongo User Definition. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class MongoUserDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cosmos_mongo_database_id: Optional[pulumi.Input[str]] = None,
                 inherited_role_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Cosmos DB Mongo User Definition.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.cosmosdb.Account("exampleAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            offer_type="Standard",
            kind="MongoDB",
            capabilities=[
                azure.cosmosdb.AccountCapabilityArgs(
                    name="EnableMongo",
                ),
                azure.cosmosdb.AccountCapabilityArgs(
                    name="EnableMongoRoleBasedAccessControl",
                ),
            ],
            consistency_policy=azure.cosmosdb.AccountConsistencyPolicyArgs(
                consistency_level="Strong",
            ),
            geo_locations=[azure.cosmosdb.AccountGeoLocationArgs(
                location=example_resource_group.location,
                failover_priority=0,
            )])
        example_mongo_database = azure.cosmosdb.MongoDatabase("exampleMongoDatabase",
            resource_group_name=example_account.resource_group_name,
            account_name=example_account.name)
        example_mongo_user_definition = azure.cosmosdb.MongoUserDefinition("exampleMongoUserDefinition",
            cosmos_mongo_database_id=example_mongo_database.id,
            username="myUserName",
            password="myPassword")
        ```

        ## Import

        Cosmos DB Mongo User Definitions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:cosmosdb/mongoUserDefinition:MongoUserDefinition example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.DocumentDB/databaseAccounts/account1/mongodbUserDefinitions/dbname1.username1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cosmos_mongo_database_id: The resource ID of the Mongo DB. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] inherited_role_names: A list of Mongo Roles that are inherited to the Mongo User Definition.
               
               > **Note:** The role that needs to be inherited should exist in the Mongo DB of `cosmos_mongo_database_id`.
        :param pulumi.Input[str] password: The password for the Mongo User Definition.
        :param pulumi.Input[str] username: The username for the Mongo User Definition. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MongoUserDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Cosmos DB Mongo User Definition.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.cosmosdb.Account("exampleAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            offer_type="Standard",
            kind="MongoDB",
            capabilities=[
                azure.cosmosdb.AccountCapabilityArgs(
                    name="EnableMongo",
                ),
                azure.cosmosdb.AccountCapabilityArgs(
                    name="EnableMongoRoleBasedAccessControl",
                ),
            ],
            consistency_policy=azure.cosmosdb.AccountConsistencyPolicyArgs(
                consistency_level="Strong",
            ),
            geo_locations=[azure.cosmosdb.AccountGeoLocationArgs(
                location=example_resource_group.location,
                failover_priority=0,
            )])
        example_mongo_database = azure.cosmosdb.MongoDatabase("exampleMongoDatabase",
            resource_group_name=example_account.resource_group_name,
            account_name=example_account.name)
        example_mongo_user_definition = azure.cosmosdb.MongoUserDefinition("exampleMongoUserDefinition",
            cosmos_mongo_database_id=example_mongo_database.id,
            username="myUserName",
            password="myPassword")
        ```

        ## Import

        Cosmos DB Mongo User Definitions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:cosmosdb/mongoUserDefinition:MongoUserDefinition example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.DocumentDB/databaseAccounts/account1/mongodbUserDefinitions/dbname1.username1
        ```

        :param str resource_name: The name of the resource.
        :param MongoUserDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MongoUserDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            MongoUserDefinitionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cosmos_mongo_database_id: Optional[pulumi.Input[str]] = None,
                 inherited_role_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MongoUserDefinitionArgs.__new__(MongoUserDefinitionArgs)

            if cosmos_mongo_database_id is None and not opts.urn:
                raise TypeError("Missing required property 'cosmos_mongo_database_id'")
            __props__.__dict__["cosmos_mongo_database_id"] = cosmos_mongo_database_id
            __props__.__dict__["inherited_role_names"] = inherited_role_names
            if password is None and not opts.urn:
                raise TypeError("Missing required property 'password'")
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            if username is None and not opts.urn:
                raise TypeError("Missing required property 'username'")
            __props__.__dict__["username"] = username
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(MongoUserDefinition, __self__).__init__(
            'azure:cosmosdb/mongoUserDefinition:MongoUserDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cosmos_mongo_database_id: Optional[pulumi.Input[str]] = None,
            inherited_role_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            password: Optional[pulumi.Input[str]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'MongoUserDefinition':
        """
        Get an existing MongoUserDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cosmos_mongo_database_id: The resource ID of the Mongo DB. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] inherited_role_names: A list of Mongo Roles that are inherited to the Mongo User Definition.
               
               > **Note:** The role that needs to be inherited should exist in the Mongo DB of `cosmos_mongo_database_id`.
        :param pulumi.Input[str] password: The password for the Mongo User Definition.
        :param pulumi.Input[str] username: The username for the Mongo User Definition. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MongoUserDefinitionState.__new__(_MongoUserDefinitionState)

        __props__.__dict__["cosmos_mongo_database_id"] = cosmos_mongo_database_id
        __props__.__dict__["inherited_role_names"] = inherited_role_names
        __props__.__dict__["password"] = password
        __props__.__dict__["username"] = username
        return MongoUserDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cosmosMongoDatabaseId")
    def cosmos_mongo_database_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the Mongo DB. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cosmos_mongo_database_id")

    @property
    @pulumi.getter(name="inheritedRoleNames")
    def inherited_role_names(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of Mongo Roles that are inherited to the Mongo User Definition.

        > **Note:** The role that needs to be inherited should exist in the Mongo DB of `cosmos_mongo_database_id`.
        """
        return pulumi.get(self, "inherited_role_names")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        The password for the Mongo User Definition.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        The username for the Mongo User Definition. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "username")


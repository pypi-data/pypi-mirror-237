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

__all__ = ['AppConnectionArgs', 'AppConnection']

@pulumi.input_type
class AppConnectionArgs:
    def __init__(__self__, *,
                 authentication: pulumi.Input['AppConnectionAuthenticationArgs'],
                 function_app_id: pulumi.Input[str],
                 target_resource_id: pulumi.Input[str],
                 client_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 secret_store: Optional[pulumi.Input['AppConnectionSecretStoreArgs']] = None,
                 vnet_solution: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AppConnection resource.
        :param pulumi.Input['AppConnectionAuthenticationArgs'] authentication: The authentication info. An `authentication` block as defined below.
               
               > **Note:** If a Managed Identity is used, this will need to be configured on the App Service.
        :param pulumi.Input[str] function_app_id: The ID of the data source function app. Changing this forces a new resource to be created.
        :param pulumi.Input[str] target_resource_id: The ID of the target resource. Changing this forces a new resource to be created. Possible target resources are `Postgres`, `PostgresFlexible`, `Mysql`, `Sql`, `Redis`, `RedisEnterprise`, `CosmosCassandra`, `CosmosGremlin`, `CosmosMongo`, `CosmosSql`, `CosmosTable`, `StorageBlob`, `StorageQueue`, `StorageFile`, `StorageTable`, `AppConfig`, `EventHub`, `ServiceBus`, `SignalR`, `WebPubSub`, `ConfluentKafka`. The integration guide can be found [here](https://learn.microsoft.com/en-us/azure/service-connector/how-to-integrate-postgres).
        :param pulumi.Input[str] client_type: The application client type. Possible values are `none`, `dotnet`, `java`, `python`, `go`, `php`, `ruby`, `django`, `nodejs` and `springBoot`.
        :param pulumi.Input[str] name: The name of the service connection. Changing this forces a new resource to be created.
        :param pulumi.Input['AppConnectionSecretStoreArgs'] secret_store: An option to store secret value in secure place. An `secret_store` block as defined below.
        :param pulumi.Input[str] vnet_solution: The type of the VNet solution. Possible values are `serviceEndpoint`, `privateLink`.
        """
        AppConnectionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            authentication=authentication,
            function_app_id=function_app_id,
            target_resource_id=target_resource_id,
            client_type=client_type,
            name=name,
            secret_store=secret_store,
            vnet_solution=vnet_solution,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             authentication: pulumi.Input['AppConnectionAuthenticationArgs'],
             function_app_id: pulumi.Input[str],
             target_resource_id: pulumi.Input[str],
             client_type: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             secret_store: Optional[pulumi.Input['AppConnectionSecretStoreArgs']] = None,
             vnet_solution: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'functionAppId' in kwargs:
            function_app_id = kwargs['functionAppId']
        if 'targetResourceId' in kwargs:
            target_resource_id = kwargs['targetResourceId']
        if 'clientType' in kwargs:
            client_type = kwargs['clientType']
        if 'secretStore' in kwargs:
            secret_store = kwargs['secretStore']
        if 'vnetSolution' in kwargs:
            vnet_solution = kwargs['vnetSolution']

        _setter("authentication", authentication)
        _setter("function_app_id", function_app_id)
        _setter("target_resource_id", target_resource_id)
        if client_type is not None:
            _setter("client_type", client_type)
        if name is not None:
            _setter("name", name)
        if secret_store is not None:
            _setter("secret_store", secret_store)
        if vnet_solution is not None:
            _setter("vnet_solution", vnet_solution)

    @property
    @pulumi.getter
    def authentication(self) -> pulumi.Input['AppConnectionAuthenticationArgs']:
        """
        The authentication info. An `authentication` block as defined below.

        > **Note:** If a Managed Identity is used, this will need to be configured on the App Service.
        """
        return pulumi.get(self, "authentication")

    @authentication.setter
    def authentication(self, value: pulumi.Input['AppConnectionAuthenticationArgs']):
        pulumi.set(self, "authentication", value)

    @property
    @pulumi.getter(name="functionAppId")
    def function_app_id(self) -> pulumi.Input[str]:
        """
        The ID of the data source function app. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "function_app_id")

    @function_app_id.setter
    def function_app_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "function_app_id", value)

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> pulumi.Input[str]:
        """
        The ID of the target resource. Changing this forces a new resource to be created. Possible target resources are `Postgres`, `PostgresFlexible`, `Mysql`, `Sql`, `Redis`, `RedisEnterprise`, `CosmosCassandra`, `CosmosGremlin`, `CosmosMongo`, `CosmosSql`, `CosmosTable`, `StorageBlob`, `StorageQueue`, `StorageFile`, `StorageTable`, `AppConfig`, `EventHub`, `ServiceBus`, `SignalR`, `WebPubSub`, `ConfluentKafka`. The integration guide can be found [here](https://learn.microsoft.com/en-us/azure/service-connector/how-to-integrate-postgres).
        """
        return pulumi.get(self, "target_resource_id")

    @target_resource_id.setter
    def target_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_resource_id", value)

    @property
    @pulumi.getter(name="clientType")
    def client_type(self) -> Optional[pulumi.Input[str]]:
        """
        The application client type. Possible values are `none`, `dotnet`, `java`, `python`, `go`, `php`, `ruby`, `django`, `nodejs` and `springBoot`.
        """
        return pulumi.get(self, "client_type")

    @client_type.setter
    def client_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the service connection. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="secretStore")
    def secret_store(self) -> Optional[pulumi.Input['AppConnectionSecretStoreArgs']]:
        """
        An option to store secret value in secure place. An `secret_store` block as defined below.
        """
        return pulumi.get(self, "secret_store")

    @secret_store.setter
    def secret_store(self, value: Optional[pulumi.Input['AppConnectionSecretStoreArgs']]):
        pulumi.set(self, "secret_store", value)

    @property
    @pulumi.getter(name="vnetSolution")
    def vnet_solution(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the VNet solution. Possible values are `serviceEndpoint`, `privateLink`.
        """
        return pulumi.get(self, "vnet_solution")

    @vnet_solution.setter
    def vnet_solution(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vnet_solution", value)


@pulumi.input_type
class _AppConnectionState:
    def __init__(__self__, *,
                 authentication: Optional[pulumi.Input['AppConnectionAuthenticationArgs']] = None,
                 client_type: Optional[pulumi.Input[str]] = None,
                 function_app_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 secret_store: Optional[pulumi.Input['AppConnectionSecretStoreArgs']] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 vnet_solution: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AppConnection resources.
        :param pulumi.Input['AppConnectionAuthenticationArgs'] authentication: The authentication info. An `authentication` block as defined below.
               
               > **Note:** If a Managed Identity is used, this will need to be configured on the App Service.
        :param pulumi.Input[str] client_type: The application client type. Possible values are `none`, `dotnet`, `java`, `python`, `go`, `php`, `ruby`, `django`, `nodejs` and `springBoot`.
        :param pulumi.Input[str] function_app_id: The ID of the data source function app. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the service connection. Changing this forces a new resource to be created.
        :param pulumi.Input['AppConnectionSecretStoreArgs'] secret_store: An option to store secret value in secure place. An `secret_store` block as defined below.
        :param pulumi.Input[str] target_resource_id: The ID of the target resource. Changing this forces a new resource to be created. Possible target resources are `Postgres`, `PostgresFlexible`, `Mysql`, `Sql`, `Redis`, `RedisEnterprise`, `CosmosCassandra`, `CosmosGremlin`, `CosmosMongo`, `CosmosSql`, `CosmosTable`, `StorageBlob`, `StorageQueue`, `StorageFile`, `StorageTable`, `AppConfig`, `EventHub`, `ServiceBus`, `SignalR`, `WebPubSub`, `ConfluentKafka`. The integration guide can be found [here](https://learn.microsoft.com/en-us/azure/service-connector/how-to-integrate-postgres).
        :param pulumi.Input[str] vnet_solution: The type of the VNet solution. Possible values are `serviceEndpoint`, `privateLink`.
        """
        _AppConnectionState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            authentication=authentication,
            client_type=client_type,
            function_app_id=function_app_id,
            name=name,
            secret_store=secret_store,
            target_resource_id=target_resource_id,
            vnet_solution=vnet_solution,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             authentication: Optional[pulumi.Input['AppConnectionAuthenticationArgs']] = None,
             client_type: Optional[pulumi.Input[str]] = None,
             function_app_id: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             secret_store: Optional[pulumi.Input['AppConnectionSecretStoreArgs']] = None,
             target_resource_id: Optional[pulumi.Input[str]] = None,
             vnet_solution: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'clientType' in kwargs:
            client_type = kwargs['clientType']
        if 'functionAppId' in kwargs:
            function_app_id = kwargs['functionAppId']
        if 'secretStore' in kwargs:
            secret_store = kwargs['secretStore']
        if 'targetResourceId' in kwargs:
            target_resource_id = kwargs['targetResourceId']
        if 'vnetSolution' in kwargs:
            vnet_solution = kwargs['vnetSolution']

        if authentication is not None:
            _setter("authentication", authentication)
        if client_type is not None:
            _setter("client_type", client_type)
        if function_app_id is not None:
            _setter("function_app_id", function_app_id)
        if name is not None:
            _setter("name", name)
        if secret_store is not None:
            _setter("secret_store", secret_store)
        if target_resource_id is not None:
            _setter("target_resource_id", target_resource_id)
        if vnet_solution is not None:
            _setter("vnet_solution", vnet_solution)

    @property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input['AppConnectionAuthenticationArgs']]:
        """
        The authentication info. An `authentication` block as defined below.

        > **Note:** If a Managed Identity is used, this will need to be configured on the App Service.
        """
        return pulumi.get(self, "authentication")

    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input['AppConnectionAuthenticationArgs']]):
        pulumi.set(self, "authentication", value)

    @property
    @pulumi.getter(name="clientType")
    def client_type(self) -> Optional[pulumi.Input[str]]:
        """
        The application client type. Possible values are `none`, `dotnet`, `java`, `python`, `go`, `php`, `ruby`, `django`, `nodejs` and `springBoot`.
        """
        return pulumi.get(self, "client_type")

    @client_type.setter
    def client_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_type", value)

    @property
    @pulumi.getter(name="functionAppId")
    def function_app_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the data source function app. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "function_app_id")

    @function_app_id.setter
    def function_app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "function_app_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the service connection. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="secretStore")
    def secret_store(self) -> Optional[pulumi.Input['AppConnectionSecretStoreArgs']]:
        """
        An option to store secret value in secure place. An `secret_store` block as defined below.
        """
        return pulumi.get(self, "secret_store")

    @secret_store.setter
    def secret_store(self, value: Optional[pulumi.Input['AppConnectionSecretStoreArgs']]):
        pulumi.set(self, "secret_store", value)

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the target resource. Changing this forces a new resource to be created. Possible target resources are `Postgres`, `PostgresFlexible`, `Mysql`, `Sql`, `Redis`, `RedisEnterprise`, `CosmosCassandra`, `CosmosGremlin`, `CosmosMongo`, `CosmosSql`, `CosmosTable`, `StorageBlob`, `StorageQueue`, `StorageFile`, `StorageTable`, `AppConfig`, `EventHub`, `ServiceBus`, `SignalR`, `WebPubSub`, `ConfluentKafka`. The integration guide can be found [here](https://learn.microsoft.com/en-us/azure/service-connector/how-to-integrate-postgres).
        """
        return pulumi.get(self, "target_resource_id")

    @target_resource_id.setter
    def target_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_resource_id", value)

    @property
    @pulumi.getter(name="vnetSolution")
    def vnet_solution(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the VNet solution. Possible values are `serviceEndpoint`, `privateLink`.
        """
        return pulumi.get(self, "vnet_solution")

    @vnet_solution.setter
    def vnet_solution(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vnet_solution", value)


class AppConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication: Optional[pulumi.Input[pulumi.InputType['AppConnectionAuthenticationArgs']]] = None,
                 client_type: Optional[pulumi.Input[str]] = None,
                 function_app_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 secret_store: Optional[pulumi.Input[pulumi.InputType['AppConnectionSecretStoreArgs']]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 vnet_solution: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a service connector for function app.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.cosmosdb.Account("exampleAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            offer_type="Standard",
            kind="GlobalDocumentDB",
            consistency_policy=azure.cosmosdb.AccountConsistencyPolicyArgs(
                consistency_level="BoundedStaleness",
                max_interval_in_seconds=10,
                max_staleness_prefix=200,
            ),
            geo_locations=[azure.cosmosdb.AccountGeoLocationArgs(
                location=example_resource_group.location,
                failover_priority=0,
            )])
        example_sql_database = azure.cosmosdb.SqlDatabase("exampleSqlDatabase",
            resource_group_name=example_account.resource_group_name,
            account_name=example_account.name,
            throughput=400)
        example_sql_container = azure.cosmosdb.SqlContainer("exampleSqlContainer",
            resource_group_name=example_account.resource_group_name,
            account_name=example_account.name,
            database_name=example_sql_database.name,
            partition_key_path="/definition")
        example_storage_account_account = azure.storage.Account("exampleStorage/accountAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_service_plan = azure.appservice.ServicePlan("exampleServicePlan",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="P1v2",
            os_type="Linux")
        test = azure.appservice.FunctionApp("test",
            location=azurerm_resource_group["test"]["location"],
            resource_group_name=azurerm_resource_group["test"]["name"],
            app_service_plan_id=azurerm_app_service_plan["test"]["id"],
            storage_account_name=azurerm_storage_account["test"]["name"],
            storage_account_access_key=azurerm_storage_account["test"]["primary_access_key"])
        example_app_connection = azure.appservice.AppConnection("exampleAppConnection",
            function_app_id=azurerm_function_app["example"]["id"],
            target_resource_id=azurerm_cosmosdb_account["test"]["id"],
            authentication=azure.appservice.AppConnectionAuthenticationArgs(
                type="systemAssignedIdentity",
            ))
        ```

        ## Import

        Service Connector for app service can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appservice/appConnection:AppConnection example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Web/sites/webapp/providers/Microsoft.ServiceLinker/linkers/serviceconnector1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AppConnectionAuthenticationArgs']] authentication: The authentication info. An `authentication` block as defined below.
               
               > **Note:** If a Managed Identity is used, this will need to be configured on the App Service.
        :param pulumi.Input[str] client_type: The application client type. Possible values are `none`, `dotnet`, `java`, `python`, `go`, `php`, `ruby`, `django`, `nodejs` and `springBoot`.
        :param pulumi.Input[str] function_app_id: The ID of the data source function app. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the service connection. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['AppConnectionSecretStoreArgs']] secret_store: An option to store secret value in secure place. An `secret_store` block as defined below.
        :param pulumi.Input[str] target_resource_id: The ID of the target resource. Changing this forces a new resource to be created. Possible target resources are `Postgres`, `PostgresFlexible`, `Mysql`, `Sql`, `Redis`, `RedisEnterprise`, `CosmosCassandra`, `CosmosGremlin`, `CosmosMongo`, `CosmosSql`, `CosmosTable`, `StorageBlob`, `StorageQueue`, `StorageFile`, `StorageTable`, `AppConfig`, `EventHub`, `ServiceBus`, `SignalR`, `WebPubSub`, `ConfluentKafka`. The integration guide can be found [here](https://learn.microsoft.com/en-us/azure/service-connector/how-to-integrate-postgres).
        :param pulumi.Input[str] vnet_solution: The type of the VNet solution. Possible values are `serviceEndpoint`, `privateLink`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a service connector for function app.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.cosmosdb.Account("exampleAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            offer_type="Standard",
            kind="GlobalDocumentDB",
            consistency_policy=azure.cosmosdb.AccountConsistencyPolicyArgs(
                consistency_level="BoundedStaleness",
                max_interval_in_seconds=10,
                max_staleness_prefix=200,
            ),
            geo_locations=[azure.cosmosdb.AccountGeoLocationArgs(
                location=example_resource_group.location,
                failover_priority=0,
            )])
        example_sql_database = azure.cosmosdb.SqlDatabase("exampleSqlDatabase",
            resource_group_name=example_account.resource_group_name,
            account_name=example_account.name,
            throughput=400)
        example_sql_container = azure.cosmosdb.SqlContainer("exampleSqlContainer",
            resource_group_name=example_account.resource_group_name,
            account_name=example_account.name,
            database_name=example_sql_database.name,
            partition_key_path="/definition")
        example_storage_account_account = azure.storage.Account("exampleStorage/accountAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_service_plan = azure.appservice.ServicePlan("exampleServicePlan",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="P1v2",
            os_type="Linux")
        test = azure.appservice.FunctionApp("test",
            location=azurerm_resource_group["test"]["location"],
            resource_group_name=azurerm_resource_group["test"]["name"],
            app_service_plan_id=azurerm_app_service_plan["test"]["id"],
            storage_account_name=azurerm_storage_account["test"]["name"],
            storage_account_access_key=azurerm_storage_account["test"]["primary_access_key"])
        example_app_connection = azure.appservice.AppConnection("exampleAppConnection",
            function_app_id=azurerm_function_app["example"]["id"],
            target_resource_id=azurerm_cosmosdb_account["test"]["id"],
            authentication=azure.appservice.AppConnectionAuthenticationArgs(
                type="systemAssignedIdentity",
            ))
        ```

        ## Import

        Service Connector for app service can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appservice/appConnection:AppConnection example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Web/sites/webapp/providers/Microsoft.ServiceLinker/linkers/serviceconnector1
        ```

        :param str resource_name: The name of the resource.
        :param AppConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AppConnectionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication: Optional[pulumi.Input[pulumi.InputType['AppConnectionAuthenticationArgs']]] = None,
                 client_type: Optional[pulumi.Input[str]] = None,
                 function_app_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 secret_store: Optional[pulumi.Input[pulumi.InputType['AppConnectionSecretStoreArgs']]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 vnet_solution: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AppConnectionArgs.__new__(AppConnectionArgs)

            if authentication is not None and not isinstance(authentication, AppConnectionAuthenticationArgs):
                authentication = authentication or {}
                def _setter(key, value):
                    authentication[key] = value
                AppConnectionAuthenticationArgs._configure(_setter, **authentication)
            if authentication is None and not opts.urn:
                raise TypeError("Missing required property 'authentication'")
            __props__.__dict__["authentication"] = authentication
            __props__.__dict__["client_type"] = client_type
            if function_app_id is None and not opts.urn:
                raise TypeError("Missing required property 'function_app_id'")
            __props__.__dict__["function_app_id"] = function_app_id
            __props__.__dict__["name"] = name
            if secret_store is not None and not isinstance(secret_store, AppConnectionSecretStoreArgs):
                secret_store = secret_store or {}
                def _setter(key, value):
                    secret_store[key] = value
                AppConnectionSecretStoreArgs._configure(_setter, **secret_store)
            __props__.__dict__["secret_store"] = secret_store
            if target_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'target_resource_id'")
            __props__.__dict__["target_resource_id"] = target_resource_id
            __props__.__dict__["vnet_solution"] = vnet_solution
        super(AppConnection, __self__).__init__(
            'azure:appservice/appConnection:AppConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authentication: Optional[pulumi.Input[pulumi.InputType['AppConnectionAuthenticationArgs']]] = None,
            client_type: Optional[pulumi.Input[str]] = None,
            function_app_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            secret_store: Optional[pulumi.Input[pulumi.InputType['AppConnectionSecretStoreArgs']]] = None,
            target_resource_id: Optional[pulumi.Input[str]] = None,
            vnet_solution: Optional[pulumi.Input[str]] = None) -> 'AppConnection':
        """
        Get an existing AppConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AppConnectionAuthenticationArgs']] authentication: The authentication info. An `authentication` block as defined below.
               
               > **Note:** If a Managed Identity is used, this will need to be configured on the App Service.
        :param pulumi.Input[str] client_type: The application client type. Possible values are `none`, `dotnet`, `java`, `python`, `go`, `php`, `ruby`, `django`, `nodejs` and `springBoot`.
        :param pulumi.Input[str] function_app_id: The ID of the data source function app. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the service connection. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['AppConnectionSecretStoreArgs']] secret_store: An option to store secret value in secure place. An `secret_store` block as defined below.
        :param pulumi.Input[str] target_resource_id: The ID of the target resource. Changing this forces a new resource to be created. Possible target resources are `Postgres`, `PostgresFlexible`, `Mysql`, `Sql`, `Redis`, `RedisEnterprise`, `CosmosCassandra`, `CosmosGremlin`, `CosmosMongo`, `CosmosSql`, `CosmosTable`, `StorageBlob`, `StorageQueue`, `StorageFile`, `StorageTable`, `AppConfig`, `EventHub`, `ServiceBus`, `SignalR`, `WebPubSub`, `ConfluentKafka`. The integration guide can be found [here](https://learn.microsoft.com/en-us/azure/service-connector/how-to-integrate-postgres).
        :param pulumi.Input[str] vnet_solution: The type of the VNet solution. Possible values are `serviceEndpoint`, `privateLink`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AppConnectionState.__new__(_AppConnectionState)

        __props__.__dict__["authentication"] = authentication
        __props__.__dict__["client_type"] = client_type
        __props__.__dict__["function_app_id"] = function_app_id
        __props__.__dict__["name"] = name
        __props__.__dict__["secret_store"] = secret_store
        __props__.__dict__["target_resource_id"] = target_resource_id
        __props__.__dict__["vnet_solution"] = vnet_solution
        return AppConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def authentication(self) -> pulumi.Output['outputs.AppConnectionAuthentication']:
        """
        The authentication info. An `authentication` block as defined below.

        > **Note:** If a Managed Identity is used, this will need to be configured on the App Service.
        """
        return pulumi.get(self, "authentication")

    @property
    @pulumi.getter(name="clientType")
    def client_type(self) -> pulumi.Output[Optional[str]]:
        """
        The application client type. Possible values are `none`, `dotnet`, `java`, `python`, `go`, `php`, `ruby`, `django`, `nodejs` and `springBoot`.
        """
        return pulumi.get(self, "client_type")

    @property
    @pulumi.getter(name="functionAppId")
    def function_app_id(self) -> pulumi.Output[str]:
        """
        The ID of the data source function app. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "function_app_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the service connection. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="secretStore")
    def secret_store(self) -> pulumi.Output[Optional['outputs.AppConnectionSecretStore']]:
        """
        An option to store secret value in secure place. An `secret_store` block as defined below.
        """
        return pulumi.get(self, "secret_store")

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> pulumi.Output[str]:
        """
        The ID of the target resource. Changing this forces a new resource to be created. Possible target resources are `Postgres`, `PostgresFlexible`, `Mysql`, `Sql`, `Redis`, `RedisEnterprise`, `CosmosCassandra`, `CosmosGremlin`, `CosmosMongo`, `CosmosSql`, `CosmosTable`, `StorageBlob`, `StorageQueue`, `StorageFile`, `StorageTable`, `AppConfig`, `EventHub`, `ServiceBus`, `SignalR`, `WebPubSub`, `ConfluentKafka`. The integration guide can be found [here](https://learn.microsoft.com/en-us/azure/service-connector/how-to-integrate-postgres).
        """
        return pulumi.get(self, "target_resource_id")

    @property
    @pulumi.getter(name="vnetSolution")
    def vnet_solution(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the VNet solution. Possible values are `serviceEndpoint`, `privateLink`.
        """
        return pulumi.get(self, "vnet_solution")


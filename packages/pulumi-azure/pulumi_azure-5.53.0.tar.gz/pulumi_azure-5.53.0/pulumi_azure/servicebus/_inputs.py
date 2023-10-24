# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'NamespaceCustomerManagedKeyArgs',
    'NamespaceIdentityArgs',
    'NamespaceNetworkRuleSetArgs',
    'NamespaceNetworkRuleSetNetworkRuleArgs',
    'SubscriptionClientScopedSubscriptionArgs',
    'SubscriptionRuleCorrelationFilterArgs',
]

@pulumi.input_type
class NamespaceCustomerManagedKeyArgs:
    def __init__(__self__, *,
                 identity_id: pulumi.Input[str],
                 key_vault_key_id: pulumi.Input[str],
                 infrastructure_encryption_enabled: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] identity_id: The ID of the User Assigned Identity that has access to the key.
        :param pulumi.Input[str] key_vault_key_id: The ID of the Key Vault Key which should be used to Encrypt the data in this ServiceBus Namespace.
        :param pulumi.Input[bool] infrastructure_encryption_enabled: Used to specify whether enable Infrastructure Encryption (Double Encryption). Changing this forces a new resource to be created.
        """
        NamespaceCustomerManagedKeyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            identity_id=identity_id,
            key_vault_key_id=key_vault_key_id,
            infrastructure_encryption_enabled=infrastructure_encryption_enabled,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             identity_id: pulumi.Input[str],
             key_vault_key_id: pulumi.Input[str],
             infrastructure_encryption_enabled: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'identityId' in kwargs:
            identity_id = kwargs['identityId']
        if 'keyVaultKeyId' in kwargs:
            key_vault_key_id = kwargs['keyVaultKeyId']
        if 'infrastructureEncryptionEnabled' in kwargs:
            infrastructure_encryption_enabled = kwargs['infrastructureEncryptionEnabled']

        _setter("identity_id", identity_id)
        _setter("key_vault_key_id", key_vault_key_id)
        if infrastructure_encryption_enabled is not None:
            _setter("infrastructure_encryption_enabled", infrastructure_encryption_enabled)

    @property
    @pulumi.getter(name="identityId")
    def identity_id(self) -> pulumi.Input[str]:
        """
        The ID of the User Assigned Identity that has access to the key.
        """
        return pulumi.get(self, "identity_id")

    @identity_id.setter
    def identity_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "identity_id", value)

    @property
    @pulumi.getter(name="keyVaultKeyId")
    def key_vault_key_id(self) -> pulumi.Input[str]:
        """
        The ID of the Key Vault Key which should be used to Encrypt the data in this ServiceBus Namespace.
        """
        return pulumi.get(self, "key_vault_key_id")

    @key_vault_key_id.setter
    def key_vault_key_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_vault_key_id", value)

    @property
    @pulumi.getter(name="infrastructureEncryptionEnabled")
    def infrastructure_encryption_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Used to specify whether enable Infrastructure Encryption (Double Encryption). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "infrastructure_encryption_enabled")

    @infrastructure_encryption_enabled.setter
    def infrastructure_encryption_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "infrastructure_encryption_enabled", value)


@pulumi.input_type
class NamespaceIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 identity_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: Specifies the type of Managed Service Identity that should be configured on this ServiceBus Namespace. Possible values are `SystemAssigned`, `UserAssigned`, `SystemAssigned, UserAssigned` (to enable both).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] identity_ids: Specifies a list of User Assigned Managed Identity IDs to be assigned to this ServiceBus namespace.
               
               > **NOTE:** This is required when `type` is set to `UserAssigned` or `SystemAssigned, UserAssigned`.
        :param pulumi.Input[str] principal_id: The Principal ID for the Service Principal associated with the Managed Service Identity of this ServiceBus Namespace.
        :param pulumi.Input[str] tenant_id: The Tenant ID for the Service Principal associated with the Managed Service Identity of this ServiceBus Namespace.
        """
        NamespaceIdentityArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            type=type,
            identity_ids=identity_ids,
            principal_id=principal_id,
            tenant_id=tenant_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             type: pulumi.Input[str],
             identity_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             principal_id: Optional[pulumi.Input[str]] = None,
             tenant_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'identityIds' in kwargs:
            identity_ids = kwargs['identityIds']
        if 'principalId' in kwargs:
            principal_id = kwargs['principalId']
        if 'tenantId' in kwargs:
            tenant_id = kwargs['tenantId']

        _setter("type", type)
        if identity_ids is not None:
            _setter("identity_ids", identity_ids)
        if principal_id is not None:
            _setter("principal_id", principal_id)
        if tenant_id is not None:
            _setter("tenant_id", tenant_id)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Specifies the type of Managed Service Identity that should be configured on this ServiceBus Namespace. Possible values are `SystemAssigned`, `UserAssigned`, `SystemAssigned, UserAssigned` (to enable both).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="identityIds")
    def identity_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies a list of User Assigned Managed Identity IDs to be assigned to this ServiceBus namespace.

        > **NOTE:** This is required when `type` is set to `UserAssigned` or `SystemAssigned, UserAssigned`.
        """
        return pulumi.get(self, "identity_ids")

    @identity_ids.setter
    def identity_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "identity_ids", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Principal ID for the Service Principal associated with the Managed Service Identity of this ServiceBus Namespace.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Tenant ID for the Service Principal associated with the Managed Service Identity of this ServiceBus Namespace.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


@pulumi.input_type
class NamespaceNetworkRuleSetArgs:
    def __init__(__self__, *,
                 default_action: Optional[pulumi.Input[str]] = None,
                 ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 network_rules: Optional[pulumi.Input[Sequence[pulumi.Input['NamespaceNetworkRuleSetNetworkRuleArgs']]]] = None,
                 public_network_access_enabled: Optional[pulumi.Input[bool]] = None,
                 trusted_services_allowed: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] default_action: Specifies the default action for the Network Rule Set. Possible values are `Allow` and `Deny`. Defaults to `Deny`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_rules: One or more IP Addresses, or CIDR Blocks which should be able to access the ServiceBus Namespace.
        :param pulumi.Input[Sequence[pulumi.Input['NamespaceNetworkRuleSetNetworkRuleArgs']]] network_rules: One or more `network_rules` blocks as defined below.
        :param pulumi.Input[bool] public_network_access_enabled: Whether to allow traffic over public network. Possible values are `true` and `false`. Defaults to `true`.
        :param pulumi.Input[bool] trusted_services_allowed: Are Azure Services that are known and trusted for this resource type are allowed to bypass firewall configuration? See [Trusted Microsoft Services](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/service-bus-messaging/includes/service-bus-trusted-services.md)
        """
        NamespaceNetworkRuleSetArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            default_action=default_action,
            ip_rules=ip_rules,
            network_rules=network_rules,
            public_network_access_enabled=public_network_access_enabled,
            trusted_services_allowed=trusted_services_allowed,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             default_action: Optional[pulumi.Input[str]] = None,
             ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             network_rules: Optional[pulumi.Input[Sequence[pulumi.Input['NamespaceNetworkRuleSetNetworkRuleArgs']]]] = None,
             public_network_access_enabled: Optional[pulumi.Input[bool]] = None,
             trusted_services_allowed: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'defaultAction' in kwargs:
            default_action = kwargs['defaultAction']
        if 'ipRules' in kwargs:
            ip_rules = kwargs['ipRules']
        if 'networkRules' in kwargs:
            network_rules = kwargs['networkRules']
        if 'publicNetworkAccessEnabled' in kwargs:
            public_network_access_enabled = kwargs['publicNetworkAccessEnabled']
        if 'trustedServicesAllowed' in kwargs:
            trusted_services_allowed = kwargs['trustedServicesAllowed']

        if default_action is not None:
            _setter("default_action", default_action)
        if ip_rules is not None:
            _setter("ip_rules", ip_rules)
        if network_rules is not None:
            _setter("network_rules", network_rules)
        if public_network_access_enabled is not None:
            _setter("public_network_access_enabled", public_network_access_enabled)
        if trusted_services_allowed is not None:
            _setter("trusted_services_allowed", trusted_services_allowed)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the default action for the Network Rule Set. Possible values are `Allow` and `Deny`. Defaults to `Deny`.
        """
        return pulumi.get(self, "default_action")

    @default_action.setter
    def default_action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_action", value)

    @property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        One or more IP Addresses, or CIDR Blocks which should be able to access the ServiceBus Namespace.
        """
        return pulumi.get(self, "ip_rules")

    @ip_rules.setter
    def ip_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ip_rules", value)

    @property
    @pulumi.getter(name="networkRules")
    def network_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NamespaceNetworkRuleSetNetworkRuleArgs']]]]:
        """
        One or more `network_rules` blocks as defined below.
        """
        return pulumi.get(self, "network_rules")

    @network_rules.setter
    def network_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NamespaceNetworkRuleSetNetworkRuleArgs']]]]):
        pulumi.set(self, "network_rules", value)

    @property
    @pulumi.getter(name="publicNetworkAccessEnabled")
    def public_network_access_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to allow traffic over public network. Possible values are `true` and `false`. Defaults to `true`.
        """
        return pulumi.get(self, "public_network_access_enabled")

    @public_network_access_enabled.setter
    def public_network_access_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public_network_access_enabled", value)

    @property
    @pulumi.getter(name="trustedServicesAllowed")
    def trusted_services_allowed(self) -> Optional[pulumi.Input[bool]]:
        """
        Are Azure Services that are known and trusted for this resource type are allowed to bypass firewall configuration? See [Trusted Microsoft Services](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/service-bus-messaging/includes/service-bus-trusted-services.md)
        """
        return pulumi.get(self, "trusted_services_allowed")

    @trusted_services_allowed.setter
    def trusted_services_allowed(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "trusted_services_allowed", value)


@pulumi.input_type
class NamespaceNetworkRuleSetNetworkRuleArgs:
    def __init__(__self__, *,
                 subnet_id: pulumi.Input[str],
                 ignore_missing_vnet_service_endpoint: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] subnet_id: The Subnet ID which should be able to access this ServiceBus Namespace.
        :param pulumi.Input[bool] ignore_missing_vnet_service_endpoint: Should the ServiceBus Namespace Network Rule Set ignore missing Virtual Network Service Endpoint option in the Subnet? Defaults to `false`.
        """
        NamespaceNetworkRuleSetNetworkRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            subnet_id=subnet_id,
            ignore_missing_vnet_service_endpoint=ignore_missing_vnet_service_endpoint,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             subnet_id: pulumi.Input[str],
             ignore_missing_vnet_service_endpoint: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'subnetId' in kwargs:
            subnet_id = kwargs['subnetId']
        if 'ignoreMissingVnetServiceEndpoint' in kwargs:
            ignore_missing_vnet_service_endpoint = kwargs['ignoreMissingVnetServiceEndpoint']

        _setter("subnet_id", subnet_id)
        if ignore_missing_vnet_service_endpoint is not None:
            _setter("ignore_missing_vnet_service_endpoint", ignore_missing_vnet_service_endpoint)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        The Subnet ID which should be able to access this ServiceBus Namespace.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter(name="ignoreMissingVnetServiceEndpoint")
    def ignore_missing_vnet_service_endpoint(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the ServiceBus Namespace Network Rule Set ignore missing Virtual Network Service Endpoint option in the Subnet? Defaults to `false`.
        """
        return pulumi.get(self, "ignore_missing_vnet_service_endpoint")

    @ignore_missing_vnet_service_endpoint.setter
    def ignore_missing_vnet_service_endpoint(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_missing_vnet_service_endpoint", value)


@pulumi.input_type
class SubscriptionClientScopedSubscriptionArgs:
    def __init__(__self__, *,
                 client_id: Optional[pulumi.Input[str]] = None,
                 is_client_scoped_subscription_durable: Optional[pulumi.Input[bool]] = None,
                 is_client_scoped_subscription_shareable: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] client_id: Specifies the Client ID of the application that created the client-scoped subscription. Changing this forces a new resource to be created.
               
               > **NOTE:** Client ID can be null or empty, but it must match the client ID set on the JMS client application. From the Azure Service Bus perspective, a null client ID and an empty client id have the same behavior. If the client ID is set to null or empty, it is only accessible to client applications whose client ID is also set to null or empty.
        :param pulumi.Input[bool] is_client_scoped_subscription_durable: Whether the client scoped subscription is durable. This property can only be controlled from the application side.
        :param pulumi.Input[bool] is_client_scoped_subscription_shareable: Whether the client scoped subscription is shareable. Defaults to `true` Changing this forces a new resource to be created.
        """
        SubscriptionClientScopedSubscriptionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            client_id=client_id,
            is_client_scoped_subscription_durable=is_client_scoped_subscription_durable,
            is_client_scoped_subscription_shareable=is_client_scoped_subscription_shareable,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             client_id: Optional[pulumi.Input[str]] = None,
             is_client_scoped_subscription_durable: Optional[pulumi.Input[bool]] = None,
             is_client_scoped_subscription_shareable: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'clientId' in kwargs:
            client_id = kwargs['clientId']
        if 'isClientScopedSubscriptionDurable' in kwargs:
            is_client_scoped_subscription_durable = kwargs['isClientScopedSubscriptionDurable']
        if 'isClientScopedSubscriptionShareable' in kwargs:
            is_client_scoped_subscription_shareable = kwargs['isClientScopedSubscriptionShareable']

        if client_id is not None:
            _setter("client_id", client_id)
        if is_client_scoped_subscription_durable is not None:
            _setter("is_client_scoped_subscription_durable", is_client_scoped_subscription_durable)
        if is_client_scoped_subscription_shareable is not None:
            _setter("is_client_scoped_subscription_shareable", is_client_scoped_subscription_shareable)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Client ID of the application that created the client-scoped subscription. Changing this forces a new resource to be created.

        > **NOTE:** Client ID can be null or empty, but it must match the client ID set on the JMS client application. From the Azure Service Bus perspective, a null client ID and an empty client id have the same behavior. If the client ID is set to null or empty, it is only accessible to client applications whose client ID is also set to null or empty.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="isClientScopedSubscriptionDurable")
    def is_client_scoped_subscription_durable(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the client scoped subscription is durable. This property can only be controlled from the application side.
        """
        return pulumi.get(self, "is_client_scoped_subscription_durable")

    @is_client_scoped_subscription_durable.setter
    def is_client_scoped_subscription_durable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_client_scoped_subscription_durable", value)

    @property
    @pulumi.getter(name="isClientScopedSubscriptionShareable")
    def is_client_scoped_subscription_shareable(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the client scoped subscription is shareable. Defaults to `true` Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "is_client_scoped_subscription_shareable")

    @is_client_scoped_subscription_shareable.setter
    def is_client_scoped_subscription_shareable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_client_scoped_subscription_shareable", value)


@pulumi.input_type
class SubscriptionRuleCorrelationFilterArgs:
    def __init__(__self__, *,
                 content_type: Optional[pulumi.Input[str]] = None,
                 correlation_id: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 message_id: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 reply_to: Optional[pulumi.Input[str]] = None,
                 reply_to_session_id: Optional[pulumi.Input[str]] = None,
                 session_id: Optional[pulumi.Input[str]] = None,
                 to: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] content_type: Content type of the message.
        :param pulumi.Input[str] correlation_id: Identifier of the correlation.
        :param pulumi.Input[str] label: Application specific label.
        :param pulumi.Input[str] message_id: Identifier of the message.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: A list of user defined properties to be included in the filter. Specified as a map of name/value pairs.
               
               > **NOTE:** When creating a subscription rule of type `CorrelationFilter` at least one property must be set in the `correlation_filter` block.
        :param pulumi.Input[str] reply_to: Address of the queue to reply to.
        :param pulumi.Input[str] reply_to_session_id: Session identifier to reply to.
        :param pulumi.Input[str] session_id: Session identifier.
        :param pulumi.Input[str] to: Address to send to.
        """
        SubscriptionRuleCorrelationFilterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            content_type=content_type,
            correlation_id=correlation_id,
            label=label,
            message_id=message_id,
            properties=properties,
            reply_to=reply_to,
            reply_to_session_id=reply_to_session_id,
            session_id=session_id,
            to=to,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             content_type: Optional[pulumi.Input[str]] = None,
             correlation_id: Optional[pulumi.Input[str]] = None,
             label: Optional[pulumi.Input[str]] = None,
             message_id: Optional[pulumi.Input[str]] = None,
             properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             reply_to: Optional[pulumi.Input[str]] = None,
             reply_to_session_id: Optional[pulumi.Input[str]] = None,
             session_id: Optional[pulumi.Input[str]] = None,
             to: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'contentType' in kwargs:
            content_type = kwargs['contentType']
        if 'correlationId' in kwargs:
            correlation_id = kwargs['correlationId']
        if 'messageId' in kwargs:
            message_id = kwargs['messageId']
        if 'replyTo' in kwargs:
            reply_to = kwargs['replyTo']
        if 'replyToSessionId' in kwargs:
            reply_to_session_id = kwargs['replyToSessionId']
        if 'sessionId' in kwargs:
            session_id = kwargs['sessionId']

        if content_type is not None:
            _setter("content_type", content_type)
        if correlation_id is not None:
            _setter("correlation_id", correlation_id)
        if label is not None:
            _setter("label", label)
        if message_id is not None:
            _setter("message_id", message_id)
        if properties is not None:
            _setter("properties", properties)
        if reply_to is not None:
            _setter("reply_to", reply_to)
        if reply_to_session_id is not None:
            _setter("reply_to_session_id", reply_to_session_id)
        if session_id is not None:
            _setter("session_id", session_id)
        if to is not None:
            _setter("to", to)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[str]]:
        """
        Content type of the message.
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the correlation.
        """
        return pulumi.get(self, "correlation_id")

    @correlation_id.setter
    def correlation_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "correlation_id", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        Application specific label.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="messageId")
    def message_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the message.
        """
        return pulumi.get(self, "message_id")

    @message_id.setter
    def message_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message_id", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A list of user defined properties to be included in the filter. Specified as a map of name/value pairs.

        > **NOTE:** When creating a subscription rule of type `CorrelationFilter` at least one property must be set in the `correlation_filter` block.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="replyTo")
    def reply_to(self) -> Optional[pulumi.Input[str]]:
        """
        Address of the queue to reply to.
        """
        return pulumi.get(self, "reply_to")

    @reply_to.setter
    def reply_to(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reply_to", value)

    @property
    @pulumi.getter(name="replyToSessionId")
    def reply_to_session_id(self) -> Optional[pulumi.Input[str]]:
        """
        Session identifier to reply to.
        """
        return pulumi.get(self, "reply_to_session_id")

    @reply_to_session_id.setter
    def reply_to_session_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reply_to_session_id", value)

    @property
    @pulumi.getter(name="sessionId")
    def session_id(self) -> Optional[pulumi.Input[str]]:
        """
        Session identifier.
        """
        return pulumi.get(self, "session_id")

    @session_id.setter
    def session_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "session_id", value)

    @property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[str]]:
        """
        Address to send to.
        """
        return pulumi.get(self, "to")

    @to.setter
    def to(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "to", value)



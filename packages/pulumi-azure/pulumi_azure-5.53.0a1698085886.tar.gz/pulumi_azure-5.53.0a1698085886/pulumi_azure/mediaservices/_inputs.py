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
    'AccountEncryptionArgs',
    'AccountEncryptionManagedIdentityArgs',
    'AccountIdentityArgs',
    'AccountKeyDeliveryAccessControlArgs',
    'AccountStorageAccountArgs',
    'AccountStorageAccountManagedIdentityArgs',
]

@pulumi.input_type
class AccountEncryptionArgs:
    def __init__(__self__, *,
                 current_key_identifier: Optional[pulumi.Input[str]] = None,
                 key_vault_key_identifier: Optional[pulumi.Input[str]] = None,
                 managed_identity: Optional[pulumi.Input['AccountEncryptionManagedIdentityArgs']] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] current_key_identifier: The current key used to encrypt the Media Services Account, including the key version.
        :param pulumi.Input[str] key_vault_key_identifier: Specifies the URI of the Key Vault Key used to encrypt data. The key may either be versioned (for example https://vault/keys/mykey/version1) or reference a key without a version (for example https://vault/keys/mykey).
        :param pulumi.Input['AccountEncryptionManagedIdentityArgs'] managed_identity: A `managed_identity` block as defined below.
        :param pulumi.Input[str] type: Specifies the type of key used to encrypt the account data. Possible values are `SystemKey` and `CustomerKey`.
        """
        AccountEncryptionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            current_key_identifier=current_key_identifier,
            key_vault_key_identifier=key_vault_key_identifier,
            managed_identity=managed_identity,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             current_key_identifier: Optional[pulumi.Input[str]] = None,
             key_vault_key_identifier: Optional[pulumi.Input[str]] = None,
             managed_identity: Optional[pulumi.Input['AccountEncryptionManagedIdentityArgs']] = None,
             type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'currentKeyIdentifier' in kwargs:
            current_key_identifier = kwargs['currentKeyIdentifier']
        if 'keyVaultKeyIdentifier' in kwargs:
            key_vault_key_identifier = kwargs['keyVaultKeyIdentifier']
        if 'managedIdentity' in kwargs:
            managed_identity = kwargs['managedIdentity']

        if current_key_identifier is not None:
            _setter("current_key_identifier", current_key_identifier)
        if key_vault_key_identifier is not None:
            _setter("key_vault_key_identifier", key_vault_key_identifier)
        if managed_identity is not None:
            _setter("managed_identity", managed_identity)
        if type is not None:
            _setter("type", type)

    @property
    @pulumi.getter(name="currentKeyIdentifier")
    def current_key_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The current key used to encrypt the Media Services Account, including the key version.
        """
        return pulumi.get(self, "current_key_identifier")

    @current_key_identifier.setter
    def current_key_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "current_key_identifier", value)

    @property
    @pulumi.getter(name="keyVaultKeyIdentifier")
    def key_vault_key_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the URI of the Key Vault Key used to encrypt data. The key may either be versioned (for example https://vault/keys/mykey/version1) or reference a key without a version (for example https://vault/keys/mykey).
        """
        return pulumi.get(self, "key_vault_key_identifier")

    @key_vault_key_identifier.setter
    def key_vault_key_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_vault_key_identifier", value)

    @property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> Optional[pulumi.Input['AccountEncryptionManagedIdentityArgs']]:
        """
        A `managed_identity` block as defined below.
        """
        return pulumi.get(self, "managed_identity")

    @managed_identity.setter
    def managed_identity(self, value: Optional[pulumi.Input['AccountEncryptionManagedIdentityArgs']]):
        pulumi.set(self, "managed_identity", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the type of key used to encrypt the account data. Possible values are `SystemKey` and `CustomerKey`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class AccountEncryptionManagedIdentityArgs:
    def __init__(__self__, *,
                 use_system_assigned_identity: Optional[pulumi.Input[bool]] = None,
                 user_assigned_identity_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] use_system_assigned_identity: Whether to use System Assigned Identity. Possible Values are `true` and `false`.
        :param pulumi.Input[str] user_assigned_identity_id: The ID of the User Assigned Identity. This value can only be set when `use_system_assigned_identity` is `false`
        """
        AccountEncryptionManagedIdentityArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            use_system_assigned_identity=use_system_assigned_identity,
            user_assigned_identity_id=user_assigned_identity_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             use_system_assigned_identity: Optional[pulumi.Input[bool]] = None,
             user_assigned_identity_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'useSystemAssignedIdentity' in kwargs:
            use_system_assigned_identity = kwargs['useSystemAssignedIdentity']
        if 'userAssignedIdentityId' in kwargs:
            user_assigned_identity_id = kwargs['userAssignedIdentityId']

        if use_system_assigned_identity is not None:
            _setter("use_system_assigned_identity", use_system_assigned_identity)
        if user_assigned_identity_id is not None:
            _setter("user_assigned_identity_id", user_assigned_identity_id)

    @property
    @pulumi.getter(name="useSystemAssignedIdentity")
    def use_system_assigned_identity(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to use System Assigned Identity. Possible Values are `true` and `false`.
        """
        return pulumi.get(self, "use_system_assigned_identity")

    @use_system_assigned_identity.setter
    def use_system_assigned_identity(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_system_assigned_identity", value)

    @property
    @pulumi.getter(name="userAssignedIdentityId")
    def user_assigned_identity_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the User Assigned Identity. This value can only be set when `use_system_assigned_identity` is `false`
        """
        return pulumi.get(self, "user_assigned_identity_id")

    @user_assigned_identity_id.setter
    def user_assigned_identity_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_assigned_identity_id", value)


@pulumi.input_type
class AccountIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 identity_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: Specifies the type of Managed Service Identity that should be configured on this Media Services Account. Possible values are `SystemAssigned`, `UserAssigned`, `SystemAssigned, UserAssigned` (to enable both).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] identity_ids: Specifies a list of User Assigned Managed Identity IDs to be assigned to this Media Services Account.
        :param pulumi.Input[str] principal_id: The Principal ID associated with this Managed Service Identity.
        :param pulumi.Input[str] tenant_id: The Tenant ID associated with this Managed Service Identity.
        """
        AccountIdentityArgs._configure(
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
        Specifies the type of Managed Service Identity that should be configured on this Media Services Account. Possible values are `SystemAssigned`, `UserAssigned`, `SystemAssigned, UserAssigned` (to enable both).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="identityIds")
    def identity_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies a list of User Assigned Managed Identity IDs to be assigned to this Media Services Account.
        """
        return pulumi.get(self, "identity_ids")

    @identity_ids.setter
    def identity_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "identity_ids", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Principal ID associated with this Managed Service Identity.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Tenant ID associated with this Managed Service Identity.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


@pulumi.input_type
class AccountKeyDeliveryAccessControlArgs:
    def __init__(__self__, *,
                 default_action: Optional[pulumi.Input[str]] = None,
                 ip_allow_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] default_action: The Default Action to use when no rules match from `ip_allow_list`. Possible values are `Allow` and `Deny`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_allow_lists: One or more IP Addresses, or CIDR Blocks which should be able to access the Key Delivery.
        """
        AccountKeyDeliveryAccessControlArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            default_action=default_action,
            ip_allow_lists=ip_allow_lists,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             default_action: Optional[pulumi.Input[str]] = None,
             ip_allow_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'defaultAction' in kwargs:
            default_action = kwargs['defaultAction']
        if 'ipAllowLists' in kwargs:
            ip_allow_lists = kwargs['ipAllowLists']

        if default_action is not None:
            _setter("default_action", default_action)
        if ip_allow_lists is not None:
            _setter("ip_allow_lists", ip_allow_lists)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[pulumi.Input[str]]:
        """
        The Default Action to use when no rules match from `ip_allow_list`. Possible values are `Allow` and `Deny`.
        """
        return pulumi.get(self, "default_action")

    @default_action.setter
    def default_action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_action", value)

    @property
    @pulumi.getter(name="ipAllowLists")
    def ip_allow_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        One or more IP Addresses, or CIDR Blocks which should be able to access the Key Delivery.
        """
        return pulumi.get(self, "ip_allow_lists")

    @ip_allow_lists.setter
    def ip_allow_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ip_allow_lists", value)


@pulumi.input_type
class AccountStorageAccountArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 is_primary: Optional[pulumi.Input[bool]] = None,
                 managed_identity: Optional[pulumi.Input['AccountStorageAccountManagedIdentityArgs']] = None):
        """
        :param pulumi.Input[str] id: Specifies the ID of the Storage Account that will be associated with the Media Services instance.
        :param pulumi.Input[bool] is_primary: Specifies whether the storage account should be the primary account or not. Defaults to `false`.
               
               > **NOTE:** Whilst multiple `storage_account` blocks can be specified - one of them must be set to the primary
        :param pulumi.Input['AccountStorageAccountManagedIdentityArgs'] managed_identity: A `managed_identity` block as defined below.
        """
        AccountStorageAccountArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            id=id,
            is_primary=is_primary,
            managed_identity=managed_identity,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             id: pulumi.Input[str],
             is_primary: Optional[pulumi.Input[bool]] = None,
             managed_identity: Optional[pulumi.Input['AccountStorageAccountManagedIdentityArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'isPrimary' in kwargs:
            is_primary = kwargs['isPrimary']
        if 'managedIdentity' in kwargs:
            managed_identity = kwargs['managedIdentity']

        _setter("id", id)
        if is_primary is not None:
            _setter("is_primary", is_primary)
        if managed_identity is not None:
            _setter("managed_identity", managed_identity)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        Specifies the ID of the Storage Account that will be associated with the Media Services instance.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether the storage account should be the primary account or not. Defaults to `false`.

        > **NOTE:** Whilst multiple `storage_account` blocks can be specified - one of them must be set to the primary
        """
        return pulumi.get(self, "is_primary")

    @is_primary.setter
    def is_primary(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_primary", value)

    @property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> Optional[pulumi.Input['AccountStorageAccountManagedIdentityArgs']]:
        """
        A `managed_identity` block as defined below.
        """
        return pulumi.get(self, "managed_identity")

    @managed_identity.setter
    def managed_identity(self, value: Optional[pulumi.Input['AccountStorageAccountManagedIdentityArgs']]):
        pulumi.set(self, "managed_identity", value)


@pulumi.input_type
class AccountStorageAccountManagedIdentityArgs:
    def __init__(__self__, *,
                 use_system_assigned_identity: Optional[pulumi.Input[bool]] = None,
                 user_assigned_identity_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] use_system_assigned_identity: Whether to use System Assigned Identity. Possible Values are `true` and `false`.
        :param pulumi.Input[str] user_assigned_identity_id: The ID of the User Assigned Identity. This value can only be set when `use_system_assigned_identity` is `false`
        """
        AccountStorageAccountManagedIdentityArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            use_system_assigned_identity=use_system_assigned_identity,
            user_assigned_identity_id=user_assigned_identity_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             use_system_assigned_identity: Optional[pulumi.Input[bool]] = None,
             user_assigned_identity_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'useSystemAssignedIdentity' in kwargs:
            use_system_assigned_identity = kwargs['useSystemAssignedIdentity']
        if 'userAssignedIdentityId' in kwargs:
            user_assigned_identity_id = kwargs['userAssignedIdentityId']

        if use_system_assigned_identity is not None:
            _setter("use_system_assigned_identity", use_system_assigned_identity)
        if user_assigned_identity_id is not None:
            _setter("user_assigned_identity_id", user_assigned_identity_id)

    @property
    @pulumi.getter(name="useSystemAssignedIdentity")
    def use_system_assigned_identity(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to use System Assigned Identity. Possible Values are `true` and `false`.
        """
        return pulumi.get(self, "use_system_assigned_identity")

    @use_system_assigned_identity.setter
    def use_system_assigned_identity(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_system_assigned_identity", value)

    @property
    @pulumi.getter(name="userAssignedIdentityId")
    def user_assigned_identity_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the User Assigned Identity. This value can only be set when `use_system_assigned_identity` is `false`
        """
        return pulumi.get(self, "user_assigned_identity_id")

    @user_assigned_identity_id.setter
    def user_assigned_identity_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_assigned_identity_id", value)



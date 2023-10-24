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

__all__ = ['LocalUserArgs', 'LocalUser']

@pulumi.input_type
class LocalUserArgs:
    def __init__(__self__, *,
                 storage_account_id: pulumi.Input[str],
                 home_directory: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permission_scopes: Optional[pulumi.Input[Sequence[pulumi.Input['LocalUserPermissionScopeArgs']]]] = None,
                 ssh_authorized_keys: Optional[pulumi.Input[Sequence[pulumi.Input['LocalUserSshAuthorizedKeyArgs']]]] = None,
                 ssh_key_enabled: Optional[pulumi.Input[bool]] = None,
                 ssh_password_enabled: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a LocalUser resource.
        :param pulumi.Input[str] storage_account_id: The ID of the Storage Account that this Storage Account Local User resides in. Changing this forces a new Storage Account Local User to be created.
        :param pulumi.Input[str] home_directory: The home directory of the Storage Account Local User.
        :param pulumi.Input[str] name: The name which should be used for this Storage Account Local User. Changing this forces a new Storage Account Local User to be created.
        :param pulumi.Input[Sequence[pulumi.Input['LocalUserPermissionScopeArgs']]] permission_scopes: One or more `permission_scope` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input['LocalUserSshAuthorizedKeyArgs']]] ssh_authorized_keys: One or more `ssh_authorized_key` blocks as defined below.
        :param pulumi.Input[bool] ssh_key_enabled: Specifies whether SSH Key Authentication is enabled. Defaults to `false`.
        :param pulumi.Input[bool] ssh_password_enabled: Specifies whether SSH Password Authentication is enabled. Defaults to `false`.
        """
        LocalUserArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            storage_account_id=storage_account_id,
            home_directory=home_directory,
            name=name,
            permission_scopes=permission_scopes,
            ssh_authorized_keys=ssh_authorized_keys,
            ssh_key_enabled=ssh_key_enabled,
            ssh_password_enabled=ssh_password_enabled,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             storage_account_id: pulumi.Input[str],
             home_directory: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             permission_scopes: Optional[pulumi.Input[Sequence[pulumi.Input['LocalUserPermissionScopeArgs']]]] = None,
             ssh_authorized_keys: Optional[pulumi.Input[Sequence[pulumi.Input['LocalUserSshAuthorizedKeyArgs']]]] = None,
             ssh_key_enabled: Optional[pulumi.Input[bool]] = None,
             ssh_password_enabled: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'storageAccountId' in kwargs:
            storage_account_id = kwargs['storageAccountId']
        if 'homeDirectory' in kwargs:
            home_directory = kwargs['homeDirectory']
        if 'permissionScopes' in kwargs:
            permission_scopes = kwargs['permissionScopes']
        if 'sshAuthorizedKeys' in kwargs:
            ssh_authorized_keys = kwargs['sshAuthorizedKeys']
        if 'sshKeyEnabled' in kwargs:
            ssh_key_enabled = kwargs['sshKeyEnabled']
        if 'sshPasswordEnabled' in kwargs:
            ssh_password_enabled = kwargs['sshPasswordEnabled']

        _setter("storage_account_id", storage_account_id)
        if home_directory is not None:
            _setter("home_directory", home_directory)
        if name is not None:
            _setter("name", name)
        if permission_scopes is not None:
            _setter("permission_scopes", permission_scopes)
        if ssh_authorized_keys is not None:
            _setter("ssh_authorized_keys", ssh_authorized_keys)
        if ssh_key_enabled is not None:
            _setter("ssh_key_enabled", ssh_key_enabled)
        if ssh_password_enabled is not None:
            _setter("ssh_password_enabled", ssh_password_enabled)

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Input[str]:
        """
        The ID of the Storage Account that this Storage Account Local User resides in. Changing this forces a new Storage Account Local User to be created.
        """
        return pulumi.get(self, "storage_account_id")

    @storage_account_id.setter
    def storage_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_id", value)

    @property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> Optional[pulumi.Input[str]]:
        """
        The home directory of the Storage Account Local User.
        """
        return pulumi.get(self, "home_directory")

    @home_directory.setter
    def home_directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "home_directory", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Storage Account Local User. Changing this forces a new Storage Account Local User to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="permissionScopes")
    def permission_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LocalUserPermissionScopeArgs']]]]:
        """
        One or more `permission_scope` blocks as defined below.
        """
        return pulumi.get(self, "permission_scopes")

    @permission_scopes.setter
    def permission_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LocalUserPermissionScopeArgs']]]]):
        pulumi.set(self, "permission_scopes", value)

    @property
    @pulumi.getter(name="sshAuthorizedKeys")
    def ssh_authorized_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LocalUserSshAuthorizedKeyArgs']]]]:
        """
        One or more `ssh_authorized_key` blocks as defined below.
        """
        return pulumi.get(self, "ssh_authorized_keys")

    @ssh_authorized_keys.setter
    def ssh_authorized_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LocalUserSshAuthorizedKeyArgs']]]]):
        pulumi.set(self, "ssh_authorized_keys", value)

    @property
    @pulumi.getter(name="sshKeyEnabled")
    def ssh_key_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether SSH Key Authentication is enabled. Defaults to `false`.
        """
        return pulumi.get(self, "ssh_key_enabled")

    @ssh_key_enabled.setter
    def ssh_key_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ssh_key_enabled", value)

    @property
    @pulumi.getter(name="sshPasswordEnabled")
    def ssh_password_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether SSH Password Authentication is enabled. Defaults to `false`.
        """
        return pulumi.get(self, "ssh_password_enabled")

    @ssh_password_enabled.setter
    def ssh_password_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ssh_password_enabled", value)


@pulumi.input_type
class _LocalUserState:
    def __init__(__self__, *,
                 home_directory: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 permission_scopes: Optional[pulumi.Input[Sequence[pulumi.Input['LocalUserPermissionScopeArgs']]]] = None,
                 sid: Optional[pulumi.Input[str]] = None,
                 ssh_authorized_keys: Optional[pulumi.Input[Sequence[pulumi.Input['LocalUserSshAuthorizedKeyArgs']]]] = None,
                 ssh_key_enabled: Optional[pulumi.Input[bool]] = None,
                 ssh_password_enabled: Optional[pulumi.Input[bool]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering LocalUser resources.
        :param pulumi.Input[str] home_directory: The home directory of the Storage Account Local User.
        :param pulumi.Input[str] name: The name which should be used for this Storage Account Local User. Changing this forces a new Storage Account Local User to be created.
        :param pulumi.Input[str] password: The value of the password, which is only available when `ssh_password_enabled` is set to `true`.
        :param pulumi.Input[Sequence[pulumi.Input['LocalUserPermissionScopeArgs']]] permission_scopes: One or more `permission_scope` blocks as defined below.
        :param pulumi.Input[str] sid: The unique Security Identifier of this Storage Account Local User.
        :param pulumi.Input[Sequence[pulumi.Input['LocalUserSshAuthorizedKeyArgs']]] ssh_authorized_keys: One or more `ssh_authorized_key` blocks as defined below.
        :param pulumi.Input[bool] ssh_key_enabled: Specifies whether SSH Key Authentication is enabled. Defaults to `false`.
        :param pulumi.Input[bool] ssh_password_enabled: Specifies whether SSH Password Authentication is enabled. Defaults to `false`.
        :param pulumi.Input[str] storage_account_id: The ID of the Storage Account that this Storage Account Local User resides in. Changing this forces a new Storage Account Local User to be created.
        """
        _LocalUserState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            home_directory=home_directory,
            name=name,
            password=password,
            permission_scopes=permission_scopes,
            sid=sid,
            ssh_authorized_keys=ssh_authorized_keys,
            ssh_key_enabled=ssh_key_enabled,
            ssh_password_enabled=ssh_password_enabled,
            storage_account_id=storage_account_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             home_directory: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             password: Optional[pulumi.Input[str]] = None,
             permission_scopes: Optional[pulumi.Input[Sequence[pulumi.Input['LocalUserPermissionScopeArgs']]]] = None,
             sid: Optional[pulumi.Input[str]] = None,
             ssh_authorized_keys: Optional[pulumi.Input[Sequence[pulumi.Input['LocalUserSshAuthorizedKeyArgs']]]] = None,
             ssh_key_enabled: Optional[pulumi.Input[bool]] = None,
             ssh_password_enabled: Optional[pulumi.Input[bool]] = None,
             storage_account_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'homeDirectory' in kwargs:
            home_directory = kwargs['homeDirectory']
        if 'permissionScopes' in kwargs:
            permission_scopes = kwargs['permissionScopes']
        if 'sshAuthorizedKeys' in kwargs:
            ssh_authorized_keys = kwargs['sshAuthorizedKeys']
        if 'sshKeyEnabled' in kwargs:
            ssh_key_enabled = kwargs['sshKeyEnabled']
        if 'sshPasswordEnabled' in kwargs:
            ssh_password_enabled = kwargs['sshPasswordEnabled']
        if 'storageAccountId' in kwargs:
            storage_account_id = kwargs['storageAccountId']

        if home_directory is not None:
            _setter("home_directory", home_directory)
        if name is not None:
            _setter("name", name)
        if password is not None:
            _setter("password", password)
        if permission_scopes is not None:
            _setter("permission_scopes", permission_scopes)
        if sid is not None:
            _setter("sid", sid)
        if ssh_authorized_keys is not None:
            _setter("ssh_authorized_keys", ssh_authorized_keys)
        if ssh_key_enabled is not None:
            _setter("ssh_key_enabled", ssh_key_enabled)
        if ssh_password_enabled is not None:
            _setter("ssh_password_enabled", ssh_password_enabled)
        if storage_account_id is not None:
            _setter("storage_account_id", storage_account_id)

    @property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> Optional[pulumi.Input[str]]:
        """
        The home directory of the Storage Account Local User.
        """
        return pulumi.get(self, "home_directory")

    @home_directory.setter
    def home_directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "home_directory", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Storage Account Local User. Changing this forces a new Storage Account Local User to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The value of the password, which is only available when `ssh_password_enabled` is set to `true`.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="permissionScopes")
    def permission_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LocalUserPermissionScopeArgs']]]]:
        """
        One or more `permission_scope` blocks as defined below.
        """
        return pulumi.get(self, "permission_scopes")

    @permission_scopes.setter
    def permission_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LocalUserPermissionScopeArgs']]]]):
        pulumi.set(self, "permission_scopes", value)

    @property
    @pulumi.getter
    def sid(self) -> Optional[pulumi.Input[str]]:
        """
        The unique Security Identifier of this Storage Account Local User.
        """
        return pulumi.get(self, "sid")

    @sid.setter
    def sid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sid", value)

    @property
    @pulumi.getter(name="sshAuthorizedKeys")
    def ssh_authorized_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LocalUserSshAuthorizedKeyArgs']]]]:
        """
        One or more `ssh_authorized_key` blocks as defined below.
        """
        return pulumi.get(self, "ssh_authorized_keys")

    @ssh_authorized_keys.setter
    def ssh_authorized_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LocalUserSshAuthorizedKeyArgs']]]]):
        pulumi.set(self, "ssh_authorized_keys", value)

    @property
    @pulumi.getter(name="sshKeyEnabled")
    def ssh_key_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether SSH Key Authentication is enabled. Defaults to `false`.
        """
        return pulumi.get(self, "ssh_key_enabled")

    @ssh_key_enabled.setter
    def ssh_key_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ssh_key_enabled", value)

    @property
    @pulumi.getter(name="sshPasswordEnabled")
    def ssh_password_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether SSH Password Authentication is enabled. Defaults to `false`.
        """
        return pulumi.get(self, "ssh_password_enabled")

    @ssh_password_enabled.setter
    def ssh_password_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ssh_password_enabled", value)

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Storage Account that this Storage Account Local User resides in. Changing this forces a new Storage Account Local User to be created.
        """
        return pulumi.get(self, "storage_account_id")

    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_id", value)


class LocalUser(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 home_directory: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permission_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalUserPermissionScopeArgs']]]]] = None,
                 ssh_authorized_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalUserSshAuthorizedKeyArgs']]]]] = None,
                 ssh_key_enabled: Optional[pulumi.Input[bool]] = None,
                 ssh_password_enabled: Optional[pulumi.Input[bool]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Storage Account Local User.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="WestEurope")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_kind="StorageV2",
            account_tier="Standard",
            account_replication_type="LRS",
            is_hns_enabled=True)
        example_container = azure.storage.Container("exampleContainer", storage_account_name=example_account.name)
        example_local_user = azure.storage.LocalUser("exampleLocalUser",
            storage_account_id=example_account.id,
            ssh_key_enabled=True,
            ssh_password_enabled=True,
            home_directory="example_path",
            ssh_authorized_keys=[
                azure.storage.LocalUserSshAuthorizedKeyArgs(
                    description="key1",
                    key=local["first_public_key"],
                ),
                azure.storage.LocalUserSshAuthorizedKeyArgs(
                    description="key2",
                    key=local["second_public_key"],
                ),
            ],
            permission_scopes=[azure.storage.LocalUserPermissionScopeArgs(
                permissions=azure.storage.LocalUserPermissionScopePermissionsArgs(
                    read=True,
                    create=True,
                ),
                service="blob",
                resource_name=example_container.name,
            )])
        ```

        ## Import

        Storage Account Local Users can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:storage/localUser:LocalUser example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.Storage/storageAccounts/storageAccount1/localUsers/user1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] home_directory: The home directory of the Storage Account Local User.
        :param pulumi.Input[str] name: The name which should be used for this Storage Account Local User. Changing this forces a new Storage Account Local User to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalUserPermissionScopeArgs']]]] permission_scopes: One or more `permission_scope` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalUserSshAuthorizedKeyArgs']]]] ssh_authorized_keys: One or more `ssh_authorized_key` blocks as defined below.
        :param pulumi.Input[bool] ssh_key_enabled: Specifies whether SSH Key Authentication is enabled. Defaults to `false`.
        :param pulumi.Input[bool] ssh_password_enabled: Specifies whether SSH Password Authentication is enabled. Defaults to `false`.
        :param pulumi.Input[str] storage_account_id: The ID of the Storage Account that this Storage Account Local User resides in. Changing this forces a new Storage Account Local User to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LocalUserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Storage Account Local User.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="WestEurope")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_kind="StorageV2",
            account_tier="Standard",
            account_replication_type="LRS",
            is_hns_enabled=True)
        example_container = azure.storage.Container("exampleContainer", storage_account_name=example_account.name)
        example_local_user = azure.storage.LocalUser("exampleLocalUser",
            storage_account_id=example_account.id,
            ssh_key_enabled=True,
            ssh_password_enabled=True,
            home_directory="example_path",
            ssh_authorized_keys=[
                azure.storage.LocalUserSshAuthorizedKeyArgs(
                    description="key1",
                    key=local["first_public_key"],
                ),
                azure.storage.LocalUserSshAuthorizedKeyArgs(
                    description="key2",
                    key=local["second_public_key"],
                ),
            ],
            permission_scopes=[azure.storage.LocalUserPermissionScopeArgs(
                permissions=azure.storage.LocalUserPermissionScopePermissionsArgs(
                    read=True,
                    create=True,
                ),
                service="blob",
                resource_name=example_container.name,
            )])
        ```

        ## Import

        Storage Account Local Users can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:storage/localUser:LocalUser example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.Storage/storageAccounts/storageAccount1/localUsers/user1
        ```

        :param str resource_name: The name of the resource.
        :param LocalUserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LocalUserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            LocalUserArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 home_directory: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permission_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalUserPermissionScopeArgs']]]]] = None,
                 ssh_authorized_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalUserSshAuthorizedKeyArgs']]]]] = None,
                 ssh_key_enabled: Optional[pulumi.Input[bool]] = None,
                 ssh_password_enabled: Optional[pulumi.Input[bool]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LocalUserArgs.__new__(LocalUserArgs)

            __props__.__dict__["home_directory"] = home_directory
            __props__.__dict__["name"] = name
            __props__.__dict__["permission_scopes"] = permission_scopes
            __props__.__dict__["ssh_authorized_keys"] = ssh_authorized_keys
            __props__.__dict__["ssh_key_enabled"] = ssh_key_enabled
            __props__.__dict__["ssh_password_enabled"] = ssh_password_enabled
            if storage_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_id'")
            __props__.__dict__["storage_account_id"] = storage_account_id
            __props__.__dict__["password"] = None
            __props__.__dict__["sid"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password", "sid"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(LocalUser, __self__).__init__(
            'azure:storage/localUser:LocalUser',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            home_directory: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            permission_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalUserPermissionScopeArgs']]]]] = None,
            sid: Optional[pulumi.Input[str]] = None,
            ssh_authorized_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalUserSshAuthorizedKeyArgs']]]]] = None,
            ssh_key_enabled: Optional[pulumi.Input[bool]] = None,
            ssh_password_enabled: Optional[pulumi.Input[bool]] = None,
            storage_account_id: Optional[pulumi.Input[str]] = None) -> 'LocalUser':
        """
        Get an existing LocalUser resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] home_directory: The home directory of the Storage Account Local User.
        :param pulumi.Input[str] name: The name which should be used for this Storage Account Local User. Changing this forces a new Storage Account Local User to be created.
        :param pulumi.Input[str] password: The value of the password, which is only available when `ssh_password_enabled` is set to `true`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalUserPermissionScopeArgs']]]] permission_scopes: One or more `permission_scope` blocks as defined below.
        :param pulumi.Input[str] sid: The unique Security Identifier of this Storage Account Local User.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalUserSshAuthorizedKeyArgs']]]] ssh_authorized_keys: One or more `ssh_authorized_key` blocks as defined below.
        :param pulumi.Input[bool] ssh_key_enabled: Specifies whether SSH Key Authentication is enabled. Defaults to `false`.
        :param pulumi.Input[bool] ssh_password_enabled: Specifies whether SSH Password Authentication is enabled. Defaults to `false`.
        :param pulumi.Input[str] storage_account_id: The ID of the Storage Account that this Storage Account Local User resides in. Changing this forces a new Storage Account Local User to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LocalUserState.__new__(_LocalUserState)

        __props__.__dict__["home_directory"] = home_directory
        __props__.__dict__["name"] = name
        __props__.__dict__["password"] = password
        __props__.__dict__["permission_scopes"] = permission_scopes
        __props__.__dict__["sid"] = sid
        __props__.__dict__["ssh_authorized_keys"] = ssh_authorized_keys
        __props__.__dict__["ssh_key_enabled"] = ssh_key_enabled
        __props__.__dict__["ssh_password_enabled"] = ssh_password_enabled
        __props__.__dict__["storage_account_id"] = storage_account_id
        return LocalUser(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> pulumi.Output[Optional[str]]:
        """
        The home directory of the Storage Account Local User.
        """
        return pulumi.get(self, "home_directory")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Storage Account Local User. Changing this forces a new Storage Account Local User to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        The value of the password, which is only available when `ssh_password_enabled` is set to `true`.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="permissionScopes")
    def permission_scopes(self) -> pulumi.Output[Optional[Sequence['outputs.LocalUserPermissionScope']]]:
        """
        One or more `permission_scope` blocks as defined below.
        """
        return pulumi.get(self, "permission_scopes")

    @property
    @pulumi.getter
    def sid(self) -> pulumi.Output[str]:
        """
        The unique Security Identifier of this Storage Account Local User.
        """
        return pulumi.get(self, "sid")

    @property
    @pulumi.getter(name="sshAuthorizedKeys")
    def ssh_authorized_keys(self) -> pulumi.Output[Optional[Sequence['outputs.LocalUserSshAuthorizedKey']]]:
        """
        One or more `ssh_authorized_key` blocks as defined below.
        """
        return pulumi.get(self, "ssh_authorized_keys")

    @property
    @pulumi.getter(name="sshKeyEnabled")
    def ssh_key_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether SSH Key Authentication is enabled. Defaults to `false`.
        """
        return pulumi.get(self, "ssh_key_enabled")

    @property
    @pulumi.getter(name="sshPasswordEnabled")
    def ssh_password_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether SSH Password Authentication is enabled. Defaults to `false`.
        """
        return pulumi.get(self, "ssh_password_enabled")

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Output[str]:
        """
        The ID of the Storage Account that this Storage Account Local User resides in. Changing this forces a new Storage Account Local User to be created.
        """
        return pulumi.get(self, "storage_account_id")


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['FlexibleServerActiveDirectoryAdministratorArgs', 'FlexibleServerActiveDirectoryAdministrator']

@pulumi.input_type
class FlexibleServerActiveDirectoryAdministratorArgs:
    def __init__(__self__, *,
                 identity_id: pulumi.Input[str],
                 login: pulumi.Input[str],
                 object_id: pulumi.Input[str],
                 server_id: pulumi.Input[str],
                 tenant_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a FlexibleServerActiveDirectoryAdministrator resource.
        """
        FlexibleServerActiveDirectoryAdministratorArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            identity_id=identity_id,
            login=login,
            object_id=object_id,
            server_id=server_id,
            tenant_id=tenant_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             identity_id: pulumi.Input[str],
             login: pulumi.Input[str],
             object_id: pulumi.Input[str],
             server_id: pulumi.Input[str],
             tenant_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'identityId' in kwargs:
            identity_id = kwargs['identityId']
        if 'objectId' in kwargs:
            object_id = kwargs['objectId']
        if 'serverId' in kwargs:
            server_id = kwargs['serverId']
        if 'tenantId' in kwargs:
            tenant_id = kwargs['tenantId']

        _setter("identity_id", identity_id)
        _setter("login", login)
        _setter("object_id", object_id)
        _setter("server_id", server_id)
        _setter("tenant_id", tenant_id)

    @property
    @pulumi.getter(name="identityId")
    def identity_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "identity_id")

    @identity_id.setter
    def identity_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "identity_id", value)

    @property
    @pulumi.getter
    def login(self) -> pulumi.Input[str]:
        return pulumi.get(self, "login")

    @login.setter
    def login(self, value: pulumi.Input[str]):
        pulumi.set(self, "login", value)

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "object_id")

    @object_id.setter
    def object_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "object_id", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "tenant_id", value)


@pulumi.input_type
class _FlexibleServerActiveDirectoryAdministratorState:
    def __init__(__self__, *,
                 identity_id: Optional[pulumi.Input[str]] = None,
                 login: Optional[pulumi.Input[str]] = None,
                 object_id: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FlexibleServerActiveDirectoryAdministrator resources.
        """
        _FlexibleServerActiveDirectoryAdministratorState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            identity_id=identity_id,
            login=login,
            object_id=object_id,
            server_id=server_id,
            tenant_id=tenant_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             identity_id: Optional[pulumi.Input[str]] = None,
             login: Optional[pulumi.Input[str]] = None,
             object_id: Optional[pulumi.Input[str]] = None,
             server_id: Optional[pulumi.Input[str]] = None,
             tenant_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'identityId' in kwargs:
            identity_id = kwargs['identityId']
        if 'objectId' in kwargs:
            object_id = kwargs['objectId']
        if 'serverId' in kwargs:
            server_id = kwargs['serverId']
        if 'tenantId' in kwargs:
            tenant_id = kwargs['tenantId']

        if identity_id is not None:
            _setter("identity_id", identity_id)
        if login is not None:
            _setter("login", login)
        if object_id is not None:
            _setter("object_id", object_id)
        if server_id is not None:
            _setter("server_id", server_id)
        if tenant_id is not None:
            _setter("tenant_id", tenant_id)

    @property
    @pulumi.getter(name="identityId")
    def identity_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "identity_id")

    @identity_id.setter
    def identity_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_id", value)

    @property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "login")

    @login.setter
    def login(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "login", value)

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "object_id")

    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_id", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


warnings.warn("""azure.mysql/flexibleserveractivedirectoryadministrator.FlexibleServerActiveDirectoryAdministrator has been deprecated in favor of azure.mysql/flexibleserveractivedirectoryadministratory.FlexibleServerActiveDirectoryAdministratory""", DeprecationWarning)


class FlexibleServerActiveDirectoryAdministrator(pulumi.CustomResource):
    warnings.warn("""azure.mysql/flexibleserveractivedirectoryadministrator.FlexibleServerActiveDirectoryAdministrator has been deprecated in favor of azure.mysql/flexibleserveractivedirectoryadministratory.FlexibleServerActiveDirectoryAdministratory""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity_id: Optional[pulumi.Input[str]] = None,
                 login: Optional[pulumi.Input[str]] = None,
                 object_id: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a FlexibleServerActiveDirectoryAdministrator resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FlexibleServerActiveDirectoryAdministratorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a FlexibleServerActiveDirectoryAdministrator resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param FlexibleServerActiveDirectoryAdministratorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FlexibleServerActiveDirectoryAdministratorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            FlexibleServerActiveDirectoryAdministratorArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity_id: Optional[pulumi.Input[str]] = None,
                 login: Optional[pulumi.Input[str]] = None,
                 object_id: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""FlexibleServerActiveDirectoryAdministrator is deprecated: azure.mysql/flexibleserveractivedirectoryadministrator.FlexibleServerActiveDirectoryAdministrator has been deprecated in favor of azure.mysql/flexibleserveractivedirectoryadministratory.FlexibleServerActiveDirectoryAdministratory""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FlexibleServerActiveDirectoryAdministratorArgs.__new__(FlexibleServerActiveDirectoryAdministratorArgs)

            if identity_id is None and not opts.urn:
                raise TypeError("Missing required property 'identity_id'")
            __props__.__dict__["identity_id"] = identity_id
            if login is None and not opts.urn:
                raise TypeError("Missing required property 'login'")
            __props__.__dict__["login"] = login
            if object_id is None and not opts.urn:
                raise TypeError("Missing required property 'object_id'")
            __props__.__dict__["object_id"] = object_id
            if server_id is None and not opts.urn:
                raise TypeError("Missing required property 'server_id'")
            __props__.__dict__["server_id"] = server_id
            if tenant_id is None and not opts.urn:
                raise TypeError("Missing required property 'tenant_id'")
            __props__.__dict__["tenant_id"] = tenant_id
        super(FlexibleServerActiveDirectoryAdministrator, __self__).__init__(
            'azure:mysql/flexibleServerActiveDirectoryAdministrator:FlexibleServerActiveDirectoryAdministrator',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            identity_id: Optional[pulumi.Input[str]] = None,
            login: Optional[pulumi.Input[str]] = None,
            object_id: Optional[pulumi.Input[str]] = None,
            server_id: Optional[pulumi.Input[str]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None) -> 'FlexibleServerActiveDirectoryAdministrator':
        """
        Get an existing FlexibleServerActiveDirectoryAdministrator resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FlexibleServerActiveDirectoryAdministratorState.__new__(_FlexibleServerActiveDirectoryAdministratorState)

        __props__.__dict__["identity_id"] = identity_id
        __props__.__dict__["login"] = login
        __props__.__dict__["object_id"] = object_id
        __props__.__dict__["server_id"] = server_id
        __props__.__dict__["tenant_id"] = tenant_id
        return FlexibleServerActiveDirectoryAdministrator(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="identityId")
    def identity_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "identity_id")

    @property
    @pulumi.getter
    def login(self) -> pulumi.Output[str]:
        return pulumi.get(self, "login")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "tenant_id")


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
    'ConfigurationConfigFileArgs',
    'ConfigurationProtectedFileArgs',
    'DeploymentFrontendPrivateArgs',
    'DeploymentFrontendPublicArgs',
    'DeploymentIdentityArgs',
    'DeploymentLoggingStorageAccountArgs',
    'DeploymentNetworkInterfaceArgs',
]

@pulumi.input_type
class ConfigurationConfigFileArgs:
    def __init__(__self__, *,
                 content: pulumi.Input[str],
                 virtual_path: pulumi.Input[str]):
        """
        :param pulumi.Input[str] content: Specifies the base-64 encoded contents of this config file.
        :param pulumi.Input[str] virtual_path: Specify the path of this config file.
        """
        ConfigurationConfigFileArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            content=content,
            virtual_path=virtual_path,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             content: pulumi.Input[str],
             virtual_path: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'virtualPath' in kwargs:
            virtual_path = kwargs['virtualPath']

        _setter("content", content)
        _setter("virtual_path", virtual_path)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[str]:
        """
        Specifies the base-64 encoded contents of this config file.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="virtualPath")
    def virtual_path(self) -> pulumi.Input[str]:
        """
        Specify the path of this config file.
        """
        return pulumi.get(self, "virtual_path")

    @virtual_path.setter
    def virtual_path(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_path", value)


@pulumi.input_type
class ConfigurationProtectedFileArgs:
    def __init__(__self__, *,
                 content: pulumi.Input[str],
                 virtual_path: pulumi.Input[str]):
        """
        :param pulumi.Input[str] content: Specifies the base-64 encoded contents of this config file (Sensitive).
        :param pulumi.Input[str] virtual_path: Specify the path of this config file.
        """
        ConfigurationProtectedFileArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            content=content,
            virtual_path=virtual_path,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             content: pulumi.Input[str],
             virtual_path: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'virtualPath' in kwargs:
            virtual_path = kwargs['virtualPath']

        _setter("content", content)
        _setter("virtual_path", virtual_path)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[str]:
        """
        Specifies the base-64 encoded contents of this config file (Sensitive).
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="virtualPath")
    def virtual_path(self) -> pulumi.Input[str]:
        """
        Specify the path of this config file.
        """
        return pulumi.get(self, "virtual_path")

    @virtual_path.setter
    def virtual_path(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_path", value)


@pulumi.input_type
class DeploymentFrontendPrivateArgs:
    def __init__(__self__, *,
                 allocation_method: pulumi.Input[str],
                 ip_address: pulumi.Input[str],
                 subnet_id: pulumi.Input[str]):
        """
        :param pulumi.Input[str] allocation_method: Specify the methos of allocating the private IP. Possible values are `Static` and `Dynamic`.
        :param pulumi.Input[str] ip_address: Specify the IP Address of this private IP.
        :param pulumi.Input[str] subnet_id: Specify the SubNet Resource ID to this Nginx Deployment.
        """
        DeploymentFrontendPrivateArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            allocation_method=allocation_method,
            ip_address=ip_address,
            subnet_id=subnet_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             allocation_method: pulumi.Input[str],
             ip_address: pulumi.Input[str],
             subnet_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'allocationMethod' in kwargs:
            allocation_method = kwargs['allocationMethod']
        if 'ipAddress' in kwargs:
            ip_address = kwargs['ipAddress']
        if 'subnetId' in kwargs:
            subnet_id = kwargs['subnetId']

        _setter("allocation_method", allocation_method)
        _setter("ip_address", ip_address)
        _setter("subnet_id", subnet_id)

    @property
    @pulumi.getter(name="allocationMethod")
    def allocation_method(self) -> pulumi.Input[str]:
        """
        Specify the methos of allocating the private IP. Possible values are `Static` and `Dynamic`.
        """
        return pulumi.get(self, "allocation_method")

    @allocation_method.setter
    def allocation_method(self, value: pulumi.Input[str]):
        pulumi.set(self, "allocation_method", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Input[str]:
        """
        Specify the IP Address of this private IP.
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        Specify the SubNet Resource ID to this Nginx Deployment.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)


@pulumi.input_type
class DeploymentFrontendPublicArgs:
    def __init__(__self__, *,
                 ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_addresses: Specifies a list of Public IP Resouce ID to this Nginx Deployment.
        """
        DeploymentFrontendPublicArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            ip_addresses=ip_addresses,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'ipAddresses' in kwargs:
            ip_addresses = kwargs['ipAddresses']

        if ip_addresses is not None:
            _setter("ip_addresses", ip_addresses)

    @property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies a list of Public IP Resouce ID to this Nginx Deployment.
        """
        return pulumi.get(self, "ip_addresses")

    @ip_addresses.setter
    def ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ip_addresses", value)


@pulumi.input_type
class DeploymentIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 identity_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: Specifies the identity type of the Nginx Deployment. Possible values is `UserAssigned` where you can specify the Service Principal IDs in the `identity_ids` field.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] identity_ids: Specifies a list of user managed identity ids to be assigned. Required if `type` is `UserAssigned`.
        """
        DeploymentIdentityArgs._configure(
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
        Specifies the identity type of the Nginx Deployment. Possible values is `UserAssigned` where you can specify the Service Principal IDs in the `identity_ids` field.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="identityIds")
    def identity_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies a list of user managed identity ids to be assigned. Required if `type` is `UserAssigned`.
        """
        return pulumi.get(self, "identity_ids")

    @identity_ids.setter
    def identity_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "identity_ids", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


@pulumi.input_type
class DeploymentLoggingStorageAccountArgs:
    def __init__(__self__, *,
                 container_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] container_name: Specify the container name of Stoage Account for logging.
        :param pulumi.Input[str] name: The account name of the StorageAccount for Nginx Logging.
        """
        DeploymentLoggingStorageAccountArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            container_name=container_name,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             container_name: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'containerName' in kwargs:
            container_name = kwargs['containerName']

        if container_name is not None:
            _setter("container_name", container_name)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specify the container name of Stoage Account for logging.
        """
        return pulumi.get(self, "container_name")

    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "container_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The account name of the StorageAccount for Nginx Logging.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class DeploymentNetworkInterfaceArgs:
    def __init__(__self__, *,
                 subnet_id: pulumi.Input[str]):
        """
        :param pulumi.Input[str] subnet_id: Specify The SubNet Resource ID to this Nginx Deployment.
        """
        DeploymentNetworkInterfaceArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            subnet_id=subnet_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             subnet_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'subnetId' in kwargs:
            subnet_id = kwargs['subnetId']

        _setter("subnet_id", subnet_id)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        Specify The SubNet Resource ID to this Nginx Deployment.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)



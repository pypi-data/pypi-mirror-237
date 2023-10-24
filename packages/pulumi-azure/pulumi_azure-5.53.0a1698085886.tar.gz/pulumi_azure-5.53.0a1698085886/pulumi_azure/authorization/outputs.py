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
    'RoleDefinitionPermission',
    'GetRoleDefinitionPermissionResult',
]

@pulumi.output_type
class RoleDefinitionPermission(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dataActions":
            suggest = "data_actions"
        elif key == "notActions":
            suggest = "not_actions"
        elif key == "notDataActions":
            suggest = "not_data_actions"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RoleDefinitionPermission. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RoleDefinitionPermission.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RoleDefinitionPermission.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 actions: Optional[Sequence[str]] = None,
                 data_actions: Optional[Sequence[str]] = None,
                 not_actions: Optional[Sequence[str]] = None,
                 not_data_actions: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] actions: One or more Allowed Actions, such as `*`, `Microsoft.Resources/subscriptions/resourceGroups/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/azure/role-based-access-control/resource-provider-operations) for details.
        :param Sequence[str] data_actions: One or more Allowed Data Actions, such as `*`, `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/azure/role-based-access-control/resource-provider-operations) for details.
        :param Sequence[str] not_actions: One or more Disallowed Actions, such as `*`, `Microsoft.Resources/subscriptions/resourceGroups/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/azure/role-based-access-control/resource-provider-operations) for details.
        :param Sequence[str] not_data_actions: One or more Disallowed Data Actions, such as `*`, `Microsoft.Resources/subscriptions/resourceGroups/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/azure/role-based-access-control/resource-provider-operations) for details.
        """
        RoleDefinitionPermission._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            actions=actions,
            data_actions=data_actions,
            not_actions=not_actions,
            not_data_actions=not_data_actions,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             actions: Optional[Sequence[str]] = None,
             data_actions: Optional[Sequence[str]] = None,
             not_actions: Optional[Sequence[str]] = None,
             not_data_actions: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'dataActions' in kwargs:
            data_actions = kwargs['dataActions']
        if 'notActions' in kwargs:
            not_actions = kwargs['notActions']
        if 'notDataActions' in kwargs:
            not_data_actions = kwargs['notDataActions']

        if actions is not None:
            _setter("actions", actions)
        if data_actions is not None:
            _setter("data_actions", data_actions)
        if not_actions is not None:
            _setter("not_actions", not_actions)
        if not_data_actions is not None:
            _setter("not_data_actions", not_data_actions)

    @property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[str]]:
        """
        One or more Allowed Actions, such as `*`, `Microsoft.Resources/subscriptions/resourceGroups/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/azure/role-based-access-control/resource-provider-operations) for details.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter(name="dataActions")
    def data_actions(self) -> Optional[Sequence[str]]:
        """
        One or more Allowed Data Actions, such as `*`, `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/azure/role-based-access-control/resource-provider-operations) for details.
        """
        return pulumi.get(self, "data_actions")

    @property
    @pulumi.getter(name="notActions")
    def not_actions(self) -> Optional[Sequence[str]]:
        """
        One or more Disallowed Actions, such as `*`, `Microsoft.Resources/subscriptions/resourceGroups/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/azure/role-based-access-control/resource-provider-operations) for details.
        """
        return pulumi.get(self, "not_actions")

    @property
    @pulumi.getter(name="notDataActions")
    def not_data_actions(self) -> Optional[Sequence[str]]:
        """
        One or more Disallowed Data Actions, such as `*`, `Microsoft.Resources/subscriptions/resourceGroups/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/azure/role-based-access-control/resource-provider-operations) for details.
        """
        return pulumi.get(self, "not_data_actions")


@pulumi.output_type
class GetRoleDefinitionPermissionResult(dict):
    def __init__(__self__, *,
                 actions: Sequence[str],
                 not_actions: Sequence[str],
                 data_actions: Optional[Sequence[str]] = None,
                 not_data_actions: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] actions: a list of actions supported by this role
        :param Sequence[str] not_actions: a list of actions which are denied by this role
        """
        GetRoleDefinitionPermissionResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            actions=actions,
            not_actions=not_actions,
            data_actions=data_actions,
            not_data_actions=not_data_actions,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             actions: Sequence[str],
             not_actions: Sequence[str],
             data_actions: Optional[Sequence[str]] = None,
             not_data_actions: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'notActions' in kwargs:
            not_actions = kwargs['notActions']
        if 'dataActions' in kwargs:
            data_actions = kwargs['dataActions']
        if 'notDataActions' in kwargs:
            not_data_actions = kwargs['notDataActions']

        _setter("actions", actions)
        _setter("not_actions", not_actions)
        if data_actions is not None:
            _setter("data_actions", data_actions)
        if not_data_actions is not None:
            _setter("not_data_actions", not_data_actions)

    @property
    @pulumi.getter
    def actions(self) -> Sequence[str]:
        """
        a list of actions supported by this role
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter(name="notActions")
    def not_actions(self) -> Sequence[str]:
        """
        a list of actions which are denied by this role
        """
        return pulumi.get(self, "not_actions")

    @property
    @pulumi.getter(name="dataActions")
    def data_actions(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "data_actions")

    @property
    @pulumi.getter(name="notDataActions")
    def not_data_actions(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "not_data_actions")



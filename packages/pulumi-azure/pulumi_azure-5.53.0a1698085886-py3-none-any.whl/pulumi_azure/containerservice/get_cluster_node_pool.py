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

__all__ = [
    'GetClusterNodePoolResult',
    'AwaitableGetClusterNodePoolResult',
    'get_cluster_node_pool',
    'get_cluster_node_pool_output',
]

@pulumi.output_type
class GetClusterNodePoolResult:
    """
    A collection of values returned by getClusterNodePool.
    """
    def __init__(__self__, enable_auto_scaling=None, enable_node_public_ip=None, eviction_policy=None, id=None, kubernetes_cluster_name=None, max_count=None, max_pods=None, min_count=None, mode=None, name=None, node_count=None, node_labels=None, node_public_ip_prefix_id=None, node_taints=None, orchestrator_version=None, os_disk_size_gb=None, os_disk_type=None, os_type=None, priority=None, proximity_placement_group_id=None, resource_group_name=None, spot_max_price=None, tags=None, upgrade_settings=None, vm_size=None, vnet_subnet_id=None, zones=None):
        if enable_auto_scaling and not isinstance(enable_auto_scaling, bool):
            raise TypeError("Expected argument 'enable_auto_scaling' to be a bool")
        pulumi.set(__self__, "enable_auto_scaling", enable_auto_scaling)
        if enable_node_public_ip and not isinstance(enable_node_public_ip, bool):
            raise TypeError("Expected argument 'enable_node_public_ip' to be a bool")
        pulumi.set(__self__, "enable_node_public_ip", enable_node_public_ip)
        if eviction_policy and not isinstance(eviction_policy, str):
            raise TypeError("Expected argument 'eviction_policy' to be a str")
        pulumi.set(__self__, "eviction_policy", eviction_policy)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kubernetes_cluster_name and not isinstance(kubernetes_cluster_name, str):
            raise TypeError("Expected argument 'kubernetes_cluster_name' to be a str")
        pulumi.set(__self__, "kubernetes_cluster_name", kubernetes_cluster_name)
        if max_count and not isinstance(max_count, int):
            raise TypeError("Expected argument 'max_count' to be a int")
        pulumi.set(__self__, "max_count", max_count)
        if max_pods and not isinstance(max_pods, int):
            raise TypeError("Expected argument 'max_pods' to be a int")
        pulumi.set(__self__, "max_pods", max_pods)
        if min_count and not isinstance(min_count, int):
            raise TypeError("Expected argument 'min_count' to be a int")
        pulumi.set(__self__, "min_count", min_count)
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        pulumi.set(__self__, "mode", mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if node_count and not isinstance(node_count, int):
            raise TypeError("Expected argument 'node_count' to be a int")
        pulumi.set(__self__, "node_count", node_count)
        if node_labels and not isinstance(node_labels, dict):
            raise TypeError("Expected argument 'node_labels' to be a dict")
        pulumi.set(__self__, "node_labels", node_labels)
        if node_public_ip_prefix_id and not isinstance(node_public_ip_prefix_id, str):
            raise TypeError("Expected argument 'node_public_ip_prefix_id' to be a str")
        pulumi.set(__self__, "node_public_ip_prefix_id", node_public_ip_prefix_id)
        if node_taints and not isinstance(node_taints, list):
            raise TypeError("Expected argument 'node_taints' to be a list")
        pulumi.set(__self__, "node_taints", node_taints)
        if orchestrator_version and not isinstance(orchestrator_version, str):
            raise TypeError("Expected argument 'orchestrator_version' to be a str")
        pulumi.set(__self__, "orchestrator_version", orchestrator_version)
        if os_disk_size_gb and not isinstance(os_disk_size_gb, int):
            raise TypeError("Expected argument 'os_disk_size_gb' to be a int")
        pulumi.set(__self__, "os_disk_size_gb", os_disk_size_gb)
        if os_disk_type and not isinstance(os_disk_type, str):
            raise TypeError("Expected argument 'os_disk_type' to be a str")
        pulumi.set(__self__, "os_disk_type", os_disk_type)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if priority and not isinstance(priority, str):
            raise TypeError("Expected argument 'priority' to be a str")
        pulumi.set(__self__, "priority", priority)
        if proximity_placement_group_id and not isinstance(proximity_placement_group_id, str):
            raise TypeError("Expected argument 'proximity_placement_group_id' to be a str")
        pulumi.set(__self__, "proximity_placement_group_id", proximity_placement_group_id)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if spot_max_price and not isinstance(spot_max_price, float):
            raise TypeError("Expected argument 'spot_max_price' to be a float")
        pulumi.set(__self__, "spot_max_price", spot_max_price)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if upgrade_settings and not isinstance(upgrade_settings, list):
            raise TypeError("Expected argument 'upgrade_settings' to be a list")
        pulumi.set(__self__, "upgrade_settings", upgrade_settings)
        if vm_size and not isinstance(vm_size, str):
            raise TypeError("Expected argument 'vm_size' to be a str")
        pulumi.set(__self__, "vm_size", vm_size)
        if vnet_subnet_id and not isinstance(vnet_subnet_id, str):
            raise TypeError("Expected argument 'vnet_subnet_id' to be a str")
        pulumi.set(__self__, "vnet_subnet_id", vnet_subnet_id)
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter(name="enableAutoScaling")
    def enable_auto_scaling(self) -> bool:
        """
        Does this Node Pool have Auto-Scaling enabled?
        """
        return pulumi.get(self, "enable_auto_scaling")

    @property
    @pulumi.getter(name="enableNodePublicIp")
    def enable_node_public_ip(self) -> bool:
        """
        Do nodes in this Node Pool have a Public IP Address?
        """
        return pulumi.get(self, "enable_node_public_ip")

    @property
    @pulumi.getter(name="evictionPolicy")
    def eviction_policy(self) -> str:
        """
        The eviction policy used for Virtual Machines in the Virtual Machine Scale Set, when `priority` is set to `Spot`.
        """
        return pulumi.get(self, "eviction_policy")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kubernetesClusterName")
    def kubernetes_cluster_name(self) -> str:
        return pulumi.get(self, "kubernetes_cluster_name")

    @property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> int:
        """
        The maximum number of Nodes allowed when auto-scaling is enabled.
        """
        return pulumi.get(self, "max_count")

    @property
    @pulumi.getter(name="maxPods")
    def max_pods(self) -> int:
        """
        The maximum number of Pods allowed on each Node in this Node Pool.
        """
        return pulumi.get(self, "max_pods")

    @property
    @pulumi.getter(name="minCount")
    def min_count(self) -> int:
        """
        The minimum number of Nodes allowed when auto-scaling is enabled.
        """
        return pulumi.get(self, "min_count")

    @property
    @pulumi.getter
    def mode(self) -> str:
        """
        The Mode for this Node Pool, specifying how these Nodes should be used (for either System or User resources).
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> int:
        """
        The current number of Nodes in the Node Pool.
        """
        return pulumi.get(self, "node_count")

    @property
    @pulumi.getter(name="nodeLabels")
    def node_labels(self) -> Mapping[str, str]:
        """
        A map of Kubernetes Labels applied to each Node in this Node Pool.
        """
        return pulumi.get(self, "node_labels")

    @property
    @pulumi.getter(name="nodePublicIpPrefixId")
    def node_public_ip_prefix_id(self) -> str:
        """
        Resource ID for the Public IP Addresses Prefix for the nodes in this Agent Pool.
        """
        return pulumi.get(self, "node_public_ip_prefix_id")

    @property
    @pulumi.getter(name="nodeTaints")
    def node_taints(self) -> Sequence[str]:
        """
        A map of Kubernetes Taints applied to each Node in this Node Pool.
        """
        return pulumi.get(self, "node_taints")

    @property
    @pulumi.getter(name="orchestratorVersion")
    def orchestrator_version(self) -> str:
        """
        The version of Kubernetes configured on each Node in this Node Pool.
        """
        return pulumi.get(self, "orchestrator_version")

    @property
    @pulumi.getter(name="osDiskSizeGb")
    def os_disk_size_gb(self) -> int:
        """
        The size of the OS Disk on each Node in this Node Pool.
        """
        return pulumi.get(self, "os_disk_size_gb")

    @property
    @pulumi.getter(name="osDiskType")
    def os_disk_type(self) -> str:
        """
        The type of the OS Disk on each Node in this Node Pool.
        """
        return pulumi.get(self, "os_disk_type")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> str:
        """
        The operating system used on each Node in this Node Pool.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter
    def priority(self) -> str:
        """
        The priority of the Virtual Machines in the Virtual Machine Scale Set backing this Node Pool.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="proximityPlacementGroupId")
    def proximity_placement_group_id(self) -> str:
        """
        The ID of the Proximity Placement Group where the Virtual Machine Scale Set backing this Node Pool will be placed.
        """
        return pulumi.get(self, "proximity_placement_group_id")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="spotMaxPrice")
    def spot_max_price(self) -> float:
        """
        The maximum price being paid for Virtual Machines in this Scale Set. `-1` means the current on-demand price for a Virtual Machine.
        """
        return pulumi.get(self, "spot_max_price")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags assigned to the Kubernetes Cluster Node Pool.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(self) -> Sequence['outputs.GetClusterNodePoolUpgradeSettingResult']:
        """
        A `upgrade_settings` block as documented below.
        """
        return pulumi.get(self, "upgrade_settings")

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> str:
        """
        The size of the Virtual Machines used in the Virtual Machine Scale Set backing this Node Pool.
        """
        return pulumi.get(self, "vm_size")

    @property
    @pulumi.getter(name="vnetSubnetId")
    def vnet_subnet_id(self) -> str:
        """
        The ID of the Subnet in which this Node Pool exists.
        """
        return pulumi.get(self, "vnet_subnet_id")

    @property
    @pulumi.getter
    def zones(self) -> Sequence[str]:
        """
        A list of the Availability Zones where the Nodes in this Node Pool exist.
        """
        return pulumi.get(self, "zones")


class AwaitableGetClusterNodePoolResult(GetClusterNodePoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterNodePoolResult(
            enable_auto_scaling=self.enable_auto_scaling,
            enable_node_public_ip=self.enable_node_public_ip,
            eviction_policy=self.eviction_policy,
            id=self.id,
            kubernetes_cluster_name=self.kubernetes_cluster_name,
            max_count=self.max_count,
            max_pods=self.max_pods,
            min_count=self.min_count,
            mode=self.mode,
            name=self.name,
            node_count=self.node_count,
            node_labels=self.node_labels,
            node_public_ip_prefix_id=self.node_public_ip_prefix_id,
            node_taints=self.node_taints,
            orchestrator_version=self.orchestrator_version,
            os_disk_size_gb=self.os_disk_size_gb,
            os_disk_type=self.os_disk_type,
            os_type=self.os_type,
            priority=self.priority,
            proximity_placement_group_id=self.proximity_placement_group_id,
            resource_group_name=self.resource_group_name,
            spot_max_price=self.spot_max_price,
            tags=self.tags,
            upgrade_settings=self.upgrade_settings,
            vm_size=self.vm_size,
            vnet_subnet_id=self.vnet_subnet_id,
            zones=self.zones)


def get_cluster_node_pool(kubernetes_cluster_name: Optional[str] = None,
                          name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterNodePoolResult:
    """
    Use this data source to access information about an existing Kubernetes Cluster Node Pool.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.containerservice.get_cluster_node_pool(name="existing",
        kubernetes_cluster_name="existing-cluster",
        resource_group_name="existing-resource-group")
    pulumi.export("id", example.id)
    ```


    :param str kubernetes_cluster_name: The Name of the Kubernetes Cluster where this Node Pool is located.
    :param str name: The name of this Kubernetes Cluster Node Pool.
    :param str resource_group_name: The name of the Resource Group where the Kubernetes Cluster exists.
    """
    __args__ = dict()
    __args__['kubernetesClusterName'] = kubernetes_cluster_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:containerservice/getClusterNodePool:getClusterNodePool', __args__, opts=opts, typ=GetClusterNodePoolResult).value

    return AwaitableGetClusterNodePoolResult(
        enable_auto_scaling=pulumi.get(__ret__, 'enable_auto_scaling'),
        enable_node_public_ip=pulumi.get(__ret__, 'enable_node_public_ip'),
        eviction_policy=pulumi.get(__ret__, 'eviction_policy'),
        id=pulumi.get(__ret__, 'id'),
        kubernetes_cluster_name=pulumi.get(__ret__, 'kubernetes_cluster_name'),
        max_count=pulumi.get(__ret__, 'max_count'),
        max_pods=pulumi.get(__ret__, 'max_pods'),
        min_count=pulumi.get(__ret__, 'min_count'),
        mode=pulumi.get(__ret__, 'mode'),
        name=pulumi.get(__ret__, 'name'),
        node_count=pulumi.get(__ret__, 'node_count'),
        node_labels=pulumi.get(__ret__, 'node_labels'),
        node_public_ip_prefix_id=pulumi.get(__ret__, 'node_public_ip_prefix_id'),
        node_taints=pulumi.get(__ret__, 'node_taints'),
        orchestrator_version=pulumi.get(__ret__, 'orchestrator_version'),
        os_disk_size_gb=pulumi.get(__ret__, 'os_disk_size_gb'),
        os_disk_type=pulumi.get(__ret__, 'os_disk_type'),
        os_type=pulumi.get(__ret__, 'os_type'),
        priority=pulumi.get(__ret__, 'priority'),
        proximity_placement_group_id=pulumi.get(__ret__, 'proximity_placement_group_id'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        spot_max_price=pulumi.get(__ret__, 'spot_max_price'),
        tags=pulumi.get(__ret__, 'tags'),
        upgrade_settings=pulumi.get(__ret__, 'upgrade_settings'),
        vm_size=pulumi.get(__ret__, 'vm_size'),
        vnet_subnet_id=pulumi.get(__ret__, 'vnet_subnet_id'),
        zones=pulumi.get(__ret__, 'zones'))


@_utilities.lift_output_func(get_cluster_node_pool)
def get_cluster_node_pool_output(kubernetes_cluster_name: Optional[pulumi.Input[str]] = None,
                                 name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterNodePoolResult]:
    """
    Use this data source to access information about an existing Kubernetes Cluster Node Pool.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.containerservice.get_cluster_node_pool(name="existing",
        kubernetes_cluster_name="existing-cluster",
        resource_group_name="existing-resource-group")
    pulumi.export("id", example.id)
    ```


    :param str kubernetes_cluster_name: The Name of the Kubernetes Cluster where this Node Pool is located.
    :param str name: The name of this Kubernetes Cluster Node Pool.
    :param str resource_group_name: The name of the Resource Group where the Kubernetes Cluster exists.
    """
    ...

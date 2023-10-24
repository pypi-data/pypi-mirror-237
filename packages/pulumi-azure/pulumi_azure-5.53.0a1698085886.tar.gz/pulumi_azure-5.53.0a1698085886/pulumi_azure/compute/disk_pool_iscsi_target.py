# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DiskPoolIscsiTargetArgs', 'DiskPoolIscsiTarget']

@pulumi.input_type
class DiskPoolIscsiTargetArgs:
    def __init__(__self__, *,
                 acl_mode: pulumi.Input[str],
                 disks_pool_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 target_iqn: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DiskPoolIscsiTarget resource.
        :param pulumi.Input[str] acl_mode: Mode for Target connectivity. The only supported value is `Dynamic` for now. Changing this forces a new iSCSI Target to be created.
        :param pulumi.Input[str] disks_pool_id: The ID of the Disk Pool. Changing this forces a new iSCSI Target to be created.
        :param pulumi.Input[str] name: The name of the iSCSI Target. The name can only contain lowercase letters, numbers, periods, or hyphens, and length should between [5-223]. Changing this forces a new iSCSI Target to be created.
        :param pulumi.Input[str] target_iqn: ISCSI Target IQN (iSCSI Qualified Name); example: `iqn.2005-03.org.iscsi:server`. IQN should follow the format `iqn.yyyy-mm.<abc>.<pqr>[:xyz]`; supported characters include alphanumeric characters in lower case, hyphen, dot and colon, and the length should between `4` and `223`. Changing this forces a new iSCSI Target to be created.
        """
        DiskPoolIscsiTargetArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            acl_mode=acl_mode,
            disks_pool_id=disks_pool_id,
            name=name,
            target_iqn=target_iqn,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             acl_mode: pulumi.Input[str],
             disks_pool_id: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             target_iqn: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'aclMode' in kwargs:
            acl_mode = kwargs['aclMode']
        if 'disksPoolId' in kwargs:
            disks_pool_id = kwargs['disksPoolId']
        if 'targetIqn' in kwargs:
            target_iqn = kwargs['targetIqn']

        _setter("acl_mode", acl_mode)
        _setter("disks_pool_id", disks_pool_id)
        if name is not None:
            _setter("name", name)
        if target_iqn is not None:
            _setter("target_iqn", target_iqn)

    @property
    @pulumi.getter(name="aclMode")
    def acl_mode(self) -> pulumi.Input[str]:
        """
        Mode for Target connectivity. The only supported value is `Dynamic` for now. Changing this forces a new iSCSI Target to be created.
        """
        return pulumi.get(self, "acl_mode")

    @acl_mode.setter
    def acl_mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "acl_mode", value)

    @property
    @pulumi.getter(name="disksPoolId")
    def disks_pool_id(self) -> pulumi.Input[str]:
        """
        The ID of the Disk Pool. Changing this forces a new iSCSI Target to be created.
        """
        return pulumi.get(self, "disks_pool_id")

    @disks_pool_id.setter
    def disks_pool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "disks_pool_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the iSCSI Target. The name can only contain lowercase letters, numbers, periods, or hyphens, and length should between [5-223]. Changing this forces a new iSCSI Target to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="targetIqn")
    def target_iqn(self) -> Optional[pulumi.Input[str]]:
        """
        ISCSI Target IQN (iSCSI Qualified Name); example: `iqn.2005-03.org.iscsi:server`. IQN should follow the format `iqn.yyyy-mm.<abc>.<pqr>[:xyz]`; supported characters include alphanumeric characters in lower case, hyphen, dot and colon, and the length should between `4` and `223`. Changing this forces a new iSCSI Target to be created.
        """
        return pulumi.get(self, "target_iqn")

    @target_iqn.setter
    def target_iqn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_iqn", value)


@pulumi.input_type
class _DiskPoolIscsiTargetState:
    def __init__(__self__, *,
                 acl_mode: Optional[pulumi.Input[str]] = None,
                 disks_pool_id: Optional[pulumi.Input[str]] = None,
                 endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 target_iqn: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DiskPoolIscsiTarget resources.
        :param pulumi.Input[str] acl_mode: Mode for Target connectivity. The only supported value is `Dynamic` for now. Changing this forces a new iSCSI Target to be created.
        :param pulumi.Input[str] disks_pool_id: The ID of the Disk Pool. Changing this forces a new iSCSI Target to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] endpoints: List of private IPv4 addresses to connect to the iSCSI Target.
        :param pulumi.Input[str] name: The name of the iSCSI Target. The name can only contain lowercase letters, numbers, periods, or hyphens, and length should between [5-223]. Changing this forces a new iSCSI Target to be created.
        :param pulumi.Input[int] port: The port used by iSCSI Target portal group.
        :param pulumi.Input[str] target_iqn: ISCSI Target IQN (iSCSI Qualified Name); example: `iqn.2005-03.org.iscsi:server`. IQN should follow the format `iqn.yyyy-mm.<abc>.<pqr>[:xyz]`; supported characters include alphanumeric characters in lower case, hyphen, dot and colon, and the length should between `4` and `223`. Changing this forces a new iSCSI Target to be created.
        """
        _DiskPoolIscsiTargetState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            acl_mode=acl_mode,
            disks_pool_id=disks_pool_id,
            endpoints=endpoints,
            name=name,
            port=port,
            target_iqn=target_iqn,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             acl_mode: Optional[pulumi.Input[str]] = None,
             disks_pool_id: Optional[pulumi.Input[str]] = None,
             endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             port: Optional[pulumi.Input[int]] = None,
             target_iqn: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'aclMode' in kwargs:
            acl_mode = kwargs['aclMode']
        if 'disksPoolId' in kwargs:
            disks_pool_id = kwargs['disksPoolId']
        if 'targetIqn' in kwargs:
            target_iqn = kwargs['targetIqn']

        if acl_mode is not None:
            _setter("acl_mode", acl_mode)
        if disks_pool_id is not None:
            _setter("disks_pool_id", disks_pool_id)
        if endpoints is not None:
            _setter("endpoints", endpoints)
        if name is not None:
            _setter("name", name)
        if port is not None:
            _setter("port", port)
        if target_iqn is not None:
            _setter("target_iqn", target_iqn)

    @property
    @pulumi.getter(name="aclMode")
    def acl_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Mode for Target connectivity. The only supported value is `Dynamic` for now. Changing this forces a new iSCSI Target to be created.
        """
        return pulumi.get(self, "acl_mode")

    @acl_mode.setter
    def acl_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acl_mode", value)

    @property
    @pulumi.getter(name="disksPoolId")
    def disks_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Disk Pool. Changing this forces a new iSCSI Target to be created.
        """
        return pulumi.get(self, "disks_pool_id")

    @disks_pool_id.setter
    def disks_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disks_pool_id", value)

    @property
    @pulumi.getter
    def endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of private IPv4 addresses to connect to the iSCSI Target.
        """
        return pulumi.get(self, "endpoints")

    @endpoints.setter
    def endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "endpoints", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the iSCSI Target. The name can only contain lowercase letters, numbers, periods, or hyphens, and length should between [5-223]. Changing this forces a new iSCSI Target to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        The port used by iSCSI Target portal group.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="targetIqn")
    def target_iqn(self) -> Optional[pulumi.Input[str]]:
        """
        ISCSI Target IQN (iSCSI Qualified Name); example: `iqn.2005-03.org.iscsi:server`. IQN should follow the format `iqn.yyyy-mm.<abc>.<pqr>[:xyz]`; supported characters include alphanumeric characters in lower case, hyphen, dot and colon, and the length should between `4` and `223`. Changing this forces a new iSCSI Target to be created.
        """
        return pulumi.get(self, "target_iqn")

    @target_iqn.setter
    def target_iqn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_iqn", value)


class DiskPoolIscsiTarget(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl_mode: Optional[pulumi.Input[str]] = None,
                 disks_pool_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 target_iqn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an iSCSI Target.

        !> **Note:** Azure are officially [halting](https://learn.microsoft.com/en-us/azure/azure-vmware/attach-disk-pools-to-azure-vmware-solution-hosts?tabs=azure-cli) the preview of Azure Disk Pools, and it **will not** be made generally available. New customers will not be able to register the Microsoft.StoragePool resource provider on their subscription and deploy new Disk Pools. Existing subscriptions registered with Microsoft.StoragePool may continue to deploy and manage disk pools for the time being.

        !> **Note:** Each Disk Pool can have a maximum of 1 iSCSI Target.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_azuread as azuread

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            address_spaces=["10.0.0.0/16"])
        example_subnet = azure.network.Subnet("exampleSubnet",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.0.0.0/24"],
            delegations=[azure.network.SubnetDelegationArgs(
                name="diskspool",
                service_delegation=azure.network.SubnetDelegationServiceDelegationArgs(
                    actions=["Microsoft.Network/virtualNetworks/read"],
                    name="Microsoft.StoragePool/diskPools",
                ),
            )])
        example_disk_pool = azure.compute.DiskPool("exampleDiskPool",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            subnet_id=example_subnet.id,
            zones=["1"],
            sku_name="Basic_B1")
        example_managed_disk = azure.compute.ManagedDisk("exampleManagedDisk",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            create_option="Empty",
            storage_account_type="Premium_LRS",
            disk_size_gb=4,
            max_shares=2,
            zone="1")
        example_service_principal = azuread.get_service_principal(display_name="StoragePool Resource Provider")
        roles = [
            "Disk Pool Operator",
            "Virtual Machine Contributor",
        ]
        example_assignment = []
        for range in [{"value": i} for i in range(0, len(roles))]:
            example_assignment.append(azure.authorization.Assignment(f"exampleAssignment-{range['value']}",
                principal_id=example_service_principal.id,
                role_definition_name=roles[range["value"]],
                scope=example_managed_disk.id))
        example_disk_pool_managed_disk_attachment = azure.compute.DiskPoolManagedDiskAttachment("exampleDiskPoolManagedDiskAttachment",
            disk_pool_id=example_disk_pool.id,
            managed_disk_id=example_managed_disk.id,
            opts=pulumi.ResourceOptions(depends_on=[example_assignment]))
        example_disk_pool_iscsi_target = azure.compute.DiskPoolIscsiTarget("exampleDiskPoolIscsiTarget",
            acl_mode="Dynamic",
            disks_pool_id=example_disk_pool.id,
            target_iqn="iqn.2021-11.com.microsoft:test",
            opts=pulumi.ResourceOptions(depends_on=[example_disk_pool_managed_disk_attachment]))
        ```

        ## Import

        iSCSI Targets can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:compute/diskPoolIscsiTarget:DiskPoolIscsiTarget example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/group1/providers/Microsoft.StoragePool/diskPools/pool1/iscsiTargets/iscsiTarget1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl_mode: Mode for Target connectivity. The only supported value is `Dynamic` for now. Changing this forces a new iSCSI Target to be created.
        :param pulumi.Input[str] disks_pool_id: The ID of the Disk Pool. Changing this forces a new iSCSI Target to be created.
        :param pulumi.Input[str] name: The name of the iSCSI Target. The name can only contain lowercase letters, numbers, periods, or hyphens, and length should between [5-223]. Changing this forces a new iSCSI Target to be created.
        :param pulumi.Input[str] target_iqn: ISCSI Target IQN (iSCSI Qualified Name); example: `iqn.2005-03.org.iscsi:server`. IQN should follow the format `iqn.yyyy-mm.<abc>.<pqr>[:xyz]`; supported characters include alphanumeric characters in lower case, hyphen, dot and colon, and the length should between `4` and `223`. Changing this forces a new iSCSI Target to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DiskPoolIscsiTargetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an iSCSI Target.

        !> **Note:** Azure are officially [halting](https://learn.microsoft.com/en-us/azure/azure-vmware/attach-disk-pools-to-azure-vmware-solution-hosts?tabs=azure-cli) the preview of Azure Disk Pools, and it **will not** be made generally available. New customers will not be able to register the Microsoft.StoragePool resource provider on their subscription and deploy new Disk Pools. Existing subscriptions registered with Microsoft.StoragePool may continue to deploy and manage disk pools for the time being.

        !> **Note:** Each Disk Pool can have a maximum of 1 iSCSI Target.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_azuread as azuread

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            address_spaces=["10.0.0.0/16"])
        example_subnet = azure.network.Subnet("exampleSubnet",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.0.0.0/24"],
            delegations=[azure.network.SubnetDelegationArgs(
                name="diskspool",
                service_delegation=azure.network.SubnetDelegationServiceDelegationArgs(
                    actions=["Microsoft.Network/virtualNetworks/read"],
                    name="Microsoft.StoragePool/diskPools",
                ),
            )])
        example_disk_pool = azure.compute.DiskPool("exampleDiskPool",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            subnet_id=example_subnet.id,
            zones=["1"],
            sku_name="Basic_B1")
        example_managed_disk = azure.compute.ManagedDisk("exampleManagedDisk",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            create_option="Empty",
            storage_account_type="Premium_LRS",
            disk_size_gb=4,
            max_shares=2,
            zone="1")
        example_service_principal = azuread.get_service_principal(display_name="StoragePool Resource Provider")
        roles = [
            "Disk Pool Operator",
            "Virtual Machine Contributor",
        ]
        example_assignment = []
        for range in [{"value": i} for i in range(0, len(roles))]:
            example_assignment.append(azure.authorization.Assignment(f"exampleAssignment-{range['value']}",
                principal_id=example_service_principal.id,
                role_definition_name=roles[range["value"]],
                scope=example_managed_disk.id))
        example_disk_pool_managed_disk_attachment = azure.compute.DiskPoolManagedDiskAttachment("exampleDiskPoolManagedDiskAttachment",
            disk_pool_id=example_disk_pool.id,
            managed_disk_id=example_managed_disk.id,
            opts=pulumi.ResourceOptions(depends_on=[example_assignment]))
        example_disk_pool_iscsi_target = azure.compute.DiskPoolIscsiTarget("exampleDiskPoolIscsiTarget",
            acl_mode="Dynamic",
            disks_pool_id=example_disk_pool.id,
            target_iqn="iqn.2021-11.com.microsoft:test",
            opts=pulumi.ResourceOptions(depends_on=[example_disk_pool_managed_disk_attachment]))
        ```

        ## Import

        iSCSI Targets can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:compute/diskPoolIscsiTarget:DiskPoolIscsiTarget example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/group1/providers/Microsoft.StoragePool/diskPools/pool1/iscsiTargets/iscsiTarget1
        ```

        :param str resource_name: The name of the resource.
        :param DiskPoolIscsiTargetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DiskPoolIscsiTargetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DiskPoolIscsiTargetArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl_mode: Optional[pulumi.Input[str]] = None,
                 disks_pool_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 target_iqn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DiskPoolIscsiTargetArgs.__new__(DiskPoolIscsiTargetArgs)

            if acl_mode is None and not opts.urn:
                raise TypeError("Missing required property 'acl_mode'")
            __props__.__dict__["acl_mode"] = acl_mode
            if disks_pool_id is None and not opts.urn:
                raise TypeError("Missing required property 'disks_pool_id'")
            __props__.__dict__["disks_pool_id"] = disks_pool_id
            __props__.__dict__["name"] = name
            __props__.__dict__["target_iqn"] = target_iqn
            __props__.__dict__["endpoints"] = None
            __props__.__dict__["port"] = None
        super(DiskPoolIscsiTarget, __self__).__init__(
            'azure:compute/diskPoolIscsiTarget:DiskPoolIscsiTarget',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            acl_mode: Optional[pulumi.Input[str]] = None,
            disks_pool_id: Optional[pulumi.Input[str]] = None,
            endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            target_iqn: Optional[pulumi.Input[str]] = None) -> 'DiskPoolIscsiTarget':
        """
        Get an existing DiskPoolIscsiTarget resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl_mode: Mode for Target connectivity. The only supported value is `Dynamic` for now. Changing this forces a new iSCSI Target to be created.
        :param pulumi.Input[str] disks_pool_id: The ID of the Disk Pool. Changing this forces a new iSCSI Target to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] endpoints: List of private IPv4 addresses to connect to the iSCSI Target.
        :param pulumi.Input[str] name: The name of the iSCSI Target. The name can only contain lowercase letters, numbers, periods, or hyphens, and length should between [5-223]. Changing this forces a new iSCSI Target to be created.
        :param pulumi.Input[int] port: The port used by iSCSI Target portal group.
        :param pulumi.Input[str] target_iqn: ISCSI Target IQN (iSCSI Qualified Name); example: `iqn.2005-03.org.iscsi:server`. IQN should follow the format `iqn.yyyy-mm.<abc>.<pqr>[:xyz]`; supported characters include alphanumeric characters in lower case, hyphen, dot and colon, and the length should between `4` and `223`. Changing this forces a new iSCSI Target to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DiskPoolIscsiTargetState.__new__(_DiskPoolIscsiTargetState)

        __props__.__dict__["acl_mode"] = acl_mode
        __props__.__dict__["disks_pool_id"] = disks_pool_id
        __props__.__dict__["endpoints"] = endpoints
        __props__.__dict__["name"] = name
        __props__.__dict__["port"] = port
        __props__.__dict__["target_iqn"] = target_iqn
        return DiskPoolIscsiTarget(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aclMode")
    def acl_mode(self) -> pulumi.Output[str]:
        """
        Mode for Target connectivity. The only supported value is `Dynamic` for now. Changing this forces a new iSCSI Target to be created.
        """
        return pulumi.get(self, "acl_mode")

    @property
    @pulumi.getter(name="disksPoolId")
    def disks_pool_id(self) -> pulumi.Output[str]:
        """
        The ID of the Disk Pool. Changing this forces a new iSCSI Target to be created.
        """
        return pulumi.get(self, "disks_pool_id")

    @property
    @pulumi.getter
    def endpoints(self) -> pulumi.Output[Sequence[str]]:
        """
        List of private IPv4 addresses to connect to the iSCSI Target.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the iSCSI Target. The name can only contain lowercase letters, numbers, periods, or hyphens, and length should between [5-223]. Changing this forces a new iSCSI Target to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[int]:
        """
        The port used by iSCSI Target portal group.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="targetIqn")
    def target_iqn(self) -> pulumi.Output[Optional[str]]:
        """
        ISCSI Target IQN (iSCSI Qualified Name); example: `iqn.2005-03.org.iscsi:server`. IQN should follow the format `iqn.yyyy-mm.<abc>.<pqr>[:xyz]`; supported characters include alphanumeric characters in lower case, hyphen, dot and colon, and the length should between `4` and `223`. Changing this forces a new iSCSI Target to be created.
        """
        return pulumi.get(self, "target_iqn")


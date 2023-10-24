# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['HybridRunbookWorkerArgs', 'HybridRunbookWorker']

@pulumi.input_type
class HybridRunbookWorkerArgs:
    def __init__(__self__, *,
                 automation_account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 vm_resource_id: pulumi.Input[str],
                 worker_group_name: pulumi.Input[str],
                 worker_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a HybridRunbookWorker resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account in which the Hybrid Worker is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] vm_resource_id: The ID of the virtual machine used for this HybridWorker. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] worker_group_name: The name of the HybridWorker Group. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] worker_id: Specify the ID of this HybridWorker in UUID notation. Changing this forces a new Automation to be created.
        """
        HybridRunbookWorkerArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            automation_account_name=automation_account_name,
            resource_group_name=resource_group_name,
            vm_resource_id=vm_resource_id,
            worker_group_name=worker_group_name,
            worker_id=worker_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             automation_account_name: pulumi.Input[str],
             resource_group_name: pulumi.Input[str],
             vm_resource_id: pulumi.Input[str],
             worker_group_name: pulumi.Input[str],
             worker_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'automationAccountName' in kwargs:
            automation_account_name = kwargs['automationAccountName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'vmResourceId' in kwargs:
            vm_resource_id = kwargs['vmResourceId']
        if 'workerGroupName' in kwargs:
            worker_group_name = kwargs['workerGroupName']
        if 'workerId' in kwargs:
            worker_id = kwargs['workerId']

        _setter("automation_account_name", automation_account_name)
        _setter("resource_group_name", resource_group_name)
        _setter("vm_resource_id", vm_resource_id)
        _setter("worker_group_name", worker_group_name)
        _setter("worker_id", worker_id)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[str]:
        """
        The name of the automation account in which the Hybrid Worker is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "automation_account_name")

    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "automation_account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="vmResourceId")
    def vm_resource_id(self) -> pulumi.Input[str]:
        """
        The ID of the virtual machine used for this HybridWorker. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "vm_resource_id")

    @vm_resource_id.setter
    def vm_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vm_resource_id", value)

    @property
    @pulumi.getter(name="workerGroupName")
    def worker_group_name(self) -> pulumi.Input[str]:
        """
        The name of the HybridWorker Group. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "worker_group_name")

    @worker_group_name.setter
    def worker_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "worker_group_name", value)

    @property
    @pulumi.getter(name="workerId")
    def worker_id(self) -> pulumi.Input[str]:
        """
        Specify the ID of this HybridWorker in UUID notation. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "worker_id")

    @worker_id.setter
    def worker_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "worker_id", value)


@pulumi.input_type
class _HybridRunbookWorkerState:
    def __init__(__self__, *,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 ip: Optional[pulumi.Input[str]] = None,
                 last_seen_date_time: Optional[pulumi.Input[str]] = None,
                 registration_date_time: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 vm_resource_id: Optional[pulumi.Input[str]] = None,
                 worker_group_name: Optional[pulumi.Input[str]] = None,
                 worker_id: Optional[pulumi.Input[str]] = None,
                 worker_name: Optional[pulumi.Input[str]] = None,
                 worker_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering HybridRunbookWorker resources.
        :param pulumi.Input[str] automation_account_name: The name of the automation account in which the Hybrid Worker is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] ip: The IP address of assigned machine.
        :param pulumi.Input[str] last_seen_date_time: Last Heartbeat from the Worker.
        :param pulumi.Input[str] registration_date_time: The registration time of the worker machine.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] vm_resource_id: The ID of the virtual machine used for this HybridWorker. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] worker_group_name: The name of the HybridWorker Group. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] worker_id: Specify the ID of this HybridWorker in UUID notation. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] worker_name: The name of HybridWorker.
        :param pulumi.Input[str] worker_type: The type of the HybridWorker, the possible values are `HybridV1` and `HybridV2`.
        """
        _HybridRunbookWorkerState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            automation_account_name=automation_account_name,
            ip=ip,
            last_seen_date_time=last_seen_date_time,
            registration_date_time=registration_date_time,
            resource_group_name=resource_group_name,
            vm_resource_id=vm_resource_id,
            worker_group_name=worker_group_name,
            worker_id=worker_id,
            worker_name=worker_name,
            worker_type=worker_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             automation_account_name: Optional[pulumi.Input[str]] = None,
             ip: Optional[pulumi.Input[str]] = None,
             last_seen_date_time: Optional[pulumi.Input[str]] = None,
             registration_date_time: Optional[pulumi.Input[str]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             vm_resource_id: Optional[pulumi.Input[str]] = None,
             worker_group_name: Optional[pulumi.Input[str]] = None,
             worker_id: Optional[pulumi.Input[str]] = None,
             worker_name: Optional[pulumi.Input[str]] = None,
             worker_type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'automationAccountName' in kwargs:
            automation_account_name = kwargs['automationAccountName']
        if 'lastSeenDateTime' in kwargs:
            last_seen_date_time = kwargs['lastSeenDateTime']
        if 'registrationDateTime' in kwargs:
            registration_date_time = kwargs['registrationDateTime']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'vmResourceId' in kwargs:
            vm_resource_id = kwargs['vmResourceId']
        if 'workerGroupName' in kwargs:
            worker_group_name = kwargs['workerGroupName']
        if 'workerId' in kwargs:
            worker_id = kwargs['workerId']
        if 'workerName' in kwargs:
            worker_name = kwargs['workerName']
        if 'workerType' in kwargs:
            worker_type = kwargs['workerType']

        if automation_account_name is not None:
            _setter("automation_account_name", automation_account_name)
        if ip is not None:
            _setter("ip", ip)
        if last_seen_date_time is not None:
            _setter("last_seen_date_time", last_seen_date_time)
        if registration_date_time is not None:
            _setter("registration_date_time", registration_date_time)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if vm_resource_id is not None:
            _setter("vm_resource_id", vm_resource_id)
        if worker_group_name is not None:
            _setter("worker_group_name", worker_group_name)
        if worker_id is not None:
            _setter("worker_id", worker_id)
        if worker_name is not None:
            _setter("worker_name", worker_name)
        if worker_type is not None:
            _setter("worker_type", worker_type)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the automation account in which the Hybrid Worker is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "automation_account_name")

    @automation_account_name.setter
    def automation_account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "automation_account_name", value)

    @property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of assigned machine.
        """
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip", value)

    @property
    @pulumi.getter(name="lastSeenDateTime")
    def last_seen_date_time(self) -> Optional[pulumi.Input[str]]:
        """
        Last Heartbeat from the Worker.
        """
        return pulumi.get(self, "last_seen_date_time")

    @last_seen_date_time.setter
    def last_seen_date_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_seen_date_time", value)

    @property
    @pulumi.getter(name="registrationDateTime")
    def registration_date_time(self) -> Optional[pulumi.Input[str]]:
        """
        The registration time of the worker machine.
        """
        return pulumi.get(self, "registration_date_time")

    @registration_date_time.setter
    def registration_date_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registration_date_time", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="vmResourceId")
    def vm_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the virtual machine used for this HybridWorker. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "vm_resource_id")

    @vm_resource_id.setter
    def vm_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vm_resource_id", value)

    @property
    @pulumi.getter(name="workerGroupName")
    def worker_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the HybridWorker Group. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "worker_group_name")

    @worker_group_name.setter
    def worker_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "worker_group_name", value)

    @property
    @pulumi.getter(name="workerId")
    def worker_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specify the ID of this HybridWorker in UUID notation. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "worker_id")

    @worker_id.setter
    def worker_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "worker_id", value)

    @property
    @pulumi.getter(name="workerName")
    def worker_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of HybridWorker.
        """
        return pulumi.get(self, "worker_name")

    @worker_name.setter
    def worker_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "worker_name", value)

    @property
    @pulumi.getter(name="workerType")
    def worker_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the HybridWorker, the possible values are `HybridV1` and `HybridV2`.
        """
        return pulumi.get(self, "worker_type")

    @worker_type.setter
    def worker_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "worker_type", value)


class HybridRunbookWorker(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 vm_resource_id: Optional[pulumi.Input[str]] = None,
                 worker_group_name: Optional[pulumi.Input[str]] = None,
                 worker_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Automation Hybrid Runbook Worker.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.automation.Account("exampleAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="Basic")
        example_hybrid_runbook_worker_group = azure.automation.HybridRunbookWorkerGroup("exampleHybridRunbookWorkerGroup",
            resource_group_name=example_resource_group.name,
            automation_account_name=example_account.name)
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            resource_group_name=example_resource_group.name,
            address_spaces=["192.168.1.0/24"],
            location=example_resource_group.location)
        example_subnet = azure.network.Subnet("exampleSubnet",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["192.168.1.0/24"])
        example_network_interface = azure.network.NetworkInterface("exampleNetworkInterface",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            ip_configurations=[azure.network.NetworkInterfaceIpConfigurationArgs(
                name="vm-example",
                subnet_id=example_subnet.id,
                private_ip_address_allocation="Dynamic",
            )])
        example_linux_virtual_machine = azure.compute.LinuxVirtualMachine("exampleLinuxVirtualMachine",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            size="Standard_B1s",
            admin_username="testadmin",
            admin_password="Password1234!",
            disable_password_authentication=False,
            source_image_reference=azure.compute.LinuxVirtualMachineSourceImageReferenceArgs(
                publisher="OpenLogic",
                offer="CentOS",
                sku="7.5",
                version="latest",
            ),
            os_disk=azure.compute.LinuxVirtualMachineOsDiskArgs(
                caching="ReadWrite",
                storage_account_type="Standard_LRS",
            ),
            network_interface_ids=[example_network_interface.id])
        example_hybrid_runbook_worker = azure.automation.HybridRunbookWorker("exampleHybridRunbookWorker",
            resource_group_name=example_resource_group.name,
            automation_account_name=example_account.name,
            worker_group_name=example_hybrid_runbook_worker_group.name,
            vm_resource_id=example_linux_virtual_machine.id,
            worker_id="00000000-0000-0000-0000-000000000000")
        #unique uuid
        ```

        ## Import

        Automations can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:automation/hybridRunbookWorker:HybridRunbookWorker example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/group1/providers/Microsoft.Automation/automationAccounts/account1/hybridRunbookWorkerGroups/group1/hybridRunbookWorkers/00000000-0000-0000-0000-000000000000
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account in which the Hybrid Worker is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] vm_resource_id: The ID of the virtual machine used for this HybridWorker. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] worker_group_name: The name of the HybridWorker Group. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] worker_id: Specify the ID of this HybridWorker in UUID notation. Changing this forces a new Automation to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HybridRunbookWorkerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Automation Hybrid Runbook Worker.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.automation.Account("exampleAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="Basic")
        example_hybrid_runbook_worker_group = azure.automation.HybridRunbookWorkerGroup("exampleHybridRunbookWorkerGroup",
            resource_group_name=example_resource_group.name,
            automation_account_name=example_account.name)
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            resource_group_name=example_resource_group.name,
            address_spaces=["192.168.1.0/24"],
            location=example_resource_group.location)
        example_subnet = azure.network.Subnet("exampleSubnet",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["192.168.1.0/24"])
        example_network_interface = azure.network.NetworkInterface("exampleNetworkInterface",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            ip_configurations=[azure.network.NetworkInterfaceIpConfigurationArgs(
                name="vm-example",
                subnet_id=example_subnet.id,
                private_ip_address_allocation="Dynamic",
            )])
        example_linux_virtual_machine = azure.compute.LinuxVirtualMachine("exampleLinuxVirtualMachine",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            size="Standard_B1s",
            admin_username="testadmin",
            admin_password="Password1234!",
            disable_password_authentication=False,
            source_image_reference=azure.compute.LinuxVirtualMachineSourceImageReferenceArgs(
                publisher="OpenLogic",
                offer="CentOS",
                sku="7.5",
                version="latest",
            ),
            os_disk=azure.compute.LinuxVirtualMachineOsDiskArgs(
                caching="ReadWrite",
                storage_account_type="Standard_LRS",
            ),
            network_interface_ids=[example_network_interface.id])
        example_hybrid_runbook_worker = azure.automation.HybridRunbookWorker("exampleHybridRunbookWorker",
            resource_group_name=example_resource_group.name,
            automation_account_name=example_account.name,
            worker_group_name=example_hybrid_runbook_worker_group.name,
            vm_resource_id=example_linux_virtual_machine.id,
            worker_id="00000000-0000-0000-0000-000000000000")
        #unique uuid
        ```

        ## Import

        Automations can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:automation/hybridRunbookWorker:HybridRunbookWorker example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/group1/providers/Microsoft.Automation/automationAccounts/account1/hybridRunbookWorkerGroups/group1/hybridRunbookWorkers/00000000-0000-0000-0000-000000000000
        ```

        :param str resource_name: The name of the resource.
        :param HybridRunbookWorkerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HybridRunbookWorkerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            HybridRunbookWorkerArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 vm_resource_id: Optional[pulumi.Input[str]] = None,
                 worker_group_name: Optional[pulumi.Input[str]] = None,
                 worker_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HybridRunbookWorkerArgs.__new__(HybridRunbookWorkerArgs)

            if automation_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'automation_account_name'")
            __props__.__dict__["automation_account_name"] = automation_account_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if vm_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'vm_resource_id'")
            __props__.__dict__["vm_resource_id"] = vm_resource_id
            if worker_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'worker_group_name'")
            __props__.__dict__["worker_group_name"] = worker_group_name
            if worker_id is None and not opts.urn:
                raise TypeError("Missing required property 'worker_id'")
            __props__.__dict__["worker_id"] = worker_id
            __props__.__dict__["ip"] = None
            __props__.__dict__["last_seen_date_time"] = None
            __props__.__dict__["registration_date_time"] = None
            __props__.__dict__["worker_name"] = None
            __props__.__dict__["worker_type"] = None
        super(HybridRunbookWorker, __self__).__init__(
            'azure:automation/hybridRunbookWorker:HybridRunbookWorker',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            automation_account_name: Optional[pulumi.Input[str]] = None,
            ip: Optional[pulumi.Input[str]] = None,
            last_seen_date_time: Optional[pulumi.Input[str]] = None,
            registration_date_time: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            vm_resource_id: Optional[pulumi.Input[str]] = None,
            worker_group_name: Optional[pulumi.Input[str]] = None,
            worker_id: Optional[pulumi.Input[str]] = None,
            worker_name: Optional[pulumi.Input[str]] = None,
            worker_type: Optional[pulumi.Input[str]] = None) -> 'HybridRunbookWorker':
        """
        Get an existing HybridRunbookWorker resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account in which the Hybrid Worker is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] ip: The IP address of assigned machine.
        :param pulumi.Input[str] last_seen_date_time: Last Heartbeat from the Worker.
        :param pulumi.Input[str] registration_date_time: The registration time of the worker machine.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] vm_resource_id: The ID of the virtual machine used for this HybridWorker. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] worker_group_name: The name of the HybridWorker Group. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] worker_id: Specify the ID of this HybridWorker in UUID notation. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] worker_name: The name of HybridWorker.
        :param pulumi.Input[str] worker_type: The type of the HybridWorker, the possible values are `HybridV1` and `HybridV2`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HybridRunbookWorkerState.__new__(_HybridRunbookWorkerState)

        __props__.__dict__["automation_account_name"] = automation_account_name
        __props__.__dict__["ip"] = ip
        __props__.__dict__["last_seen_date_time"] = last_seen_date_time
        __props__.__dict__["registration_date_time"] = registration_date_time
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["vm_resource_id"] = vm_resource_id
        __props__.__dict__["worker_group_name"] = worker_group_name
        __props__.__dict__["worker_id"] = worker_id
        __props__.__dict__["worker_name"] = worker_name
        __props__.__dict__["worker_type"] = worker_type
        return HybridRunbookWorker(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Output[str]:
        """
        The name of the automation account in which the Hybrid Worker is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "automation_account_name")

    @property
    @pulumi.getter
    def ip(self) -> pulumi.Output[str]:
        """
        The IP address of assigned machine.
        """
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter(name="lastSeenDateTime")
    def last_seen_date_time(self) -> pulumi.Output[str]:
        """
        Last Heartbeat from the Worker.
        """
        return pulumi.get(self, "last_seen_date_time")

    @property
    @pulumi.getter(name="registrationDateTime")
    def registration_date_time(self) -> pulumi.Output[str]:
        """
        The registration time of the worker machine.
        """
        return pulumi.get(self, "registration_date_time")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="vmResourceId")
    def vm_resource_id(self) -> pulumi.Output[str]:
        """
        The ID of the virtual machine used for this HybridWorker. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "vm_resource_id")

    @property
    @pulumi.getter(name="workerGroupName")
    def worker_group_name(self) -> pulumi.Output[str]:
        """
        The name of the HybridWorker Group. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "worker_group_name")

    @property
    @pulumi.getter(name="workerId")
    def worker_id(self) -> pulumi.Output[str]:
        """
        Specify the ID of this HybridWorker in UUID notation. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "worker_id")

    @property
    @pulumi.getter(name="workerName")
    def worker_name(self) -> pulumi.Output[str]:
        """
        The name of HybridWorker.
        """
        return pulumi.get(self, "worker_name")

    @property
    @pulumi.getter(name="workerType")
    def worker_type(self) -> pulumi.Output[str]:
        """
        The type of the HybridWorker, the possible values are `HybridV1` and `HybridV2`.
        """
        return pulumi.get(self, "worker_type")


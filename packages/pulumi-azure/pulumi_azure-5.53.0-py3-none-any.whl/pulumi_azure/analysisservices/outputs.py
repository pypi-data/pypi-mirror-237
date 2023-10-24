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
    'ServerIpv4FirewallRule',
]

@pulumi.output_type
class ServerIpv4FirewallRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "rangeEnd":
            suggest = "range_end"
        elif key == "rangeStart":
            suggest = "range_start"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServerIpv4FirewallRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServerIpv4FirewallRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServerIpv4FirewallRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 range_end: str,
                 range_start: str):
        """
        :param str name: Specifies the name of the firewall rule.
        :param str range_end: End of the firewall rule range as IPv4 address.
        :param str range_start: Start of the firewall rule range as IPv4 address.
        """
        ServerIpv4FirewallRule._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            range_end=range_end,
            range_start=range_start,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: str,
             range_end: str,
             range_start: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'rangeEnd' in kwargs:
            range_end = kwargs['rangeEnd']
        if 'rangeStart' in kwargs:
            range_start = kwargs['rangeStart']

        _setter("name", name)
        _setter("range_end", range_end)
        _setter("range_start", range_start)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Specifies the name of the firewall rule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="rangeEnd")
    def range_end(self) -> str:
        """
        End of the firewall rule range as IPv4 address.
        """
        return pulumi.get(self, "range_end")

    @property
    @pulumi.getter(name="rangeStart")
    def range_start(self) -> str:
        """
        Start of the firewall rule range as IPv4 address.
        """
        return pulumi.get(self, "range_start")



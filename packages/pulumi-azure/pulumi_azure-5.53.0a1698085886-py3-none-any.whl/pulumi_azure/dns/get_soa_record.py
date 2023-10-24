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
    'GetSoaRecordResult',
    'AwaitableGetSoaRecordResult',
    'get_soa_record',
    'get_soa_record_output',
]

@pulumi.output_type
class GetSoaRecordResult:
    """
    A collection of values returned by getSoaRecord.
    """
    def __init__(__self__, email=None, expire_time=None, fqdn=None, host_name=None, id=None, minimum_ttl=None, name=None, refresh_time=None, resource_group_name=None, retry_time=None, serial_number=None, tags=None, ttl=None, zone_name=None):
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if expire_time and not isinstance(expire_time, int):
            raise TypeError("Expected argument 'expire_time' to be a int")
        pulumi.set(__self__, "expire_time", expire_time)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if host_name and not isinstance(host_name, str):
            raise TypeError("Expected argument 'host_name' to be a str")
        pulumi.set(__self__, "host_name", host_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if minimum_ttl and not isinstance(minimum_ttl, int):
            raise TypeError("Expected argument 'minimum_ttl' to be a int")
        pulumi.set(__self__, "minimum_ttl", minimum_ttl)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if refresh_time and not isinstance(refresh_time, int):
            raise TypeError("Expected argument 'refresh_time' to be a int")
        pulumi.set(__self__, "refresh_time", refresh_time)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if retry_time and not isinstance(retry_time, int):
            raise TypeError("Expected argument 'retry_time' to be a int")
        pulumi.set(__self__, "retry_time", retry_time)
        if serial_number and not isinstance(serial_number, int):
            raise TypeError("Expected argument 'serial_number' to be a int")
        pulumi.set(__self__, "serial_number", serial_number)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if ttl and not isinstance(ttl, int):
            raise TypeError("Expected argument 'ttl' to be a int")
        pulumi.set(__self__, "ttl", ttl)
        if zone_name and not isinstance(zone_name, str):
            raise TypeError("Expected argument 'zone_name' to be a str")
        pulumi.set(__self__, "zone_name", zone_name)

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The email contact for the SOA record.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> int:
        """
        The expire time for the SOA record.
        """
        return pulumi.get(self, "expire_time")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        """
        The FQDN of the DNS SOA Record.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> str:
        """
        The domain name of the authoritative name server for the SOA record.
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="minimumTtl")
    def minimum_ttl(self) -> int:
        """
        The minimum Time To Live for the SOA record. By convention, it is used to determine the negative caching duration.
        """
        return pulumi.get(self, "minimum_ttl")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the DNS SOA Record.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="refreshTime")
    def refresh_time(self) -> int:
        """
        The refresh time for the SOA record.
        """
        return pulumi.get(self, "refresh_time")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="retryTime")
    def retry_time(self) -> int:
        """
        The retry time for the SOA record.
        """
        return pulumi.get(self, "retry_time")

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> int:
        """
        The serial number for the SOA record.
        """
        return pulumi.get(self, "serial_number")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags assigned to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def ttl(self) -> int:
        """
        The Time To Live (TTL) of the DNS record in seconds.
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> str:
        return pulumi.get(self, "zone_name")


class AwaitableGetSoaRecordResult(GetSoaRecordResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSoaRecordResult(
            email=self.email,
            expire_time=self.expire_time,
            fqdn=self.fqdn,
            host_name=self.host_name,
            id=self.id,
            minimum_ttl=self.minimum_ttl,
            name=self.name,
            refresh_time=self.refresh_time,
            resource_group_name=self.resource_group_name,
            retry_time=self.retry_time,
            serial_number=self.serial_number,
            tags=self.tags,
            ttl=self.ttl,
            zone_name=self.zone_name)


def get_soa_record(name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   zone_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSoaRecordResult:
    """
    Use this data source to access information about an existing resource.

    :param str name: The name of the DNS SOA Record.
    :param str resource_group_name: Specifies the resource group where the DNS Zone (parent resource) exists.
    :param str zone_name: Specifies the DNS Zone where the resource exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['zoneName'] = zone_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:dns/getSoaRecord:getSoaRecord', __args__, opts=opts, typ=GetSoaRecordResult).value

    return AwaitableGetSoaRecordResult(
        email=pulumi.get(__ret__, 'email'),
        expire_time=pulumi.get(__ret__, 'expire_time'),
        fqdn=pulumi.get(__ret__, 'fqdn'),
        host_name=pulumi.get(__ret__, 'host_name'),
        id=pulumi.get(__ret__, 'id'),
        minimum_ttl=pulumi.get(__ret__, 'minimum_ttl'),
        name=pulumi.get(__ret__, 'name'),
        refresh_time=pulumi.get(__ret__, 'refresh_time'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        retry_time=pulumi.get(__ret__, 'retry_time'),
        serial_number=pulumi.get(__ret__, 'serial_number'),
        tags=pulumi.get(__ret__, 'tags'),
        ttl=pulumi.get(__ret__, 'ttl'),
        zone_name=pulumi.get(__ret__, 'zone_name'))


@_utilities.lift_output_func(get_soa_record)
def get_soa_record_output(name: Optional[pulumi.Input[Optional[str]]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          zone_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSoaRecordResult]:
    """
    Use this data source to access information about an existing resource.

    :param str name: The name of the DNS SOA Record.
    :param str resource_group_name: Specifies the resource group where the DNS Zone (parent resource) exists.
    :param str zone_name: Specifies the DNS Zone where the resource exists.
    """
    ...

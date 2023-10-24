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
    'GetSharedImageVersionResult',
    'AwaitableGetSharedImageVersionResult',
    'get_shared_image_version',
    'get_shared_image_version_output',
]

@pulumi.output_type
class GetSharedImageVersionResult:
    """
    A collection of values returned by getSharedImageVersion.
    """
    def __init__(__self__, exclude_from_latest=None, gallery_name=None, id=None, image_name=None, location=None, managed_image_id=None, name=None, os_disk_image_size_gb=None, os_disk_snapshot_id=None, resource_group_name=None, sort_versions_by_semver=None, tags=None, target_regions=None):
        if exclude_from_latest and not isinstance(exclude_from_latest, bool):
            raise TypeError("Expected argument 'exclude_from_latest' to be a bool")
        pulumi.set(__self__, "exclude_from_latest", exclude_from_latest)
        if gallery_name and not isinstance(gallery_name, str):
            raise TypeError("Expected argument 'gallery_name' to be a str")
        pulumi.set(__self__, "gallery_name", gallery_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_name and not isinstance(image_name, str):
            raise TypeError("Expected argument 'image_name' to be a str")
        pulumi.set(__self__, "image_name", image_name)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_image_id and not isinstance(managed_image_id, str):
            raise TypeError("Expected argument 'managed_image_id' to be a str")
        pulumi.set(__self__, "managed_image_id", managed_image_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if os_disk_image_size_gb and not isinstance(os_disk_image_size_gb, int):
            raise TypeError("Expected argument 'os_disk_image_size_gb' to be a int")
        pulumi.set(__self__, "os_disk_image_size_gb", os_disk_image_size_gb)
        if os_disk_snapshot_id and not isinstance(os_disk_snapshot_id, str):
            raise TypeError("Expected argument 'os_disk_snapshot_id' to be a str")
        pulumi.set(__self__, "os_disk_snapshot_id", os_disk_snapshot_id)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if sort_versions_by_semver and not isinstance(sort_versions_by_semver, bool):
            raise TypeError("Expected argument 'sort_versions_by_semver' to be a bool")
        pulumi.set(__self__, "sort_versions_by_semver", sort_versions_by_semver)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if target_regions and not isinstance(target_regions, list):
            raise TypeError("Expected argument 'target_regions' to be a list")
        pulumi.set(__self__, "target_regions", target_regions)

    @property
    @pulumi.getter(name="excludeFromLatest")
    def exclude_from_latest(self) -> bool:
        """
        Is this Image Version excluded from the `latest` filter?
        """
        return pulumi.get(self, "exclude_from_latest")

    @property
    @pulumi.getter(name="galleryName")
    def gallery_name(self) -> str:
        return pulumi.get(self, "gallery_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> str:
        return pulumi.get(self, "image_name")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The supported Azure location where the Shared Image Gallery exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedImageId")
    def managed_image_id(self) -> str:
        """
        The ID of the Managed Image which was the source of this Shared Image Version.
        """
        return pulumi.get(self, "managed_image_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The Azure Region in which this Image Version exists.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osDiskImageSizeGb")
    def os_disk_image_size_gb(self) -> int:
        """
        The size of the OS disk snapshot (in Gigabytes) which was the source of this Shared Image Version.
        """
        return pulumi.get(self, "os_disk_image_size_gb")

    @property
    @pulumi.getter(name="osDiskSnapshotId")
    def os_disk_snapshot_id(self) -> str:
        """
        The ID of the OS disk snapshot which was the source of this Shared Image Version.
        """
        return pulumi.get(self, "os_disk_snapshot_id")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="sortVersionsBySemver")
    def sort_versions_by_semver(self) -> Optional[bool]:
        return pulumi.get(self, "sort_versions_by_semver")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags assigned to the Shared Image.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetRegions")
    def target_regions(self) -> Sequence['outputs.GetSharedImageVersionTargetRegionResult']:
        """
        One or more `target_region` blocks as documented below.
        """
        return pulumi.get(self, "target_regions")


class AwaitableGetSharedImageVersionResult(GetSharedImageVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSharedImageVersionResult(
            exclude_from_latest=self.exclude_from_latest,
            gallery_name=self.gallery_name,
            id=self.id,
            image_name=self.image_name,
            location=self.location,
            managed_image_id=self.managed_image_id,
            name=self.name,
            os_disk_image_size_gb=self.os_disk_image_size_gb,
            os_disk_snapshot_id=self.os_disk_snapshot_id,
            resource_group_name=self.resource_group_name,
            sort_versions_by_semver=self.sort_versions_by_semver,
            tags=self.tags,
            target_regions=self.target_regions)


def get_shared_image_version(gallery_name: Optional[str] = None,
                             image_name: Optional[str] = None,
                             name: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             sort_versions_by_semver: Optional[bool] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSharedImageVersionResult:
    """
    Use this data source to access information about an existing Version of a Shared Image within a Shared Image Gallery.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.compute.get_shared_image_version(gallery_name="my-image-gallery",
        image_name="my-image",
        name="1.0.0",
        resource_group_name="example-resources")
    ```


    :param str gallery_name: The name of the Shared Image Gallery in which the Shared Image exists.
    :param str image_name: The name of the Shared Image in which this Version exists.
    :param str name: The name of the Image Version.
           
           > **Note:** You may specify `latest` to obtain the latest version or `recent` to obtain the most recently updated version.
           
           > **Note:** In 3.0, `latest` may return an image version with `exclude_from_latest` set to `true`. Starting from 4.0 onwards `latest` will not return image versions with `exlude_from_latest` set to `true`.
    :param str resource_group_name: The name of the Resource Group in which the Shared Image Gallery exists.
    :param bool sort_versions_by_semver: Sort available versions taking SemVer versioning scheme into account. Defaults to `false`.
    """
    __args__ = dict()
    __args__['galleryName'] = gallery_name
    __args__['imageName'] = image_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['sortVersionsBySemver'] = sort_versions_by_semver
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:compute/getSharedImageVersion:getSharedImageVersion', __args__, opts=opts, typ=GetSharedImageVersionResult).value

    return AwaitableGetSharedImageVersionResult(
        exclude_from_latest=pulumi.get(__ret__, 'exclude_from_latest'),
        gallery_name=pulumi.get(__ret__, 'gallery_name'),
        id=pulumi.get(__ret__, 'id'),
        image_name=pulumi.get(__ret__, 'image_name'),
        location=pulumi.get(__ret__, 'location'),
        managed_image_id=pulumi.get(__ret__, 'managed_image_id'),
        name=pulumi.get(__ret__, 'name'),
        os_disk_image_size_gb=pulumi.get(__ret__, 'os_disk_image_size_gb'),
        os_disk_snapshot_id=pulumi.get(__ret__, 'os_disk_snapshot_id'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        sort_versions_by_semver=pulumi.get(__ret__, 'sort_versions_by_semver'),
        tags=pulumi.get(__ret__, 'tags'),
        target_regions=pulumi.get(__ret__, 'target_regions'))


@_utilities.lift_output_func(get_shared_image_version)
def get_shared_image_version_output(gallery_name: Optional[pulumi.Input[str]] = None,
                                    image_name: Optional[pulumi.Input[str]] = None,
                                    name: Optional[pulumi.Input[str]] = None,
                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                    sort_versions_by_semver: Optional[pulumi.Input[Optional[bool]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSharedImageVersionResult]:
    """
    Use this data source to access information about an existing Version of a Shared Image within a Shared Image Gallery.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.compute.get_shared_image_version(gallery_name="my-image-gallery",
        image_name="my-image",
        name="1.0.0",
        resource_group_name="example-resources")
    ```


    :param str gallery_name: The name of the Shared Image Gallery in which the Shared Image exists.
    :param str image_name: The name of the Shared Image in which this Version exists.
    :param str name: The name of the Image Version.
           
           > **Note:** You may specify `latest` to obtain the latest version or `recent` to obtain the most recently updated version.
           
           > **Note:** In 3.0, `latest` may return an image version with `exclude_from_latest` set to `true`. Starting from 4.0 onwards `latest` will not return image versions with `exlude_from_latest` set to `true`.
    :param str resource_group_name: The name of the Resource Group in which the Shared Image Gallery exists.
    :param bool sort_versions_by_semver: Sort available versions taking SemVer versioning scheme into account. Defaults to `false`.
    """
    ...

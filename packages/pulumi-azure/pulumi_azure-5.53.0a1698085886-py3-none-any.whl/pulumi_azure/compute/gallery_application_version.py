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

__all__ = ['GalleryApplicationVersionArgs', 'GalleryApplicationVersion']

@pulumi.input_type
class GalleryApplicationVersionArgs:
    def __init__(__self__, *,
                 gallery_application_id: pulumi.Input[str],
                 manage_action: pulumi.Input['GalleryApplicationVersionManageActionArgs'],
                 source: pulumi.Input['GalleryApplicationVersionSourceArgs'],
                 target_regions: pulumi.Input[Sequence[pulumi.Input['GalleryApplicationVersionTargetRegionArgs']]],
                 enable_health_check: Optional[pulumi.Input[bool]] = None,
                 end_of_life_date: Optional[pulumi.Input[str]] = None,
                 exclude_from_latest: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a GalleryApplicationVersion resource.
        :param pulumi.Input[str] gallery_application_id: The ID of the Gallery Application. Changing this forces a new resource to be created.
        :param pulumi.Input['GalleryApplicationVersionManageActionArgs'] manage_action: A `manage_action` block as defined below.
        :param pulumi.Input['GalleryApplicationVersionSourceArgs'] source: A `source` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input['GalleryApplicationVersionTargetRegionArgs']]] target_regions: One or more `target_region` blocks as defined below.
        :param pulumi.Input[bool] enable_health_check: Should the Gallery Application reports health. Defaults to `false`.
        :param pulumi.Input[str] end_of_life_date: The end of life date in RFC3339 format of the Gallery Application Version.
        :param pulumi.Input[bool] exclude_from_latest: Should the Gallery Application Version be excluded from the `latest` filter? If set to `true` this Gallery Application Version won't be returned for the `latest` version. Defaults to `false`.
        :param pulumi.Input[str] location: The Azure Region where the Gallery Application Version exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The version name of the Gallery Application Version, such as `1.0.0`. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the Gallery Application Version.
        """
        GalleryApplicationVersionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            gallery_application_id=gallery_application_id,
            manage_action=manage_action,
            source=source,
            target_regions=target_regions,
            enable_health_check=enable_health_check,
            end_of_life_date=end_of_life_date,
            exclude_from_latest=exclude_from_latest,
            location=location,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             gallery_application_id: pulumi.Input[str],
             manage_action: pulumi.Input['GalleryApplicationVersionManageActionArgs'],
             source: pulumi.Input['GalleryApplicationVersionSourceArgs'],
             target_regions: pulumi.Input[Sequence[pulumi.Input['GalleryApplicationVersionTargetRegionArgs']]],
             enable_health_check: Optional[pulumi.Input[bool]] = None,
             end_of_life_date: Optional[pulumi.Input[str]] = None,
             exclude_from_latest: Optional[pulumi.Input[bool]] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'galleryApplicationId' in kwargs:
            gallery_application_id = kwargs['galleryApplicationId']
        if 'manageAction' in kwargs:
            manage_action = kwargs['manageAction']
        if 'targetRegions' in kwargs:
            target_regions = kwargs['targetRegions']
        if 'enableHealthCheck' in kwargs:
            enable_health_check = kwargs['enableHealthCheck']
        if 'endOfLifeDate' in kwargs:
            end_of_life_date = kwargs['endOfLifeDate']
        if 'excludeFromLatest' in kwargs:
            exclude_from_latest = kwargs['excludeFromLatest']

        _setter("gallery_application_id", gallery_application_id)
        _setter("manage_action", manage_action)
        _setter("source", source)
        _setter("target_regions", target_regions)
        if enable_health_check is not None:
            _setter("enable_health_check", enable_health_check)
        if end_of_life_date is not None:
            _setter("end_of_life_date", end_of_life_date)
        if exclude_from_latest is not None:
            _setter("exclude_from_latest", exclude_from_latest)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="galleryApplicationId")
    def gallery_application_id(self) -> pulumi.Input[str]:
        """
        The ID of the Gallery Application. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "gallery_application_id")

    @gallery_application_id.setter
    def gallery_application_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "gallery_application_id", value)

    @property
    @pulumi.getter(name="manageAction")
    def manage_action(self) -> pulumi.Input['GalleryApplicationVersionManageActionArgs']:
        """
        A `manage_action` block as defined below.
        """
        return pulumi.get(self, "manage_action")

    @manage_action.setter
    def manage_action(self, value: pulumi.Input['GalleryApplicationVersionManageActionArgs']):
        pulumi.set(self, "manage_action", value)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input['GalleryApplicationVersionSourceArgs']:
        """
        A `source` block as defined below.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input['GalleryApplicationVersionSourceArgs']):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter(name="targetRegions")
    def target_regions(self) -> pulumi.Input[Sequence[pulumi.Input['GalleryApplicationVersionTargetRegionArgs']]]:
        """
        One or more `target_region` blocks as defined below.
        """
        return pulumi.get(self, "target_regions")

    @target_regions.setter
    def target_regions(self, value: pulumi.Input[Sequence[pulumi.Input['GalleryApplicationVersionTargetRegionArgs']]]):
        pulumi.set(self, "target_regions", value)

    @property
    @pulumi.getter(name="enableHealthCheck")
    def enable_health_check(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the Gallery Application reports health. Defaults to `false`.
        """
        return pulumi.get(self, "enable_health_check")

    @enable_health_check.setter
    def enable_health_check(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_health_check", value)

    @property
    @pulumi.getter(name="endOfLifeDate")
    def end_of_life_date(self) -> Optional[pulumi.Input[str]]:
        """
        The end of life date in RFC3339 format of the Gallery Application Version.
        """
        return pulumi.get(self, "end_of_life_date")

    @end_of_life_date.setter
    def end_of_life_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_of_life_date", value)

    @property
    @pulumi.getter(name="excludeFromLatest")
    def exclude_from_latest(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the Gallery Application Version be excluded from the `latest` filter? If set to `true` this Gallery Application Version won't be returned for the `latest` version. Defaults to `false`.
        """
        return pulumi.get(self, "exclude_from_latest")

    @exclude_from_latest.setter
    def exclude_from_latest(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "exclude_from_latest", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region where the Gallery Application Version exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The version name of the Gallery Application Version, such as `1.0.0`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the Gallery Application Version.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _GalleryApplicationVersionState:
    def __init__(__self__, *,
                 enable_health_check: Optional[pulumi.Input[bool]] = None,
                 end_of_life_date: Optional[pulumi.Input[str]] = None,
                 exclude_from_latest: Optional[pulumi.Input[bool]] = None,
                 gallery_application_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 manage_action: Optional[pulumi.Input['GalleryApplicationVersionManageActionArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input['GalleryApplicationVersionSourceArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_regions: Optional[pulumi.Input[Sequence[pulumi.Input['GalleryApplicationVersionTargetRegionArgs']]]] = None):
        """
        Input properties used for looking up and filtering GalleryApplicationVersion resources.
        :param pulumi.Input[bool] enable_health_check: Should the Gallery Application reports health. Defaults to `false`.
        :param pulumi.Input[str] end_of_life_date: The end of life date in RFC3339 format of the Gallery Application Version.
        :param pulumi.Input[bool] exclude_from_latest: Should the Gallery Application Version be excluded from the `latest` filter? If set to `true` this Gallery Application Version won't be returned for the `latest` version. Defaults to `false`.
        :param pulumi.Input[str] gallery_application_id: The ID of the Gallery Application. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: The Azure Region where the Gallery Application Version exists. Changing this forces a new resource to be created.
        :param pulumi.Input['GalleryApplicationVersionManageActionArgs'] manage_action: A `manage_action` block as defined below.
        :param pulumi.Input[str] name: The version name of the Gallery Application Version, such as `1.0.0`. Changing this forces a new resource to be created.
        :param pulumi.Input['GalleryApplicationVersionSourceArgs'] source: A `source` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the Gallery Application Version.
        :param pulumi.Input[Sequence[pulumi.Input['GalleryApplicationVersionTargetRegionArgs']]] target_regions: One or more `target_region` blocks as defined below.
        """
        _GalleryApplicationVersionState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            enable_health_check=enable_health_check,
            end_of_life_date=end_of_life_date,
            exclude_from_latest=exclude_from_latest,
            gallery_application_id=gallery_application_id,
            location=location,
            manage_action=manage_action,
            name=name,
            source=source,
            tags=tags,
            target_regions=target_regions,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             enable_health_check: Optional[pulumi.Input[bool]] = None,
             end_of_life_date: Optional[pulumi.Input[str]] = None,
             exclude_from_latest: Optional[pulumi.Input[bool]] = None,
             gallery_application_id: Optional[pulumi.Input[str]] = None,
             location: Optional[pulumi.Input[str]] = None,
             manage_action: Optional[pulumi.Input['GalleryApplicationVersionManageActionArgs']] = None,
             name: Optional[pulumi.Input[str]] = None,
             source: Optional[pulumi.Input['GalleryApplicationVersionSourceArgs']] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             target_regions: Optional[pulumi.Input[Sequence[pulumi.Input['GalleryApplicationVersionTargetRegionArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'enableHealthCheck' in kwargs:
            enable_health_check = kwargs['enableHealthCheck']
        if 'endOfLifeDate' in kwargs:
            end_of_life_date = kwargs['endOfLifeDate']
        if 'excludeFromLatest' in kwargs:
            exclude_from_latest = kwargs['excludeFromLatest']
        if 'galleryApplicationId' in kwargs:
            gallery_application_id = kwargs['galleryApplicationId']
        if 'manageAction' in kwargs:
            manage_action = kwargs['manageAction']
        if 'targetRegions' in kwargs:
            target_regions = kwargs['targetRegions']

        if enable_health_check is not None:
            _setter("enable_health_check", enable_health_check)
        if end_of_life_date is not None:
            _setter("end_of_life_date", end_of_life_date)
        if exclude_from_latest is not None:
            _setter("exclude_from_latest", exclude_from_latest)
        if gallery_application_id is not None:
            _setter("gallery_application_id", gallery_application_id)
        if location is not None:
            _setter("location", location)
        if manage_action is not None:
            _setter("manage_action", manage_action)
        if name is not None:
            _setter("name", name)
        if source is not None:
            _setter("source", source)
        if tags is not None:
            _setter("tags", tags)
        if target_regions is not None:
            _setter("target_regions", target_regions)

    @property
    @pulumi.getter(name="enableHealthCheck")
    def enable_health_check(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the Gallery Application reports health. Defaults to `false`.
        """
        return pulumi.get(self, "enable_health_check")

    @enable_health_check.setter
    def enable_health_check(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_health_check", value)

    @property
    @pulumi.getter(name="endOfLifeDate")
    def end_of_life_date(self) -> Optional[pulumi.Input[str]]:
        """
        The end of life date in RFC3339 format of the Gallery Application Version.
        """
        return pulumi.get(self, "end_of_life_date")

    @end_of_life_date.setter
    def end_of_life_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_of_life_date", value)

    @property
    @pulumi.getter(name="excludeFromLatest")
    def exclude_from_latest(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the Gallery Application Version be excluded from the `latest` filter? If set to `true` this Gallery Application Version won't be returned for the `latest` version. Defaults to `false`.
        """
        return pulumi.get(self, "exclude_from_latest")

    @exclude_from_latest.setter
    def exclude_from_latest(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "exclude_from_latest", value)

    @property
    @pulumi.getter(name="galleryApplicationId")
    def gallery_application_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Gallery Application. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "gallery_application_id")

    @gallery_application_id.setter
    def gallery_application_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gallery_application_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region where the Gallery Application Version exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="manageAction")
    def manage_action(self) -> Optional[pulumi.Input['GalleryApplicationVersionManageActionArgs']]:
        """
        A `manage_action` block as defined below.
        """
        return pulumi.get(self, "manage_action")

    @manage_action.setter
    def manage_action(self, value: Optional[pulumi.Input['GalleryApplicationVersionManageActionArgs']]):
        pulumi.set(self, "manage_action", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The version name of the Gallery Application Version, such as `1.0.0`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input['GalleryApplicationVersionSourceArgs']]:
        """
        A `source` block as defined below.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input['GalleryApplicationVersionSourceArgs']]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the Gallery Application Version.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="targetRegions")
    def target_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GalleryApplicationVersionTargetRegionArgs']]]]:
        """
        One or more `target_region` blocks as defined below.
        """
        return pulumi.get(self, "target_regions")

    @target_regions.setter
    def target_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GalleryApplicationVersionTargetRegionArgs']]]]):
        pulumi.set(self, "target_regions", value)


class GalleryApplicationVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable_health_check: Optional[pulumi.Input[bool]] = None,
                 end_of_life_date: Optional[pulumi.Input[str]] = None,
                 exclude_from_latest: Optional[pulumi.Input[bool]] = None,
                 gallery_application_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 manage_action: Optional[pulumi.Input[pulumi.InputType['GalleryApplicationVersionManageActionArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['GalleryApplicationVersionSourceArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_regions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GalleryApplicationVersionTargetRegionArgs']]]]] = None,
                 __props__=None):
        """
        Manages a Gallery Application Version.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_shared_image_gallery = azure.compute.SharedImageGallery("exampleSharedImageGallery",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_gallery_application = azure.compute.GalleryApplication("exampleGalleryApplication",
            gallery_id=example_shared_image_gallery.id,
            location=example_resource_group.location,
            supported_os_type="Linux")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_container = azure.storage.Container("exampleContainer",
            storage_account_name=example_account.name,
            container_access_type="blob")
        example_blob = azure.storage.Blob("exampleBlob",
            storage_account_name=example_account.name,
            storage_container_name=example_container.name,
            type="Block",
            source_content="[scripts file content]")
        example_gallery_application_version = azure.compute.GalleryApplicationVersion("exampleGalleryApplicationVersion",
            gallery_application_id=example_gallery_application.id,
            location=example_gallery_application.location,
            manage_action=azure.compute.GalleryApplicationVersionManageActionArgs(
                install="[install command]",
                remove="[remove command]",
            ),
            source=azure.compute.GalleryApplicationVersionSourceArgs(
                media_link=example_blob.id,
            ),
            target_regions=[azure.compute.GalleryApplicationVersionTargetRegionArgs(
                name=example_gallery_application.location,
                regional_replica_count=1,
            )])
        ```

        ## Import

        Gallery Application Versions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:compute/galleryApplicationVersion:GalleryApplicationVersion example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Compute/galleries/gallery1/applications/galleryApplication1/versions/galleryApplicationVersion1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable_health_check: Should the Gallery Application reports health. Defaults to `false`.
        :param pulumi.Input[str] end_of_life_date: The end of life date in RFC3339 format of the Gallery Application Version.
        :param pulumi.Input[bool] exclude_from_latest: Should the Gallery Application Version be excluded from the `latest` filter? If set to `true` this Gallery Application Version won't be returned for the `latest` version. Defaults to `false`.
        :param pulumi.Input[str] gallery_application_id: The ID of the Gallery Application. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: The Azure Region where the Gallery Application Version exists. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['GalleryApplicationVersionManageActionArgs']] manage_action: A `manage_action` block as defined below.
        :param pulumi.Input[str] name: The version name of the Gallery Application Version, such as `1.0.0`. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['GalleryApplicationVersionSourceArgs']] source: A `source` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the Gallery Application Version.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GalleryApplicationVersionTargetRegionArgs']]]] target_regions: One or more `target_region` blocks as defined below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GalleryApplicationVersionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Gallery Application Version.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_shared_image_gallery = azure.compute.SharedImageGallery("exampleSharedImageGallery",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_gallery_application = azure.compute.GalleryApplication("exampleGalleryApplication",
            gallery_id=example_shared_image_gallery.id,
            location=example_resource_group.location,
            supported_os_type="Linux")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_container = azure.storage.Container("exampleContainer",
            storage_account_name=example_account.name,
            container_access_type="blob")
        example_blob = azure.storage.Blob("exampleBlob",
            storage_account_name=example_account.name,
            storage_container_name=example_container.name,
            type="Block",
            source_content="[scripts file content]")
        example_gallery_application_version = azure.compute.GalleryApplicationVersion("exampleGalleryApplicationVersion",
            gallery_application_id=example_gallery_application.id,
            location=example_gallery_application.location,
            manage_action=azure.compute.GalleryApplicationVersionManageActionArgs(
                install="[install command]",
                remove="[remove command]",
            ),
            source=azure.compute.GalleryApplicationVersionSourceArgs(
                media_link=example_blob.id,
            ),
            target_regions=[azure.compute.GalleryApplicationVersionTargetRegionArgs(
                name=example_gallery_application.location,
                regional_replica_count=1,
            )])
        ```

        ## Import

        Gallery Application Versions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:compute/galleryApplicationVersion:GalleryApplicationVersion example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Compute/galleries/gallery1/applications/galleryApplication1/versions/galleryApplicationVersion1
        ```

        :param str resource_name: The name of the resource.
        :param GalleryApplicationVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GalleryApplicationVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            GalleryApplicationVersionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable_health_check: Optional[pulumi.Input[bool]] = None,
                 end_of_life_date: Optional[pulumi.Input[str]] = None,
                 exclude_from_latest: Optional[pulumi.Input[bool]] = None,
                 gallery_application_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 manage_action: Optional[pulumi.Input[pulumi.InputType['GalleryApplicationVersionManageActionArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['GalleryApplicationVersionSourceArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_regions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GalleryApplicationVersionTargetRegionArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GalleryApplicationVersionArgs.__new__(GalleryApplicationVersionArgs)

            __props__.__dict__["enable_health_check"] = enable_health_check
            __props__.__dict__["end_of_life_date"] = end_of_life_date
            __props__.__dict__["exclude_from_latest"] = exclude_from_latest
            if gallery_application_id is None and not opts.urn:
                raise TypeError("Missing required property 'gallery_application_id'")
            __props__.__dict__["gallery_application_id"] = gallery_application_id
            __props__.__dict__["location"] = location
            if manage_action is not None and not isinstance(manage_action, GalleryApplicationVersionManageActionArgs):
                manage_action = manage_action or {}
                def _setter(key, value):
                    manage_action[key] = value
                GalleryApplicationVersionManageActionArgs._configure(_setter, **manage_action)
            if manage_action is None and not opts.urn:
                raise TypeError("Missing required property 'manage_action'")
            __props__.__dict__["manage_action"] = manage_action
            __props__.__dict__["name"] = name
            if source is not None and not isinstance(source, GalleryApplicationVersionSourceArgs):
                source = source or {}
                def _setter(key, value):
                    source[key] = value
                GalleryApplicationVersionSourceArgs._configure(_setter, **source)
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__.__dict__["source"] = source
            __props__.__dict__["tags"] = tags
            if target_regions is None and not opts.urn:
                raise TypeError("Missing required property 'target_regions'")
            __props__.__dict__["target_regions"] = target_regions
        super(GalleryApplicationVersion, __self__).__init__(
            'azure:compute/galleryApplicationVersion:GalleryApplicationVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enable_health_check: Optional[pulumi.Input[bool]] = None,
            end_of_life_date: Optional[pulumi.Input[str]] = None,
            exclude_from_latest: Optional[pulumi.Input[bool]] = None,
            gallery_application_id: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            manage_action: Optional[pulumi.Input[pulumi.InputType['GalleryApplicationVersionManageActionArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            source: Optional[pulumi.Input[pulumi.InputType['GalleryApplicationVersionSourceArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            target_regions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GalleryApplicationVersionTargetRegionArgs']]]]] = None) -> 'GalleryApplicationVersion':
        """
        Get an existing GalleryApplicationVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable_health_check: Should the Gallery Application reports health. Defaults to `false`.
        :param pulumi.Input[str] end_of_life_date: The end of life date in RFC3339 format of the Gallery Application Version.
        :param pulumi.Input[bool] exclude_from_latest: Should the Gallery Application Version be excluded from the `latest` filter? If set to `true` this Gallery Application Version won't be returned for the `latest` version. Defaults to `false`.
        :param pulumi.Input[str] gallery_application_id: The ID of the Gallery Application. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: The Azure Region where the Gallery Application Version exists. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['GalleryApplicationVersionManageActionArgs']] manage_action: A `manage_action` block as defined below.
        :param pulumi.Input[str] name: The version name of the Gallery Application Version, such as `1.0.0`. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['GalleryApplicationVersionSourceArgs']] source: A `source` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the Gallery Application Version.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GalleryApplicationVersionTargetRegionArgs']]]] target_regions: One or more `target_region` blocks as defined below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GalleryApplicationVersionState.__new__(_GalleryApplicationVersionState)

        __props__.__dict__["enable_health_check"] = enable_health_check
        __props__.__dict__["end_of_life_date"] = end_of_life_date
        __props__.__dict__["exclude_from_latest"] = exclude_from_latest
        __props__.__dict__["gallery_application_id"] = gallery_application_id
        __props__.__dict__["location"] = location
        __props__.__dict__["manage_action"] = manage_action
        __props__.__dict__["name"] = name
        __props__.__dict__["source"] = source
        __props__.__dict__["tags"] = tags
        __props__.__dict__["target_regions"] = target_regions
        return GalleryApplicationVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="enableHealthCheck")
    def enable_health_check(self) -> pulumi.Output[Optional[bool]]:
        """
        Should the Gallery Application reports health. Defaults to `false`.
        """
        return pulumi.get(self, "enable_health_check")

    @property
    @pulumi.getter(name="endOfLifeDate")
    def end_of_life_date(self) -> pulumi.Output[Optional[str]]:
        """
        The end of life date in RFC3339 format of the Gallery Application Version.
        """
        return pulumi.get(self, "end_of_life_date")

    @property
    @pulumi.getter(name="excludeFromLatest")
    def exclude_from_latest(self) -> pulumi.Output[Optional[bool]]:
        """
        Should the Gallery Application Version be excluded from the `latest` filter? If set to `true` this Gallery Application Version won't be returned for the `latest` version. Defaults to `false`.
        """
        return pulumi.get(self, "exclude_from_latest")

    @property
    @pulumi.getter(name="galleryApplicationId")
    def gallery_application_id(self) -> pulumi.Output[str]:
        """
        The ID of the Gallery Application. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "gallery_application_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Azure Region where the Gallery Application Version exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="manageAction")
    def manage_action(self) -> pulumi.Output['outputs.GalleryApplicationVersionManageAction']:
        """
        A `manage_action` block as defined below.
        """
        return pulumi.get(self, "manage_action")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The version name of the Gallery Application Version, such as `1.0.0`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output['outputs.GalleryApplicationVersionSource']:
        """
        A `source` block as defined below.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the Gallery Application Version.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetRegions")
    def target_regions(self) -> pulumi.Output[Sequence['outputs.GalleryApplicationVersionTargetRegion']]:
        """
        One or more `target_region` blocks as defined below.
        """
        return pulumi.get(self, "target_regions")


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DashboardArgs', 'Dashboard']

@pulumi.input_type
class DashboardArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 dashboard_properties: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Dashboard resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the dashboard. Changing this forces a new resource to be created.
        :param pulumi.Input[str] dashboard_properties: JSON data representing dashboard body. See above for details on how to obtain this from the Portal.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Shared Dashboard. Changing this forces a new resource to be created.
               
               > **Note**: You can specify a tag with the key `hidden-title` to set a more user-friendly title for this Dashboard.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        DashboardArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            resource_group_name=resource_group_name,
            dashboard_properties=dashboard_properties,
            location=location,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             resource_group_name: pulumi.Input[str],
             dashboard_properties: Optional[pulumi.Input[str]] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'dashboardProperties' in kwargs:
            dashboard_properties = kwargs['dashboardProperties']

        _setter("resource_group_name", resource_group_name)
        if dashboard_properties is not None:
            _setter("dashboard_properties", dashboard_properties)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group in which to create the dashboard. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="dashboardProperties")
    def dashboard_properties(self) -> Optional[pulumi.Input[str]]:
        """
        JSON data representing dashboard body. See above for details on how to obtain this from the Portal.
        """
        return pulumi.get(self, "dashboard_properties")

    @dashboard_properties.setter
    def dashboard_properties(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dashboard_properties", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Shared Dashboard. Changing this forces a new resource to be created.

        > **Note**: You can specify a tag with the key `hidden-title` to set a more user-friendly title for this Dashboard.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _DashboardState:
    def __init__(__self__, *,
                 dashboard_properties: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Dashboard resources.
        :param pulumi.Input[str] dashboard_properties: JSON data representing dashboard body. See above for details on how to obtain this from the Portal.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Shared Dashboard. Changing this forces a new resource to be created.
               
               > **Note**: You can specify a tag with the key `hidden-title` to set a more user-friendly title for this Dashboard.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the dashboard. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        _DashboardState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            dashboard_properties=dashboard_properties,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             dashboard_properties: Optional[pulumi.Input[str]] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'dashboardProperties' in kwargs:
            dashboard_properties = kwargs['dashboardProperties']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']

        if dashboard_properties is not None:
            _setter("dashboard_properties", dashboard_properties)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="dashboardProperties")
    def dashboard_properties(self) -> Optional[pulumi.Input[str]]:
        """
        JSON data representing dashboard body. See above for details on how to obtain this from the Portal.
        """
        return pulumi.get(self, "dashboard_properties")

    @dashboard_properties.setter
    def dashboard_properties(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dashboard_properties", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Shared Dashboard. Changing this forces a new resource to be created.

        > **Note**: You can specify a tag with the key `hidden-title` to set a more user-friendly title for this Dashboard.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group in which to create the dashboard. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Dashboard(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_properties: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages a shared dashboard in the Azure Portal.

        !> **Note:** The `portal.Dashboard` resource is deprecated in version 3.0 of the AzureRM provider and will be removed in version 4.0. Please use the `portal.PortalDashboard` resource instead.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        config = pulumi.Config()
        md_content = config.get("mdContent")
        if md_content is None:
            md_content = "# Hello all :)"
        video_link = config.get("videoLink")
        if video_link is None:
            video_link = "https://www.youtube.com/watch?v=......"
        current = azure.core.get_subscription()
        example = azure.core.ResourceGroup("example", location="West Europe")
        my_board = azure.portal.Dashboard("my-board",
            resource_group_name=example.name,
            location=example.location,
            tags={
                "source": "managed",
            },
            dashboard_properties=f\"\"\"{{
           "lenses": {{
                "0": {{
                    "order": 0,
                    "parts": {{
                        "0": {{
                            "position": {{
                                "x": 0,
                                "y": 0,
                                "rowSpan": 2,
                                "colSpan": 3
                            }},
                            "metadata": {{
                                "inputs": [],
                                "type": "Extension/HubsExtension/PartType/MarkdownPart",
                                "settings": {{
                                    "content": {{
                                        "settings": {{
                                            "content": "{md_content}",
                                            "subtitle": "",
                                            "title": ""
                                        }}
                                    }}
                                }}
                            }}
                        }},               
                        "1": {{
                            "position": {{
                                "x": 5,
                                "y": 0,
                                "rowSpan": 4,
                                "colSpan": 6
                            }},
                            "metadata": {{
                                "inputs": [],
                                "type": "Extension/HubsExtension/PartType/VideoPart",
                                "settings": {{
                                    "content": {{
                                        "settings": {{
                                            "title": "Important Information",
                                            "subtitle": "",
                                            "src": "{video_link}",
                                            "autoplay": true
                                        }}
                                    }}
                                }}
                            }}
                        }},
                        "2": {{
                            "position": {{
                                "x": 0,
                                "y": 4,
                                "rowSpan": 4,
                                "colSpan": 6
                            }},
                            "metadata": {{
                                "inputs": [
                                    {{
                                        "name": "ComponentId",
                                        "value": "/subscriptions/{current.subscription_id}/resourceGroups/myRG/providers/microsoft.insights/components/myWebApp"
                                    }}
                                ],
                                "type": "Extension/AppInsightsExtension/PartType/AppMapGalPt",
                                "settings": {{}},
                                "asset": {{
                                    "idInputName": "ComponentId",
                                    "type": "ApplicationInsights"
                                }}
                            }}
                        }}              
                    }}
                }}
            }},
            "metadata": {{
                "model": {{
                    "timeRange": {{
                        "value": {{
                            "relative": {{
                                "duration": 24,
                                "timeUnit": 1
                            }}
                        }},
                        "type": "MsPortalFx.Composition.Configuration.ValueTypes.TimeRange"
                    }},
                    "filterLocale": {{
                        "value": "en-us"
                    }},
                    "filters": {{
                        "value": {{
                            "MsPortalFx_TimeRange": {{
                                "model": {{
                                    "format": "utc",
                                    "granularity": "auto",
                                    "relative": "24h"
                                }},
                                "displayCache": {{
                                    "name": "UTC Time",
                                    "value": "Past 24 hours"
                                }},
                                "filteredPartIds": [
                                    "StartboardPart-UnboundPart-ae44fef5-76b8-46b0-86f0-2b3f47bad1c7"
                                ]
                            }}
                        }}
                    }}
                }}
            }}
        }}
        \"\"\")
        ```

        It is recommended to follow the steps outlined
        [here](https://docs.microsoft.com/azure/azure-portal/azure-portal-dashboards-create-programmatically#fetch-the-json-representation-of-the-dashboard) to create a Dashboard in the Portal and extract the relevant JSON to use in this resource. From the extracted JSON, the contents of the `properties: {}` object can used. Variables can be injected as needed - see above example.

        ## Import

        Dashboards can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:portal/dashboard:Dashboard my-board /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.Portal/dashboards/00000000-0000-0000-0000-000000000000
        ```

         Note the URI in the above sample can be found using the Resource Explorer tool in the Azure Portal.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dashboard_properties: JSON data representing dashboard body. See above for details on how to obtain this from the Portal.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Shared Dashboard. Changing this forces a new resource to be created.
               
               > **Note**: You can specify a tag with the key `hidden-title` to set a more user-friendly title for this Dashboard.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the dashboard. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DashboardArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a shared dashboard in the Azure Portal.

        !> **Note:** The `portal.Dashboard` resource is deprecated in version 3.0 of the AzureRM provider and will be removed in version 4.0. Please use the `portal.PortalDashboard` resource instead.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        config = pulumi.Config()
        md_content = config.get("mdContent")
        if md_content is None:
            md_content = "# Hello all :)"
        video_link = config.get("videoLink")
        if video_link is None:
            video_link = "https://www.youtube.com/watch?v=......"
        current = azure.core.get_subscription()
        example = azure.core.ResourceGroup("example", location="West Europe")
        my_board = azure.portal.Dashboard("my-board",
            resource_group_name=example.name,
            location=example.location,
            tags={
                "source": "managed",
            },
            dashboard_properties=f\"\"\"{{
           "lenses": {{
                "0": {{
                    "order": 0,
                    "parts": {{
                        "0": {{
                            "position": {{
                                "x": 0,
                                "y": 0,
                                "rowSpan": 2,
                                "colSpan": 3
                            }},
                            "metadata": {{
                                "inputs": [],
                                "type": "Extension/HubsExtension/PartType/MarkdownPart",
                                "settings": {{
                                    "content": {{
                                        "settings": {{
                                            "content": "{md_content}",
                                            "subtitle": "",
                                            "title": ""
                                        }}
                                    }}
                                }}
                            }}
                        }},               
                        "1": {{
                            "position": {{
                                "x": 5,
                                "y": 0,
                                "rowSpan": 4,
                                "colSpan": 6
                            }},
                            "metadata": {{
                                "inputs": [],
                                "type": "Extension/HubsExtension/PartType/VideoPart",
                                "settings": {{
                                    "content": {{
                                        "settings": {{
                                            "title": "Important Information",
                                            "subtitle": "",
                                            "src": "{video_link}",
                                            "autoplay": true
                                        }}
                                    }}
                                }}
                            }}
                        }},
                        "2": {{
                            "position": {{
                                "x": 0,
                                "y": 4,
                                "rowSpan": 4,
                                "colSpan": 6
                            }},
                            "metadata": {{
                                "inputs": [
                                    {{
                                        "name": "ComponentId",
                                        "value": "/subscriptions/{current.subscription_id}/resourceGroups/myRG/providers/microsoft.insights/components/myWebApp"
                                    }}
                                ],
                                "type": "Extension/AppInsightsExtension/PartType/AppMapGalPt",
                                "settings": {{}},
                                "asset": {{
                                    "idInputName": "ComponentId",
                                    "type": "ApplicationInsights"
                                }}
                            }}
                        }}              
                    }}
                }}
            }},
            "metadata": {{
                "model": {{
                    "timeRange": {{
                        "value": {{
                            "relative": {{
                                "duration": 24,
                                "timeUnit": 1
                            }}
                        }},
                        "type": "MsPortalFx.Composition.Configuration.ValueTypes.TimeRange"
                    }},
                    "filterLocale": {{
                        "value": "en-us"
                    }},
                    "filters": {{
                        "value": {{
                            "MsPortalFx_TimeRange": {{
                                "model": {{
                                    "format": "utc",
                                    "granularity": "auto",
                                    "relative": "24h"
                                }},
                                "displayCache": {{
                                    "name": "UTC Time",
                                    "value": "Past 24 hours"
                                }},
                                "filteredPartIds": [
                                    "StartboardPart-UnboundPart-ae44fef5-76b8-46b0-86f0-2b3f47bad1c7"
                                ]
                            }}
                        }}
                    }}
                }}
            }}
        }}
        \"\"\")
        ```

        It is recommended to follow the steps outlined
        [here](https://docs.microsoft.com/azure/azure-portal/azure-portal-dashboards-create-programmatically#fetch-the-json-representation-of-the-dashboard) to create a Dashboard in the Portal and extract the relevant JSON to use in this resource. From the extracted JSON, the contents of the `properties: {}` object can used. Variables can be injected as needed - see above example.

        ## Import

        Dashboards can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:portal/dashboard:Dashboard my-board /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.Portal/dashboards/00000000-0000-0000-0000-000000000000
        ```

         Note the URI in the above sample can be found using the Resource Explorer tool in the Azure Portal.

        :param str resource_name: The name of the resource.
        :param DashboardArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DashboardArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DashboardArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_properties: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DashboardArgs.__new__(DashboardArgs)

            __props__.__dict__["dashboard_properties"] = dashboard_properties
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure:dashboard/dashboard:Dashboard")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Dashboard, __self__).__init__(
            'azure:portal/dashboard:Dashboard',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dashboard_properties: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Dashboard':
        """
        Get an existing Dashboard resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dashboard_properties: JSON data representing dashboard body. See above for details on how to obtain this from the Portal.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Shared Dashboard. Changing this forces a new resource to be created.
               
               > **Note**: You can specify a tag with the key `hidden-title` to set a more user-friendly title for this Dashboard.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the dashboard. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DashboardState.__new__(_DashboardState)

        __props__.__dict__["dashboard_properties"] = dashboard_properties
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["tags"] = tags
        return Dashboard(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dashboardProperties")
    def dashboard_properties(self) -> pulumi.Output[str]:
        """
        JSON data representing dashboard body. See above for details on how to obtain this from the Portal.
        """
        return pulumi.get(self, "dashboard_properties")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Shared Dashboard. Changing this forces a new resource to be created.

        > **Note**: You can specify a tag with the key `hidden-title` to set a more user-friendly title for this Dashboard.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the dashboard. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")


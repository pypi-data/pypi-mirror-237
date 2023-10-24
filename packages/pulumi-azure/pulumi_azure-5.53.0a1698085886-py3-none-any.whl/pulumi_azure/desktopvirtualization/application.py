# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ApplicationArgs', 'Application']

@pulumi.input_type
class ApplicationArgs:
    def __init__(__self__, *,
                 application_group_id: pulumi.Input[str],
                 command_line_argument_policy: pulumi.Input[str],
                 path: pulumi.Input[str],
                 command_line_arguments: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 icon_index: Optional[pulumi.Input[int]] = None,
                 icon_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 show_in_portal: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Application resource.
        :param pulumi.Input[str] application_group_id: Resource ID for a Virtual Desktop Application Group to associate with the Virtual Desktop Application. Changing this forces a new resource to be created.
        :param pulumi.Input[str] command_line_argument_policy: Specifies whether this published application can be launched with command line arguments provided by the client, command line arguments specified at publish time, or no command line arguments at all. Possible values include: `DoNotAllow`, `Allow`, `Require`.
        :param pulumi.Input[str] path: The file path location of the app on the Virtual Desktop OS.
        :param pulumi.Input[str] command_line_arguments: Command Line Arguments for Virtual Desktop Application.
        :param pulumi.Input[str] description: Option to set a description for the Virtual Desktop Application.
        :param pulumi.Input[str] friendly_name: Option to set a friendly name for the Virtual Desktop Application.
        :param pulumi.Input[int] icon_index: The index of the icon you wish to use.
        :param pulumi.Input[str] icon_path: Specifies the path for an icon which will be used for this Virtual Desktop Application.
        :param pulumi.Input[str] name: The name of the Virtual Desktop Application. Changing the name forces a new resource to be created.
        :param pulumi.Input[bool] show_in_portal: Specifies whether to show the RemoteApp program in the RD Web Access server.
        """
        ApplicationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            application_group_id=application_group_id,
            command_line_argument_policy=command_line_argument_policy,
            path=path,
            command_line_arguments=command_line_arguments,
            description=description,
            friendly_name=friendly_name,
            icon_index=icon_index,
            icon_path=icon_path,
            name=name,
            show_in_portal=show_in_portal,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             application_group_id: pulumi.Input[str],
             command_line_argument_policy: pulumi.Input[str],
             path: pulumi.Input[str],
             command_line_arguments: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             friendly_name: Optional[pulumi.Input[str]] = None,
             icon_index: Optional[pulumi.Input[int]] = None,
             icon_path: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             show_in_portal: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'applicationGroupId' in kwargs:
            application_group_id = kwargs['applicationGroupId']
        if 'commandLineArgumentPolicy' in kwargs:
            command_line_argument_policy = kwargs['commandLineArgumentPolicy']
        if 'commandLineArguments' in kwargs:
            command_line_arguments = kwargs['commandLineArguments']
        if 'friendlyName' in kwargs:
            friendly_name = kwargs['friendlyName']
        if 'iconIndex' in kwargs:
            icon_index = kwargs['iconIndex']
        if 'iconPath' in kwargs:
            icon_path = kwargs['iconPath']
        if 'showInPortal' in kwargs:
            show_in_portal = kwargs['showInPortal']

        _setter("application_group_id", application_group_id)
        _setter("command_line_argument_policy", command_line_argument_policy)
        _setter("path", path)
        if command_line_arguments is not None:
            _setter("command_line_arguments", command_line_arguments)
        if description is not None:
            _setter("description", description)
        if friendly_name is not None:
            _setter("friendly_name", friendly_name)
        if icon_index is not None:
            _setter("icon_index", icon_index)
        if icon_path is not None:
            _setter("icon_path", icon_path)
        if name is not None:
            _setter("name", name)
        if show_in_portal is not None:
            _setter("show_in_portal", show_in_portal)

    @property
    @pulumi.getter(name="applicationGroupId")
    def application_group_id(self) -> pulumi.Input[str]:
        """
        Resource ID for a Virtual Desktop Application Group to associate with the Virtual Desktop Application. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "application_group_id")

    @application_group_id.setter
    def application_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_group_id", value)

    @property
    @pulumi.getter(name="commandLineArgumentPolicy")
    def command_line_argument_policy(self) -> pulumi.Input[str]:
        """
        Specifies whether this published application can be launched with command line arguments provided by the client, command line arguments specified at publish time, or no command line arguments at all. Possible values include: `DoNotAllow`, `Allow`, `Require`.
        """
        return pulumi.get(self, "command_line_argument_policy")

    @command_line_argument_policy.setter
    def command_line_argument_policy(self, value: pulumi.Input[str]):
        pulumi.set(self, "command_line_argument_policy", value)

    @property
    @pulumi.getter
    def path(self) -> pulumi.Input[str]:
        """
        The file path location of the app on the Virtual Desktop OS.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: pulumi.Input[str]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter(name="commandLineArguments")
    def command_line_arguments(self) -> Optional[pulumi.Input[str]]:
        """
        Command Line Arguments for Virtual Desktop Application.
        """
        return pulumi.get(self, "command_line_arguments")

    @command_line_arguments.setter
    def command_line_arguments(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "command_line_arguments", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Option to set a description for the Virtual Desktop Application.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[str]]:
        """
        Option to set a friendly name for the Virtual Desktop Application.
        """
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter(name="iconIndex")
    def icon_index(self) -> Optional[pulumi.Input[int]]:
        """
        The index of the icon you wish to use.
        """
        return pulumi.get(self, "icon_index")

    @icon_index.setter
    def icon_index(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "icon_index", value)

    @property
    @pulumi.getter(name="iconPath")
    def icon_path(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the path for an icon which will be used for this Virtual Desktop Application.
        """
        return pulumi.get(self, "icon_path")

    @icon_path.setter
    def icon_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_path", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Virtual Desktop Application. Changing the name forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="showInPortal")
    def show_in_portal(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to show the RemoteApp program in the RD Web Access server.
        """
        return pulumi.get(self, "show_in_portal")

    @show_in_portal.setter
    def show_in_portal(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "show_in_portal", value)


@pulumi.input_type
class _ApplicationState:
    def __init__(__self__, *,
                 application_group_id: Optional[pulumi.Input[str]] = None,
                 command_line_argument_policy: Optional[pulumi.Input[str]] = None,
                 command_line_arguments: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 icon_index: Optional[pulumi.Input[int]] = None,
                 icon_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 show_in_portal: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Application resources.
        :param pulumi.Input[str] application_group_id: Resource ID for a Virtual Desktop Application Group to associate with the Virtual Desktop Application. Changing this forces a new resource to be created.
        :param pulumi.Input[str] command_line_argument_policy: Specifies whether this published application can be launched with command line arguments provided by the client, command line arguments specified at publish time, or no command line arguments at all. Possible values include: `DoNotAllow`, `Allow`, `Require`.
        :param pulumi.Input[str] command_line_arguments: Command Line Arguments for Virtual Desktop Application.
        :param pulumi.Input[str] description: Option to set a description for the Virtual Desktop Application.
        :param pulumi.Input[str] friendly_name: Option to set a friendly name for the Virtual Desktop Application.
        :param pulumi.Input[int] icon_index: The index of the icon you wish to use.
        :param pulumi.Input[str] icon_path: Specifies the path for an icon which will be used for this Virtual Desktop Application.
        :param pulumi.Input[str] name: The name of the Virtual Desktop Application. Changing the name forces a new resource to be created.
        :param pulumi.Input[str] path: The file path location of the app on the Virtual Desktop OS.
        :param pulumi.Input[bool] show_in_portal: Specifies whether to show the RemoteApp program in the RD Web Access server.
        """
        _ApplicationState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            application_group_id=application_group_id,
            command_line_argument_policy=command_line_argument_policy,
            command_line_arguments=command_line_arguments,
            description=description,
            friendly_name=friendly_name,
            icon_index=icon_index,
            icon_path=icon_path,
            name=name,
            path=path,
            show_in_portal=show_in_portal,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             application_group_id: Optional[pulumi.Input[str]] = None,
             command_line_argument_policy: Optional[pulumi.Input[str]] = None,
             command_line_arguments: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             friendly_name: Optional[pulumi.Input[str]] = None,
             icon_index: Optional[pulumi.Input[int]] = None,
             icon_path: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             path: Optional[pulumi.Input[str]] = None,
             show_in_portal: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'applicationGroupId' in kwargs:
            application_group_id = kwargs['applicationGroupId']
        if 'commandLineArgumentPolicy' in kwargs:
            command_line_argument_policy = kwargs['commandLineArgumentPolicy']
        if 'commandLineArguments' in kwargs:
            command_line_arguments = kwargs['commandLineArguments']
        if 'friendlyName' in kwargs:
            friendly_name = kwargs['friendlyName']
        if 'iconIndex' in kwargs:
            icon_index = kwargs['iconIndex']
        if 'iconPath' in kwargs:
            icon_path = kwargs['iconPath']
        if 'showInPortal' in kwargs:
            show_in_portal = kwargs['showInPortal']

        if application_group_id is not None:
            _setter("application_group_id", application_group_id)
        if command_line_argument_policy is not None:
            _setter("command_line_argument_policy", command_line_argument_policy)
        if command_line_arguments is not None:
            _setter("command_line_arguments", command_line_arguments)
        if description is not None:
            _setter("description", description)
        if friendly_name is not None:
            _setter("friendly_name", friendly_name)
        if icon_index is not None:
            _setter("icon_index", icon_index)
        if icon_path is not None:
            _setter("icon_path", icon_path)
        if name is not None:
            _setter("name", name)
        if path is not None:
            _setter("path", path)
        if show_in_portal is not None:
            _setter("show_in_portal", show_in_portal)

    @property
    @pulumi.getter(name="applicationGroupId")
    def application_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID for a Virtual Desktop Application Group to associate with the Virtual Desktop Application. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "application_group_id")

    @application_group_id.setter
    def application_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_group_id", value)

    @property
    @pulumi.getter(name="commandLineArgumentPolicy")
    def command_line_argument_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether this published application can be launched with command line arguments provided by the client, command line arguments specified at publish time, or no command line arguments at all. Possible values include: `DoNotAllow`, `Allow`, `Require`.
        """
        return pulumi.get(self, "command_line_argument_policy")

    @command_line_argument_policy.setter
    def command_line_argument_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "command_line_argument_policy", value)

    @property
    @pulumi.getter(name="commandLineArguments")
    def command_line_arguments(self) -> Optional[pulumi.Input[str]]:
        """
        Command Line Arguments for Virtual Desktop Application.
        """
        return pulumi.get(self, "command_line_arguments")

    @command_line_arguments.setter
    def command_line_arguments(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "command_line_arguments", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Option to set a description for the Virtual Desktop Application.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[str]]:
        """
        Option to set a friendly name for the Virtual Desktop Application.
        """
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter(name="iconIndex")
    def icon_index(self) -> Optional[pulumi.Input[int]]:
        """
        The index of the icon you wish to use.
        """
        return pulumi.get(self, "icon_index")

    @icon_index.setter
    def icon_index(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "icon_index", value)

    @property
    @pulumi.getter(name="iconPath")
    def icon_path(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the path for an icon which will be used for this Virtual Desktop Application.
        """
        return pulumi.get(self, "icon_path")

    @icon_path.setter
    def icon_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_path", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Virtual Desktop Application. Changing the name forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        The file path location of the app on the Virtual Desktop OS.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter(name="showInPortal")
    def show_in_portal(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to show the RemoteApp program in the RD Web Access server.
        """
        return pulumi.get(self, "show_in_portal")

    @show_in_portal.setter
    def show_in_portal(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "show_in_portal", value)


class Application(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_group_id: Optional[pulumi.Input[str]] = None,
                 command_line_argument_policy: Optional[pulumi.Input[str]] = None,
                 command_line_arguments: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 icon_index: Optional[pulumi.Input[int]] = None,
                 icon_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 show_in_portal: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Manages a Virtual Desktop Application.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example", location="West Europe")
        pooledbreadthfirst = azure.desktopvirtualization.HostPool("pooledbreadthfirst",
            location=example.location,
            resource_group_name=example.name,
            type="Pooled",
            load_balancer_type="BreadthFirst")
        personalautomatic = azure.desktopvirtualization.HostPool("personalautomatic",
            location=example.location,
            resource_group_name=example.name,
            type="Personal",
            personal_desktop_assignment_type="Automatic",
            load_balancer_type="BreadthFirst")
        remoteapp = azure.desktopvirtualization.ApplicationGroup("remoteapp",
            location=example.location,
            resource_group_name=example.name,
            type="RemoteApp",
            host_pool_id=pooledbreadthfirst.id,
            friendly_name="TestAppGroup",
            description="Acceptance Test: An application group")
        chrome = azure.desktopvirtualization.Application("chrome",
            application_group_id=remoteapp.id,
            friendly_name="Google Chrome",
            description="Chromium based web browser",
            path="C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe",
            command_line_argument_policy="DoNotAllow",
            command_line_arguments="--incognito",
            show_in_portal=False,
            icon_path="C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe",
            icon_index=0)
        ```

        ## Import

        Virtual Desktop Application can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:desktopvirtualization/application:Application example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup1/providers/Microsoft.DesktopVirtualization/applicationGroups/myapplicationgroup/applications/myapplication
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_group_id: Resource ID for a Virtual Desktop Application Group to associate with the Virtual Desktop Application. Changing this forces a new resource to be created.
        :param pulumi.Input[str] command_line_argument_policy: Specifies whether this published application can be launched with command line arguments provided by the client, command line arguments specified at publish time, or no command line arguments at all. Possible values include: `DoNotAllow`, `Allow`, `Require`.
        :param pulumi.Input[str] command_line_arguments: Command Line Arguments for Virtual Desktop Application.
        :param pulumi.Input[str] description: Option to set a description for the Virtual Desktop Application.
        :param pulumi.Input[str] friendly_name: Option to set a friendly name for the Virtual Desktop Application.
        :param pulumi.Input[int] icon_index: The index of the icon you wish to use.
        :param pulumi.Input[str] icon_path: Specifies the path for an icon which will be used for this Virtual Desktop Application.
        :param pulumi.Input[str] name: The name of the Virtual Desktop Application. Changing the name forces a new resource to be created.
        :param pulumi.Input[str] path: The file path location of the app on the Virtual Desktop OS.
        :param pulumi.Input[bool] show_in_portal: Specifies whether to show the RemoteApp program in the RD Web Access server.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Virtual Desktop Application.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example", location="West Europe")
        pooledbreadthfirst = azure.desktopvirtualization.HostPool("pooledbreadthfirst",
            location=example.location,
            resource_group_name=example.name,
            type="Pooled",
            load_balancer_type="BreadthFirst")
        personalautomatic = azure.desktopvirtualization.HostPool("personalautomatic",
            location=example.location,
            resource_group_name=example.name,
            type="Personal",
            personal_desktop_assignment_type="Automatic",
            load_balancer_type="BreadthFirst")
        remoteapp = azure.desktopvirtualization.ApplicationGroup("remoteapp",
            location=example.location,
            resource_group_name=example.name,
            type="RemoteApp",
            host_pool_id=pooledbreadthfirst.id,
            friendly_name="TestAppGroup",
            description="Acceptance Test: An application group")
        chrome = azure.desktopvirtualization.Application("chrome",
            application_group_id=remoteapp.id,
            friendly_name="Google Chrome",
            description="Chromium based web browser",
            path="C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe",
            command_line_argument_policy="DoNotAllow",
            command_line_arguments="--incognito",
            show_in_portal=False,
            icon_path="C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe",
            icon_index=0)
        ```

        ## Import

        Virtual Desktop Application can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:desktopvirtualization/application:Application example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup1/providers/Microsoft.DesktopVirtualization/applicationGroups/myapplicationgroup/applications/myapplication
        ```

        :param str resource_name: The name of the resource.
        :param ApplicationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ApplicationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_group_id: Optional[pulumi.Input[str]] = None,
                 command_line_argument_policy: Optional[pulumi.Input[str]] = None,
                 command_line_arguments: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 icon_index: Optional[pulumi.Input[int]] = None,
                 icon_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 show_in_portal: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationArgs.__new__(ApplicationArgs)

            if application_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'application_group_id'")
            __props__.__dict__["application_group_id"] = application_group_id
            if command_line_argument_policy is None and not opts.urn:
                raise TypeError("Missing required property 'command_line_argument_policy'")
            __props__.__dict__["command_line_argument_policy"] = command_line_argument_policy
            __props__.__dict__["command_line_arguments"] = command_line_arguments
            __props__.__dict__["description"] = description
            __props__.__dict__["friendly_name"] = friendly_name
            __props__.__dict__["icon_index"] = icon_index
            __props__.__dict__["icon_path"] = icon_path
            __props__.__dict__["name"] = name
            if path is None and not opts.urn:
                raise TypeError("Missing required property 'path'")
            __props__.__dict__["path"] = path
            __props__.__dict__["show_in_portal"] = show_in_portal
        super(Application, __self__).__init__(
            'azure:desktopvirtualization/application:Application',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            application_group_id: Optional[pulumi.Input[str]] = None,
            command_line_argument_policy: Optional[pulumi.Input[str]] = None,
            command_line_arguments: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            friendly_name: Optional[pulumi.Input[str]] = None,
            icon_index: Optional[pulumi.Input[int]] = None,
            icon_path: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            path: Optional[pulumi.Input[str]] = None,
            show_in_portal: Optional[pulumi.Input[bool]] = None) -> 'Application':
        """
        Get an existing Application resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_group_id: Resource ID for a Virtual Desktop Application Group to associate with the Virtual Desktop Application. Changing this forces a new resource to be created.
        :param pulumi.Input[str] command_line_argument_policy: Specifies whether this published application can be launched with command line arguments provided by the client, command line arguments specified at publish time, or no command line arguments at all. Possible values include: `DoNotAllow`, `Allow`, `Require`.
        :param pulumi.Input[str] command_line_arguments: Command Line Arguments for Virtual Desktop Application.
        :param pulumi.Input[str] description: Option to set a description for the Virtual Desktop Application.
        :param pulumi.Input[str] friendly_name: Option to set a friendly name for the Virtual Desktop Application.
        :param pulumi.Input[int] icon_index: The index of the icon you wish to use.
        :param pulumi.Input[str] icon_path: Specifies the path for an icon which will be used for this Virtual Desktop Application.
        :param pulumi.Input[str] name: The name of the Virtual Desktop Application. Changing the name forces a new resource to be created.
        :param pulumi.Input[str] path: The file path location of the app on the Virtual Desktop OS.
        :param pulumi.Input[bool] show_in_portal: Specifies whether to show the RemoteApp program in the RD Web Access server.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ApplicationState.__new__(_ApplicationState)

        __props__.__dict__["application_group_id"] = application_group_id
        __props__.__dict__["command_line_argument_policy"] = command_line_argument_policy
        __props__.__dict__["command_line_arguments"] = command_line_arguments
        __props__.__dict__["description"] = description
        __props__.__dict__["friendly_name"] = friendly_name
        __props__.__dict__["icon_index"] = icon_index
        __props__.__dict__["icon_path"] = icon_path
        __props__.__dict__["name"] = name
        __props__.__dict__["path"] = path
        __props__.__dict__["show_in_portal"] = show_in_portal
        return Application(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationGroupId")
    def application_group_id(self) -> pulumi.Output[str]:
        """
        Resource ID for a Virtual Desktop Application Group to associate with the Virtual Desktop Application. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "application_group_id")

    @property
    @pulumi.getter(name="commandLineArgumentPolicy")
    def command_line_argument_policy(self) -> pulumi.Output[str]:
        """
        Specifies whether this published application can be launched with command line arguments provided by the client, command line arguments specified at publish time, or no command line arguments at all. Possible values include: `DoNotAllow`, `Allow`, `Require`.
        """
        return pulumi.get(self, "command_line_argument_policy")

    @property
    @pulumi.getter(name="commandLineArguments")
    def command_line_arguments(self) -> pulumi.Output[Optional[str]]:
        """
        Command Line Arguments for Virtual Desktop Application.
        """
        return pulumi.get(self, "command_line_arguments")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Option to set a description for the Virtual Desktop Application.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[str]:
        """
        Option to set a friendly name for the Virtual Desktop Application.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="iconIndex")
    def icon_index(self) -> pulumi.Output[Optional[int]]:
        """
        The index of the icon you wish to use.
        """
        return pulumi.get(self, "icon_index")

    @property
    @pulumi.getter(name="iconPath")
    def icon_path(self) -> pulumi.Output[str]:
        """
        Specifies the path for an icon which will be used for this Virtual Desktop Application.
        """
        return pulumi.get(self, "icon_path")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Virtual Desktop Application. Changing the name forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        """
        The file path location of the app on the Virtual Desktop OS.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="showInPortal")
    def show_in_portal(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether to show the RemoteApp program in the RD Web Access server.
        """
        return pulumi.get(self, "show_in_portal")


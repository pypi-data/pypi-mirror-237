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

__all__ = ['BackendArgs', 'Backend']

@pulumi.input_type
class BackendArgs:
    def __init__(__self__, *,
                 api_management_name: pulumi.Input[str],
                 protocol: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 url: pulumi.Input[str],
                 credentials: Optional[pulumi.Input['BackendCredentialsArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 proxy: Optional[pulumi.Input['BackendProxyArgs']] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 service_fabric_cluster: Optional[pulumi.Input['BackendServiceFabricClusterArgs']] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 tls: Optional[pulumi.Input['BackendTlsArgs']] = None):
        """
        The set of arguments for constructing a Backend resource.
        :param pulumi.Input[str] api_management_name: The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] protocol: The protocol used by the backend host. Possible values are `http` or `soap`.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] url: The URL of the backend host.
        :param pulumi.Input['BackendCredentialsArgs'] credentials: A `credentials` block as documented below.
        :param pulumi.Input[str] description: The description of the backend.
        :param pulumi.Input[str] name: The name of the API Management backend. Changing this forces a new resource to be created.
        :param pulumi.Input['BackendProxyArgs'] proxy: A `proxy` block as documented below.
        :param pulumi.Input[str] resource_id: The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
        :param pulumi.Input['BackendServiceFabricClusterArgs'] service_fabric_cluster: A `service_fabric_cluster` block as documented below.
        :param pulumi.Input[str] title: The title of the backend.
        :param pulumi.Input['BackendTlsArgs'] tls: A `tls` block as documented below.
        """
        BackendArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            api_management_name=api_management_name,
            protocol=protocol,
            resource_group_name=resource_group_name,
            url=url,
            credentials=credentials,
            description=description,
            name=name,
            proxy=proxy,
            resource_id=resource_id,
            service_fabric_cluster=service_fabric_cluster,
            title=title,
            tls=tls,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             api_management_name: pulumi.Input[str],
             protocol: pulumi.Input[str],
             resource_group_name: pulumi.Input[str],
             url: pulumi.Input[str],
             credentials: Optional[pulumi.Input['BackendCredentialsArgs']] = None,
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             proxy: Optional[pulumi.Input['BackendProxyArgs']] = None,
             resource_id: Optional[pulumi.Input[str]] = None,
             service_fabric_cluster: Optional[pulumi.Input['BackendServiceFabricClusterArgs']] = None,
             title: Optional[pulumi.Input[str]] = None,
             tls: Optional[pulumi.Input['BackendTlsArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'apiManagementName' in kwargs:
            api_management_name = kwargs['apiManagementName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'resourceId' in kwargs:
            resource_id = kwargs['resourceId']
        if 'serviceFabricCluster' in kwargs:
            service_fabric_cluster = kwargs['serviceFabricCluster']

        _setter("api_management_name", api_management_name)
        _setter("protocol", protocol)
        _setter("resource_group_name", resource_group_name)
        _setter("url", url)
        if credentials is not None:
            _setter("credentials", credentials)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if proxy is not None:
            _setter("proxy", proxy)
        if resource_id is not None:
            _setter("resource_id", resource_id)
        if service_fabric_cluster is not None:
            _setter("service_fabric_cluster", service_fabric_cluster)
        if title is not None:
            _setter("title", title)
        if tls is not None:
            _setter("tls", tls)

    @property
    @pulumi.getter(name="apiManagementName")
    def api_management_name(self) -> pulumi.Input[str]:
        """
        The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "api_management_name")

    @api_management_name.setter
    def api_management_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_management_name", value)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[str]:
        """
        The protocol used by the backend host. Possible values are `http` or `soap`.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        The URL of the backend host.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input['BackendCredentialsArgs']]:
        """
        A `credentials` block as documented below.
        """
        return pulumi.get(self, "credentials")

    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input['BackendCredentialsArgs']]):
        pulumi.set(self, "credentials", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the backend.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the API Management backend. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def proxy(self) -> Optional[pulumi.Input['BackendProxyArgs']]:
        """
        A `proxy` block as documented below.
        """
        return pulumi.get(self, "proxy")

    @proxy.setter
    def proxy(self, value: Optional[pulumi.Input['BackendProxyArgs']]):
        pulumi.set(self, "proxy", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="serviceFabricCluster")
    def service_fabric_cluster(self) -> Optional[pulumi.Input['BackendServiceFabricClusterArgs']]:
        """
        A `service_fabric_cluster` block as documented below.
        """
        return pulumi.get(self, "service_fabric_cluster")

    @service_fabric_cluster.setter
    def service_fabric_cluster(self, value: Optional[pulumi.Input['BackendServiceFabricClusterArgs']]):
        pulumi.set(self, "service_fabric_cluster", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        The title of the backend.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def tls(self) -> Optional[pulumi.Input['BackendTlsArgs']]:
        """
        A `tls` block as documented below.
        """
        return pulumi.get(self, "tls")

    @tls.setter
    def tls(self, value: Optional[pulumi.Input['BackendTlsArgs']]):
        pulumi.set(self, "tls", value)


@pulumi.input_type
class _BackendState:
    def __init__(__self__, *,
                 api_management_name: Optional[pulumi.Input[str]] = None,
                 credentials: Optional[pulumi.Input['BackendCredentialsArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 proxy: Optional[pulumi.Input['BackendProxyArgs']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 service_fabric_cluster: Optional[pulumi.Input['BackendServiceFabricClusterArgs']] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 tls: Optional[pulumi.Input['BackendTlsArgs']] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Backend resources.
        :param pulumi.Input[str] api_management_name: The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
        :param pulumi.Input['BackendCredentialsArgs'] credentials: A `credentials` block as documented below.
        :param pulumi.Input[str] description: The description of the backend.
        :param pulumi.Input[str] name: The name of the API Management backend. Changing this forces a new resource to be created.
        :param pulumi.Input[str] protocol: The protocol used by the backend host. Possible values are `http` or `soap`.
        :param pulumi.Input['BackendProxyArgs'] proxy: A `proxy` block as documented below.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_id: The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
        :param pulumi.Input['BackendServiceFabricClusterArgs'] service_fabric_cluster: A `service_fabric_cluster` block as documented below.
        :param pulumi.Input[str] title: The title of the backend.
        :param pulumi.Input['BackendTlsArgs'] tls: A `tls` block as documented below.
        :param pulumi.Input[str] url: The URL of the backend host.
        """
        _BackendState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            api_management_name=api_management_name,
            credentials=credentials,
            description=description,
            name=name,
            protocol=protocol,
            proxy=proxy,
            resource_group_name=resource_group_name,
            resource_id=resource_id,
            service_fabric_cluster=service_fabric_cluster,
            title=title,
            tls=tls,
            url=url,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             api_management_name: Optional[pulumi.Input[str]] = None,
             credentials: Optional[pulumi.Input['BackendCredentialsArgs']] = None,
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             protocol: Optional[pulumi.Input[str]] = None,
             proxy: Optional[pulumi.Input['BackendProxyArgs']] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             resource_id: Optional[pulumi.Input[str]] = None,
             service_fabric_cluster: Optional[pulumi.Input['BackendServiceFabricClusterArgs']] = None,
             title: Optional[pulumi.Input[str]] = None,
             tls: Optional[pulumi.Input['BackendTlsArgs']] = None,
             url: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'apiManagementName' in kwargs:
            api_management_name = kwargs['apiManagementName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'resourceId' in kwargs:
            resource_id = kwargs['resourceId']
        if 'serviceFabricCluster' in kwargs:
            service_fabric_cluster = kwargs['serviceFabricCluster']

        if api_management_name is not None:
            _setter("api_management_name", api_management_name)
        if credentials is not None:
            _setter("credentials", credentials)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if protocol is not None:
            _setter("protocol", protocol)
        if proxy is not None:
            _setter("proxy", proxy)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if resource_id is not None:
            _setter("resource_id", resource_id)
        if service_fabric_cluster is not None:
            _setter("service_fabric_cluster", service_fabric_cluster)
        if title is not None:
            _setter("title", title)
        if tls is not None:
            _setter("tls", tls)
        if url is not None:
            _setter("url", url)

    @property
    @pulumi.getter(name="apiManagementName")
    def api_management_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "api_management_name")

    @api_management_name.setter
    def api_management_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_management_name", value)

    @property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input['BackendCredentialsArgs']]:
        """
        A `credentials` block as documented below.
        """
        return pulumi.get(self, "credentials")

    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input['BackendCredentialsArgs']]):
        pulumi.set(self, "credentials", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the backend.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the API Management backend. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The protocol used by the backend host. Possible values are `http` or `soap`.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def proxy(self) -> Optional[pulumi.Input['BackendProxyArgs']]:
        """
        A `proxy` block as documented below.
        """
        return pulumi.get(self, "proxy")

    @proxy.setter
    def proxy(self, value: Optional[pulumi.Input['BackendProxyArgs']]):
        pulumi.set(self, "proxy", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="serviceFabricCluster")
    def service_fabric_cluster(self) -> Optional[pulumi.Input['BackendServiceFabricClusterArgs']]:
        """
        A `service_fabric_cluster` block as documented below.
        """
        return pulumi.get(self, "service_fabric_cluster")

    @service_fabric_cluster.setter
    def service_fabric_cluster(self, value: Optional[pulumi.Input['BackendServiceFabricClusterArgs']]):
        pulumi.set(self, "service_fabric_cluster", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        The title of the backend.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def tls(self) -> Optional[pulumi.Input['BackendTlsArgs']]:
        """
        A `tls` block as documented below.
        """
        return pulumi.get(self, "tls")

    @tls.setter
    def tls(self, value: Optional[pulumi.Input['BackendTlsArgs']]):
        pulumi.set(self, "tls", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the backend host.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class Backend(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_management_name: Optional[pulumi.Input[str]] = None,
                 credentials: Optional[pulumi.Input[pulumi.InputType['BackendCredentialsArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 proxy: Optional[pulumi.Input[pulumi.InputType['BackendProxyArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 service_fabric_cluster: Optional[pulumi.Input[pulumi.InputType['BackendServiceFabricClusterArgs']]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 tls: Optional[pulumi.Input[pulumi.InputType['BackendTlsArgs']]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a backend within an API Management Service.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_service = azure.apimanagement.Service("exampleService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            publisher_name="My Company",
            publisher_email="company@exmaple.com",
            sku_name="Developer_1")
        example_backend = azure.apimanagement.Backend("exampleBackend",
            resource_group_name=example_resource_group.name,
            api_management_name=example_service.name,
            protocol="http",
            url="https://backend")
        ```

        ## Import

        API Management backends can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:apimanagement/backend:Backend example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.ApiManagement/service/instance1/backends/backend1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_management_name: The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['BackendCredentialsArgs']] credentials: A `credentials` block as documented below.
        :param pulumi.Input[str] description: The description of the backend.
        :param pulumi.Input[str] name: The name of the API Management backend. Changing this forces a new resource to be created.
        :param pulumi.Input[str] protocol: The protocol used by the backend host. Possible values are `http` or `soap`.
        :param pulumi.Input[pulumi.InputType['BackendProxyArgs']] proxy: A `proxy` block as documented below.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_id: The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
        :param pulumi.Input[pulumi.InputType['BackendServiceFabricClusterArgs']] service_fabric_cluster: A `service_fabric_cluster` block as documented below.
        :param pulumi.Input[str] title: The title of the backend.
        :param pulumi.Input[pulumi.InputType['BackendTlsArgs']] tls: A `tls` block as documented below.
        :param pulumi.Input[str] url: The URL of the backend host.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BackendArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a backend within an API Management Service.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_service = azure.apimanagement.Service("exampleService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            publisher_name="My Company",
            publisher_email="company@exmaple.com",
            sku_name="Developer_1")
        example_backend = azure.apimanagement.Backend("exampleBackend",
            resource_group_name=example_resource_group.name,
            api_management_name=example_service.name,
            protocol="http",
            url="https://backend")
        ```

        ## Import

        API Management backends can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:apimanagement/backend:Backend example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.ApiManagement/service/instance1/backends/backend1
        ```

        :param str resource_name: The name of the resource.
        :param BackendArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BackendArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            BackendArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_management_name: Optional[pulumi.Input[str]] = None,
                 credentials: Optional[pulumi.Input[pulumi.InputType['BackendCredentialsArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 proxy: Optional[pulumi.Input[pulumi.InputType['BackendProxyArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 service_fabric_cluster: Optional[pulumi.Input[pulumi.InputType['BackendServiceFabricClusterArgs']]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 tls: Optional[pulumi.Input[pulumi.InputType['BackendTlsArgs']]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BackendArgs.__new__(BackendArgs)

            if api_management_name is None and not opts.urn:
                raise TypeError("Missing required property 'api_management_name'")
            __props__.__dict__["api_management_name"] = api_management_name
            if credentials is not None and not isinstance(credentials, BackendCredentialsArgs):
                credentials = credentials or {}
                def _setter(key, value):
                    credentials[key] = value
                BackendCredentialsArgs._configure(_setter, **credentials)
            __props__.__dict__["credentials"] = credentials
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__.__dict__["protocol"] = protocol
            if proxy is not None and not isinstance(proxy, BackendProxyArgs):
                proxy = proxy or {}
                def _setter(key, value):
                    proxy[key] = value
                BackendProxyArgs._configure(_setter, **proxy)
            __props__.__dict__["proxy"] = proxy
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_id"] = resource_id
            if service_fabric_cluster is not None and not isinstance(service_fabric_cluster, BackendServiceFabricClusterArgs):
                service_fabric_cluster = service_fabric_cluster or {}
                def _setter(key, value):
                    service_fabric_cluster[key] = value
                BackendServiceFabricClusterArgs._configure(_setter, **service_fabric_cluster)
            __props__.__dict__["service_fabric_cluster"] = service_fabric_cluster
            __props__.__dict__["title"] = title
            if tls is not None and not isinstance(tls, BackendTlsArgs):
                tls = tls or {}
                def _setter(key, value):
                    tls[key] = value
                BackendTlsArgs._configure(_setter, **tls)
            __props__.__dict__["tls"] = tls
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
        super(Backend, __self__).__init__(
            'azure:apimanagement/backend:Backend',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_management_name: Optional[pulumi.Input[str]] = None,
            credentials: Optional[pulumi.Input[pulumi.InputType['BackendCredentialsArgs']]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            proxy: Optional[pulumi.Input[pulumi.InputType['BackendProxyArgs']]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            resource_id: Optional[pulumi.Input[str]] = None,
            service_fabric_cluster: Optional[pulumi.Input[pulumi.InputType['BackendServiceFabricClusterArgs']]] = None,
            title: Optional[pulumi.Input[str]] = None,
            tls: Optional[pulumi.Input[pulumi.InputType['BackendTlsArgs']]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'Backend':
        """
        Get an existing Backend resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_management_name: The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['BackendCredentialsArgs']] credentials: A `credentials` block as documented below.
        :param pulumi.Input[str] description: The description of the backend.
        :param pulumi.Input[str] name: The name of the API Management backend. Changing this forces a new resource to be created.
        :param pulumi.Input[str] protocol: The protocol used by the backend host. Possible values are `http` or `soap`.
        :param pulumi.Input[pulumi.InputType['BackendProxyArgs']] proxy: A `proxy` block as documented below.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_id: The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
        :param pulumi.Input[pulumi.InputType['BackendServiceFabricClusterArgs']] service_fabric_cluster: A `service_fabric_cluster` block as documented below.
        :param pulumi.Input[str] title: The title of the backend.
        :param pulumi.Input[pulumi.InputType['BackendTlsArgs']] tls: A `tls` block as documented below.
        :param pulumi.Input[str] url: The URL of the backend host.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BackendState.__new__(_BackendState)

        __props__.__dict__["api_management_name"] = api_management_name
        __props__.__dict__["credentials"] = credentials
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["protocol"] = protocol
        __props__.__dict__["proxy"] = proxy
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["resource_id"] = resource_id
        __props__.__dict__["service_fabric_cluster"] = service_fabric_cluster
        __props__.__dict__["title"] = title
        __props__.__dict__["tls"] = tls
        __props__.__dict__["url"] = url
        return Backend(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiManagementName")
    def api_management_name(self) -> pulumi.Output[str]:
        """
        The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "api_management_name")

    @property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional['outputs.BackendCredentials']]:
        """
        A `credentials` block as documented below.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the backend.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the API Management backend. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        """
        The protocol used by the backend host. Possible values are `http` or `soap`.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def proxy(self) -> pulumi.Output[Optional['outputs.BackendProxy']]:
        """
        A `proxy` block as documented below.
        """
        return pulumi.get(self, "proxy")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="serviceFabricCluster")
    def service_fabric_cluster(self) -> pulumi.Output[Optional['outputs.BackendServiceFabricCluster']]:
        """
        A `service_fabric_cluster` block as documented below.
        """
        return pulumi.get(self, "service_fabric_cluster")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[str]]:
        """
        The title of the backend.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def tls(self) -> pulumi.Output[Optional['outputs.BackendTls']]:
        """
        A `tls` block as documented below.
        """
        return pulumi.get(self, "tls")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The URL of the backend host.
        """
        return pulumi.get(self, "url")


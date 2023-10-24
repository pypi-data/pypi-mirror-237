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

__all__ = ['ApiOperationArgs', 'ApiOperation']

@pulumi.input_type
class ApiOperationArgs:
    def __init__(__self__, *,
                 api_management_name: pulumi.Input[str],
                 api_name: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 method: pulumi.Input[str],
                 operation_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 url_template: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 request: Optional[pulumi.Input['ApiOperationRequestArgs']] = None,
                 responses: Optional[pulumi.Input[Sequence[pulumi.Input['ApiOperationResponseArgs']]]] = None,
                 template_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['ApiOperationTemplateParameterArgs']]]] = None):
        """
        The set of arguments for constructing a ApiOperation resource.
        :param pulumi.Input[str] api_management_name: The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] api_name: The name of the API within the API Management Service where this API Operation should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] display_name: The Display Name for this API Management Operation.
        :param pulumi.Input[str] method: The HTTP Method used for this API Management Operation, like `GET`, `DELETE`, `PUT` or `POST` - but not limited to these values.
        :param pulumi.Input[str] operation_id: A unique identifier for this API Operation. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] url_template: The relative URL Template identifying the target resource for this operation, which may include parameters.
        :param pulumi.Input[str] description: A description for this API Operation, which may include HTML formatting tags.
        :param pulumi.Input['ApiOperationRequestArgs'] request: A `request` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input['ApiOperationResponseArgs']]] responses: One or more `response` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input['ApiOperationTemplateParameterArgs']]] template_parameters: One or more `template_parameter` blocks as defined below.
        """
        ApiOperationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            api_management_name=api_management_name,
            api_name=api_name,
            display_name=display_name,
            method=method,
            operation_id=operation_id,
            resource_group_name=resource_group_name,
            url_template=url_template,
            description=description,
            request=request,
            responses=responses,
            template_parameters=template_parameters,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             api_management_name: pulumi.Input[str],
             api_name: pulumi.Input[str],
             display_name: pulumi.Input[str],
             method: pulumi.Input[str],
             operation_id: pulumi.Input[str],
             resource_group_name: pulumi.Input[str],
             url_template: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             request: Optional[pulumi.Input['ApiOperationRequestArgs']] = None,
             responses: Optional[pulumi.Input[Sequence[pulumi.Input['ApiOperationResponseArgs']]]] = None,
             template_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['ApiOperationTemplateParameterArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'apiManagementName' in kwargs:
            api_management_name = kwargs['apiManagementName']
        if 'apiName' in kwargs:
            api_name = kwargs['apiName']
        if 'displayName' in kwargs:
            display_name = kwargs['displayName']
        if 'operationId' in kwargs:
            operation_id = kwargs['operationId']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'urlTemplate' in kwargs:
            url_template = kwargs['urlTemplate']
        if 'templateParameters' in kwargs:
            template_parameters = kwargs['templateParameters']

        _setter("api_management_name", api_management_name)
        _setter("api_name", api_name)
        _setter("display_name", display_name)
        _setter("method", method)
        _setter("operation_id", operation_id)
        _setter("resource_group_name", resource_group_name)
        _setter("url_template", url_template)
        if description is not None:
            _setter("description", description)
        if request is not None:
            _setter("request", request)
        if responses is not None:
            _setter("responses", responses)
        if template_parameters is not None:
            _setter("template_parameters", template_parameters)

    @property
    @pulumi.getter(name="apiManagementName")
    def api_management_name(self) -> pulumi.Input[str]:
        """
        The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "api_management_name")

    @api_management_name.setter
    def api_management_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_management_name", value)

    @property
    @pulumi.getter(name="apiName")
    def api_name(self) -> pulumi.Input[str]:
        """
        The name of the API within the API Management Service where this API Operation should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "api_name")

    @api_name.setter
    def api_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_name", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The Display Name for this API Management Operation.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def method(self) -> pulumi.Input[str]:
        """
        The HTTP Method used for this API Management Operation, like `GET`, `DELETE`, `PUT` or `POST` - but not limited to these values.
        """
        return pulumi.get(self, "method")

    @method.setter
    def method(self, value: pulumi.Input[str]):
        pulumi.set(self, "method", value)

    @property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> pulumi.Input[str]:
        """
        A unique identifier for this API Operation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "operation_id")

    @operation_id.setter
    def operation_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "operation_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="urlTemplate")
    def url_template(self) -> pulumi.Input[str]:
        """
        The relative URL Template identifying the target resource for this operation, which may include parameters.
        """
        return pulumi.get(self, "url_template")

    @url_template.setter
    def url_template(self, value: pulumi.Input[str]):
        pulumi.set(self, "url_template", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for this API Operation, which may include HTML formatting tags.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def request(self) -> Optional[pulumi.Input['ApiOperationRequestArgs']]:
        """
        A `request` block as defined below.
        """
        return pulumi.get(self, "request")

    @request.setter
    def request(self, value: Optional[pulumi.Input['ApiOperationRequestArgs']]):
        pulumi.set(self, "request", value)

    @property
    @pulumi.getter
    def responses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApiOperationResponseArgs']]]]:
        """
        One or more `response` blocks as defined below.
        """
        return pulumi.get(self, "responses")

    @responses.setter
    def responses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApiOperationResponseArgs']]]]):
        pulumi.set(self, "responses", value)

    @property
    @pulumi.getter(name="templateParameters")
    def template_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApiOperationTemplateParameterArgs']]]]:
        """
        One or more `template_parameter` blocks as defined below.
        """
        return pulumi.get(self, "template_parameters")

    @template_parameters.setter
    def template_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApiOperationTemplateParameterArgs']]]]):
        pulumi.set(self, "template_parameters", value)


@pulumi.input_type
class _ApiOperationState:
    def __init__(__self__, *,
                 api_management_name: Optional[pulumi.Input[str]] = None,
                 api_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 method: Optional[pulumi.Input[str]] = None,
                 operation_id: Optional[pulumi.Input[str]] = None,
                 request: Optional[pulumi.Input['ApiOperationRequestArgs']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 responses: Optional[pulumi.Input[Sequence[pulumi.Input['ApiOperationResponseArgs']]]] = None,
                 template_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['ApiOperationTemplateParameterArgs']]]] = None,
                 url_template: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ApiOperation resources.
        :param pulumi.Input[str] api_management_name: The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] api_name: The name of the API within the API Management Service where this API Operation should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: A description for this API Operation, which may include HTML formatting tags.
        :param pulumi.Input[str] display_name: The Display Name for this API Management Operation.
        :param pulumi.Input[str] method: The HTTP Method used for this API Management Operation, like `GET`, `DELETE`, `PUT` or `POST` - but not limited to these values.
        :param pulumi.Input[str] operation_id: A unique identifier for this API Operation. Changing this forces a new resource to be created.
        :param pulumi.Input['ApiOperationRequestArgs'] request: A `request` block as defined below.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input['ApiOperationResponseArgs']]] responses: One or more `response` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input['ApiOperationTemplateParameterArgs']]] template_parameters: One or more `template_parameter` blocks as defined below.
        :param pulumi.Input[str] url_template: The relative URL Template identifying the target resource for this operation, which may include parameters.
        """
        _ApiOperationState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            api_management_name=api_management_name,
            api_name=api_name,
            description=description,
            display_name=display_name,
            method=method,
            operation_id=operation_id,
            request=request,
            resource_group_name=resource_group_name,
            responses=responses,
            template_parameters=template_parameters,
            url_template=url_template,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             api_management_name: Optional[pulumi.Input[str]] = None,
             api_name: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             method: Optional[pulumi.Input[str]] = None,
             operation_id: Optional[pulumi.Input[str]] = None,
             request: Optional[pulumi.Input['ApiOperationRequestArgs']] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             responses: Optional[pulumi.Input[Sequence[pulumi.Input['ApiOperationResponseArgs']]]] = None,
             template_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['ApiOperationTemplateParameterArgs']]]] = None,
             url_template: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'apiManagementName' in kwargs:
            api_management_name = kwargs['apiManagementName']
        if 'apiName' in kwargs:
            api_name = kwargs['apiName']
        if 'displayName' in kwargs:
            display_name = kwargs['displayName']
        if 'operationId' in kwargs:
            operation_id = kwargs['operationId']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'templateParameters' in kwargs:
            template_parameters = kwargs['templateParameters']
        if 'urlTemplate' in kwargs:
            url_template = kwargs['urlTemplate']

        if api_management_name is not None:
            _setter("api_management_name", api_management_name)
        if api_name is not None:
            _setter("api_name", api_name)
        if description is not None:
            _setter("description", description)
        if display_name is not None:
            _setter("display_name", display_name)
        if method is not None:
            _setter("method", method)
        if operation_id is not None:
            _setter("operation_id", operation_id)
        if request is not None:
            _setter("request", request)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if responses is not None:
            _setter("responses", responses)
        if template_parameters is not None:
            _setter("template_parameters", template_parameters)
        if url_template is not None:
            _setter("url_template", url_template)

    @property
    @pulumi.getter(name="apiManagementName")
    def api_management_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "api_management_name")

    @api_management_name.setter
    def api_management_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_management_name", value)

    @property
    @pulumi.getter(name="apiName")
    def api_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the API within the API Management Service where this API Operation should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "api_name")

    @api_name.setter
    def api_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for this API Operation, which may include HTML formatting tags.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Display Name for this API Management Operation.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[str]]:
        """
        The HTTP Method used for this API Management Operation, like `GET`, `DELETE`, `PUT` or `POST` - but not limited to these values.
        """
        return pulumi.get(self, "method")

    @method.setter
    def method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "method", value)

    @property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> Optional[pulumi.Input[str]]:
        """
        A unique identifier for this API Operation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "operation_id")

    @operation_id.setter
    def operation_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operation_id", value)

    @property
    @pulumi.getter
    def request(self) -> Optional[pulumi.Input['ApiOperationRequestArgs']]:
        """
        A `request` block as defined below.
        """
        return pulumi.get(self, "request")

    @request.setter
    def request(self, value: Optional[pulumi.Input['ApiOperationRequestArgs']]):
        pulumi.set(self, "request", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def responses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApiOperationResponseArgs']]]]:
        """
        One or more `response` blocks as defined below.
        """
        return pulumi.get(self, "responses")

    @responses.setter
    def responses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApiOperationResponseArgs']]]]):
        pulumi.set(self, "responses", value)

    @property
    @pulumi.getter(name="templateParameters")
    def template_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApiOperationTemplateParameterArgs']]]]:
        """
        One or more `template_parameter` blocks as defined below.
        """
        return pulumi.get(self, "template_parameters")

    @template_parameters.setter
    def template_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApiOperationTemplateParameterArgs']]]]):
        pulumi.set(self, "template_parameters", value)

    @property
    @pulumi.getter(name="urlTemplate")
    def url_template(self) -> Optional[pulumi.Input[str]]:
        """
        The relative URL Template identifying the target resource for this operation, which may include parameters.
        """
        return pulumi.get(self, "url_template")

    @url_template.setter
    def url_template(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url_template", value)


class ApiOperation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_management_name: Optional[pulumi.Input[str]] = None,
                 api_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 method: Optional[pulumi.Input[str]] = None,
                 operation_id: Optional[pulumi.Input[str]] = None,
                 request: Optional[pulumi.Input[pulumi.InputType['ApiOperationRequestArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 responses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApiOperationResponseArgs']]]]] = None,
                 template_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApiOperationTemplateParameterArgs']]]]] = None,
                 url_template: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an API Operation within an API Management Service.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_api = azure.apimanagement.get_api(name="search-api",
            api_management_name="search-api-management",
            resource_group_name="search-service",
            revision="2")
        example_api_operation = azure.apimanagement.ApiOperation("exampleApiOperation",
            operation_id="user-delete",
            api_name=example_api.name,
            api_management_name=example_api.api_management_name,
            resource_group_name=example_api.resource_group_name,
            display_name="Delete User Operation",
            method="DELETE",
            url_template="/users/{id}/delete",
            description="This can only be done by the logged in user.",
            responses=[azure.apimanagement.ApiOperationResponseArgs(
                status_code=200,
            )])
        ```

        ## Import

        API Management API Operation's can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:apimanagement/apiOperation:ApiOperation example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.ApiManagement/service/instance1/apis/api1/operations/operation1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_management_name: The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] api_name: The name of the API within the API Management Service where this API Operation should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: A description for this API Operation, which may include HTML formatting tags.
        :param pulumi.Input[str] display_name: The Display Name for this API Management Operation.
        :param pulumi.Input[str] method: The HTTP Method used for this API Management Operation, like `GET`, `DELETE`, `PUT` or `POST` - but not limited to these values.
        :param pulumi.Input[str] operation_id: A unique identifier for this API Operation. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['ApiOperationRequestArgs']] request: A `request` block as defined below.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApiOperationResponseArgs']]]] responses: One or more `response` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApiOperationTemplateParameterArgs']]]] template_parameters: One or more `template_parameter` blocks as defined below.
        :param pulumi.Input[str] url_template: The relative URL Template identifying the target resource for this operation, which may include parameters.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApiOperationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an API Operation within an API Management Service.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_api = azure.apimanagement.get_api(name="search-api",
            api_management_name="search-api-management",
            resource_group_name="search-service",
            revision="2")
        example_api_operation = azure.apimanagement.ApiOperation("exampleApiOperation",
            operation_id="user-delete",
            api_name=example_api.name,
            api_management_name=example_api.api_management_name,
            resource_group_name=example_api.resource_group_name,
            display_name="Delete User Operation",
            method="DELETE",
            url_template="/users/{id}/delete",
            description="This can only be done by the logged in user.",
            responses=[azure.apimanagement.ApiOperationResponseArgs(
                status_code=200,
            )])
        ```

        ## Import

        API Management API Operation's can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:apimanagement/apiOperation:ApiOperation example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.ApiManagement/service/instance1/apis/api1/operations/operation1
        ```

        :param str resource_name: The name of the resource.
        :param ApiOperationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiOperationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ApiOperationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_management_name: Optional[pulumi.Input[str]] = None,
                 api_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 method: Optional[pulumi.Input[str]] = None,
                 operation_id: Optional[pulumi.Input[str]] = None,
                 request: Optional[pulumi.Input[pulumi.InputType['ApiOperationRequestArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 responses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApiOperationResponseArgs']]]]] = None,
                 template_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApiOperationTemplateParameterArgs']]]]] = None,
                 url_template: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApiOperationArgs.__new__(ApiOperationArgs)

            if api_management_name is None and not opts.urn:
                raise TypeError("Missing required property 'api_management_name'")
            __props__.__dict__["api_management_name"] = api_management_name
            if api_name is None and not opts.urn:
                raise TypeError("Missing required property 'api_name'")
            __props__.__dict__["api_name"] = api_name
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            if method is None and not opts.urn:
                raise TypeError("Missing required property 'method'")
            __props__.__dict__["method"] = method
            if operation_id is None and not opts.urn:
                raise TypeError("Missing required property 'operation_id'")
            __props__.__dict__["operation_id"] = operation_id
            if request is not None and not isinstance(request, ApiOperationRequestArgs):
                request = request or {}
                def _setter(key, value):
                    request[key] = value
                ApiOperationRequestArgs._configure(_setter, **request)
            __props__.__dict__["request"] = request
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["responses"] = responses
            __props__.__dict__["template_parameters"] = template_parameters
            if url_template is None and not opts.urn:
                raise TypeError("Missing required property 'url_template'")
            __props__.__dict__["url_template"] = url_template
        super(ApiOperation, __self__).__init__(
            'azure:apimanagement/apiOperation:ApiOperation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_management_name: Optional[pulumi.Input[str]] = None,
            api_name: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            method: Optional[pulumi.Input[str]] = None,
            operation_id: Optional[pulumi.Input[str]] = None,
            request: Optional[pulumi.Input[pulumi.InputType['ApiOperationRequestArgs']]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            responses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApiOperationResponseArgs']]]]] = None,
            template_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApiOperationTemplateParameterArgs']]]]] = None,
            url_template: Optional[pulumi.Input[str]] = None) -> 'ApiOperation':
        """
        Get an existing ApiOperation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_management_name: The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] api_name: The name of the API within the API Management Service where this API Operation should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: A description for this API Operation, which may include HTML formatting tags.
        :param pulumi.Input[str] display_name: The Display Name for this API Management Operation.
        :param pulumi.Input[str] method: The HTTP Method used for this API Management Operation, like `GET`, `DELETE`, `PUT` or `POST` - but not limited to these values.
        :param pulumi.Input[str] operation_id: A unique identifier for this API Operation. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['ApiOperationRequestArgs']] request: A `request` block as defined below.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApiOperationResponseArgs']]]] responses: One or more `response` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApiOperationTemplateParameterArgs']]]] template_parameters: One or more `template_parameter` blocks as defined below.
        :param pulumi.Input[str] url_template: The relative URL Template identifying the target resource for this operation, which may include parameters.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ApiOperationState.__new__(_ApiOperationState)

        __props__.__dict__["api_management_name"] = api_management_name
        __props__.__dict__["api_name"] = api_name
        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["method"] = method
        __props__.__dict__["operation_id"] = operation_id
        __props__.__dict__["request"] = request
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["responses"] = responses
        __props__.__dict__["template_parameters"] = template_parameters
        __props__.__dict__["url_template"] = url_template
        return ApiOperation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiManagementName")
    def api_management_name(self) -> pulumi.Output[str]:
        """
        The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "api_management_name")

    @property
    @pulumi.getter(name="apiName")
    def api_name(self) -> pulumi.Output[str]:
        """
        The name of the API within the API Management Service where this API Operation should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "api_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for this API Operation, which may include HTML formatting tags.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The Display Name for this API Management Operation.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def method(self) -> pulumi.Output[str]:
        """
        The HTTP Method used for this API Management Operation, like `GET`, `DELETE`, `PUT` or `POST` - but not limited to these values.
        """
        return pulumi.get(self, "method")

    @property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> pulumi.Output[str]:
        """
        A unique identifier for this API Operation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "operation_id")

    @property
    @pulumi.getter
    def request(self) -> pulumi.Output['outputs.ApiOperationRequest']:
        """
        A `request` block as defined below.
        """
        return pulumi.get(self, "request")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def responses(self) -> pulumi.Output[Optional[Sequence['outputs.ApiOperationResponse']]]:
        """
        One or more `response` blocks as defined below.
        """
        return pulumi.get(self, "responses")

    @property
    @pulumi.getter(name="templateParameters")
    def template_parameters(self) -> pulumi.Output[Optional[Sequence['outputs.ApiOperationTemplateParameter']]]:
        """
        One or more `template_parameter` blocks as defined below.
        """
        return pulumi.get(self, "template_parameters")

    @property
    @pulumi.getter(name="urlTemplate")
    def url_template(self) -> pulumi.Output[str]:
        """
        The relative URL Template identifying the target resource for this operation, which may include parameters.
        """
        return pulumi.get(self, "url_template")


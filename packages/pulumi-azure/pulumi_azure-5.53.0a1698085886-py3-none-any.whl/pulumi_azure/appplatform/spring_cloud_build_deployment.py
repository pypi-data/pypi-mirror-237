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

__all__ = ['SpringCloudBuildDeploymentArgs', 'SpringCloudBuildDeployment']

@pulumi.input_type
class SpringCloudBuildDeploymentArgs:
    def __init__(__self__, *,
                 build_result_id: pulumi.Input[str],
                 spring_cloud_app_id: pulumi.Input[str],
                 addon_json: Optional[pulumi.Input[str]] = None,
                 environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 instance_count: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quota: Optional[pulumi.Input['SpringCloudBuildDeploymentQuotaArgs']] = None):
        """
        The set of arguments for constructing a SpringCloudBuildDeployment resource.
        :param pulumi.Input[str] build_result_id: The ID of the Spring Cloud Build Result.
        :param pulumi.Input[str] spring_cloud_app_id: The ID of the Spring Cloud Service. Changing this forces a new Spring Cloud Build Deployment to be created.
        :param pulumi.Input[str] addon_json: A JSON object that contains the addon configurations of the Spring Cloud Build Deployment.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] environment_variables: Specifies the environment variables of the Spring Cloud Deployment as a map of key-value pairs.
        :param pulumi.Input[int] instance_count: Specifies the required instance count of the Spring Cloud Deployment. Possible Values are between `1` and `500`. Defaults to `1` if not specified.
        :param pulumi.Input[str] name: The name which should be used for this Spring Cloud Build Deployment. Changing this forces a new Spring Cloud Build Deployment to be created.
        :param pulumi.Input['SpringCloudBuildDeploymentQuotaArgs'] quota: A `quota` block as defined below.
        """
        SpringCloudBuildDeploymentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            build_result_id=build_result_id,
            spring_cloud_app_id=spring_cloud_app_id,
            addon_json=addon_json,
            environment_variables=environment_variables,
            instance_count=instance_count,
            name=name,
            quota=quota,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             build_result_id: pulumi.Input[str],
             spring_cloud_app_id: pulumi.Input[str],
             addon_json: Optional[pulumi.Input[str]] = None,
             environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             instance_count: Optional[pulumi.Input[int]] = None,
             name: Optional[pulumi.Input[str]] = None,
             quota: Optional[pulumi.Input['SpringCloudBuildDeploymentQuotaArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'buildResultId' in kwargs:
            build_result_id = kwargs['buildResultId']
        if 'springCloudAppId' in kwargs:
            spring_cloud_app_id = kwargs['springCloudAppId']
        if 'addonJson' in kwargs:
            addon_json = kwargs['addonJson']
        if 'environmentVariables' in kwargs:
            environment_variables = kwargs['environmentVariables']
        if 'instanceCount' in kwargs:
            instance_count = kwargs['instanceCount']

        _setter("build_result_id", build_result_id)
        _setter("spring_cloud_app_id", spring_cloud_app_id)
        if addon_json is not None:
            _setter("addon_json", addon_json)
        if environment_variables is not None:
            _setter("environment_variables", environment_variables)
        if instance_count is not None:
            _setter("instance_count", instance_count)
        if name is not None:
            _setter("name", name)
        if quota is not None:
            _setter("quota", quota)

    @property
    @pulumi.getter(name="buildResultId")
    def build_result_id(self) -> pulumi.Input[str]:
        """
        The ID of the Spring Cloud Build Result.
        """
        return pulumi.get(self, "build_result_id")

    @build_result_id.setter
    def build_result_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "build_result_id", value)

    @property
    @pulumi.getter(name="springCloudAppId")
    def spring_cloud_app_id(self) -> pulumi.Input[str]:
        """
        The ID of the Spring Cloud Service. Changing this forces a new Spring Cloud Build Deployment to be created.
        """
        return pulumi.get(self, "spring_cloud_app_id")

    @spring_cloud_app_id.setter
    def spring_cloud_app_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "spring_cloud_app_id", value)

    @property
    @pulumi.getter(name="addonJson")
    def addon_json(self) -> Optional[pulumi.Input[str]]:
        """
        A JSON object that contains the addon configurations of the Spring Cloud Build Deployment.
        """
        return pulumi.get(self, "addon_json")

    @addon_json.setter
    def addon_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "addon_json", value)

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Specifies the environment variables of the Spring Cloud Deployment as a map of key-value pairs.
        """
        return pulumi.get(self, "environment_variables")

    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "environment_variables", value)

    @property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the required instance count of the Spring Cloud Deployment. Possible Values are between `1` and `500`. Defaults to `1` if not specified.
        """
        return pulumi.get(self, "instance_count")

    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "instance_count", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Spring Cloud Build Deployment. Changing this forces a new Spring Cloud Build Deployment to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def quota(self) -> Optional[pulumi.Input['SpringCloudBuildDeploymentQuotaArgs']]:
        """
        A `quota` block as defined below.
        """
        return pulumi.get(self, "quota")

    @quota.setter
    def quota(self, value: Optional[pulumi.Input['SpringCloudBuildDeploymentQuotaArgs']]):
        pulumi.set(self, "quota", value)


@pulumi.input_type
class _SpringCloudBuildDeploymentState:
    def __init__(__self__, *,
                 addon_json: Optional[pulumi.Input[str]] = None,
                 build_result_id: Optional[pulumi.Input[str]] = None,
                 environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 instance_count: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quota: Optional[pulumi.Input['SpringCloudBuildDeploymentQuotaArgs']] = None,
                 spring_cloud_app_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SpringCloudBuildDeployment resources.
        :param pulumi.Input[str] addon_json: A JSON object that contains the addon configurations of the Spring Cloud Build Deployment.
        :param pulumi.Input[str] build_result_id: The ID of the Spring Cloud Build Result.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] environment_variables: Specifies the environment variables of the Spring Cloud Deployment as a map of key-value pairs.
        :param pulumi.Input[int] instance_count: Specifies the required instance count of the Spring Cloud Deployment. Possible Values are between `1` and `500`. Defaults to `1` if not specified.
        :param pulumi.Input[str] name: The name which should be used for this Spring Cloud Build Deployment. Changing this forces a new Spring Cloud Build Deployment to be created.
        :param pulumi.Input['SpringCloudBuildDeploymentQuotaArgs'] quota: A `quota` block as defined below.
        :param pulumi.Input[str] spring_cloud_app_id: The ID of the Spring Cloud Service. Changing this forces a new Spring Cloud Build Deployment to be created.
        """
        _SpringCloudBuildDeploymentState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            addon_json=addon_json,
            build_result_id=build_result_id,
            environment_variables=environment_variables,
            instance_count=instance_count,
            name=name,
            quota=quota,
            spring_cloud_app_id=spring_cloud_app_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             addon_json: Optional[pulumi.Input[str]] = None,
             build_result_id: Optional[pulumi.Input[str]] = None,
             environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             instance_count: Optional[pulumi.Input[int]] = None,
             name: Optional[pulumi.Input[str]] = None,
             quota: Optional[pulumi.Input['SpringCloudBuildDeploymentQuotaArgs']] = None,
             spring_cloud_app_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'addonJson' in kwargs:
            addon_json = kwargs['addonJson']
        if 'buildResultId' in kwargs:
            build_result_id = kwargs['buildResultId']
        if 'environmentVariables' in kwargs:
            environment_variables = kwargs['environmentVariables']
        if 'instanceCount' in kwargs:
            instance_count = kwargs['instanceCount']
        if 'springCloudAppId' in kwargs:
            spring_cloud_app_id = kwargs['springCloudAppId']

        if addon_json is not None:
            _setter("addon_json", addon_json)
        if build_result_id is not None:
            _setter("build_result_id", build_result_id)
        if environment_variables is not None:
            _setter("environment_variables", environment_variables)
        if instance_count is not None:
            _setter("instance_count", instance_count)
        if name is not None:
            _setter("name", name)
        if quota is not None:
            _setter("quota", quota)
        if spring_cloud_app_id is not None:
            _setter("spring_cloud_app_id", spring_cloud_app_id)

    @property
    @pulumi.getter(name="addonJson")
    def addon_json(self) -> Optional[pulumi.Input[str]]:
        """
        A JSON object that contains the addon configurations of the Spring Cloud Build Deployment.
        """
        return pulumi.get(self, "addon_json")

    @addon_json.setter
    def addon_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "addon_json", value)

    @property
    @pulumi.getter(name="buildResultId")
    def build_result_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Spring Cloud Build Result.
        """
        return pulumi.get(self, "build_result_id")

    @build_result_id.setter
    def build_result_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "build_result_id", value)

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Specifies the environment variables of the Spring Cloud Deployment as a map of key-value pairs.
        """
        return pulumi.get(self, "environment_variables")

    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "environment_variables", value)

    @property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the required instance count of the Spring Cloud Deployment. Possible Values are between `1` and `500`. Defaults to `1` if not specified.
        """
        return pulumi.get(self, "instance_count")

    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "instance_count", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Spring Cloud Build Deployment. Changing this forces a new Spring Cloud Build Deployment to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def quota(self) -> Optional[pulumi.Input['SpringCloudBuildDeploymentQuotaArgs']]:
        """
        A `quota` block as defined below.
        """
        return pulumi.get(self, "quota")

    @quota.setter
    def quota(self, value: Optional[pulumi.Input['SpringCloudBuildDeploymentQuotaArgs']]):
        pulumi.set(self, "quota", value)

    @property
    @pulumi.getter(name="springCloudAppId")
    def spring_cloud_app_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Spring Cloud Service. Changing this forces a new Spring Cloud Build Deployment to be created.
        """
        return pulumi.get(self, "spring_cloud_app_id")

    @spring_cloud_app_id.setter
    def spring_cloud_app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "spring_cloud_app_id", value)


class SpringCloudBuildDeployment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 addon_json: Optional[pulumi.Input[str]] = None,
                 build_result_id: Optional[pulumi.Input[str]] = None,
                 environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 instance_count: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quota: Optional[pulumi.Input[pulumi.InputType['SpringCloudBuildDeploymentQuotaArgs']]] = None,
                 spring_cloud_app_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Spring Cloud Build Deployment.

        > **NOTE:** This resource is applicable only for Spring Cloud Service with enterprise tier.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_spring_cloud_service = azure.appplatform.SpringCloudService("exampleSpringCloudService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="E0")
        example_spring_cloud_app = azure.appplatform.SpringCloudApp("exampleSpringCloudApp",
            resource_group_name=example_spring_cloud_service.resource_group_name,
            service_name=example_spring_cloud_service.name)
        example_spring_cloud_build_deployment = azure.appplatform.SpringCloudBuildDeployment("exampleSpringCloudBuildDeployment",
            spring_cloud_app_id=example_spring_cloud_app.id,
            build_result_id="<default>",
            instance_count=2,
            environment_variables={
                "Foo": "Bar",
                "Env": "Staging",
            },
            quota=azure.appplatform.SpringCloudBuildDeploymentQuotaArgs(
                cpu="2",
                memory="4Gi",
            ))
        ```

        ## Import

        Spring Cloud Build Deployments can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appplatform/springCloudBuildDeployment:SpringCloudBuildDeployment example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resGroup1/providers/Microsoft.AppPlatform/spring/spring1/apps/app1/deployments/deploy1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] addon_json: A JSON object that contains the addon configurations of the Spring Cloud Build Deployment.
        :param pulumi.Input[str] build_result_id: The ID of the Spring Cloud Build Result.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] environment_variables: Specifies the environment variables of the Spring Cloud Deployment as a map of key-value pairs.
        :param pulumi.Input[int] instance_count: Specifies the required instance count of the Spring Cloud Deployment. Possible Values are between `1` and `500`. Defaults to `1` if not specified.
        :param pulumi.Input[str] name: The name which should be used for this Spring Cloud Build Deployment. Changing this forces a new Spring Cloud Build Deployment to be created.
        :param pulumi.Input[pulumi.InputType['SpringCloudBuildDeploymentQuotaArgs']] quota: A `quota` block as defined below.
        :param pulumi.Input[str] spring_cloud_app_id: The ID of the Spring Cloud Service. Changing this forces a new Spring Cloud Build Deployment to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SpringCloudBuildDeploymentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Spring Cloud Build Deployment.

        > **NOTE:** This resource is applicable only for Spring Cloud Service with enterprise tier.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_spring_cloud_service = azure.appplatform.SpringCloudService("exampleSpringCloudService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="E0")
        example_spring_cloud_app = azure.appplatform.SpringCloudApp("exampleSpringCloudApp",
            resource_group_name=example_spring_cloud_service.resource_group_name,
            service_name=example_spring_cloud_service.name)
        example_spring_cloud_build_deployment = azure.appplatform.SpringCloudBuildDeployment("exampleSpringCloudBuildDeployment",
            spring_cloud_app_id=example_spring_cloud_app.id,
            build_result_id="<default>",
            instance_count=2,
            environment_variables={
                "Foo": "Bar",
                "Env": "Staging",
            },
            quota=azure.appplatform.SpringCloudBuildDeploymentQuotaArgs(
                cpu="2",
                memory="4Gi",
            ))
        ```

        ## Import

        Spring Cloud Build Deployments can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appplatform/springCloudBuildDeployment:SpringCloudBuildDeployment example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resGroup1/providers/Microsoft.AppPlatform/spring/spring1/apps/app1/deployments/deploy1
        ```

        :param str resource_name: The name of the resource.
        :param SpringCloudBuildDeploymentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SpringCloudBuildDeploymentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SpringCloudBuildDeploymentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 addon_json: Optional[pulumi.Input[str]] = None,
                 build_result_id: Optional[pulumi.Input[str]] = None,
                 environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 instance_count: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quota: Optional[pulumi.Input[pulumi.InputType['SpringCloudBuildDeploymentQuotaArgs']]] = None,
                 spring_cloud_app_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SpringCloudBuildDeploymentArgs.__new__(SpringCloudBuildDeploymentArgs)

            __props__.__dict__["addon_json"] = addon_json
            if build_result_id is None and not opts.urn:
                raise TypeError("Missing required property 'build_result_id'")
            __props__.__dict__["build_result_id"] = build_result_id
            __props__.__dict__["environment_variables"] = environment_variables
            __props__.__dict__["instance_count"] = instance_count
            __props__.__dict__["name"] = name
            if quota is not None and not isinstance(quota, SpringCloudBuildDeploymentQuotaArgs):
                quota = quota or {}
                def _setter(key, value):
                    quota[key] = value
                SpringCloudBuildDeploymentQuotaArgs._configure(_setter, **quota)
            __props__.__dict__["quota"] = quota
            if spring_cloud_app_id is None and not opts.urn:
                raise TypeError("Missing required property 'spring_cloud_app_id'")
            __props__.__dict__["spring_cloud_app_id"] = spring_cloud_app_id
        super(SpringCloudBuildDeployment, __self__).__init__(
            'azure:appplatform/springCloudBuildDeployment:SpringCloudBuildDeployment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            addon_json: Optional[pulumi.Input[str]] = None,
            build_result_id: Optional[pulumi.Input[str]] = None,
            environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            instance_count: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            quota: Optional[pulumi.Input[pulumi.InputType['SpringCloudBuildDeploymentQuotaArgs']]] = None,
            spring_cloud_app_id: Optional[pulumi.Input[str]] = None) -> 'SpringCloudBuildDeployment':
        """
        Get an existing SpringCloudBuildDeployment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] addon_json: A JSON object that contains the addon configurations of the Spring Cloud Build Deployment.
        :param pulumi.Input[str] build_result_id: The ID of the Spring Cloud Build Result.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] environment_variables: Specifies the environment variables of the Spring Cloud Deployment as a map of key-value pairs.
        :param pulumi.Input[int] instance_count: Specifies the required instance count of the Spring Cloud Deployment. Possible Values are between `1` and `500`. Defaults to `1` if not specified.
        :param pulumi.Input[str] name: The name which should be used for this Spring Cloud Build Deployment. Changing this forces a new Spring Cloud Build Deployment to be created.
        :param pulumi.Input[pulumi.InputType['SpringCloudBuildDeploymentQuotaArgs']] quota: A `quota` block as defined below.
        :param pulumi.Input[str] spring_cloud_app_id: The ID of the Spring Cloud Service. Changing this forces a new Spring Cloud Build Deployment to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SpringCloudBuildDeploymentState.__new__(_SpringCloudBuildDeploymentState)

        __props__.__dict__["addon_json"] = addon_json
        __props__.__dict__["build_result_id"] = build_result_id
        __props__.__dict__["environment_variables"] = environment_variables
        __props__.__dict__["instance_count"] = instance_count
        __props__.__dict__["name"] = name
        __props__.__dict__["quota"] = quota
        __props__.__dict__["spring_cloud_app_id"] = spring_cloud_app_id
        return SpringCloudBuildDeployment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addonJson")
    def addon_json(self) -> pulumi.Output[str]:
        """
        A JSON object that contains the addon configurations of the Spring Cloud Build Deployment.
        """
        return pulumi.get(self, "addon_json")

    @property
    @pulumi.getter(name="buildResultId")
    def build_result_id(self) -> pulumi.Output[str]:
        """
        The ID of the Spring Cloud Build Result.
        """
        return pulumi.get(self, "build_result_id")

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Specifies the environment variables of the Spring Cloud Deployment as a map of key-value pairs.
        """
        return pulumi.get(self, "environment_variables")

    @property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> pulumi.Output[Optional[int]]:
        """
        Specifies the required instance count of the Spring Cloud Deployment. Possible Values are between `1` and `500`. Defaults to `1` if not specified.
        """
        return pulumi.get(self, "instance_count")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Spring Cloud Build Deployment. Changing this forces a new Spring Cloud Build Deployment to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def quota(self) -> pulumi.Output['outputs.SpringCloudBuildDeploymentQuota']:
        """
        A `quota` block as defined below.
        """
        return pulumi.get(self, "quota")

    @property
    @pulumi.getter(name="springCloudAppId")
    def spring_cloud_app_id(self) -> pulumi.Output[str]:
        """
        The ID of the Spring Cloud Service. Changing this forces a new Spring Cloud Build Deployment to be created.
        """
        return pulumi.get(self, "spring_cloud_app_id")


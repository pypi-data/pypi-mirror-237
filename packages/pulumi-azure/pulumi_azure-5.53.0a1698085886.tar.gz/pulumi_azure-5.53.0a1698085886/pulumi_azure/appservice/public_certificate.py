# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['PublicCertificateArgs', 'PublicCertificate']

@pulumi.input_type
class PublicCertificateArgs:
    def __init__(__self__, *,
                 app_service_name: pulumi.Input[str],
                 blob: pulumi.Input[str],
                 certificate_location: pulumi.Input[str],
                 certificate_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a PublicCertificate resource.
        :param pulumi.Input[str] app_service_name: The name of the App Service. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] blob: The base64-encoded contents of the certificate. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] certificate_location: The location of the certificate. Possible values are `CurrentUserMy`, `LocalMachineMy` and `Unknown`. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] certificate_name: The name of the public certificate. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the App Service Public Certificate should exist. Changing this forces a new App Service Public Certificate to be created.
        """
        PublicCertificateArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            app_service_name=app_service_name,
            blob=blob,
            certificate_location=certificate_location,
            certificate_name=certificate_name,
            resource_group_name=resource_group_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             app_service_name: pulumi.Input[str],
             blob: pulumi.Input[str],
             certificate_location: pulumi.Input[str],
             certificate_name: pulumi.Input[str],
             resource_group_name: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'appServiceName' in kwargs:
            app_service_name = kwargs['appServiceName']
        if 'certificateLocation' in kwargs:
            certificate_location = kwargs['certificateLocation']
        if 'certificateName' in kwargs:
            certificate_name = kwargs['certificateName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']

        _setter("app_service_name", app_service_name)
        _setter("blob", blob)
        _setter("certificate_location", certificate_location)
        _setter("certificate_name", certificate_name)
        _setter("resource_group_name", resource_group_name)

    @property
    @pulumi.getter(name="appServiceName")
    def app_service_name(self) -> pulumi.Input[str]:
        """
        The name of the App Service. Changing this forces a new App Service Public Certificate to be created.
        """
        return pulumi.get(self, "app_service_name")

    @app_service_name.setter
    def app_service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_service_name", value)

    @property
    @pulumi.getter
    def blob(self) -> pulumi.Input[str]:
        """
        The base64-encoded contents of the certificate. Changing this forces a new App Service Public Certificate to be created.
        """
        return pulumi.get(self, "blob")

    @blob.setter
    def blob(self, value: pulumi.Input[str]):
        pulumi.set(self, "blob", value)

    @property
    @pulumi.getter(name="certificateLocation")
    def certificate_location(self) -> pulumi.Input[str]:
        """
        The location of the certificate. Possible values are `CurrentUserMy`, `LocalMachineMy` and `Unknown`. Changing this forces a new App Service Public Certificate to be created.
        """
        return pulumi.get(self, "certificate_location")

    @certificate_location.setter
    def certificate_location(self, value: pulumi.Input[str]):
        pulumi.set(self, "certificate_location", value)

    @property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> pulumi.Input[str]:
        """
        The name of the public certificate. Changing this forces a new App Service Public Certificate to be created.
        """
        return pulumi.get(self, "certificate_name")

    @certificate_name.setter
    def certificate_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "certificate_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group where the App Service Public Certificate should exist. Changing this forces a new App Service Public Certificate to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)


@pulumi.input_type
class _PublicCertificateState:
    def __init__(__self__, *,
                 app_service_name: Optional[pulumi.Input[str]] = None,
                 blob: Optional[pulumi.Input[str]] = None,
                 certificate_location: Optional[pulumi.Input[str]] = None,
                 certificate_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 thumbprint: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PublicCertificate resources.
        :param pulumi.Input[str] app_service_name: The name of the App Service. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] blob: The base64-encoded contents of the certificate. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] certificate_location: The location of the certificate. Possible values are `CurrentUserMy`, `LocalMachineMy` and `Unknown`. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] certificate_name: The name of the public certificate. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the App Service Public Certificate should exist. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] thumbprint: The thumbprint of the public certificate.
        """
        _PublicCertificateState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            app_service_name=app_service_name,
            blob=blob,
            certificate_location=certificate_location,
            certificate_name=certificate_name,
            resource_group_name=resource_group_name,
            thumbprint=thumbprint,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             app_service_name: Optional[pulumi.Input[str]] = None,
             blob: Optional[pulumi.Input[str]] = None,
             certificate_location: Optional[pulumi.Input[str]] = None,
             certificate_name: Optional[pulumi.Input[str]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             thumbprint: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'appServiceName' in kwargs:
            app_service_name = kwargs['appServiceName']
        if 'certificateLocation' in kwargs:
            certificate_location = kwargs['certificateLocation']
        if 'certificateName' in kwargs:
            certificate_name = kwargs['certificateName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']

        if app_service_name is not None:
            _setter("app_service_name", app_service_name)
        if blob is not None:
            _setter("blob", blob)
        if certificate_location is not None:
            _setter("certificate_location", certificate_location)
        if certificate_name is not None:
            _setter("certificate_name", certificate_name)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if thumbprint is not None:
            _setter("thumbprint", thumbprint)

    @property
    @pulumi.getter(name="appServiceName")
    def app_service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the App Service. Changing this forces a new App Service Public Certificate to be created.
        """
        return pulumi.get(self, "app_service_name")

    @app_service_name.setter
    def app_service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_service_name", value)

    @property
    @pulumi.getter
    def blob(self) -> Optional[pulumi.Input[str]]:
        """
        The base64-encoded contents of the certificate. Changing this forces a new App Service Public Certificate to be created.
        """
        return pulumi.get(self, "blob")

    @blob.setter
    def blob(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "blob", value)

    @property
    @pulumi.getter(name="certificateLocation")
    def certificate_location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the certificate. Possible values are `CurrentUserMy`, `LocalMachineMy` and `Unknown`. Changing this forces a new App Service Public Certificate to be created.
        """
        return pulumi.get(self, "certificate_location")

    @certificate_location.setter
    def certificate_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_location", value)

    @property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the public certificate. Changing this forces a new App Service Public Certificate to be created.
        """
        return pulumi.get(self, "certificate_name")

    @certificate_name.setter
    def certificate_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group where the App Service Public Certificate should exist. Changing this forces a new App Service Public Certificate to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def thumbprint(self) -> Optional[pulumi.Input[str]]:
        """
        The thumbprint of the public certificate.
        """
        return pulumi.get(self, "thumbprint")

    @thumbprint.setter
    def thumbprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "thumbprint", value)


class PublicCertificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_service_name: Optional[pulumi.Input[str]] = None,
                 blob: Optional[pulumi.Input[str]] = None,
                 certificate_location: Optional[pulumi.Input[str]] = None,
                 certificate_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an App Service Public Certificate.

        ## Example Usage

        ```python
        import pulumi
        import base64
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_plan = azure.appservice.Plan("examplePlan",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku=azure.appservice.PlanSkuArgs(
                tier="Standard",
                size="S1",
            ))
        example_app_service = azure.appservice.AppService("exampleAppService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            app_service_plan_id=example_plan.id)
        example_public_certificate = azure.appservice.PublicCertificate("examplePublicCertificate",
            resource_group_name=example_resource_group.name,
            app_service_name=example_app_service.name,
            certificate_name="example-public-certificate",
            certificate_location="Unknown",
            blob=(lambda path: base64.b64encode(open(path).read().encode()).decode())("app_service_public_certificate.cer"))
        ```

        ## Import

        App Service Public Certificates can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appservice/publicCertificate:PublicCertificate example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Web/sites/site1/publicCertificates/publicCertificate1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_service_name: The name of the App Service. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] blob: The base64-encoded contents of the certificate. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] certificate_location: The location of the certificate. Possible values are `CurrentUserMy`, `LocalMachineMy` and `Unknown`. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] certificate_name: The name of the public certificate. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the App Service Public Certificate should exist. Changing this forces a new App Service Public Certificate to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PublicCertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an App Service Public Certificate.

        ## Example Usage

        ```python
        import pulumi
        import base64
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_plan = azure.appservice.Plan("examplePlan",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku=azure.appservice.PlanSkuArgs(
                tier="Standard",
                size="S1",
            ))
        example_app_service = azure.appservice.AppService("exampleAppService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            app_service_plan_id=example_plan.id)
        example_public_certificate = azure.appservice.PublicCertificate("examplePublicCertificate",
            resource_group_name=example_resource_group.name,
            app_service_name=example_app_service.name,
            certificate_name="example-public-certificate",
            certificate_location="Unknown",
            blob=(lambda path: base64.b64encode(open(path).read().encode()).decode())("app_service_public_certificate.cer"))
        ```

        ## Import

        App Service Public Certificates can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appservice/publicCertificate:PublicCertificate example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Web/sites/site1/publicCertificates/publicCertificate1
        ```

        :param str resource_name: The name of the resource.
        :param PublicCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PublicCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            PublicCertificateArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_service_name: Optional[pulumi.Input[str]] = None,
                 blob: Optional[pulumi.Input[str]] = None,
                 certificate_location: Optional[pulumi.Input[str]] = None,
                 certificate_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PublicCertificateArgs.__new__(PublicCertificateArgs)

            if app_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'app_service_name'")
            __props__.__dict__["app_service_name"] = app_service_name
            if blob is None and not opts.urn:
                raise TypeError("Missing required property 'blob'")
            __props__.__dict__["blob"] = blob
            if certificate_location is None and not opts.urn:
                raise TypeError("Missing required property 'certificate_location'")
            __props__.__dict__["certificate_location"] = certificate_location
            if certificate_name is None and not opts.urn:
                raise TypeError("Missing required property 'certificate_name'")
            __props__.__dict__["certificate_name"] = certificate_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["thumbprint"] = None
        super(PublicCertificate, __self__).__init__(
            'azure:appservice/publicCertificate:PublicCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_service_name: Optional[pulumi.Input[str]] = None,
            blob: Optional[pulumi.Input[str]] = None,
            certificate_location: Optional[pulumi.Input[str]] = None,
            certificate_name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            thumbprint: Optional[pulumi.Input[str]] = None) -> 'PublicCertificate':
        """
        Get an existing PublicCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_service_name: The name of the App Service. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] blob: The base64-encoded contents of the certificate. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] certificate_location: The location of the certificate. Possible values are `CurrentUserMy`, `LocalMachineMy` and `Unknown`. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] certificate_name: The name of the public certificate. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the App Service Public Certificate should exist. Changing this forces a new App Service Public Certificate to be created.
        :param pulumi.Input[str] thumbprint: The thumbprint of the public certificate.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PublicCertificateState.__new__(_PublicCertificateState)

        __props__.__dict__["app_service_name"] = app_service_name
        __props__.__dict__["blob"] = blob
        __props__.__dict__["certificate_location"] = certificate_location
        __props__.__dict__["certificate_name"] = certificate_name
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["thumbprint"] = thumbprint
        return PublicCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appServiceName")
    def app_service_name(self) -> pulumi.Output[str]:
        """
        The name of the App Service. Changing this forces a new App Service Public Certificate to be created.
        """
        return pulumi.get(self, "app_service_name")

    @property
    @pulumi.getter
    def blob(self) -> pulumi.Output[str]:
        """
        The base64-encoded contents of the certificate. Changing this forces a new App Service Public Certificate to be created.
        """
        return pulumi.get(self, "blob")

    @property
    @pulumi.getter(name="certificateLocation")
    def certificate_location(self) -> pulumi.Output[str]:
        """
        The location of the certificate. Possible values are `CurrentUserMy`, `LocalMachineMy` and `Unknown`. Changing this forces a new App Service Public Certificate to be created.
        """
        return pulumi.get(self, "certificate_location")

    @property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> pulumi.Output[str]:
        """
        The name of the public certificate. Changing this forces a new App Service Public Certificate to be created.
        """
        return pulumi.get(self, "certificate_name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the App Service Public Certificate should exist. Changing this forces a new App Service Public Certificate to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def thumbprint(self) -> pulumi.Output[str]:
        """
        The thumbprint of the public certificate.
        """
        return pulumi.get(self, "thumbprint")


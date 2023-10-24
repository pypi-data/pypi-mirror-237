# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['IdentityProviderAadb2cArgs', 'IdentityProviderAadb2c']

@pulumi.input_type
class IdentityProviderAadb2cArgs:
    def __init__(__self__, *,
                 allowed_tenant: pulumi.Input[str],
                 api_management_name: pulumi.Input[str],
                 authority: pulumi.Input[str],
                 client_id: pulumi.Input[str],
                 client_secret: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 signin_policy: pulumi.Input[str],
                 signin_tenant: pulumi.Input[str],
                 signup_policy: pulumi.Input[str],
                 password_reset_policy: Optional[pulumi.Input[str]] = None,
                 profile_editing_policy: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IdentityProviderAadb2c resource.
        :param pulumi.Input[str] allowed_tenant: The allowed AAD tenant, usually your B2C tenant domain.
        :param pulumi.Input[str] api_management_name: The Name of the API Management Service where this AAD Identity Provider should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] authority: OpenID Connect discovery endpoint hostname, usually your b2clogin.com domain.
        :param pulumi.Input[str] client_id: Client ID of the Application in your B2C tenant.
        :param pulumi.Input[str] client_secret: Client secret of the Application in your B2C tenant.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] signin_policy: Signin Policy Name.
        :param pulumi.Input[str] signin_tenant: The tenant to use instead of Common when logging into Active Directory, usually your B2C tenant domain.
        :param pulumi.Input[str] signup_policy: Signup Policy Name.
        :param pulumi.Input[str] password_reset_policy: Password reset Policy Name.
        :param pulumi.Input[str] profile_editing_policy: Profile editing Policy Name.
        """
        IdentityProviderAadb2cArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            allowed_tenant=allowed_tenant,
            api_management_name=api_management_name,
            authority=authority,
            client_id=client_id,
            client_secret=client_secret,
            resource_group_name=resource_group_name,
            signin_policy=signin_policy,
            signin_tenant=signin_tenant,
            signup_policy=signup_policy,
            password_reset_policy=password_reset_policy,
            profile_editing_policy=profile_editing_policy,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             allowed_tenant: pulumi.Input[str],
             api_management_name: pulumi.Input[str],
             authority: pulumi.Input[str],
             client_id: pulumi.Input[str],
             client_secret: pulumi.Input[str],
             resource_group_name: pulumi.Input[str],
             signin_policy: pulumi.Input[str],
             signin_tenant: pulumi.Input[str],
             signup_policy: pulumi.Input[str],
             password_reset_policy: Optional[pulumi.Input[str]] = None,
             profile_editing_policy: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'allowedTenant' in kwargs:
            allowed_tenant = kwargs['allowedTenant']
        if 'apiManagementName' in kwargs:
            api_management_name = kwargs['apiManagementName']
        if 'clientId' in kwargs:
            client_id = kwargs['clientId']
        if 'clientSecret' in kwargs:
            client_secret = kwargs['clientSecret']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'signinPolicy' in kwargs:
            signin_policy = kwargs['signinPolicy']
        if 'signinTenant' in kwargs:
            signin_tenant = kwargs['signinTenant']
        if 'signupPolicy' in kwargs:
            signup_policy = kwargs['signupPolicy']
        if 'passwordResetPolicy' in kwargs:
            password_reset_policy = kwargs['passwordResetPolicy']
        if 'profileEditingPolicy' in kwargs:
            profile_editing_policy = kwargs['profileEditingPolicy']

        _setter("allowed_tenant", allowed_tenant)
        _setter("api_management_name", api_management_name)
        _setter("authority", authority)
        _setter("client_id", client_id)
        _setter("client_secret", client_secret)
        _setter("resource_group_name", resource_group_name)
        _setter("signin_policy", signin_policy)
        _setter("signin_tenant", signin_tenant)
        _setter("signup_policy", signup_policy)
        if password_reset_policy is not None:
            _setter("password_reset_policy", password_reset_policy)
        if profile_editing_policy is not None:
            _setter("profile_editing_policy", profile_editing_policy)

    @property
    @pulumi.getter(name="allowedTenant")
    def allowed_tenant(self) -> pulumi.Input[str]:
        """
        The allowed AAD tenant, usually your B2C tenant domain.
        """
        return pulumi.get(self, "allowed_tenant")

    @allowed_tenant.setter
    def allowed_tenant(self, value: pulumi.Input[str]):
        pulumi.set(self, "allowed_tenant", value)

    @property
    @pulumi.getter(name="apiManagementName")
    def api_management_name(self) -> pulumi.Input[str]:
        """
        The Name of the API Management Service where this AAD Identity Provider should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "api_management_name")

    @api_management_name.setter
    def api_management_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_management_name", value)

    @property
    @pulumi.getter
    def authority(self) -> pulumi.Input[str]:
        """
        OpenID Connect discovery endpoint hostname, usually your b2clogin.com domain.
        """
        return pulumi.get(self, "authority")

    @authority.setter
    def authority(self, value: pulumi.Input[str]):
        pulumi.set(self, "authority", value)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[str]:
        """
        Client ID of the Application in your B2C tenant.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[str]:
        """
        Client secret of the Application in your B2C tenant.
        """
        return pulumi.get(self, "client_secret")

    @client_secret.setter
    def client_secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_secret", value)

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
    @pulumi.getter(name="signinPolicy")
    def signin_policy(self) -> pulumi.Input[str]:
        """
        Signin Policy Name.
        """
        return pulumi.get(self, "signin_policy")

    @signin_policy.setter
    def signin_policy(self, value: pulumi.Input[str]):
        pulumi.set(self, "signin_policy", value)

    @property
    @pulumi.getter(name="signinTenant")
    def signin_tenant(self) -> pulumi.Input[str]:
        """
        The tenant to use instead of Common when logging into Active Directory, usually your B2C tenant domain.
        """
        return pulumi.get(self, "signin_tenant")

    @signin_tenant.setter
    def signin_tenant(self, value: pulumi.Input[str]):
        pulumi.set(self, "signin_tenant", value)

    @property
    @pulumi.getter(name="signupPolicy")
    def signup_policy(self) -> pulumi.Input[str]:
        """
        Signup Policy Name.
        """
        return pulumi.get(self, "signup_policy")

    @signup_policy.setter
    def signup_policy(self, value: pulumi.Input[str]):
        pulumi.set(self, "signup_policy", value)

    @property
    @pulumi.getter(name="passwordResetPolicy")
    def password_reset_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Password reset Policy Name.
        """
        return pulumi.get(self, "password_reset_policy")

    @password_reset_policy.setter
    def password_reset_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password_reset_policy", value)

    @property
    @pulumi.getter(name="profileEditingPolicy")
    def profile_editing_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Profile editing Policy Name.
        """
        return pulumi.get(self, "profile_editing_policy")

    @profile_editing_policy.setter
    def profile_editing_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "profile_editing_policy", value)


@pulumi.input_type
class _IdentityProviderAadb2cState:
    def __init__(__self__, *,
                 allowed_tenant: Optional[pulumi.Input[str]] = None,
                 api_management_name: Optional[pulumi.Input[str]] = None,
                 authority: Optional[pulumi.Input[str]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 password_reset_policy: Optional[pulumi.Input[str]] = None,
                 profile_editing_policy: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 signin_policy: Optional[pulumi.Input[str]] = None,
                 signin_tenant: Optional[pulumi.Input[str]] = None,
                 signup_policy: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IdentityProviderAadb2c resources.
        :param pulumi.Input[str] allowed_tenant: The allowed AAD tenant, usually your B2C tenant domain.
        :param pulumi.Input[str] api_management_name: The Name of the API Management Service where this AAD Identity Provider should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] authority: OpenID Connect discovery endpoint hostname, usually your b2clogin.com domain.
        :param pulumi.Input[str] client_id: Client ID of the Application in your B2C tenant.
        :param pulumi.Input[str] client_secret: Client secret of the Application in your B2C tenant.
        :param pulumi.Input[str] password_reset_policy: Password reset Policy Name.
        :param pulumi.Input[str] profile_editing_policy: Profile editing Policy Name.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] signin_policy: Signin Policy Name.
        :param pulumi.Input[str] signin_tenant: The tenant to use instead of Common when logging into Active Directory, usually your B2C tenant domain.
        :param pulumi.Input[str] signup_policy: Signup Policy Name.
        """
        _IdentityProviderAadb2cState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            allowed_tenant=allowed_tenant,
            api_management_name=api_management_name,
            authority=authority,
            client_id=client_id,
            client_secret=client_secret,
            password_reset_policy=password_reset_policy,
            profile_editing_policy=profile_editing_policy,
            resource_group_name=resource_group_name,
            signin_policy=signin_policy,
            signin_tenant=signin_tenant,
            signup_policy=signup_policy,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             allowed_tenant: Optional[pulumi.Input[str]] = None,
             api_management_name: Optional[pulumi.Input[str]] = None,
             authority: Optional[pulumi.Input[str]] = None,
             client_id: Optional[pulumi.Input[str]] = None,
             client_secret: Optional[pulumi.Input[str]] = None,
             password_reset_policy: Optional[pulumi.Input[str]] = None,
             profile_editing_policy: Optional[pulumi.Input[str]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             signin_policy: Optional[pulumi.Input[str]] = None,
             signin_tenant: Optional[pulumi.Input[str]] = None,
             signup_policy: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'allowedTenant' in kwargs:
            allowed_tenant = kwargs['allowedTenant']
        if 'apiManagementName' in kwargs:
            api_management_name = kwargs['apiManagementName']
        if 'clientId' in kwargs:
            client_id = kwargs['clientId']
        if 'clientSecret' in kwargs:
            client_secret = kwargs['clientSecret']
        if 'passwordResetPolicy' in kwargs:
            password_reset_policy = kwargs['passwordResetPolicy']
        if 'profileEditingPolicy' in kwargs:
            profile_editing_policy = kwargs['profileEditingPolicy']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'signinPolicy' in kwargs:
            signin_policy = kwargs['signinPolicy']
        if 'signinTenant' in kwargs:
            signin_tenant = kwargs['signinTenant']
        if 'signupPolicy' in kwargs:
            signup_policy = kwargs['signupPolicy']

        if allowed_tenant is not None:
            _setter("allowed_tenant", allowed_tenant)
        if api_management_name is not None:
            _setter("api_management_name", api_management_name)
        if authority is not None:
            _setter("authority", authority)
        if client_id is not None:
            _setter("client_id", client_id)
        if client_secret is not None:
            _setter("client_secret", client_secret)
        if password_reset_policy is not None:
            _setter("password_reset_policy", password_reset_policy)
        if profile_editing_policy is not None:
            _setter("profile_editing_policy", profile_editing_policy)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if signin_policy is not None:
            _setter("signin_policy", signin_policy)
        if signin_tenant is not None:
            _setter("signin_tenant", signin_tenant)
        if signup_policy is not None:
            _setter("signup_policy", signup_policy)

    @property
    @pulumi.getter(name="allowedTenant")
    def allowed_tenant(self) -> Optional[pulumi.Input[str]]:
        """
        The allowed AAD tenant, usually your B2C tenant domain.
        """
        return pulumi.get(self, "allowed_tenant")

    @allowed_tenant.setter
    def allowed_tenant(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allowed_tenant", value)

    @property
    @pulumi.getter(name="apiManagementName")
    def api_management_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Name of the API Management Service where this AAD Identity Provider should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "api_management_name")

    @api_management_name.setter
    def api_management_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_management_name", value)

    @property
    @pulumi.getter
    def authority(self) -> Optional[pulumi.Input[str]]:
        """
        OpenID Connect discovery endpoint hostname, usually your b2clogin.com domain.
        """
        return pulumi.get(self, "authority")

    @authority.setter
    def authority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authority", value)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[str]]:
        """
        Client ID of the Application in your B2C tenant.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[str]]:
        """
        Client secret of the Application in your B2C tenant.
        """
        return pulumi.get(self, "client_secret")

    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_secret", value)

    @property
    @pulumi.getter(name="passwordResetPolicy")
    def password_reset_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Password reset Policy Name.
        """
        return pulumi.get(self, "password_reset_policy")

    @password_reset_policy.setter
    def password_reset_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password_reset_policy", value)

    @property
    @pulumi.getter(name="profileEditingPolicy")
    def profile_editing_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Profile editing Policy Name.
        """
        return pulumi.get(self, "profile_editing_policy")

    @profile_editing_policy.setter
    def profile_editing_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "profile_editing_policy", value)

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
    @pulumi.getter(name="signinPolicy")
    def signin_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Signin Policy Name.
        """
        return pulumi.get(self, "signin_policy")

    @signin_policy.setter
    def signin_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "signin_policy", value)

    @property
    @pulumi.getter(name="signinTenant")
    def signin_tenant(self) -> Optional[pulumi.Input[str]]:
        """
        The tenant to use instead of Common when logging into Active Directory, usually your B2C tenant domain.
        """
        return pulumi.get(self, "signin_tenant")

    @signin_tenant.setter
    def signin_tenant(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "signin_tenant", value)

    @property
    @pulumi.getter(name="signupPolicy")
    def signup_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Signup Policy Name.
        """
        return pulumi.get(self, "signup_policy")

    @signup_policy.setter
    def signup_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "signup_policy", value)


class IdentityProviderAadb2c(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_tenant: Optional[pulumi.Input[str]] = None,
                 api_management_name: Optional[pulumi.Input[str]] = None,
                 authority: Optional[pulumi.Input[str]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 password_reset_policy: Optional[pulumi.Input[str]] = None,
                 profile_editing_policy: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 signin_policy: Optional[pulumi.Input[str]] = None,
                 signin_tenant: Optional[pulumi.Input[str]] = None,
                 signup_policy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an API Management Azure AD B2C Identity Provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_azuread as azuread

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_service = azure.apimanagement.Service("exampleService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            publisher_name="My Company",
            publisher_email="company@terraform.io",
            sku_name="Developer_1")
        example_application = azuread.Application("exampleApplication", display_name="acctestam-example")
        example_application_password = azuread.ApplicationPassword("exampleApplicationPassword",
            application_object_id=example_application.object_id,
            end_date_relative="36h")
        example_identity_provider_aadb2c = azure.apimanagement.IdentityProviderAadb2c("exampleIdentityProviderAadb2c",
            resource_group_name=example_resource_group.name,
            api_management_name=example_service.name,
            client_id=example_application.application_id,
            client_secret="P@55w0rD!",
            allowed_tenant="myb2ctenant.onmicrosoft.com",
            signin_tenant="myb2ctenant.onmicrosoft.com",
            authority="myb2ctenant.b2clogin.com",
            signin_policy="B2C_1_Login",
            signup_policy="B2C_1_Signup",
            opts=pulumi.ResourceOptions(depends_on=[example_application_password]))
        ```

        ## Import

        API Management Azure AD B2C Identity Providers can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:apimanagement/identityProviderAadb2c:IdentityProviderAadb2c example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.ApiManagement/service/service1/identityProviders/aadB2C
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] allowed_tenant: The allowed AAD tenant, usually your B2C tenant domain.
        :param pulumi.Input[str] api_management_name: The Name of the API Management Service where this AAD Identity Provider should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] authority: OpenID Connect discovery endpoint hostname, usually your b2clogin.com domain.
        :param pulumi.Input[str] client_id: Client ID of the Application in your B2C tenant.
        :param pulumi.Input[str] client_secret: Client secret of the Application in your B2C tenant.
        :param pulumi.Input[str] password_reset_policy: Password reset Policy Name.
        :param pulumi.Input[str] profile_editing_policy: Profile editing Policy Name.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] signin_policy: Signin Policy Name.
        :param pulumi.Input[str] signin_tenant: The tenant to use instead of Common when logging into Active Directory, usually your B2C tenant domain.
        :param pulumi.Input[str] signup_policy: Signup Policy Name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IdentityProviderAadb2cArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an API Management Azure AD B2C Identity Provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_azuread as azuread

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_service = azure.apimanagement.Service("exampleService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            publisher_name="My Company",
            publisher_email="company@terraform.io",
            sku_name="Developer_1")
        example_application = azuread.Application("exampleApplication", display_name="acctestam-example")
        example_application_password = azuread.ApplicationPassword("exampleApplicationPassword",
            application_object_id=example_application.object_id,
            end_date_relative="36h")
        example_identity_provider_aadb2c = azure.apimanagement.IdentityProviderAadb2c("exampleIdentityProviderAadb2c",
            resource_group_name=example_resource_group.name,
            api_management_name=example_service.name,
            client_id=example_application.application_id,
            client_secret="P@55w0rD!",
            allowed_tenant="myb2ctenant.onmicrosoft.com",
            signin_tenant="myb2ctenant.onmicrosoft.com",
            authority="myb2ctenant.b2clogin.com",
            signin_policy="B2C_1_Login",
            signup_policy="B2C_1_Signup",
            opts=pulumi.ResourceOptions(depends_on=[example_application_password]))
        ```

        ## Import

        API Management Azure AD B2C Identity Providers can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:apimanagement/identityProviderAadb2c:IdentityProviderAadb2c example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.ApiManagement/service/service1/identityProviders/aadB2C
        ```

        :param str resource_name: The name of the resource.
        :param IdentityProviderAadb2cArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IdentityProviderAadb2cArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            IdentityProviderAadb2cArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_tenant: Optional[pulumi.Input[str]] = None,
                 api_management_name: Optional[pulumi.Input[str]] = None,
                 authority: Optional[pulumi.Input[str]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 password_reset_policy: Optional[pulumi.Input[str]] = None,
                 profile_editing_policy: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 signin_policy: Optional[pulumi.Input[str]] = None,
                 signin_tenant: Optional[pulumi.Input[str]] = None,
                 signup_policy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IdentityProviderAadb2cArgs.__new__(IdentityProviderAadb2cArgs)

            if allowed_tenant is None and not opts.urn:
                raise TypeError("Missing required property 'allowed_tenant'")
            __props__.__dict__["allowed_tenant"] = allowed_tenant
            if api_management_name is None and not opts.urn:
                raise TypeError("Missing required property 'api_management_name'")
            __props__.__dict__["api_management_name"] = api_management_name
            if authority is None and not opts.urn:
                raise TypeError("Missing required property 'authority'")
            __props__.__dict__["authority"] = authority
            if client_id is None and not opts.urn:
                raise TypeError("Missing required property 'client_id'")
            __props__.__dict__["client_id"] = client_id
            if client_secret is None and not opts.urn:
                raise TypeError("Missing required property 'client_secret'")
            __props__.__dict__["client_secret"] = None if client_secret is None else pulumi.Output.secret(client_secret)
            __props__.__dict__["password_reset_policy"] = password_reset_policy
            __props__.__dict__["profile_editing_policy"] = profile_editing_policy
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if signin_policy is None and not opts.urn:
                raise TypeError("Missing required property 'signin_policy'")
            __props__.__dict__["signin_policy"] = signin_policy
            if signin_tenant is None and not opts.urn:
                raise TypeError("Missing required property 'signin_tenant'")
            __props__.__dict__["signin_tenant"] = signin_tenant
            if signup_policy is None and not opts.urn:
                raise TypeError("Missing required property 'signup_policy'")
            __props__.__dict__["signup_policy"] = signup_policy
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["clientSecret"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(IdentityProviderAadb2c, __self__).__init__(
            'azure:apimanagement/identityProviderAadb2c:IdentityProviderAadb2c',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allowed_tenant: Optional[pulumi.Input[str]] = None,
            api_management_name: Optional[pulumi.Input[str]] = None,
            authority: Optional[pulumi.Input[str]] = None,
            client_id: Optional[pulumi.Input[str]] = None,
            client_secret: Optional[pulumi.Input[str]] = None,
            password_reset_policy: Optional[pulumi.Input[str]] = None,
            profile_editing_policy: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            signin_policy: Optional[pulumi.Input[str]] = None,
            signin_tenant: Optional[pulumi.Input[str]] = None,
            signup_policy: Optional[pulumi.Input[str]] = None) -> 'IdentityProviderAadb2c':
        """
        Get an existing IdentityProviderAadb2c resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] allowed_tenant: The allowed AAD tenant, usually your B2C tenant domain.
        :param pulumi.Input[str] api_management_name: The Name of the API Management Service where this AAD Identity Provider should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] authority: OpenID Connect discovery endpoint hostname, usually your b2clogin.com domain.
        :param pulumi.Input[str] client_id: Client ID of the Application in your B2C tenant.
        :param pulumi.Input[str] client_secret: Client secret of the Application in your B2C tenant.
        :param pulumi.Input[str] password_reset_policy: Password reset Policy Name.
        :param pulumi.Input[str] profile_editing_policy: Profile editing Policy Name.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] signin_policy: Signin Policy Name.
        :param pulumi.Input[str] signin_tenant: The tenant to use instead of Common when logging into Active Directory, usually your B2C tenant domain.
        :param pulumi.Input[str] signup_policy: Signup Policy Name.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IdentityProviderAadb2cState.__new__(_IdentityProviderAadb2cState)

        __props__.__dict__["allowed_tenant"] = allowed_tenant
        __props__.__dict__["api_management_name"] = api_management_name
        __props__.__dict__["authority"] = authority
        __props__.__dict__["client_id"] = client_id
        __props__.__dict__["client_secret"] = client_secret
        __props__.__dict__["password_reset_policy"] = password_reset_policy
        __props__.__dict__["profile_editing_policy"] = profile_editing_policy
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["signin_policy"] = signin_policy
        __props__.__dict__["signin_tenant"] = signin_tenant
        __props__.__dict__["signup_policy"] = signup_policy
        return IdentityProviderAadb2c(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowedTenant")
    def allowed_tenant(self) -> pulumi.Output[str]:
        """
        The allowed AAD tenant, usually your B2C tenant domain.
        """
        return pulumi.get(self, "allowed_tenant")

    @property
    @pulumi.getter(name="apiManagementName")
    def api_management_name(self) -> pulumi.Output[str]:
        """
        The Name of the API Management Service where this AAD Identity Provider should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "api_management_name")

    @property
    @pulumi.getter
    def authority(self) -> pulumi.Output[str]:
        """
        OpenID Connect discovery endpoint hostname, usually your b2clogin.com domain.
        """
        return pulumi.get(self, "authority")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[str]:
        """
        Client ID of the Application in your B2C tenant.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Output[str]:
        """
        Client secret of the Application in your B2C tenant.
        """
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter(name="passwordResetPolicy")
    def password_reset_policy(self) -> pulumi.Output[Optional[str]]:
        """
        Password reset Policy Name.
        """
        return pulumi.get(self, "password_reset_policy")

    @property
    @pulumi.getter(name="profileEditingPolicy")
    def profile_editing_policy(self) -> pulumi.Output[Optional[str]]:
        """
        Profile editing Policy Name.
        """
        return pulumi.get(self, "profile_editing_policy")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="signinPolicy")
    def signin_policy(self) -> pulumi.Output[str]:
        """
        Signin Policy Name.
        """
        return pulumi.get(self, "signin_policy")

    @property
    @pulumi.getter(name="signinTenant")
    def signin_tenant(self) -> pulumi.Output[str]:
        """
        The tenant to use instead of Common when logging into Active Directory, usually your B2C tenant domain.
        """
        return pulumi.get(self, "signin_tenant")

    @property
    @pulumi.getter(name="signupPolicy")
    def signup_policy(self) -> pulumi.Output[str]:
        """
        Signup Policy Name.
        """
        return pulumi.get(self, "signup_policy")


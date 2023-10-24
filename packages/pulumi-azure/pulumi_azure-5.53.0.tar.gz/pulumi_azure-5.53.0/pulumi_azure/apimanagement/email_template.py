# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['EmailTemplateArgs', 'EmailTemplate']

@pulumi.input_type
class EmailTemplateArgs:
    def __init__(__self__, *,
                 api_management_name: pulumi.Input[str],
                 body: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 subject: pulumi.Input[str],
                 template_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a EmailTemplate resource.
        :param pulumi.Input[str] api_management_name: The name of the API Management Service in which the Email Template should exist. Changing this forces a new API Management Email Template to be created.
        :param pulumi.Input[str] body: The body of the Email. Its format has to be a well-formed HTML document.
               
               > **NOTE:** In `subject` and `body` predefined parameters can be used. The available parameters depend on the template. Schema to use a parameter: `$` followed by the `parameter.name` - `$<parameter.name>`. The available parameters can be seen in the Notification templates section of the API-Management Service instance within the Azure Portal.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the API Management Email Template should exist. Changing this forces a new API Management Email Template to be created.
        :param pulumi.Input[str] subject: The subject of the Email.
        :param pulumi.Input[str] template_name: The name of the Email Template. Possible values are `AccountClosedDeveloper`, `ApplicationApprovedNotificationMessage`, `ConfirmSignUpIdentityDefault`, `EmailChangeIdentityDefault`, `InviteUserNotificationMessage`, `NewCommentNotificationMessage`, `NewDeveloperNotificationMessage`, `NewIssueNotificationMessage`, `PasswordResetByAdminNotificationMessage`, `PasswordResetIdentityDefault`, `PurchaseDeveloperNotificationMessage`, `QuotaLimitApproachingDeveloperNotificationMessage`, `RejectDeveloperNotificationMessage`, `RequestDeveloperNotificationMessage`. Changing this forces a new API Management Email Template to be created.
        """
        EmailTemplateArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            api_management_name=api_management_name,
            body=body,
            resource_group_name=resource_group_name,
            subject=subject,
            template_name=template_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             api_management_name: pulumi.Input[str],
             body: pulumi.Input[str],
             resource_group_name: pulumi.Input[str],
             subject: pulumi.Input[str],
             template_name: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'apiManagementName' in kwargs:
            api_management_name = kwargs['apiManagementName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'templateName' in kwargs:
            template_name = kwargs['templateName']

        _setter("api_management_name", api_management_name)
        _setter("body", body)
        _setter("resource_group_name", resource_group_name)
        _setter("subject", subject)
        _setter("template_name", template_name)

    @property
    @pulumi.getter(name="apiManagementName")
    def api_management_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management Service in which the Email Template should exist. Changing this forces a new API Management Email Template to be created.
        """
        return pulumi.get(self, "api_management_name")

    @api_management_name.setter
    def api_management_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_management_name", value)

    @property
    @pulumi.getter
    def body(self) -> pulumi.Input[str]:
        """
        The body of the Email. Its format has to be a well-formed HTML document.

        > **NOTE:** In `subject` and `body` predefined parameters can be used. The available parameters depend on the template. Schema to use a parameter: `$` followed by the `parameter.name` - `$<parameter.name>`. The available parameters can be seen in the Notification templates section of the API-Management Service instance within the Azure Portal.
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: pulumi.Input[str]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group where the API Management Email Template should exist. Changing this forces a new API Management Email Template to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def subject(self) -> pulumi.Input[str]:
        """
        The subject of the Email.
        """
        return pulumi.get(self, "subject")

    @subject.setter
    def subject(self, value: pulumi.Input[str]):
        pulumi.set(self, "subject", value)

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> pulumi.Input[str]:
        """
        The name of the Email Template. Possible values are `AccountClosedDeveloper`, `ApplicationApprovedNotificationMessage`, `ConfirmSignUpIdentityDefault`, `EmailChangeIdentityDefault`, `InviteUserNotificationMessage`, `NewCommentNotificationMessage`, `NewDeveloperNotificationMessage`, `NewIssueNotificationMessage`, `PasswordResetByAdminNotificationMessage`, `PasswordResetIdentityDefault`, `PurchaseDeveloperNotificationMessage`, `QuotaLimitApproachingDeveloperNotificationMessage`, `RejectDeveloperNotificationMessage`, `RequestDeveloperNotificationMessage`. Changing this forces a new API Management Email Template to be created.
        """
        return pulumi.get(self, "template_name")

    @template_name.setter
    def template_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "template_name", value)


@pulumi.input_type
class _EmailTemplateState:
    def __init__(__self__, *,
                 api_management_name: Optional[pulumi.Input[str]] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subject: Optional[pulumi.Input[str]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering EmailTemplate resources.
        :param pulumi.Input[str] api_management_name: The name of the API Management Service in which the Email Template should exist. Changing this forces a new API Management Email Template to be created.
        :param pulumi.Input[str] body: The body of the Email. Its format has to be a well-formed HTML document.
               
               > **NOTE:** In `subject` and `body` predefined parameters can be used. The available parameters depend on the template. Schema to use a parameter: `$` followed by the `parameter.name` - `$<parameter.name>`. The available parameters can be seen in the Notification templates section of the API-Management Service instance within the Azure Portal.
        :param pulumi.Input[str] description: The description of the Email Template.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the API Management Email Template should exist. Changing this forces a new API Management Email Template to be created.
        :param pulumi.Input[str] subject: The subject of the Email.
        :param pulumi.Input[str] template_name: The name of the Email Template. Possible values are `AccountClosedDeveloper`, `ApplicationApprovedNotificationMessage`, `ConfirmSignUpIdentityDefault`, `EmailChangeIdentityDefault`, `InviteUserNotificationMessage`, `NewCommentNotificationMessage`, `NewDeveloperNotificationMessage`, `NewIssueNotificationMessage`, `PasswordResetByAdminNotificationMessage`, `PasswordResetIdentityDefault`, `PurchaseDeveloperNotificationMessage`, `QuotaLimitApproachingDeveloperNotificationMessage`, `RejectDeveloperNotificationMessage`, `RequestDeveloperNotificationMessage`. Changing this forces a new API Management Email Template to be created.
        :param pulumi.Input[str] title: The title of the Email Template.
        """
        _EmailTemplateState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            api_management_name=api_management_name,
            body=body,
            description=description,
            resource_group_name=resource_group_name,
            subject=subject,
            template_name=template_name,
            title=title,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             api_management_name: Optional[pulumi.Input[str]] = None,
             body: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             subject: Optional[pulumi.Input[str]] = None,
             template_name: Optional[pulumi.Input[str]] = None,
             title: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'apiManagementName' in kwargs:
            api_management_name = kwargs['apiManagementName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'templateName' in kwargs:
            template_name = kwargs['templateName']

        if api_management_name is not None:
            _setter("api_management_name", api_management_name)
        if body is not None:
            _setter("body", body)
        if description is not None:
            _setter("description", description)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if subject is not None:
            _setter("subject", subject)
        if template_name is not None:
            _setter("template_name", template_name)
        if title is not None:
            _setter("title", title)

    @property
    @pulumi.getter(name="apiManagementName")
    def api_management_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the API Management Service in which the Email Template should exist. Changing this forces a new API Management Email Template to be created.
        """
        return pulumi.get(self, "api_management_name")

    @api_management_name.setter
    def api_management_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_management_name", value)

    @property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[str]]:
        """
        The body of the Email. Its format has to be a well-formed HTML document.

        > **NOTE:** In `subject` and `body` predefined parameters can be used. The available parameters depend on the template. Schema to use a parameter: `$` followed by the `parameter.name` - `$<parameter.name>`. The available parameters can be seen in the Notification templates section of the API-Management Service instance within the Azure Portal.
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Email Template.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group where the API Management Email Template should exist. Changing this forces a new API Management Email Template to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def subject(self) -> Optional[pulumi.Input[str]]:
        """
        The subject of the Email.
        """
        return pulumi.get(self, "subject")

    @subject.setter
    def subject(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subject", value)

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Email Template. Possible values are `AccountClosedDeveloper`, `ApplicationApprovedNotificationMessage`, `ConfirmSignUpIdentityDefault`, `EmailChangeIdentityDefault`, `InviteUserNotificationMessage`, `NewCommentNotificationMessage`, `NewDeveloperNotificationMessage`, `NewIssueNotificationMessage`, `PasswordResetByAdminNotificationMessage`, `PasswordResetIdentityDefault`, `PurchaseDeveloperNotificationMessage`, `QuotaLimitApproachingDeveloperNotificationMessage`, `RejectDeveloperNotificationMessage`, `RequestDeveloperNotificationMessage`. Changing this forces a new API Management Email Template to be created.
        """
        return pulumi.get(self, "template_name")

    @template_name.setter
    def template_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_name", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        The title of the Email Template.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)


class EmailTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_management_name: Optional[pulumi.Input[str]] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subject: Optional[pulumi.Input[str]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a API Management Email Template.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_service = azure.apimanagement.Service("exampleService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            publisher_name="My Company",
            publisher_email="company@terraform.io",
            sku_name="Developer_1")
        example_email_template = azure.apimanagement.EmailTemplate("exampleEmailTemplate",
            template_name="ConfirmSignUpIdentityDefault",
            resource_group_name=example_resource_group.name,
            api_management_name=example_service.name,
            subject="Customized confirmation email for your new $OrganizationName API account",
            body=\"\"\"<!DOCTYPE html >
        <html>
        <head>
          <meta charset="UTF-8" />
          <title>Customized Letter Title</title>
        </head>
        <body>
          <p style="font-size:12pt;font-family:'Segoe UI'">Dear $DevFirstName $DevLastName,</p>
        </body>
        </html>
        \"\"\")
        ```

        ## Import

        API Management Email Templates can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:apimanagement/emailTemplate:EmailTemplate example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.ApiManagement/service/instance1/templates/template1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_management_name: The name of the API Management Service in which the Email Template should exist. Changing this forces a new API Management Email Template to be created.
        :param pulumi.Input[str] body: The body of the Email. Its format has to be a well-formed HTML document.
               
               > **NOTE:** In `subject` and `body` predefined parameters can be used. The available parameters depend on the template. Schema to use a parameter: `$` followed by the `parameter.name` - `$<parameter.name>`. The available parameters can be seen in the Notification templates section of the API-Management Service instance within the Azure Portal.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the API Management Email Template should exist. Changing this forces a new API Management Email Template to be created.
        :param pulumi.Input[str] subject: The subject of the Email.
        :param pulumi.Input[str] template_name: The name of the Email Template. Possible values are `AccountClosedDeveloper`, `ApplicationApprovedNotificationMessage`, `ConfirmSignUpIdentityDefault`, `EmailChangeIdentityDefault`, `InviteUserNotificationMessage`, `NewCommentNotificationMessage`, `NewDeveloperNotificationMessage`, `NewIssueNotificationMessage`, `PasswordResetByAdminNotificationMessage`, `PasswordResetIdentityDefault`, `PurchaseDeveloperNotificationMessage`, `QuotaLimitApproachingDeveloperNotificationMessage`, `RejectDeveloperNotificationMessage`, `RequestDeveloperNotificationMessage`. Changing this forces a new API Management Email Template to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EmailTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a API Management Email Template.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_service = azure.apimanagement.Service("exampleService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            publisher_name="My Company",
            publisher_email="company@terraform.io",
            sku_name="Developer_1")
        example_email_template = azure.apimanagement.EmailTemplate("exampleEmailTemplate",
            template_name="ConfirmSignUpIdentityDefault",
            resource_group_name=example_resource_group.name,
            api_management_name=example_service.name,
            subject="Customized confirmation email for your new $OrganizationName API account",
            body=\"\"\"<!DOCTYPE html >
        <html>
        <head>
          <meta charset="UTF-8" />
          <title>Customized Letter Title</title>
        </head>
        <body>
          <p style="font-size:12pt;font-family:'Segoe UI'">Dear $DevFirstName $DevLastName,</p>
        </body>
        </html>
        \"\"\")
        ```

        ## Import

        API Management Email Templates can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:apimanagement/emailTemplate:EmailTemplate example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.ApiManagement/service/instance1/templates/template1
        ```

        :param str resource_name: The name of the resource.
        :param EmailTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EmailTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            EmailTemplateArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_management_name: Optional[pulumi.Input[str]] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subject: Optional[pulumi.Input[str]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EmailTemplateArgs.__new__(EmailTemplateArgs)

            if api_management_name is None and not opts.urn:
                raise TypeError("Missing required property 'api_management_name'")
            __props__.__dict__["api_management_name"] = api_management_name
            if body is None and not opts.urn:
                raise TypeError("Missing required property 'body'")
            __props__.__dict__["body"] = body
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if subject is None and not opts.urn:
                raise TypeError("Missing required property 'subject'")
            __props__.__dict__["subject"] = subject
            if template_name is None and not opts.urn:
                raise TypeError("Missing required property 'template_name'")
            __props__.__dict__["template_name"] = template_name
            __props__.__dict__["description"] = None
            __props__.__dict__["title"] = None
        super(EmailTemplate, __self__).__init__(
            'azure:apimanagement/emailTemplate:EmailTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_management_name: Optional[pulumi.Input[str]] = None,
            body: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            subject: Optional[pulumi.Input[str]] = None,
            template_name: Optional[pulumi.Input[str]] = None,
            title: Optional[pulumi.Input[str]] = None) -> 'EmailTemplate':
        """
        Get an existing EmailTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_management_name: The name of the API Management Service in which the Email Template should exist. Changing this forces a new API Management Email Template to be created.
        :param pulumi.Input[str] body: The body of the Email. Its format has to be a well-formed HTML document.
               
               > **NOTE:** In `subject` and `body` predefined parameters can be used. The available parameters depend on the template. Schema to use a parameter: `$` followed by the `parameter.name` - `$<parameter.name>`. The available parameters can be seen in the Notification templates section of the API-Management Service instance within the Azure Portal.
        :param pulumi.Input[str] description: The description of the Email Template.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the API Management Email Template should exist. Changing this forces a new API Management Email Template to be created.
        :param pulumi.Input[str] subject: The subject of the Email.
        :param pulumi.Input[str] template_name: The name of the Email Template. Possible values are `AccountClosedDeveloper`, `ApplicationApprovedNotificationMessage`, `ConfirmSignUpIdentityDefault`, `EmailChangeIdentityDefault`, `InviteUserNotificationMessage`, `NewCommentNotificationMessage`, `NewDeveloperNotificationMessage`, `NewIssueNotificationMessage`, `PasswordResetByAdminNotificationMessage`, `PasswordResetIdentityDefault`, `PurchaseDeveloperNotificationMessage`, `QuotaLimitApproachingDeveloperNotificationMessage`, `RejectDeveloperNotificationMessage`, `RequestDeveloperNotificationMessage`. Changing this forces a new API Management Email Template to be created.
        :param pulumi.Input[str] title: The title of the Email Template.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EmailTemplateState.__new__(_EmailTemplateState)

        __props__.__dict__["api_management_name"] = api_management_name
        __props__.__dict__["body"] = body
        __props__.__dict__["description"] = description
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["subject"] = subject
        __props__.__dict__["template_name"] = template_name
        __props__.__dict__["title"] = title
        return EmailTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiManagementName")
    def api_management_name(self) -> pulumi.Output[str]:
        """
        The name of the API Management Service in which the Email Template should exist. Changing this forces a new API Management Email Template to be created.
        """
        return pulumi.get(self, "api_management_name")

    @property
    @pulumi.getter
    def body(self) -> pulumi.Output[str]:
        """
        The body of the Email. Its format has to be a well-formed HTML document.

        > **NOTE:** In `subject` and `body` predefined parameters can be used. The available parameters depend on the template. Schema to use a parameter: `$` followed by the `parameter.name` - `$<parameter.name>`. The available parameters can be seen in the Notification templates section of the API-Management Service instance within the Azure Portal.
        """
        return pulumi.get(self, "body")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the Email Template.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the API Management Email Template should exist. Changing this forces a new API Management Email Template to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def subject(self) -> pulumi.Output[str]:
        """
        The subject of the Email.
        """
        return pulumi.get(self, "subject")

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> pulumi.Output[str]:
        """
        The name of the Email Template. Possible values are `AccountClosedDeveloper`, `ApplicationApprovedNotificationMessage`, `ConfirmSignUpIdentityDefault`, `EmailChangeIdentityDefault`, `InviteUserNotificationMessage`, `NewCommentNotificationMessage`, `NewDeveloperNotificationMessage`, `NewIssueNotificationMessage`, `PasswordResetByAdminNotificationMessage`, `PasswordResetIdentityDefault`, `PurchaseDeveloperNotificationMessage`, `QuotaLimitApproachingDeveloperNotificationMessage`, `RejectDeveloperNotificationMessage`, `RequestDeveloperNotificationMessage`. Changing this forces a new API Management Email Template to be created.
        """
        return pulumi.get(self, "template_name")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        The title of the Email Template.
        """
        return pulumi.get(self, "title")


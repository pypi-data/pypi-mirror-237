# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DataConnectorAwsCloudTrailArgs', 'DataConnectorAwsCloudTrail']

@pulumi.input_type
class DataConnectorAwsCloudTrailArgs:
    def __init__(__self__, *,
                 aws_role_arn: pulumi.Input[str],
                 log_analytics_workspace_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DataConnectorAwsCloudTrail resource.
        :param pulumi.Input[str] aws_role_arn: The ARN of the AWS CloudTrail role, which is connected to this AWS CloudTrail Data Connector.
        :param pulumi.Input[str] log_analytics_workspace_id: The ID of the Log Analytics Workspace that this AWS CloudTrail Data Connector resides in. Changing this forces a new AWS CloudTrail Data Connector to be created.
        :param pulumi.Input[str] name: The name which should be used for this AWS CloudTrail Data Connector. Changing this forces a new AWS CloudTrail Data Connector to be created.
        """
        DataConnectorAwsCloudTrailArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            aws_role_arn=aws_role_arn,
            log_analytics_workspace_id=log_analytics_workspace_id,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             aws_role_arn: pulumi.Input[str],
             log_analytics_workspace_id: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'awsRoleArn' in kwargs:
            aws_role_arn = kwargs['awsRoleArn']
        if 'logAnalyticsWorkspaceId' in kwargs:
            log_analytics_workspace_id = kwargs['logAnalyticsWorkspaceId']

        _setter("aws_role_arn", aws_role_arn)
        _setter("log_analytics_workspace_id", log_analytics_workspace_id)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="awsRoleArn")
    def aws_role_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the AWS CloudTrail role, which is connected to this AWS CloudTrail Data Connector.
        """
        return pulumi.get(self, "aws_role_arn")

    @aws_role_arn.setter
    def aws_role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "aws_role_arn", value)

    @property
    @pulumi.getter(name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> pulumi.Input[str]:
        """
        The ID of the Log Analytics Workspace that this AWS CloudTrail Data Connector resides in. Changing this forces a new AWS CloudTrail Data Connector to be created.
        """
        return pulumi.get(self, "log_analytics_workspace_id")

    @log_analytics_workspace_id.setter
    def log_analytics_workspace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "log_analytics_workspace_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this AWS CloudTrail Data Connector. Changing this forces a new AWS CloudTrail Data Connector to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _DataConnectorAwsCloudTrailState:
    def __init__(__self__, *,
                 aws_role_arn: Optional[pulumi.Input[str]] = None,
                 log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DataConnectorAwsCloudTrail resources.
        :param pulumi.Input[str] aws_role_arn: The ARN of the AWS CloudTrail role, which is connected to this AWS CloudTrail Data Connector.
        :param pulumi.Input[str] log_analytics_workspace_id: The ID of the Log Analytics Workspace that this AWS CloudTrail Data Connector resides in. Changing this forces a new AWS CloudTrail Data Connector to be created.
        :param pulumi.Input[str] name: The name which should be used for this AWS CloudTrail Data Connector. Changing this forces a new AWS CloudTrail Data Connector to be created.
        """
        _DataConnectorAwsCloudTrailState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            aws_role_arn=aws_role_arn,
            log_analytics_workspace_id=log_analytics_workspace_id,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             aws_role_arn: Optional[pulumi.Input[str]] = None,
             log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'awsRoleArn' in kwargs:
            aws_role_arn = kwargs['awsRoleArn']
        if 'logAnalyticsWorkspaceId' in kwargs:
            log_analytics_workspace_id = kwargs['logAnalyticsWorkspaceId']

        if aws_role_arn is not None:
            _setter("aws_role_arn", aws_role_arn)
        if log_analytics_workspace_id is not None:
            _setter("log_analytics_workspace_id", log_analytics_workspace_id)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="awsRoleArn")
    def aws_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the AWS CloudTrail role, which is connected to this AWS CloudTrail Data Connector.
        """
        return pulumi.get(self, "aws_role_arn")

    @aws_role_arn.setter
    def aws_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_role_arn", value)

    @property
    @pulumi.getter(name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Log Analytics Workspace that this AWS CloudTrail Data Connector resides in. Changing this forces a new AWS CloudTrail Data Connector to be created.
        """
        return pulumi.get(self, "log_analytics_workspace_id")

    @log_analytics_workspace_id.setter
    def log_analytics_workspace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_analytics_workspace_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this AWS CloudTrail Data Connector. Changing this forces a new AWS CloudTrail Data Connector to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class DataConnectorAwsCloudTrail(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_role_arn: Optional[pulumi.Input[str]] = None,
                 log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a AWS CloudTrail Data Connector.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="PerGB2018")
        example_log_analytics_workspace_onboarding = azure.sentinel.LogAnalyticsWorkspaceOnboarding("exampleLogAnalyticsWorkspaceOnboarding", workspace_id=example_analytics_workspace.id)
        example_data_connector_aws_cloud_trail = azure.sentinel.DataConnectorAwsCloudTrail("exampleDataConnectorAwsCloudTrail",
            log_analytics_workspace_id=example_log_analytics_workspace_onboarding.workspace_id,
            aws_role_arn="arn:aws:iam::000000000000:role/role1")
        ```

        ## Import

        AWS CloudTrail Data Connectors can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:sentinel/dataConnectorAwsCloudTrail:DataConnectorAwsCloudTrail example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.OperationalInsights/workspaces/workspace1/providers/Microsoft.SecurityInsights/dataConnectors/dc1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] aws_role_arn: The ARN of the AWS CloudTrail role, which is connected to this AWS CloudTrail Data Connector.
        :param pulumi.Input[str] log_analytics_workspace_id: The ID of the Log Analytics Workspace that this AWS CloudTrail Data Connector resides in. Changing this forces a new AWS CloudTrail Data Connector to be created.
        :param pulumi.Input[str] name: The name which should be used for this AWS CloudTrail Data Connector. Changing this forces a new AWS CloudTrail Data Connector to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataConnectorAwsCloudTrailArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a AWS CloudTrail Data Connector.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="PerGB2018")
        example_log_analytics_workspace_onboarding = azure.sentinel.LogAnalyticsWorkspaceOnboarding("exampleLogAnalyticsWorkspaceOnboarding", workspace_id=example_analytics_workspace.id)
        example_data_connector_aws_cloud_trail = azure.sentinel.DataConnectorAwsCloudTrail("exampleDataConnectorAwsCloudTrail",
            log_analytics_workspace_id=example_log_analytics_workspace_onboarding.workspace_id,
            aws_role_arn="arn:aws:iam::000000000000:role/role1")
        ```

        ## Import

        AWS CloudTrail Data Connectors can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:sentinel/dataConnectorAwsCloudTrail:DataConnectorAwsCloudTrail example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.OperationalInsights/workspaces/workspace1/providers/Microsoft.SecurityInsights/dataConnectors/dc1
        ```

        :param str resource_name: The name of the resource.
        :param DataConnectorAwsCloudTrailArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataConnectorAwsCloudTrailArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DataConnectorAwsCloudTrailArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_role_arn: Optional[pulumi.Input[str]] = None,
                 log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataConnectorAwsCloudTrailArgs.__new__(DataConnectorAwsCloudTrailArgs)

            if aws_role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'aws_role_arn'")
            __props__.__dict__["aws_role_arn"] = aws_role_arn
            if log_analytics_workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'log_analytics_workspace_id'")
            __props__.__dict__["log_analytics_workspace_id"] = log_analytics_workspace_id
            __props__.__dict__["name"] = name
        super(DataConnectorAwsCloudTrail, __self__).__init__(
            'azure:sentinel/dataConnectorAwsCloudTrail:DataConnectorAwsCloudTrail',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            aws_role_arn: Optional[pulumi.Input[str]] = None,
            log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'DataConnectorAwsCloudTrail':
        """
        Get an existing DataConnectorAwsCloudTrail resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] aws_role_arn: The ARN of the AWS CloudTrail role, which is connected to this AWS CloudTrail Data Connector.
        :param pulumi.Input[str] log_analytics_workspace_id: The ID of the Log Analytics Workspace that this AWS CloudTrail Data Connector resides in. Changing this forces a new AWS CloudTrail Data Connector to be created.
        :param pulumi.Input[str] name: The name which should be used for this AWS CloudTrail Data Connector. Changing this forces a new AWS CloudTrail Data Connector to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DataConnectorAwsCloudTrailState.__new__(_DataConnectorAwsCloudTrailState)

        __props__.__dict__["aws_role_arn"] = aws_role_arn
        __props__.__dict__["log_analytics_workspace_id"] = log_analytics_workspace_id
        __props__.__dict__["name"] = name
        return DataConnectorAwsCloudTrail(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="awsRoleArn")
    def aws_role_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the AWS CloudTrail role, which is connected to this AWS CloudTrail Data Connector.
        """
        return pulumi.get(self, "aws_role_arn")

    @property
    @pulumi.getter(name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> pulumi.Output[str]:
        """
        The ID of the Log Analytics Workspace that this AWS CloudTrail Data Connector resides in. Changing this forces a new AWS CloudTrail Data Connector to be created.
        """
        return pulumi.get(self, "log_analytics_workspace_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this AWS CloudTrail Data Connector. Changing this forces a new AWS CloudTrail Data Connector to be created.
        """
        return pulumi.get(self, "name")


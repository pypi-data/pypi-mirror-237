# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['OutputFunctionArgs', 'OutputFunction']

@pulumi.input_type
class OutputFunctionArgs:
    def __init__(__self__, *,
                 api_key: pulumi.Input[str],
                 function_app: pulumi.Input[str],
                 function_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 stream_analytics_job_name: pulumi.Input[str],
                 batch_max_count: Optional[pulumi.Input[int]] = None,
                 batch_max_in_bytes: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OutputFunction resource.
        :param pulumi.Input[str] api_key: The API key for the Function.
        :param pulumi.Input[str] function_app: The name of the Function App.
        :param pulumi.Input[str] function_name: The name of the function in the Function App.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Stream Analytics Output should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] stream_analytics_job_name: The name of the Stream Analytics Job. Changing this forces a new resource to be created.
        :param pulumi.Input[int] batch_max_count: The maximum number of events in each batch that's sent to the function. Defaults to `100`.
        :param pulumi.Input[int] batch_max_in_bytes: The maximum batch size in bytes that's sent to the function. Defaults to `262144` (256 kB).
        :param pulumi.Input[str] name: The name which should be used for this Stream Analytics Output. Changing this forces a new resource to be created.
        """
        OutputFunctionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            api_key=api_key,
            function_app=function_app,
            function_name=function_name,
            resource_group_name=resource_group_name,
            stream_analytics_job_name=stream_analytics_job_name,
            batch_max_count=batch_max_count,
            batch_max_in_bytes=batch_max_in_bytes,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             api_key: pulumi.Input[str],
             function_app: pulumi.Input[str],
             function_name: pulumi.Input[str],
             resource_group_name: pulumi.Input[str],
             stream_analytics_job_name: pulumi.Input[str],
             batch_max_count: Optional[pulumi.Input[int]] = None,
             batch_max_in_bytes: Optional[pulumi.Input[int]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'apiKey' in kwargs:
            api_key = kwargs['apiKey']
        if 'functionApp' in kwargs:
            function_app = kwargs['functionApp']
        if 'functionName' in kwargs:
            function_name = kwargs['functionName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'streamAnalyticsJobName' in kwargs:
            stream_analytics_job_name = kwargs['streamAnalyticsJobName']
        if 'batchMaxCount' in kwargs:
            batch_max_count = kwargs['batchMaxCount']
        if 'batchMaxInBytes' in kwargs:
            batch_max_in_bytes = kwargs['batchMaxInBytes']

        _setter("api_key", api_key)
        _setter("function_app", function_app)
        _setter("function_name", function_name)
        _setter("resource_group_name", resource_group_name)
        _setter("stream_analytics_job_name", stream_analytics_job_name)
        if batch_max_count is not None:
            _setter("batch_max_count", batch_max_count)
        if batch_max_in_bytes is not None:
            _setter("batch_max_in_bytes", batch_max_in_bytes)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Input[str]:
        """
        The API key for the Function.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="functionApp")
    def function_app(self) -> pulumi.Input[str]:
        """
        The name of the Function App.
        """
        return pulumi.get(self, "function_app")

    @function_app.setter
    def function_app(self, value: pulumi.Input[str]):
        pulumi.set(self, "function_app", value)

    @property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Input[str]:
        """
        The name of the function in the Function App.
        """
        return pulumi.get(self, "function_name")

    @function_name.setter
    def function_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "function_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group where the Stream Analytics Output should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="streamAnalyticsJobName")
    def stream_analytics_job_name(self) -> pulumi.Input[str]:
        """
        The name of the Stream Analytics Job. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "stream_analytics_job_name")

    @stream_analytics_job_name.setter
    def stream_analytics_job_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "stream_analytics_job_name", value)

    @property
    @pulumi.getter(name="batchMaxCount")
    def batch_max_count(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of events in each batch that's sent to the function. Defaults to `100`.
        """
        return pulumi.get(self, "batch_max_count")

    @batch_max_count.setter
    def batch_max_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "batch_max_count", value)

    @property
    @pulumi.getter(name="batchMaxInBytes")
    def batch_max_in_bytes(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum batch size in bytes that's sent to the function. Defaults to `262144` (256 kB).
        """
        return pulumi.get(self, "batch_max_in_bytes")

    @batch_max_in_bytes.setter
    def batch_max_in_bytes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "batch_max_in_bytes", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Stream Analytics Output. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _OutputFunctionState:
    def __init__(__self__, *,
                 api_key: Optional[pulumi.Input[str]] = None,
                 batch_max_count: Optional[pulumi.Input[int]] = None,
                 batch_max_in_bytes: Optional[pulumi.Input[int]] = None,
                 function_app: Optional[pulumi.Input[str]] = None,
                 function_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 stream_analytics_job_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering OutputFunction resources.
        :param pulumi.Input[str] api_key: The API key for the Function.
        :param pulumi.Input[int] batch_max_count: The maximum number of events in each batch that's sent to the function. Defaults to `100`.
        :param pulumi.Input[int] batch_max_in_bytes: The maximum batch size in bytes that's sent to the function. Defaults to `262144` (256 kB).
        :param pulumi.Input[str] function_app: The name of the Function App.
        :param pulumi.Input[str] function_name: The name of the function in the Function App.
        :param pulumi.Input[str] name: The name which should be used for this Stream Analytics Output. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Stream Analytics Output should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] stream_analytics_job_name: The name of the Stream Analytics Job. Changing this forces a new resource to be created.
        """
        _OutputFunctionState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            api_key=api_key,
            batch_max_count=batch_max_count,
            batch_max_in_bytes=batch_max_in_bytes,
            function_app=function_app,
            function_name=function_name,
            name=name,
            resource_group_name=resource_group_name,
            stream_analytics_job_name=stream_analytics_job_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             api_key: Optional[pulumi.Input[str]] = None,
             batch_max_count: Optional[pulumi.Input[int]] = None,
             batch_max_in_bytes: Optional[pulumi.Input[int]] = None,
             function_app: Optional[pulumi.Input[str]] = None,
             function_name: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             resource_group_name: Optional[pulumi.Input[str]] = None,
             stream_analytics_job_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'apiKey' in kwargs:
            api_key = kwargs['apiKey']
        if 'batchMaxCount' in kwargs:
            batch_max_count = kwargs['batchMaxCount']
        if 'batchMaxInBytes' in kwargs:
            batch_max_in_bytes = kwargs['batchMaxInBytes']
        if 'functionApp' in kwargs:
            function_app = kwargs['functionApp']
        if 'functionName' in kwargs:
            function_name = kwargs['functionName']
        if 'resourceGroupName' in kwargs:
            resource_group_name = kwargs['resourceGroupName']
        if 'streamAnalyticsJobName' in kwargs:
            stream_analytics_job_name = kwargs['streamAnalyticsJobName']

        if api_key is not None:
            _setter("api_key", api_key)
        if batch_max_count is not None:
            _setter("batch_max_count", batch_max_count)
        if batch_max_in_bytes is not None:
            _setter("batch_max_in_bytes", batch_max_in_bytes)
        if function_app is not None:
            _setter("function_app", function_app)
        if function_name is not None:
            _setter("function_name", function_name)
        if name is not None:
            _setter("name", name)
        if resource_group_name is not None:
            _setter("resource_group_name", resource_group_name)
        if stream_analytics_job_name is not None:
            _setter("stream_analytics_job_name", stream_analytics_job_name)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        The API key for the Function.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="batchMaxCount")
    def batch_max_count(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of events in each batch that's sent to the function. Defaults to `100`.
        """
        return pulumi.get(self, "batch_max_count")

    @batch_max_count.setter
    def batch_max_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "batch_max_count", value)

    @property
    @pulumi.getter(name="batchMaxInBytes")
    def batch_max_in_bytes(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum batch size in bytes that's sent to the function. Defaults to `262144` (256 kB).
        """
        return pulumi.get(self, "batch_max_in_bytes")

    @batch_max_in_bytes.setter
    def batch_max_in_bytes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "batch_max_in_bytes", value)

    @property
    @pulumi.getter(name="functionApp")
    def function_app(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Function App.
        """
        return pulumi.get(self, "function_app")

    @function_app.setter
    def function_app(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "function_app", value)

    @property
    @pulumi.getter(name="functionName")
    def function_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the function in the Function App.
        """
        return pulumi.get(self, "function_name")

    @function_name.setter
    def function_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "function_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Stream Analytics Output. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group where the Stream Analytics Output should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="streamAnalyticsJobName")
    def stream_analytics_job_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Stream Analytics Job. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "stream_analytics_job_name")

    @stream_analytics_job_name.setter
    def stream_analytics_job_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stream_analytics_job_name", value)


class OutputFunction(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 batch_max_count: Optional[pulumi.Input[int]] = None,
                 batch_max_in_bytes: Optional[pulumi.Input[int]] = None,
                 function_app: Optional[pulumi.Input[str]] = None,
                 function_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 stream_analytics_job_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Stream Analytics Output Function.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_plan = azure.appservice.Plan("examplePlan",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            kind="FunctionApp",
            reserved=True,
            sku=azure.appservice.PlanSkuArgs(
                tier="Dynamic",
                size="Y1",
            ))
        example_function_app = azure.appservice.FunctionApp("exampleFunctionApp",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            app_service_plan_id=example_plan.id,
            storage_account_name=example_account.name,
            storage_account_access_key=example_account.primary_access_key,
            os_type="linux",
            version="~3")
        example_job = azure.streamanalytics.Job("exampleJob",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            streaming_units=3,
            transformation_query=\"\"\"    SELECT *
            INTO [YourOutputAlias]
            FROM [YourInputAlias]
        \"\"\")
        example_output_function = azure.streamanalytics.OutputFunction("exampleOutputFunction",
            resource_group_name=example_job.resource_group_name,
            stream_analytics_job_name=example_job.name,
            function_app=example_function_app.name,
            function_name="examplefunctionname",
            api_key="exampleapikey")
        ```

        ## Import

        Stream Analytics Output Functions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:streamanalytics/outputFunction:OutputFunction example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.StreamAnalytics/streamingJobs/job1/outputs/output1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: The API key for the Function.
        :param pulumi.Input[int] batch_max_count: The maximum number of events in each batch that's sent to the function. Defaults to `100`.
        :param pulumi.Input[int] batch_max_in_bytes: The maximum batch size in bytes that's sent to the function. Defaults to `262144` (256 kB).
        :param pulumi.Input[str] function_app: The name of the Function App.
        :param pulumi.Input[str] function_name: The name of the function in the Function App.
        :param pulumi.Input[str] name: The name which should be used for this Stream Analytics Output. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Stream Analytics Output should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] stream_analytics_job_name: The name of the Stream Analytics Job. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OutputFunctionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Stream Analytics Output Function.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_plan = azure.appservice.Plan("examplePlan",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            kind="FunctionApp",
            reserved=True,
            sku=azure.appservice.PlanSkuArgs(
                tier="Dynamic",
                size="Y1",
            ))
        example_function_app = azure.appservice.FunctionApp("exampleFunctionApp",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            app_service_plan_id=example_plan.id,
            storage_account_name=example_account.name,
            storage_account_access_key=example_account.primary_access_key,
            os_type="linux",
            version="~3")
        example_job = azure.streamanalytics.Job("exampleJob",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            streaming_units=3,
            transformation_query=\"\"\"    SELECT *
            INTO [YourOutputAlias]
            FROM [YourInputAlias]
        \"\"\")
        example_output_function = azure.streamanalytics.OutputFunction("exampleOutputFunction",
            resource_group_name=example_job.resource_group_name,
            stream_analytics_job_name=example_job.name,
            function_app=example_function_app.name,
            function_name="examplefunctionname",
            api_key="exampleapikey")
        ```

        ## Import

        Stream Analytics Output Functions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:streamanalytics/outputFunction:OutputFunction example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.StreamAnalytics/streamingJobs/job1/outputs/output1
        ```

        :param str resource_name: The name of the resource.
        :param OutputFunctionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OutputFunctionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            OutputFunctionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 batch_max_count: Optional[pulumi.Input[int]] = None,
                 batch_max_in_bytes: Optional[pulumi.Input[int]] = None,
                 function_app: Optional[pulumi.Input[str]] = None,
                 function_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 stream_analytics_job_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OutputFunctionArgs.__new__(OutputFunctionArgs)

            if api_key is None and not opts.urn:
                raise TypeError("Missing required property 'api_key'")
            __props__.__dict__["api_key"] = None if api_key is None else pulumi.Output.secret(api_key)
            __props__.__dict__["batch_max_count"] = batch_max_count
            __props__.__dict__["batch_max_in_bytes"] = batch_max_in_bytes
            if function_app is None and not opts.urn:
                raise TypeError("Missing required property 'function_app'")
            __props__.__dict__["function_app"] = function_app
            if function_name is None and not opts.urn:
                raise TypeError("Missing required property 'function_name'")
            __props__.__dict__["function_name"] = function_name
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if stream_analytics_job_name is None and not opts.urn:
                raise TypeError("Missing required property 'stream_analytics_job_name'")
            __props__.__dict__["stream_analytics_job_name"] = stream_analytics_job_name
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["apiKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(OutputFunction, __self__).__init__(
            'azure:streamanalytics/outputFunction:OutputFunction',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_key: Optional[pulumi.Input[str]] = None,
            batch_max_count: Optional[pulumi.Input[int]] = None,
            batch_max_in_bytes: Optional[pulumi.Input[int]] = None,
            function_app: Optional[pulumi.Input[str]] = None,
            function_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            stream_analytics_job_name: Optional[pulumi.Input[str]] = None) -> 'OutputFunction':
        """
        Get an existing OutputFunction resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: The API key for the Function.
        :param pulumi.Input[int] batch_max_count: The maximum number of events in each batch that's sent to the function. Defaults to `100`.
        :param pulumi.Input[int] batch_max_in_bytes: The maximum batch size in bytes that's sent to the function. Defaults to `262144` (256 kB).
        :param pulumi.Input[str] function_app: The name of the Function App.
        :param pulumi.Input[str] function_name: The name of the function in the Function App.
        :param pulumi.Input[str] name: The name which should be used for this Stream Analytics Output. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Stream Analytics Output should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] stream_analytics_job_name: The name of the Stream Analytics Job. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OutputFunctionState.__new__(_OutputFunctionState)

        __props__.__dict__["api_key"] = api_key
        __props__.__dict__["batch_max_count"] = batch_max_count
        __props__.__dict__["batch_max_in_bytes"] = batch_max_in_bytes
        __props__.__dict__["function_app"] = function_app
        __props__.__dict__["function_name"] = function_name
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["stream_analytics_job_name"] = stream_analytics_job_name
        return OutputFunction(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[str]:
        """
        The API key for the Function.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="batchMaxCount")
    def batch_max_count(self) -> pulumi.Output[Optional[int]]:
        """
        The maximum number of events in each batch that's sent to the function. Defaults to `100`.
        """
        return pulumi.get(self, "batch_max_count")

    @property
    @pulumi.getter(name="batchMaxInBytes")
    def batch_max_in_bytes(self) -> pulumi.Output[Optional[int]]:
        """
        The maximum batch size in bytes that's sent to the function. Defaults to `262144` (256 kB).
        """
        return pulumi.get(self, "batch_max_in_bytes")

    @property
    @pulumi.getter(name="functionApp")
    def function_app(self) -> pulumi.Output[str]:
        """
        The name of the Function App.
        """
        return pulumi.get(self, "function_app")

    @property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Output[str]:
        """
        The name of the function in the Function App.
        """
        return pulumi.get(self, "function_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Stream Analytics Output. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Stream Analytics Output should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="streamAnalyticsJobName")
    def stream_analytics_job_name(self) -> pulumi.Output[str]:
        """
        The name of the Stream Analytics Job. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "stream_analytics_job_name")


# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from multinode.api_client.models.execution_info import ExecutionInfo  # noqa: E501

class TestExecutionInfo(unittest.TestCase):
    """ExecutionInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExecutionInfo:
        """Test ExecutionInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExecutionInfo`
        """
        model = ExecutionInfo()  # noqa: E501
        if include_optional:
            return ExecutionInfo(
                project_name = '',
                version_id = '',
                function_name = '',
                invocation_id = '',
                execution_id = '',
                input = '',
                cancellation_request_time = 56,
                resource_spec = multinode.api_client.models.resource_spec.ResourceSpec(
                    virtual_cpus = 1.337, 
                    memory_gbs = 1.337, 
                    max_concurrency = 56, ),
                execution_spec = multinode.api_client.models.execution_spec.ExecutionSpec(
                    max_retries = 56, 
                    timeout_seconds = 56, ),
                function_status = 'PENDING',
                prepared_function_details = multinode.api_client.models.prepared_function_details.PreparedFunctionDetails(
                    type = 'TEST', 
                    identifier = '', ),
                worker_status = 'PENDING',
                worker_details = multinode.api_client.models.worker_details.WorkerDetails(
                    type = 'TEST', 
                    identifier = '', 
                    logs_identifier = '', ),
                termination_signal_time = 56,
                outcome = 'SUCCEEDED',
                output = '',
                error_message = '',
                creation_time = 56,
                last_update_time = 56,
                execution_start_time = 56,
                execution_finish_time = 56,
                invocation_creation_time = 56
            )
        else:
            return ExecutionInfo(
                project_name = '',
                version_id = '',
                function_name = '',
                invocation_id = '',
                execution_id = '',
                input = '',
                cancellation_request_time = 56,
                resource_spec = multinode.api_client.models.resource_spec.ResourceSpec(
                    virtual_cpus = 1.337, 
                    memory_gbs = 1.337, 
                    max_concurrency = 56, ),
                execution_spec = multinode.api_client.models.execution_spec.ExecutionSpec(
                    max_retries = 56, 
                    timeout_seconds = 56, ),
                function_status = 'PENDING',
                prepared_function_details = multinode.api_client.models.prepared_function_details.PreparedFunctionDetails(
                    type = 'TEST', 
                    identifier = '', ),
                worker_status = 'PENDING',
                worker_details = multinode.api_client.models.worker_details.WorkerDetails(
                    type = 'TEST', 
                    identifier = '', 
                    logs_identifier = '', ),
                termination_signal_time = 56,
                outcome = 'SUCCEEDED',
                output = '',
                error_message = '',
                creation_time = 56,
                last_update_time = 56,
                execution_start_time = 56,
                execution_finish_time = 56,
                invocation_creation_time = 56,
        )
        """

    def testExecutionInfo(self):
        """Test ExecutionInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

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

from multinode.api_client.models.invocations_list_for_function import InvocationsListForFunction  # noqa: E501

class TestInvocationsListForFunction(unittest.TestCase):
    """InvocationsListForFunction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvocationsListForFunction:
        """Test InvocationsListForFunction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvocationsListForFunction`
        """
        model = InvocationsListForFunction()  # noqa: E501
        if include_optional:
            return InvocationsListForFunction(
                project_name = '',
                version_id = '',
                function_name = '',
                invocations = [
                    multinode.api_client.models.invocation_info_for_function.InvocationInfoForFunction(
                        invocation_id = '', 
                        parent_invocation = multinode.api_client.models.parent_invocation_definition.ParentInvocationDefinition(
                            function_name = '', 
                            invocation_id = '', ), 
                        cancellation_request_time = 56, 
                        invocation_status = 'RUNNING', 
                        creation_time = 56, 
                        last_update_time = 56, )
                    ],
                next_offset = ''
            )
        else:
            return InvocationsListForFunction(
                project_name = '',
                version_id = '',
                function_name = '',
                invocations = [
                    multinode.api_client.models.invocation_info_for_function.InvocationInfoForFunction(
                        invocation_id = '', 
                        parent_invocation = multinode.api_client.models.parent_invocation_definition.ParentInvocationDefinition(
                            function_name = '', 
                            invocation_id = '', ), 
                        cancellation_request_time = 56, 
                        invocation_status = 'RUNNING', 
                        creation_time = 56, 
                        last_update_time = 56, )
                    ],
                next_offset = '',
        )
        """

    def testInvocationsListForFunction(self):
        """Test InvocationsListForFunction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

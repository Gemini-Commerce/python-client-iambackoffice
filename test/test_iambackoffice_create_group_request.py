# coding: utf-8

"""
    IamBackoffice Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from iambackoffice.models.iambackoffice_create_group_request import IambackofficeCreateGroupRequest

class TestIambackofficeCreateGroupRequest(unittest.TestCase):
    """IambackofficeCreateGroupRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IambackofficeCreateGroupRequest:
        """Test IambackofficeCreateGroupRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IambackofficeCreateGroupRequest`
        """
        model = IambackofficeCreateGroupRequest()
        if include_optional:
            return IambackofficeCreateGroupRequest(
                tenant_id = '',
                name = '',
                data = {
                    'key' : ''
                    }
            )
        else:
            return IambackofficeCreateGroupRequest(
        )
        """

    def testIambackofficeCreateGroupRequest(self):
        """Test IambackofficeCreateGroupRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
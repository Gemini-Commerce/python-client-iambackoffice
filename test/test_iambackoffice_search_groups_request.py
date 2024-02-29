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

from iambackoffice.models.iambackoffice_search_groups_request import IambackofficeSearchGroupsRequest

class TestIambackofficeSearchGroupsRequest(unittest.TestCase):
    """IambackofficeSearchGroupsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IambackofficeSearchGroupsRequest:
        """Test IambackofficeSearchGroupsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IambackofficeSearchGroupsRequest`
        """
        model = IambackofficeSearchGroupsRequest()
        if include_optional:
            return IambackofficeSearchGroupsRequest(
                tenant_id = '',
                filters = iambackoffice.models.search_groups_request_filters.SearchGroupsRequestFilters(
                    data = {
                        'key' : ''
                        }, ),
                filters_mask = ''
            )
        else:
            return IambackofficeSearchGroupsRequest(
        )
        """

    def testIambackofficeSearchGroupsRequest(self):
        """Test IambackofficeSearchGroupsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
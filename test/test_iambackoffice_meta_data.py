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

from iambackoffice.models.iambackoffice_meta_data import IambackofficeMetaData

class TestIambackofficeMetaData(unittest.TestCase):
    """IambackofficeMetaData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IambackofficeMetaData:
        """Test IambackofficeMetaData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IambackofficeMetaData`
        """
        model = IambackofficeMetaData()
        if include_optional:
            return IambackofficeMetaData(
                device = iambackoffice.models.iambackoffice_device.iambackofficeDevice(
                    description = '', 
                    name = '', 
                    device_type = '', )
            )
        else:
            return IambackofficeMetaData(
        )
        """

    def testIambackofficeMetaData(self):
        """Test IambackofficeMetaData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
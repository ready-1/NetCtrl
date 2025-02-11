# coding: utf-8

"""
M4300 REST API

M4300 REST API with ConfigAgent Documentation.

The version of the OpenAPI document: 2.0.0.59
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.fdbs_inner import FdbsInner


class TestFdbsInner(unittest.TestCase):
    """FdbsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FdbsInner:
        """Test FdbsInner
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `FdbsInner`
        """
        model = FdbsInner()
        if include_optional:
            return FdbsInner(
                interface = 56,
                vlan_id = 56,
                mac = '',
                entry_type = 0
            )
        else:
            return FdbsInner(
        )
        """

    def testFdbsInner(self):
        """Test FdbsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

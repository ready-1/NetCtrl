# coding: utf-8

"""
M4300 REST API

M4300 REST API with ConfigAgent Documentation.

The version of the OpenAPI document: 2.0.0.59
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.snooping_queriers_get import SnoopingQueriersGet


class TestSnoopingQueriersGet(unittest.TestCase):
    """SnoopingQueriersGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SnoopingQueriersGet:
        """Test SnoopingQueriersGet
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SnoopingQueriersGet`
        """
        model = SnoopingQueriersGet()
        if include_optional:
            return SnoopingQueriersGet(
                address = '',
                admin_mode = 'enabled',
                expiry_interval = 60,
                last_querier_address = '',
                last_querier_version = 56,
                oper_max_resp_time = 56,
                oper_state = '',
                oper_version = 56,
                query_interval = 1,
                querier_version = 1,
                vlan_address = '',
                vlan_election_mode = 'enabled',
                vlan_mode = 'enabled'
            )
        else:
            return SnoopingQueriersGet(
        )
        """

    def testSnoopingQueriersGet(self):
        """Test SnoopingQueriersGet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

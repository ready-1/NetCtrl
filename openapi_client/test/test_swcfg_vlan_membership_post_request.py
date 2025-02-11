# coding: utf-8

"""
M4300 REST API

M4300 REST API with ConfigAgent Documentation.

The version of the OpenAPI document: 2.0.0.59
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.swcfg_vlan_membership_post_request import (
    SwcfgVlanMembershipPostRequest,
)


class TestSwcfgVlanMembershipPostRequest(unittest.TestCase):
    """SwcfgVlanMembershipPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SwcfgVlanMembershipPostRequest:
        """Test SwcfgVlanMembershipPostRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SwcfgVlanMembershipPostRequest`
        """
        model = SwcfgVlanMembershipPostRequest()
        if include_optional:
            return SwcfgVlanMembershipPostRequest(
                vlan_membership = {"vlanid":2,"portMembers":[{"port":1,"tagged":false},{"port":2,"tagged":false},{"port":3,"tagged":false}],"lagMembers":[{"port":4,"tagged":false},{"port":5,"tagged":false},{"port":6,"tagged":false}],"trafficPrio":6,"trafficPrioPortMem":[{"port":1},{"port":2},{"port":3}],"trafficPrioLagMem":[{"port":1},{"port":2},{"port":3}],"pvidMembers":[{"port":7},{"port":8},{"port":9}]}
            )
        else:
            return SwcfgVlanMembershipPostRequest(
        )
        """

    def testSwcfgVlanMembershipPostRequest(self):
        """Test SwcfgVlanMembershipPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

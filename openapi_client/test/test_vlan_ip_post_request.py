# coding: utf-8

"""
M4300 REST API

M4300 REST API with ConfigAgent Documentation.

The version of the OpenAPI document: 2.0.0.59
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.vlan_ip_post_request import VlanIpPostRequest


class TestVlanIpPostRequest(unittest.TestCase):
    """VlanIpPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VlanIpPostRequest:
        """Test VlanIpPostRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `VlanIpPostRequest`
        """
        model = VlanIpPostRequest()
        if include_optional:
            return VlanIpPostRequest(
                vlan_ip = {"vlanId":1,"dhcpStatus":true,"ipAddr":"10.40.7.100","ipMask":"255.255.252.0","ipMtu":1500,"vlanRouting":true}
            )
        else:
            return VlanIpPostRequest(
        )
        """

    def testVlanIpPostRequest(self):
        """Test VlanIpPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

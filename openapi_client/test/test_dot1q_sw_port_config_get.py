# coding: utf-8

"""
M4300 REST API

M4300 REST API with ConfigAgent Documentation.

The version of the OpenAPI document: 2.0.0.59
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.dot1q_sw_port_config_get import Dot1qSwPortConfigGet


class TestDot1qSwPortConfigGet(unittest.TestCase):
    """Dot1qSwPortConfigGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dot1qSwPortConfigGet:
        """Test Dot1qSwPortConfigGet
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Dot1qSwPortConfigGet`
        """
        model = Dot1qSwPortConfigGet()
        if include_optional:
            return Dot1qSwPortConfigGet(
                interface = '',
                access_vlan = 56,
                allowed_vlan_list = [
                    ''
                    ],
                dynamically_added_vlan_list = '',
                forbidden_vlan_list = '',
                config_mode = 'none',
                native_vlan = 56,
                tagged_vlan_list = [
                    ''
                    ],
                untagged_vlan_list = [
                    ''
                    ]
            )
        else:
            return Dot1qSwPortConfigGet(
        )
        """

    def testDot1qSwPortConfigGet(self):
        """Test Dot1qSwPortConfigGet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

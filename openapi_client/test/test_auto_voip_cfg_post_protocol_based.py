# coding: utf-8

"""
M4300 REST API

M4300 REST API with ConfigAgent Documentation.

The version of the OpenAPI document: 2.0.0.59
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.auto_voip_cfg_post_protocol_based import (
    AutoVoipCfgPostProtocolBased,
)


class TestAutoVoipCfgPostProtocolBased(unittest.TestCase):
    """AutoVoipCfgPostProtocolBased unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AutoVoipCfgPostProtocolBased:
        """Test AutoVoipCfgPostProtocolBased
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AutoVoipCfgPostProtocolBased`
        """
        model = AutoVoipCfgPostProtocolBased()
        if include_optional:
            return AutoVoipCfgPostProtocolBased(
                prioritization_type = 'traffic-class',
                class_value = 0,
                mode = True
            )
        else:
            return AutoVoipCfgPostProtocolBased(
                prioritization_type = 'traffic-class',
                class_value = 0,
                mode = True,
        )
        """

    def testAutoVoipCfgPostProtocolBased(self):
        """Test AutoVoipCfgPostProtocolBased"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

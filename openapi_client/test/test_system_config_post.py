# coding: utf-8

"""
M4300 REST API

M4300 REST API with ConfigAgent Documentation.

The version of the OpenAPI document: 2.0.0.59
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.system_config_post import SystemConfigPost


class TestSystemConfigPost(unittest.TestCase):
    """SystemConfigPost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemConfigPost:
        """Test SystemConfigPost
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SystemConfigPost`
        """
        model = SystemConfigPost()
        if include_optional:
            return SystemConfigPost(
                sys_line_terminal_default_len = 56,
                sys_line_terminal_len = 56,
                sys_serial_time_out_default = 56,
                sys_serial_time_out = 56,
                sys_telnet_server_admin_mode = 'enabled',
                sys_transfer_bytes_completed = 56
            )
        else:
            return SystemConfigPost(
                sys_line_terminal_default_len = 56,
                sys_line_terminal_len = 56,
                sys_serial_time_out_default = 56,
                sys_serial_time_out = 56,
                sys_telnet_server_admin_mode = 'enabled',
                sys_transfer_bytes_completed = 56,
        )
        """

    def testSystemConfigPost(self):
        """Test SystemConfigPost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

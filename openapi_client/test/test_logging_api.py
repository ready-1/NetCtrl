# coding: utf-8

"""
M4300 REST API

M4300 REST API with ConfigAgent Documentation.

The version of the OpenAPI document: 2.0.0.59
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.logging_api import LoggingApi


class TestLoggingApi(unittest.TestCase):
    """LoggingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LoggingApi()

    def tearDown(self) -> None:
        pass

    def test_device_log_reader_get(self) -> None:
        """Test case for device_log_reader_get"""
        pass


if __name__ == "__main__":
    unittest.main()

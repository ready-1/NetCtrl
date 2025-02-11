# coding: utf-8

"""
M4300 REST API

M4300 REST API with ConfigAgent Documentation.

The version of the OpenAPI document: 2.0.0.59
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.logout_post200_response import LogoutPost200Response


class TestLogoutPost200Response(unittest.TestCase):
    """LogoutPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LogoutPost200Response:
        """Test LogoutPost200Response
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `LogoutPost200Response`
        """
        model = LogoutPost200Response()
        if include_optional:
            return LogoutPost200Response(
                resp = openapi_client.models.general_responses_code.general_responses_code(
                    status = 'success',
                    resp_code = 0,
                    resp_msg = 'Operation success', )
            )
        else:
            return LogoutPost200Response(
        )
        """

    def testLogoutPost200Response(self):
        """Test LogoutPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

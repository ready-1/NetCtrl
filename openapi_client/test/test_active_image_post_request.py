# coding: utf-8

"""
M4300 REST API

M4300 REST API with ConfigAgent Documentation.

The version of the OpenAPI document: 2.0.0.59
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.active_image_post_request import ActiveImagePostRequest


class TestActiveImagePostRequest(unittest.TestCase):
    """ActiveImagePostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActiveImagePostRequest:
        """Test ActiveImagePostRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ActiveImagePostRequest`
        """
        model = ActiveImagePostRequest()
        if include_optional:
            return ActiveImagePostRequest(
                active_image = openapi_client.models.active_image_post.active_image_post(
                    label = 'image1', )
            )
        else:
            return ActiveImagePostRequest(
        )
        """

    def testActiveImagePostRequest(self):
        """Test ActiveImagePostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

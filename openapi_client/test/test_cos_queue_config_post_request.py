# coding: utf-8

"""
M4300 REST API

M4300 REST API with ConfigAgent Documentation.

The version of the OpenAPI document: 2.0.0.59
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.cos_queue_config_post_request import (
    CosQueueConfigPostRequest,
)


class TestCosQueueConfigPostRequest(unittest.TestCase):
    """CosQueueConfigPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CosQueueConfigPostRequest:
        """Test CosQueueConfigPostRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CosQueueConfigPostRequest`
        """
        model = CosQueueConfigPostRequest()
        if include_optional:
            return CosQueueConfigPostRequest(
                cos_queue_config = [{"id":"0","min_bw":"1","mgmt_type":"TailDrop","schedule_type":"Weighted"},{"id":"1","min_bw":"1","mgmt_type":"WRED","schedule_type":"Strict"},{"id":"2","min_bw":"1","mgmt_type":"TailDrop","schedule_type":"Weighted"},{"id":"3","min_bw":"1","mgmt_type":"WRED","schedule_type":"Strict"},{"id":"4","min_bw":"1","mgmt_type":"TailDrop","schedule_type":"Weighted"},{"id":"5","min_bw":"1","mgmt_type":"WRED","schedule_type":"Strict"},{"id":"6","min_bw":"1","mgmt_type":"TailDrop","schedule_type":"Weighted"},{"id":"7","min_bw":"1","mgmt_type":"WRED","schedule_type":"Strict"}]
            )
        else:
            return CosQueueConfigPostRequest(
        )
        """

    def testCosQueueConfigPostRequest(self):
        """Test CosQueueConfigPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

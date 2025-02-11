# coding: utf-8

"""
M4300 REST API

M4300 REST API with ConfigAgent Documentation.

The version of the OpenAPI document: 2.0.0.59
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.fiber_optics_get200_response import FiberOpticsGet200Response


class TestFiberOpticsGet200Response(unittest.TestCase):
    """FiberOpticsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FiberOpticsGet200Response:
        """Test FiberOpticsGet200Response
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `FiberOpticsGet200Response`
        """
        model = FiberOpticsGet200Response()
        if include_optional:
            return FiberOpticsGet200Response(
                resp = openapi_client.models.general_responses_code.general_responses_code(
                    status = 'success',
                    resp_code = 0,
                    resp_msg = 'Operation success', ),
                fiber_optics = {"port":"1/0/1","temp":1,"voltage":1,"current":1,"outputPower":1,"inputPower":1,"txFault":1,"los":1,"faultStatus":"No Fault","vendorName":"NETGEAR","linkLength_50_um":0,"linkLength_62.5_um":0,"linkLength":"1M","serialNumber":"M7A05393","partNumber":"CABSFP10G1MNC","nominalBitRate":10000,"rev":"C","compliance":"DAC","Supported":true,"possibleSpeedDetected":"10G"}
            )
        else:
            return FiberOpticsGet200Response(
        )
        """

    def testFiberOpticsGet200Response(self):
        """Test FiberOpticsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

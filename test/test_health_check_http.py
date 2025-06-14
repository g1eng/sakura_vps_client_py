# coding: utf-8

"""
    さくらのVPS APIドキュメント

    Sakura VPS API client written in Python (generated with openapi-generator)

    The version of the OpenAPI document: 5.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sakura_vps_client_py.models.health_check_http import HealthCheckHttp

class TestHealthCheckHttp(unittest.TestCase):
    """HealthCheckHttp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HealthCheckHttp:
        """Test HealthCheckHttp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HealthCheckHttp`
        """
        model = HealthCheckHttp()
        if include_optional:
            return HealthCheckHttp(
                port = 80,
                host = '0',
                path = '/',
                basic_auth_username = '0',
                basic_auth_password = '0',
                status = 100,
                interval_minutes = 1,
                protocol = 'http'
            )
        else:
            return HealthCheckHttp(
                port = 80,
                host = '0',
                path = '/',
                basic_auth_username = '0',
                basic_auth_password = '0',
                status = 100,
                interval_minutes = 1,
                protocol = 'http',
        )
        """

    def testHealthCheckHttp(self):
        """Test HealthCheckHttp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

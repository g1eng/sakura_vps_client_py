# coding: utf-8

"""
    さくらのVPS APIドキュメント

    Sakura VPS API client written in Python (generated with openapi-generator)

    The version of the OpenAPI document: 5.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sakura_vps_client_py.models.nfs_server_power_status import NfsServerPowerStatus

class TestNfsServerPowerStatus(unittest.TestCase):
    """NfsServerPowerStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NfsServerPowerStatus:
        """Test NfsServerPowerStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NfsServerPowerStatus`
        """
        model = NfsServerPowerStatus()
        if include_optional:
            return NfsServerPowerStatus(
                status = 'power_on'
            )
        else:
            return NfsServerPowerStatus(
                status = 'power_on',
        )
        """

    def testNfsServerPowerStatus(self):
        """Test NfsServerPowerStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

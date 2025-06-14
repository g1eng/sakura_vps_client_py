# coding: utf-8

"""
    さくらのVPS APIドキュメント

    Sakura VPS API client written in Python (generated with openapi-generator)

    The version of the OpenAPI document: 5.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sakura_vps_client_py.api.zone_api import ZoneApi


class TestZoneApi(unittest.TestCase):
    """ZoneApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ZoneApi()

    def tearDown(self) -> None:
        pass

    def test_get_zone_list(self) -> None:
        """Test case for get_zone_list

        ゾーン情報一覧を取得する
        """
        pass


if __name__ == '__main__':
    unittest.main()

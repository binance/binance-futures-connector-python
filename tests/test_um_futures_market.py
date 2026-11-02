import unittest
from unittest.mock import Mock

from binance.um_futures import UMFutures


class FundingInfoTests(unittest.TestCase):
    def test_funding_rate_keeps_using_funding_rate_endpoint(self):
        client = UMFutures()
        client.query = Mock(return_value=[])

        result = client.funding_rate("BTCUSDT")

        client.query.assert_called_once_with(
            "/fapi/v1/fundingRate", {"symbol": "BTCUSDT"}
        )
        self.assertEqual([], result)

    def test_uses_funding_info_endpoint(self):
        client = UMFutures()
        response = [{"symbol": "BTCUSDT", "fundingIntervalHours": 8}]
        client.query = Mock(return_value=response)

        result = client.funding_info()

        client.query.assert_called_once_with("/fapi/v1/fundingInfo")
        self.assertIs(response, result)

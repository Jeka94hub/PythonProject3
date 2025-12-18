import unittest
from unittest.mock import patch, Mock
import requests
from src.external_api import get_exchange_rates

class TestExternalApi(unittest.TestCase):

    @patch('external_api.requests.get')
    def test_get_exchange_rates_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            'rates': {'USD': 75.0, 'EUR': 88.0}
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        rates = get_exchange_rates()
        self.assertEqual(rates['USD'], 75.0)
        self.assertEqual(rates['EUR'], 88.0)

    @patch('external_api.requests.get')
    def test_get_exchange_rates_http_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.HTTPError()
        mock_get.return_value = mock_response

        with self.assertRaises(requests.HTTPError):
            get_exchange_rates()

if __name__ == '__main__':
    unittest.main()


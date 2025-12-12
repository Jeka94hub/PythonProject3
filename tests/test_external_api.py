from src.external_api import convert_to_rub, CurrencyConversionError
from unittest.mock import patch


@patch("src.external_api.API_KEY", "fake_key")
@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 7500.0}

    result = convert_to_rub(100, "USD")

    assert result == 7500.0


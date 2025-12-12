from unittest.mock import patch
from src.transaction import get_transaction_amount


@patch("src.transaction.convert_to_rub")
def test_get_transaction_amount(mock_convert):
    mock_convert.return_value = 5000.0

    tx = {"amount": 50, "currency": "USD"}
    result = get_transaction_amount(tx)

    assert result == 5000.0
    mock_convert.assert_called_once_with(50, "USD")


def test_get_transaction_amount_rub():
    tx = {"amount": 300, "currency": "RUB"}

    #  RUB не трогаем, но convert_to_rub всё равно вызывается
    # так что можно протестировать возврат 1:1 через мок
    with patch("src.transaction.convert_to_rub", return_value=300):
        result = get_transaction_amount(tx)
        assert result == 300


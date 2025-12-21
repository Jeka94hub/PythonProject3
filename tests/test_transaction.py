import unittest
from unittest.mock import patch
from src.transaction import get_transaction_amount


class TestTransactionAmount(unittest.TestCase):

    @patch('external_api.convert_to_rubles')
    def test_get_transaction_amount(self, mock_convert):
        # Настраиваем возврат функции mock
        mock_convert.side_effect = lambda amount, currency: amount * (70 if currency == 'USD' else 1)

        # Тестовая транзакция
        transaction = {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-10-10T10:00:00",
            "operationAmount": {
                "amount": "10",
                "currency": {"name": "USD", "code": "USD"}
            }
        }

        result = get_transaction_amount(transaction)
        self.assertEqual(result, 10 * 70)  # Ожидаемый результат: 700

        # Еще один тест — для случая, когда валюта — RUB
        transaction_rub = {
            "operationAmount": {
                "amount": "5",
                "currency": {"name": "RUB", "code": "RUB"}
            }
        }

        result_rub = get_transaction_amount(transaction_rub)
        self.assertEqual(result_rub, 5 * 1)  # Ожидаемый результат: 5

if __name__ == '__main__':
    unittest.main()
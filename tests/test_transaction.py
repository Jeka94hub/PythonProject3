# Тест с использованием встроенного модуля unittest
import unittest
from src.external_api import convert_to_rubles
from src.transaction import get_transaction_amount

# Мокаем функцию convert_to_rubles
def mock_convert_to_rubles(amount, currency):
    rates = {"USD": 70, "EUR": 80, "RUB": 1}
    return amount * rates.get(currency, 1)

class TestGetTransactionAmount(unittest.TestCase):
    def setUp(self):
        global convert_to_rubles
        self._original_convert = convert_to_rubles
        convert_to_rubles = mock_convert_to_rubles

    def tearDown(self):
        global convert_to_rubles
        convert_to_rubles = self._original_convert

    def test_valid_transaction(self):
        transaction = {
            "operationAmount": {
                "amount": "100",
                "currency": {"name": "USD", "code": "USD"}
            }
        }
        result = get_transaction_amount(transaction)
        self.assertEqual(result, 7000)  # 100 * 70

    def test_missing_amount(self):
        transaction = {
            "operationAmount": {
                "currency": {"name": "USD", "code": "USD"}
            }
        }
        with self.assertRaises(ValueError):
            get_transaction_amount(transaction)

    def test_missing_currency_code(self):
        transaction = {
            "operationAmount": {
                "amount": "50",
                "currency": {}  # Нет кода валюты
            }
        }
        result = get_transaction_amount(transaction)
        self.assertEqual(result, 50)  # Предполагается, что это в рублях

    def test_invalid_amount(self):
        transaction = {
            "operationAmount": {
                "amount": "abc",
                "currency": {"name": "EUR", "code": "EUR"}
            }
        }
        with self.assertRaises(ValueError):
            get_transaction_amount(transaction)

if __name__ == "__main__":
    unittest.main()
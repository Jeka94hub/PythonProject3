import unittest
from unittest.mock import patch, Mock
from src.transaction_processor import get_transaction_amount_in_rub
from src.external_api import convert_to_rub # Импортируем для того, чтобы использовать patch

class TestTransactionProcessor(unittest.TestCase):

    @patch('transaction_processor.convert_to_rub') # Мокируем функцию convert_to_rub
    def test_get_transaction_amount_in_rub_with_rub(self, mock_convert_to_rub):
        """Тестируем получение суммы в рублях."""
        transaction = {"amount": 100.50, "currency": "RUB"}
        # Убедимся, что convert_to_rub вызывается с правильными аргументами
        # и возвращает ожидаемое значение (даже если она была замокана)
        mock_convert_to_rub.return_value = 100.50
        result = get_transaction_amount_in_rub(transaction)
        self.assertEqual(result, 100.50)
        mock_convert_to_rub.assert_called_once_with(100.50, "RUB")

    @patch('transaction_processor.convert_to_rub')
    def test_get_transaction_amount_in_rub_with_usd(self, mock_convert_to_rub):
        """Тестируем получение суммы в рублях из USD."""
        transaction = {"amount": 50.00, "currency": "USD"}
        # Задаем возвращаемое значение для мока
        mock_convert_to_rub.return_value = 4500.75 # Примерный курс: 1 USD = 90.015 RUB
        result = get_transaction_amount_in_rub(transaction)
        self.assertEqual(result, 4500.75)
        mock_convert_to_rub.assert_called_once_with(50.00, "USD")

    @patch('transaction_processor.convert_to_rub')
    def test_get_transaction_amount_in_rub_with_eur(self, mock_convert_to_rub):
        """Тестируем получение суммы в рублях из EUR."""
        transaction = {"amount": 75.00, "currency": "EUR"}
        mock_convert_to_rub.return_value = 7200.00 # Примерный курс: 1 EUR = 96.00 RUB
        result = get_transaction_amount_in_rub(transaction)
        self.assertEqual(result, 7200.00)
        mock_convert_to_rub.assert_called_once_with(75.00, "EUR")

    def test_get_transaction_amount_in_rub_invalid_transaction(self):
        """Тестируем некорректный формат транзакции."""
        with self.assertRaisesRegex(ValueError, "Некорректный формат транзакции"):
            get_transaction_amount_in_rub({"amount": 100}) # Нет currency
        with self.assertRaisesRegex(ValueError, "Некорректный формат транзакции"):
            get_transaction_amount_in_rub({"currency": "USD"}) # Нет amount
        with self.assertRaisesRegex(ValueError, "Некорректный формат транзакции"):
            get_transaction_amount_in_rub({}) # Пустой словарь

# --- Тесты для функции convert_to_rub (требуют мокирования requests) ---

# Для тестирования convert_to_rub нам потребуется мокировать `requests.get`
# и `external_api.get_exchange_rate`
class TestExternalApi(unittest.TestCase):

    @patch('external_api.get_exchange_rate') # Мокируем функцию получения курса
    def test_convert_to_rub_with_usd(self, mock_get_exchange_rate):
        """Тестируем конвертацию USD в RUB."""
        # Устанавливаем возвращаемое значение для get_exchange_rate
        mock_get_exchange_rate.return_value = 90.015
        result = convert_to_rub(50.00, "USD")
        self.assertEqual(result, 4500.75)
        mock_get_exchange_rate.assert_called_once_with("USD")

    @patch('external_api.get_exchange_rate')
    def test_convert_to_rub_with_eur(self, mock_get_exchange_rate):
        """Тестируем конвертацию EUR в RUB."""
        mock_get_exchange_rate.return_value = 96.00
        result = convert_to_rub(75.00, "EUR")
        self.assertEqual(result, 7200.00)
        mock_get_exchange_rate.assert_called_once_with("EUR")

    def test_convert_to_rub_with_rub(self):
        """Тестируем конвертацию RUB в RUB (должна быть 1:1)."""
        result = convert_to_rub(150.00, "RUB")
        self.assertEqual(result, 150.00)

    def test_convert_to_rub_unsupported_currency(self):
        """Тестируем неподдерживаемую валюту."""
        with self.assertRaisesRegex(ValueError, "Валюта GBP не поддерживается"):
            convert_to_rub(100.00, "GBP")

    # Пример того, как можно мокировать `requests.get` внутри `get_exchange_rate`
    # Это более сложный случай, но полезен, если вам нужно тестировать именно `get_exchange_rate`
    @patch('external_api.requests.get')
    def test_get_exchange_rate_success(self, mock_requests_get):
        """Тестируем успешное получение курса валюты."""
        # Создаем объект Mock для ответа requests
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None # Имитируем успешный запрос
        mock_response.json.return_value = {
            "success": True,
            "rates": {"USD": 90.015}
        }
        mock_requests_get.return_value = mock_response

        # Устанавливаем API ключ для теста (можно через os.environ или мокировать os.environ.get)
        with patch.dict(os.environ, {"EXCHANGE_RATES_API_KEY": "test_api_key"}):
            rate = get_exchange_rate("USD")
            self.assertEqual(rate, 90.015)
            mock_requests_get.assert_called_once_with(
                "http://api.exchangeratesapi.io/v1/latest?access_key=test_api_key&symbols=USD&base=RUB"
            )

    @patch('external_api.requests.get')
    def test_get_exchange_rate_api_error(self, mock_requests_get):
        """Тестируем ошибку API при получении курса."""
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "success": False,
            "error": {"code": 105, "type": "missing_api_key", "info": "Invalid API key."}
        }
        mock_requests_get.return_value = mock_response

        with patch.dict(os.environ, {"EXCHANGE_RATES_API_KEY": "invalid_key"}):
            with self.assertRaisesRegex(Exception, "Invalid API key."):
                get_exchange_rate("USD")

    @patch('external_api.requests.get')
    def test_get_exchange_rate_connection_error(self, mock_requests_get):
        """Тестируем ошибку соединения."""
        mock_requests_get.side_effect = requests.exceptions.ConnectionError("Network error")

        with patch.dict(os.environ, {"EXCHANGE_RATES_API_KEY": "test_api_key"}):
            with self.assertRaisesRegex(ConnectionError, "Не удалось подключиться к API курсов валют: Network error"):
                get_exchange_rate("USD")

    # Пример теста на отсутствие API ключа
    @patch('external_api.requests.get')
    def test_get_exchange_rate_no_api_key(self, mock_requests_get):
        """Тестируем случай, когда API ключ отсутствует."""
        # Убедимся, что os.environ.get возвращает None
        with patch.dict(os.environ, {"EXCHANGE_RATES_API_KEY": None}):
             with self.assertRaisesRegex(ValueError, "API ключ для Exchange Rates Data API не найден"):
                get_exchange_rate("USD")
        # Убедимся, что requests.get не вызывается, если ключ не найден
        mock_requests_get.assert_not_called()

if __name__ == '__main__':
    unittest.main()



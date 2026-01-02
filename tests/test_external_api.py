import unittest
from unittest.mock import patch, Mock
import os
import requests # Нужен для имитации ошибок requests

# Предполагаем, что ваш файл называется external_api.py
from src import external_api

class TestExternalApi(unittest.TestCase):

    # --- Тесты для get_exchange_rate ---

    # Убедимся, что API ключ есть в окружении для этого теста
    @patch.dict('os.environ', {'EXCHANGE_RATES_API_KEY': 'my_fake_api_key'})
    # Замокируем requests.get, чтобы он не делал реальных запросов
    @patch('external_api.requests.get')
    def test_get_exchange_rate_success(self, mock_requests_get):
        """Проверяем, что курс валюты успешно получается."""
        # Создаем мок-объект для ответа от requests.get
        mock_response = Mock()
        # Указываем, какой JSON-ответ должен вернуть мок
        mock_response.json.return_value = {"success": True, "rates": {"USD": 75.0}}
        # Указываем, что метод raise_for_status() ничего не должен делать (нет ошибок)
        mock_response.raise_for_status.return_value = None
        # Говорим mock_requests_get вернуть наш мок-ответ
        mock_requests_get.return_value = mock_response

        # Вызываем функцию, которую тестируем
        rate = external_api.get_exchange_rate("USD")

        # Проверяем, что requests.get был вызван ровно 1 раз
        mock_requests_get.assert_called_once()
        # Проверяем, что мы получили правильный курс
        self.assertEqual(rate, 75.0)

    @patch.dict('os.environ', {'EXCHANGE_RATES_API_KEY': 'my_fake_api_key'})
    @patch('external_api.requests.get')
    def test_get_exchange_rate_api_returns_error(self, mock_requests_get):
        """Проверяем, что происходит при ошибке от API."""
        mock_response = Mock()
        # Имитируем ответ API с ошибкой
        mock_response.json.return_value = {"success": False, "error": {"code": 101, "type": "invalid_access_key", "info": "API ключ недействителен"}}
        mock_response.raise_for_status.return_value = None
        mock_requests_get.return_value = mock_response

        # Ожидаем, что при вызове функции будет выброшено исключение RuntimeError
        with self.assertRaises(RuntimeError):
            external_api.get_exchange_rate("USD")
        # Проверяем, что requests.get был вызван
        mock_requests_get.assert_called_once()

    @patch.dict('os.environ', {'EXCHANGE_RATES_API_KEY': 'my_fake_api_key'})
    @patch('external_api.requests.get')
    def test_get_exchange_rate_currency_not_found(self, mock_requests_get):
        """Проверяем случай, когда валюты нет в ответе API."""
        mock_response = Mock()
        # API ответил, но нужной валюты нет
        mock_response.json.return_value = {"success": True, "rates": {"EUR": 80.0}}
        mock_response.raise_for_status.return_value = None
        mock_requests_get.return_value = mock_response

        # Ожидаем исключение, так как USD не в "rates"
        with self.assertRaises(Exception):
            external_api.get_exchange_rate("USD")
        mock_requests_get.assert_called_once()

    # Убираем API ключ для этого теста
    @patch.dict('os.environ', {}, clear=True)
    def test_get_exchange_rate_missing_api_key(self):
        """Проверяем, что будет, если API ключа нет."""
        # Ожидаем ValueError, если ключ не найден
        with self.assertRaises(ValueError):
            external_api.get_exchange_rate("USD")

    @patch.dict('os.environ', {'EXCHANGE_RATES_API_KEY': 'my_fake_api_key'})
    @patch('external_api.requests.get')
    def test_get_exchange_rate_connection_error(self, mock_requests_get):
        """Проверяем обработку ошибки сети."""
        # Заставляем requests.get вызвать ошибку соединения
        mock_requests_get.side_effect = requests.exceptions.RequestException("Нет сети")

        # Ожидаем ConnectionError
        with self.assertRaises(ConnectionError):
            external_api.get_exchange_rate("USD")
        mock_requests_get.assert_called_once()


    # --- Тесты для convert_to_rub ---

    # Нам нужно замокировать get_exchange_rate, потому что convert_to_rub ее вызывает
    # Патчим функцию в том модуле, где она используется (external_api)
    @patch('external_api.get_exchange_rate')
    def test_convert_to_rub_is_rub(self, mock_get_exchange_rate):
        """Конвертация из RUB в RUB должна просто вернуть сумму."""
        result = external_api.convert_to_rub(100, "RUB")
        # Проверяем, что get_exchange_rate не вызывалась
        mock_get_exchange_rate.assert_not_called()
        # Проверяем, что результат верный
        self.assertEqual(result, 100.0)

    @patch('external_api.get_exchange_rate')
    def test_convert_to_rub_from_usd(self, mock_get_exchange_rate):
        """Конвертация из USD в RUB."""
        # Устанавливаем, какой результат должна вернуть замокированная get_exchange_rate
        mock_get_exchange_rate.return_value = 75.0 # Курс USD
        # Вызываем функцию конвертации
        result = external_api.convert_to_rub(50, "USD") # 50 USD

        # Проверяем, что get_exchange_rate была вызвана с правильным кодом валюты
        mock_get_exchange_rate.assert_called_once_with("USD")
        # Проверяем, что результат конвертации правильный (50 * 75.0)
        self.assertEqual(result, 3750.0)

    @patch('external_api.get_exchange_rate')
    def test_convert_to_rub_from_eur(self, mock_get_exchange_rate):
        """Конвертация из EUR в RUB."""
        mock_get_exchange_rate.return_value = 85.5 # Курс EUR
        result = external_api.convert_to_rub(20, "EUR") # 20 EUR

        mock_get_exchange_rate.assert_called_once_with("EUR")
        self.assertEqual(result, 20 * 85.5)

    def test_convert_to_rub_unsupported_currency(self):
        """Проверяем, что для неподдерживаемых валют выбрасывается ошибка."""
        # Ожидаем ValueError для валюты CHF
        with self.assertRaises(ValueError):
            external_api.convert_to_rub(100, "CHF")


    # --- Тесты для get_transaction_amount_in_rub ---

    # Здесь мы можем не мокировать convert_to_rub, если хотим проверить её работу вместе с get_transaction_amount_in_rub
    # Но для большей чистоты тестов, часто мокируют и её тоже. Давайте замокируем.
    @patch('external_api.convert_to_rub')
    def test_get_transaction_amount_in_rub_valid_transaction(self, mock_convert_to_rub):
        """Проверка корректно сформированной транзакции."""
        # Устанавливаем, что convert_to_rub должна вернуть 1000.0
        mock_convert_to_rub.return_value = 1000.0

        transaction = {"amount": 10, "currency": "USD"}
        result = external_api.get_transaction_amount_in_rub(transaction)

        # Проверяем, что convert_to_rub была вызвана с правильными данными
        mock_convert_to_rub.assert_called_once_with(10, "USD")
        # Проверяем, что результат такой же, как вернула convert_to_rub
        self.assertEqual(result, 1000.0)

    def test_get_transaction_amount_in_rub_missing_amount(self):
        """Проверяем транзакцию без поля 'amount'."""
        transaction = {"currency": "USD"}
        # Ожидаем ValueError
        with self.assertRaises(ValueError):
            external_api.get_transaction_amount_in_rub(transaction)

    def test_get_transaction_amount_in_rub_missing_currency(self):
        """Проверяем транзакцию без поля 'currency'."""
        transaction = {"amount": 100}
        # Ожидаем ValueError
        with self.assertRaises(ValueError):
            external_api.get_transaction_amount_in_rub(transaction)

    def test_get_transaction_amount_in_rub_empty_transaction(self):
        """Проверяем пустую транзакцию."""
        transaction = {}
        # Ожидаем ValueError
        with self.assertRaises(ValueError):
            external_api.get_transaction_amount_in_rub(transaction)


import unittest
from unittest.mock import patch
from src.utils import load_transactions_from_file
from src.external_api import convert_to_rubles

class TestUtils(unittest.TestCase):

    def test_load_transactions_empty_file(self):
        data = load_transactions_from_file('nonexistent.json')
        self.assertEqual(data, [])

    def test_load_transactions_invalid_json(self):
        # Создайте временный файл с некорректным JSON
        import tempfile
        with tempfile.NamedTemporaryFile('w+', delete=False) as tmp:
            tmp.write('invalid json')
            tmp_name = tmp.name
        result = load_transactions_from_file(tmp_name)
        self.assertEqual(result, [])
        os.remove(tmp_name)

    def test_load_transactions_not_list(self):
        import tempfile
        with tempfile.NamedTemporaryFile('w+', delete=False) as tmp:
            json.dump({"key": "value"}, tmp)
            tmp_name = tmp.name
        result = load_transactions_from_file(tmp_name)
        self.assertEqual(result, [])
        os.remove(tmp_name)

    def test_load_transactions_valid_list(self):
        import tempfile
        sample_data = [{"amount": "100", "currency": "RUB"}]
        with tempfile.NamedTemporaryFile('w+', delete=False) as tmp:
            json.dump(sample_data, tmp)
            tmp_name = tmp.name
        result = load_transactions_from_file(tmp_name)
        self.assertEqual(result, sample_data)
        os.remove(tmp_name)

    @patch('external_api.get_exchange_rates')
    def test_convert_transaction_amount_usd(self, mock_get_rates):
        mock_get_rates.return_value = {'USD': 75.0, 'EUR': 88.0}
        amount = 10
        self.assertAlmostEqual(convert_to_rubles(amount, 'USD'), 750.0)

    @patch('external_api.get_exchange_rates')
    def test_convert_transaction_amount_eur(self, mock_get_rates):
        mock_get_rates.return_value = {'USD': 75.0, 'EUR': 88.0}
        amount = 5
        self.assertAlmostEqual(convert_to_rubles(amount, 'EUR'), 440.0)

    def test_convert_transaction_amount_rub(self):
        self.assertEqual(convert_to_rubles(55, 'RUB'), 55)

if __name__ == '__main__':
    unittest.main()
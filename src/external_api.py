import os
import requests

API_TOKEN = os.getenv('EXCHANGE_API_TOKEN')

def get_exchange_rates():
    url = "https://api.apilayer.com/exchangerates_data/latest"
    headers = {"apikey": API_TOKEN}
    params = {
        "symbols": "USD,EUR",
        "base": "RUB"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    return data['rates']

def convert_to_rubles(amount, currency):
    """
    Конвертирует сумму из валюты currency в рубли с помощью API.
    """
    rates = get_exchange_rates()
    if currency == 'RUB':
        return float(amount)
    elif currency in ('USD', 'EUR'):
        rate = rates.get(currency)
        if rate is None:
            raise ValueError(f"Нет курса для валюты {currency}")
        return float(amount) * rate
    else:
        raise ValueError(f"Неизвестная валюта: {currency}")



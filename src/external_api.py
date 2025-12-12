import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


class CurrencyConversionError(Exception):
    pass


def convert_to_rub(amount: float, currency: str) -> float:
    """
    Конвертирует сумму из USD или EUR в RUB через Exchange Rates Data API.
    """
    if currency == "RUB":
        return amount

    if API_KEY is None:
        raise CurrencyConversionError("API key not found in environment variables")

    params = {
        "to": "RUB",
        "from": currency,
        "amount": amount
    }

    headers = {"apikey": API_KEY}

    response = requests.get(BASE_URL, params=params, headers=headers)

    if response.status_code != 200:
        raise CurrencyConversionError("API request failed")

    data = response.json()

    if "result" not in data:
        raise CurrencyConversionError("Invalid API response")

    return float(data["result"])


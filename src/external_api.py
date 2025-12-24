import os
import requests

def get_exchange_rate(currency_code):
    """
    Получает текущий обменный курс для указанной валюты по отношению к RUB.
    Использует API Exchange Rates Data API.
    """
    api_key = os.environ.get("EXCHANGE_RATES_API_KEY")
    if not api_key:
        raise ValueError("API ключ для Exchange Rates Data API не найден в переменных окружения.")

    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}&symbols={currency_code}&base=RUB"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Вызывает исключение для плохих ответов (4xx или 5xx)
        data = response.json()
        if data.get("success"):
            return data["rates"][currency_code]
        else:
            raise Exception(f"Ошибка API: {data.get('error', {}).get('info')}")
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Не удалось подключиться к API курсов валют: {e}")
    except Exception as e:
        raise RuntimeError(f"Ошибка при получении курса валют: {e}")

def convert_to_rub(amount, currency_code):
    """
    Конвертирует сумму из указанной валюты в рубли.
    """
    if currency_code == "RUB":
        return float(amount)
    elif currency_code in ["USD", "EUR"]:
        rate = get_exchange_rate(currency_code)
        return float(amount) * rate
    else:
        raise ValueError(f"Валюта {currency_code} не поддерживается для конвертации.")




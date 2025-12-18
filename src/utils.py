import json
import os
from .external_api import convert_to_rubles

def load_transactions_from_file(file_path):
    """
    Загружает список транзакций из файла JSON.
    Возвращает пустой список, если файл пустой, содержит не список или не найден.
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        else:
            return []
    except (json.JSONDecodeError, FileNotFoundError):
        return []




from external_api import convert_to_rubles

def get_transaction_amount_in_rubles(transaction):
    """
    Принимает словарь транзакции и возвращает сумму в рублях (float).
    """
    amount = float(transaction['amount'])
    currency = transaction['currency']
    return convert_to_rubles(amount, currency)
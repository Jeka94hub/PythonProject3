import json
import os

def load_transactions_simple(file_path):
    """ Функция для загрузки транзакций из JSON """
    try:

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                print("Файл не содержит список.")
                return []
    except FileNotFoundError:
        # Если файла нет, говорим об этом и возвращаем пустой список
        print(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        # Если JSON некорректный (например, файл пустой или с ошибкой)
        print(f"Ошибка в формате JSON файла: {file_path}")
        return []
    except Exception as e:
        # Ловим любые другие ошибки на всякий случай
        print(f"Произошла другая ошибка: {e}")
        return []




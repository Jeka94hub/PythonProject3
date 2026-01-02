import json
import logging.config
import os

logs_path = "../logs"
log_file = os.path.join(logs_path, "utils.log")
# Создаем логгер
logger = logging.getLogger(__name__)
# Проверяем существуют ли уже обработчики у логов
if not logger.handlers:
    logger.setLevel(logging.DEBUG)

    # Создаем папку для логов
    if not os.path.exists(logs_path):
         os.makedirs(logs_path)

    # Настраиваем форматтер
    file_handler = logging.FileHandler(log_file, mode= 'w', encoding = 'utf-8')
    file_handler. setLevel(logging.DEBUG)
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)



def load_transactions_simple(file_path):
    """ Функция для загрузки транзакций из JSON """
    # Логируем начало выполнения функции
    logger.debug(f"Начало загрузки транзакций из файла: {file_path}")
    try:

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f'Транзакции успешно загружены из {file_path}. Количество записей: {len(data)}')
                return data
            else:
                # Логируем ошибку, если данные не являются списком
                logger.error(f' Данные в файле {file_path} не являются списком. Получено: {type(data)}')
                print("Файл не содержит список.")
                return []
    except FileNotFoundError:
        # Логируем ошибку если файл не найден
        logger.error(f'Файл не найден: {file_path}')
        print(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        # Логируем ошибку если JSON не корректный
        logger.error(f'Ошибка в формате JSON файла: {file_path}')
        print(f"Ошибка в формате JSON файла: {file_path}")
        return []
    except Exception as e:
        # Логируем любые другие ошибки
        logger.error(f'Произошла другая ошибка {file_path}: {e}', exc_info=True)
        print(f"Произошла другая ошибка: {e}")
        return []





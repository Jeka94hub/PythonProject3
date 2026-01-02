import logging
import os

# Определяем путь к файлу логов. Создаем папку logs, если она не существует.
log_path = "logs"
log_file = os.path.join(log_path, "masks.log")

# Создаем логер для модуля 'masks'
logger = logging.getLogger('masks')

# Добавляем файловый обработчик к логеру
# Проверяем, есть ли уже обработчики, чтобы избежать дублирования при повторном запуске
if not logger.handlers:
    logger.setLevel(logging.DEBUG)

    # Создаем папку для логов
    if not os.path.exists(log_path):
        os.makedirs(log_path)
log_file = os.path.join(log_path, "masks.log")
file_handler = logging.FileHandler(log_file, mode='w', encoding ='utf-8')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате: XXXX XX** **** XXXX"""
    try:
        digits = card_number.replace(" ", "")
        if len(digits) != 16 or not digits.isdigit():
            logger.error(f"Invalid card number format: {card_number}. Expected 16 digits.")
            raise ValueError("Card number too short to mask")

        masked = (
            digits[0:4] + " "
            + digits[4:6] + "** "
            + "**** "
            + digits[12:16]
        )
        logger.debug(f"Card number {card_number} masked successfully to {masked}")
        return masked
    except ValueError as e:
        logger.error(f"Error masking card number {card_number}: {e}")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred while masking card number {card_number}: {e}")
        raise

def get_mask_account(account_number: str) -> str :
    """Маскирует номер счета в формате: **XXXX"""
    try:
        digits = account_number.replace(" ", "")
        if len(digits) < 4 or not digits.isdigit():
            logger.error(f"Invalid account number format: {account_number}. Expected at least 4 digits.")
            raise ValueError("Account number too short to mask")

        masked = "**" + digits[-4:]
        logger.debug(f"Account number {account_number} masked successfully to {masked}")
        return masked
    except ValueError as e:
        logger.error(f"Error masking account number {account_number}: {e}")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred while masking account number {account_number}: {e}")
        raise


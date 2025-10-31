import re

def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате ****XXXX (оставляет только последние 4 цифры)"""
    digits = card_number.replace(" ", "")
    if len(digits) != 16 or not digits.isdigit():
        raise ValueError("Card number too short to mask")
    return f"****{digits[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета в формате **XXXX (оставляет последние 4 цифры)"""
    digits = account_number.replace(" ", "")
    if len(digits) < 4 or not digits.isdigit():
        raise ValueError("Account number too short to mask")
    return f"**{digits[-4:]}"


def mask_account_card(text: str) -> str:
    """
    Маскирует карту или счёт в строке.
    - Карта: оставляем только последние 4 цифры
    - Счёт: оставляем только последние 4 цифры
    """
    # Ищем 16-значный номер карты
    card_match = re.search(r'\b\d{16}\b', text)
    if card_match:
        masked_card = get_mask_card_number(card_match.group())
        return text.replace(card_match.group(), masked_card)

    # Ищем длинный номер счёта (4+ цифр)
    account_match = re.search(r'\d{4,}', text)
    if account_match:
        masked_account = get_mask_account(account_match.group())
        return text.replace(account_match.group(), masked_account)

    return text

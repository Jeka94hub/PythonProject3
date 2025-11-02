import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    """Проверяем корректную маскировку номера карты"""
    card_number = "7000 7922 8960 6361"
    expected = "7000 79** **** 6361"
    result = get_mask_card_number(card_number)
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"

    # Проверка — без пробелов
    card_number_no_spaces = "7000792289606361"
    result = get_mask_card_number(card_number_no_spaces)
    assert result == expected, "Маскировка без пробелов работает некорректно"

    # Проверка — некорректный номер (слишком короткий)
    with pytest.raises(ValueError, match="Card number too short to mask"):
        get_mask_card_number("12345678")


def test_get_mask_account():
    """Проверяем корректную маскировку номера счёта"""
    account_number = "73654108430135874305"
    expected = "**4305"
    result = get_mask_account(account_number)
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"

    # Проверка — с пробелами
    account_with_spaces = "73 6541 0843 0135 8743 05"
    result = get_mask_account(account_with_spaces)
    assert result == expected, "Маскировка с пробелами работает некорректно"

    # Проверка — короткий номер
    with pytest.raises(ValueError, match="Account number too short to mask"):
        get_mask_account("123")
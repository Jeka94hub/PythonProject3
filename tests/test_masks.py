import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    # Общий случай
    card_number = "7000 7922 8960 6361"
    result = get_mask_card_number(card_number)
    expected = "****6361"
    assert result == expected, f"Ожидалось: {expected}, Получено: {result}"

    # Неправильная длина
    with pytest.raises(ValueError):
        get_mask_card_number("123456789012")


def test_get_mask_account():
    # Общий случай
    account_number = "73654108430135874305"
    result = get_mask_account(account_number)
    expected = "**4305"
    assert result == expected, f"Ожидалось: {expected}, Получено: {result}"

    # С пробелами
    account_spaces = "73 6541 0843 0135 8743 05"
    result_spaces = get_mask_account(account_spaces)
    assert result_spaces == "**4305", f"Ожидалось: {expected}, Получено: {result_spaces}"

    # Меньше 4 цифр
    short_account = "123"
    with pytest.raises(ValueError):
        get_mask_account(short_account)

import pytest
from src.widget import mask_account_card


def test_mask_account_card():
    # Тест с картой
    input_card = "Visa Platinum 7000792289606361"
    result_card = mask_account_card(input_card)
    expected_card = "Visa Platinum 7000 79** **** 6361"
    assert result_card == expected_card, f"Ожидалось: {expected_card}, Получено: {result_card}"

    # Тест со счетом
    input_account = "Счет 73654108430135874305"
    result_account = mask_account_card(input_account)
    expected_account = "Счет **4305"
    assert result_account == expected_account, f"Ожидалось: {expected_account}, Получено: {result_account}"


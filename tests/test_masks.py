from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    # Общий случай
    card_number = "7000 7922 8960 6361"
    result = get_mask_card_number(card_number)
    expected = "7000 79** **** 6361"
    assert result == expected, f"Ожидалось: {expected}, Получено: {result}"

    # Без пробелов
    card_number_no_spaces = "7000792289606361"
    result_no_spaces = get_mask_card_number(card_number_no_spaces)
    assert result_no_spaces == expected, f"Ожидалось: {expected}, Получено: {result_no_spaces}"

    # Неверная длина (меньше 16)
    short_card = "1234 5678 9012 345"
    try:
        get_mask_card_number(short_card)
        assert False, "Должно было подняться исключение ValueError для короткого номера"
    except ValueError as e:
        assert str(e) == "Card number too short to mask"

    # Нецифровой символ
    invalid_card = "7000 79AB 8960 6361"
    try:
        get_mask_card_number(invalid_card)
        assert False, "Должно было подняться исключение ValueError для нецифровых символов"
    except ValueError as e:
        assert str(e) == "Card number too short to mask"

# Тесты для get_mask_account
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
    try:
        get_mask_account(short_account)
        assert False, "Должно было подняться исключение ValueError для короткого номера"
    except ValueError as e:
        assert str(e) == "Account number too short to mask"

    # Неверные символы
    invalid_account = "1234abcd"
    try:
        get_mask_account(invalid_account)
        assert False, "Должно было подняться исключение ValueError для нецифровых символов"
    except ValueError as e:
        assert str(e) == "Account number too short to mask"

# Запуск всех тестов
def run_tests():
    test_get_mask_card_number()
    test_get_mask_account()
    print("Все тесты прошли успешно.")

if __name__ == "__main__":
    run_tests()
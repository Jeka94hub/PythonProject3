from src.widget import mask_account_card, get_date


def test_mask_account_card():
    # Тест с картой
    input_card = "Visa Platinum 7000792289606361"
    result_card = mask_account_card(input_card)
    expected_card = "Visa Platinum ****6361"
    assert result_card == expected_card, f"Ожидалось: {expected_card}, Получено: {result_card}"

    # Тест со счетом
    input_account = "Счет 73654108430135874305"
    result_account = mask_account_card(input_account)
    expected_account = "Счет **05"
    assert result_account == expected_account, f"Ожидалось: {expected_account}, Получено: {result_account}"

    # Тест с пробелами и без номера
    try:
        mask_account_card("Время проверить")
        assert False, "Должно было подняться исключение ValueError"
    except ValueError:
        pass

    # Тест с номером только из цифр и пробелов
    input_empty_type = "  3000"
    result_empty_type = mask_account_card(input_empty_type)
    expected_empty_type = "3000 ****00"
    assert result_empty_type == expected_empty_type, f"Ожидалось: {expected_empty_type}, Получено: {result_empty_type}"

# Тесты для get_date
def test_get_date():
    # Правильный случай
    date_str = "2024-03-11T02:26:18.671407"
    result = get_date(date_str)
    expected = "11.03.2024"
    assert result == expected, f"Ожидалось: {expected}, Получено: {result}"

    # Некорректный формат
    try:
        get_date("2024/03/11")
        assert False, "Должно было подняться исключение ValueError"
    except ValueError:
        pass

    # Еще один правильный случай с другой датой
    date_str2 = "2020-01-01T00:00:00"
    result2 = get_date(date_str2)
    expected2 = "01.01.2020"
    assert result2 == expected2, f"Ожидалось: {expected2}, Получено: {result2}"

# Запуск всех тестов
def run_tests():
    test_mask_account_card()
    test_get_date()
    print("Все тесты пройдены успешно.")

if __name__ == "__main__":
    run_tests()
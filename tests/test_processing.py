from src.processing import filter_by_state, sort_by_date

def test_filter_by_state():
    data = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'CANCELED'},
        {'id': 3, 'state': 'EXECUTED'},
        {'id': 4, 'state': 'PENDING'},
        {'id': 5}  # без ключа 'state'
    ]

    # Тест 1: фильтрация по умолчанию ('EXECUTED')
    result = filter_by_state(data)
    expected = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 3, 'state': 'EXECUTED'}
    ]
    assert result == expected, f"Тест 1 не пройден: ожидаемый {expected}, полученный {result}"

    # Тест 2: фильтрация по состоянию 'CANCELED'
    result = filter_by_state(data, 'CANCELED')
    expected = [{'id': 2, 'state': 'CANCELED'}]
    assert result == expected, f"Тест 2 не пройден: ожидаемый {expected}, полученный {result}"

    # Тест 3: состояние отсутствует, результат должен быть пустым списком
    result = filter_by_state(data, 'NONEXISTENT')
    expected = []
    assert result == expected, f"Тест 3 не пройден: ожидаемый {expected}, полученный {result}"

    # Тест 4: пустой список
    result = filter_by_state([])
    expected = []
    assert result == expected, f"Тест 4 не пройден: ожидаемый {expected}, полученный {result}"

    # Тест 5: список с объектами без ключа 'state'
    data_no_state = [{'id': 6}, {'id': 7}]
    result = filter_by_state(data_no_state)
    expected = []
    assert result == expected, f"Тест 5 не пройден: ожидаемый {expected}, полученный {result}"

# Запускаем тесты
test_filter_by_state()
print("Все тесты filter_by_state прошли успешно.")


def test_sort_by_date():
    data = [
        {'id': 1, 'date': '2023-10-01T14:23:00'},
        {'id': 2, 'date': '2023-09-15T09:00:00'},
        {'id': 3, 'date': '2023-10-02T08:00:00'},
        {'id': 4, 'date': '2023-09-20T12:30:00'},
        {'id': 5}  # без ключа 'date'
    ]

    # Тест 1: сортировка по возрастанию (по умолчанию)
    result = sort_by_date(data)
    expected = [
        {'id': 2, 'date': '2023-09-15T09:00:00'},
        {'id': 4, 'date': '2023-09-20T12:30:00'},
        {'id': 1, 'date': '2023-10-01T14:23:00'},
        {'id': 3, 'date': '2023-10-02T08:00:00'},
        {'id': 5}
    ]
    assert result == expected, f"Ошибка в Тесте 1: ожидаемый {expected}, полученный {result}"

    # Тест 2: сортировка по убыванию
    result_desc = sort_by_date(data, reverse=True)
    expected_desc = [
        {'id': 3, 'date': '2023-10-02T08:00:00'},
        {'id': 1, 'date': '2023-10-01T14:23:00'},
        {'id': 4, 'date': '2023-09-20T12:30:00'},
        {'id': 2, 'date': '2023-09-15T09:00:00'},
        {'id': 5}
    ]
    assert result_desc == expected_desc, f"Ошибка в Тесте 2: ожидаемый {expected_desc}, полученный {result_desc}"

    # Тест 3: пустой список
    empty_result = sort_by_date([])
    assert empty_result == [], f"Ошибка в Тесте 3: ожидаемый [], полученный {empty_result}"

    # Тест 4: все объекты без ключа 'date'
    data_no_date = [{'id': 6}, {'id': 7}]
    result_no_date = sort_by_date(data_no_date)
    assert result_no_date == data_no_date, f"Ошибка в Тесте 4: ожидаемый {data_no_date}, полученный {result_no_date}"

# Запускаем тесты
test_sort_by_date()
print("Все тесты пройдены успешно.")
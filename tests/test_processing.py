import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed():
    data = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'CANCELED'},
        {'id': 3, 'state': 'EXECUTED'}
    ]
    result = filter_by_state(data)
    expected = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 3, 'state': 'EXECUTED'}
    ]
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_filter_by_state_custom():
    data = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'CANCELED'},
    ]
    result = filter_by_state(data, 'CANCELED')
    expected = [{'id': 2, 'state': 'CANCELED'}]
    assert result == expected


def test_sort_by_date_ascending():
    data = [
        {'id': 1, 'date': '2023-10-01T14:23:00'},
        {'id': 2, 'date': '2023-09-15T09:00:00'},
        {'id': 3, 'date': '2023-10-02T08:00:00'},
        {'id': 4, 'date': '2023-09-20T12:30:00'},
        {'id': 5}  # без ключа 'date'
    ]

    result = sort_by_date(data, descending=False)
    expected = [
        {'id': 2, 'date': '2023-09-15T09:00:00'},
        {'id': 4, 'date': '2023-09-20T12:30:00'},
        {'id': 1, 'date': '2023-10-01T14:23:00'},
        {'id': 3, 'date': '2023-10-02T08:00:00'},
        {'id': 5}
    ]

    assert result == expected, f"Ошибка сортировки по возрастанию: {result}"


def test_sort_by_date_descending():
    data = [
        {'id': 1, 'date': '2023-10-01T14:23:00'},
        {'id': 2, 'date': '2023-09-15T09:00:00'},
        {'id': 3, 'date': '2023-10-02T08:00:00'},
        {'id': 4, 'date': '2023-09-20T12:30:00'},
        {'id': 5}  # без ключа 'date'
    ]

    result = sort_by_date(data, descending=True)
    expected = [
        {'id': 3, 'date': '2023-10-02T08:00:00'},
        {'id': 1, 'date': '2023-10-01T14:23:00'},
        {'id': 4, 'date': '2023-09-20T12:30:00'},
        {'id': 2, 'date': '2023-09-15T09:00:00'},
        {'id': 5}
    ]

    assert result == expected, f"Ошибка сортировки по убыванию: {result}"
import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    """Пример набора транзакций для тестов."""
    return [
        {"id": 1, "amount": 100, "currency": "USD", "description": "Оплата подписки"},
        {"id": 2, "amount": 250, "currency": "EUR", "description": "Покупка билета"},
        {"id": 3, "amount": 75, "currency": "USD", "description": "Чай"},
        {"id": 4, "amount": 300, "currency": "RUB", "description": "Кофе"},
    ]


def test_filter_by_currency_usd(sample_transactions):
    """Проверяем фильтрацию по валюте USD."""
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2
    assert all(t["currency"] == "USD" for t in result)


def test_filter_by_currency_no_match(sample_transactions):
    """Проверяем поведение, если нет совпадений по валюте."""
    result = list(filter_by_currency(sample_transactions, "GBP"))
    assert result == []


def test_transaction_descriptions(sample_transactions):
    """Проверяем генерацию описаний транзакций."""
    descriptions = list(transaction_descriptions(sample_transactions))
    expected = ["Оплата подписки", "Покупка билета", "Чай", "Кофе"]
    assert descriptions == expected


def test_transaction_descriptions_missing_field():
    """Проверяем, что пропуск описания не ломает генератор."""
    data = [
        {"id": 1, "currency": "USD"},
        {"id": 2, "currency": "EUR", "description": "Есть описание"},
    ]
    result = list(transaction_descriptions(data))
    assert result == ["Есть описание"]


def test_card_number_generator_basic():
    """Проверяем корректность генерации номеров карт."""
    cards = list(card_number_generator(1234, 1237))
    assert cards == [
        "**** **** **** 1234",
        "**** **** **** 1235",
        "**** **** **** 1236",
    ]


def test_card_number_generator_padding():
    """Проверяем добавление ведущих нулей для коротких номеров."""
    cards = list(card_number_generator(1, 4))
    assert cards == [
        "**** **** **** 0001",
        "**** **** **** 0002",
        "**** **** **** 0003",
    ]


def test_card_number_generator_empty():
    """Проверяем, что генератор возвращает пустой результат при start == stop."""
    cards = list(card_number_generator(1000, 1000))
    assert cards == []
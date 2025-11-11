import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Пример транзакций
sample_transactions = [
    {"id": 1, "amount": 100, "currency": "USD", "description": "Оплата подписки"},
    {"id": 2, "amount": 250, "currency": "EUR", "description": "Покупка билета"},
    {"id": 3, "amount": 75, "currency": "USD", "description": "Чай"},
    {"id": 4, "amount": 300, "currency": "RUB", "description": "Кофе"},
]

# ------------------------------
# Тесты filter_by_currency
# ------------------------------
@pytest.mark.parametrize(
    "currency, expected_count",
    [
        ("USD", 2),
        ("EUR", 1),
        ("RUB", 1),
        ("GBP", 0),  # случай, когда совпадений нет
    ]
)
def test_filter_by_currency_various(currency, expected_count):
    result = list(filter_by_currency(sample_transactions, currency))
    assert len(result) == expected_count
    assert all(t.get("currency") == currency for t in result)


# ------------------------------
# Тесты transaction_descriptions
# ------------------------------
@pytest.mark.parametrize(
    "transactions, expected",
    [
        (sample_transactions, ["Оплата подписки", "Покупка билета", "Чай", "Кофе"]),
        ([{"id": 1}, {"id": 2, "description": "Есть описание"}], ["Есть описание"]),
        ([], []),  # пустой список
    ]
)
def test_transaction_descriptions_various(transactions, expected):
    result = list(transaction_descriptions(transactions))
    assert result == expected


# ------------------------------
# Тесты card_number_generator
# ------------------------------
@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 4, ["**** **** **** 0001", "**** **** **** 0002", "**** **** **** 0003"]),
        (1234, 1237, ["**** **** **** 1234", "**** **** **** 1235", "**** **** **** 1236"]),
        (1000, 1000, []),  # start == stop
    ]
)
def test_card_number_generator_various(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected

# Проект: Фильтрация и сортировка операций

## Описание

Этот проект реализует функции для работы со списком операций (операции представлены в виде словарей), позволяя:

- Фильтровать операции по их состоянию (`state`).
- Сортировать операции по дате (`date`).

## Функции

### filter_by_state(records, state='EXECUTED')

Функция фильтрует список операций, возвращая только те, у которых ключ `state` равен заданному значению (по умолчанию `'EXECUTED'`).

**Аргументы:**

- `records` — список словарей с операциями.
- `state` — строка, значение состояния для фильтрации (по умолчанию `'EXECUTED'`).

**Возвращает:**

Список отфильтрованных операций.

---

### sort_by_date(records, descending=True)

Функция сортирует список операций по ключу `date`.

**Аргументы:**

- `records` — список словарей с операциями.
- `descending` — булево значение, если `True` — сортировка по убыванию даты (по умолчанию), иначе — по возрастанию.

**Возвращает:**

Отсортированный список операций.

---

## Установка

1. Клонируйте или скачайте проект.
2. Убедитесь, что у вас установлен Python 3.
3. (Опционально) Рекомендуется использовать виртуальное окружение:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   
# Generators Module

Модуль `generators.py` содержит функции и генераторы для работы с транзакциями и номерами карт.

## Содержание модуля

1. **`filter_by_currency(transactions, currency)`**  
   Фильтрует список транзакций по указанной валюте.  
   Возвращает **итератор**, который можно перебрать в цикле или преобразовать в список.  

2. **`transaction_descriptions(transactions)`**  
   Генератор, который возвращает описания транзакций (`description`) по очереди.  
   Использует `yield` для экономии памяти при работе с большими списками.  

3. **`card_number_generator(start, stop)`**  
   Генератор номеров карт в формате `**** **** **** 0001`.  
   Аргументы `start` и `stop` задают диапазон чисел.  
   Используется форматирование с ведущими нулями через `{number:04d}`.

---

## Примеры использования

```python
from generators import filter_by_currency, transaction_descriptions, card_number_generator

transactions = [
    {"id": 1, "amount": 100, "currency": "USD", "description": "Оплата подписки"},
    {"id": 2, "amount": 250, "currency": "EUR", "description": "Покупка билета"},
    {"id": 3, "amount": 75, "currency": "USD", "description": "Чай"},
]

# 1. Фильтрация по валюте
usd_transactions = filter_by_currency(transactions, "USD")
print(list(usd_transactions))
# Вывод: [{'id': 1, 'amount': 100, 'currency': 'USD', 'description': 'Оплата подписки'}, {'id': 3, 'amount': 75, 'currency': 'USD', 'description': 'Чай'}]

# 2. Получение описаний транзакций
for desc in transaction_descriptions(transactions):
    print(desc)
# Вывод:
# Оплата подписки
# Покупка билета
# Чай

# 3. Генерация номеров карт
for card in card_number_generator(1, 5):
    print(card)
# Вывод:
# **** **** **** 0001
# **** **** **** 0002
# **** **** **** 0003
# **** **** **** 0004


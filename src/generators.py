def filter_by_currency(transactions, currency):
    """
    Фильтрует список транзакций по указанной валюте.
    Возвращает итератор (не список!).

    :param transactions: список словарей с ключом 'currency'
    :param currency: строка, валюта для фильтрации, например 'USD'
    :return: итератор отфильтрованных транзакций
    """
    return (t for t in transactions if t.get("currency") == currency)


def transaction_descriptions(transactions):
    """
    Генератор, который возвращает описания транзакций.
    Использует yield для поочерёдной выдачи значений.

    :param transactions: список словарей с ключом 'description'
    :yield: описание транзакции
    """
    for t in transactions:
        desc = t.get("description")
        if desc:
            yield desc


def card_number_generator(start, stop):
    """
    Генератор номеров карт от start до stop (не включая stop).

    :param start: начальное значение
    :param stop: конечное значение (не включительно)
    :yield: номер карты в формате '**** **** **** 0001'
    """
    for number in range(start, stop):
        yield f"**** **** **** {number:04d}"
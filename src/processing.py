def filter_by_state(records, state='EXECUTED'):
    """Фильтрует список записей по заданному состоянию.
       Args:
           records (list): список словарей, каждый из которых должен содержать ключ 'state'.
           state (str): состояние, по которому фильтруются записи (по умолчанию 'EXECUTED').
       Returns:
           list: список словарей, удовлетворяющих условию фильтрации.
       """
    return [record for record in records if record.get('state') == state]

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

executed_records = filter_by_state(data)
canceled_records = filter_by_state(data, 'CANCELED')

print("EXECUTED:", executed_records)
print("CANCELED:", canceled_records)


def sort_by_date(records, descending=True):
    """Сортирует список словарей по ключу 'date'.
    Args:
        records (list): список словарей, каждый из которых содержит ключ 'date'.
        descending (bool): направление сортировки. True — по убыванию, False — по возрастанию.
    Returns:
        list: отсортированный список словарей.
    """
    return sorted(records, key=lambda x: x.get('date', ''), reverse=descending)

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]

# Сортировка по убыванию (по умолчанию)
sorted_desc = sort_by_date(data)
print(sorted_desc)

# Сортировка по возрастанию
sorted_asc = sort_by_date(data, descending=False)
print(sorted_asc)



from datetime import datetime


def filter_by_state(records, state='EXECUTED'):
    """Фильтрует список записей по заданному состоянию.
    Args:
        records (list): список словарей, каждый из которых должен содержать ключ 'state'.
        state (str): состояние, по которому фильтруются записи (по умолчанию 'EXECUTED').
    Returns:
        list: список словарей, удовлетворяющих условию фильтрации.
    """
    return [record for record in records if record.get('state') == state]


def sort_by_date(records, descending=True):
    """Сортирует список словарей по ключу 'date'.
    Args:
        records (list): список словарей, каждый из которых содержит ключ 'date'.
        descending (bool): направление сортировки.
            True — по убыванию, False — по возрастанию.
    Returns:
        list: отсортированный список словарей.
    """
    def get_date(record):
        date_str = record.get('date')
        if date_str:
            return datetime.fromisoformat(date_str)
        # элементы без 'date' должны идти в конец независимо от порядка
        return datetime.min if descending else datetime.max

    return sorted(records, key=get_date, reverse=descending)
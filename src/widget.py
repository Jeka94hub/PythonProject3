import re
from datetime import datetime

def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты по формату:
    первые 6 цифр и последние 4 — показываем,
    остальные заменяем на '*',
    при этом форматируем группами по 4 цифры, заменяя уязвимые на '**' или '****' для читаемости.
    Пример: 7000792289606361 -> 7000 79** **** 6361
    """


    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Некорректный номер карты")

    # Разбиваем число на группы по 4 символа
    g1 = card_number[:4]          # первые 4
    g2 = card_number[4:6]         # 5-6
    g2_masked = g2 + "**"
    g3 = "****"
    g4 = card_number[-4:]         # последние 4

    return f"{g1} {g2_masked} {g3} {g4}"


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета по формату:
    показывает только последние 4 цифры,
    перед ними ставит '**'
    Пример: 73654108430135874305 -> **4305
    """

    # Проверка минимальной длины, чтобы не ломалась маска
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Некорректный номер счета")

    last4 = account_number[-4:]
    return f"**{last4}"


def mask_account_card(s: str) -> str:
    """
    Принимает строку — название типа и номер (без разбивания строки),
    возвращает строку с замаскированным номером в зависимости от типа:
    для карт — используем mask_card_number,
    для счетов — mask_account_number.
    """

    # Ищем номер — последовательность цифр в конце строки
    match = re.search(r"(\d+)$", s.strip())
    if not match:
        raise ValueError("Входная строка не содержит номера")

    number = match.group(1)
    # Тип — всё, что перед номером (срез строки без номера)
    type_str = s[: -len(number)].strip()

    # Если тип содержит слово "Счет" (русская "Счет")
    if "Счет" in type_str:
        masked_number = mask_account_number(number)
    else:
        masked_number = mask_card_number(number)

    return f"{type_str} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Принимает строку с датой в формате ISO с микросекундами,
    возвращает строку в формате ДД.ММ.ГГГГ.
    Пример:
      "2024-03-11T02:26:18.671407" -> "11.03.2024"
    """
    try:
        dt = datetime.fromisoformat(date_str)
    except ValueError:
        raise ValueError("Неправильный формат даты")

    return dt.strftime("%d.%m.%Y")
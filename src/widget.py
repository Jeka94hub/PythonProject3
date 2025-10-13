import re
from datetime import datetime
from masks import get_mask_card_number, get_mask_account  # импорт функций из masks


def mask_account_card(s: str) -> str:
    match = re.search(r"(\d+)$", s.strip())
    if not match:
        raise ValueError("Входная строка не содержит номера")

    number = match.group(1)
    type_str = s[: -len(number)].strip()

    if "Счет" in type_str:
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{type_str} {masked_number}"


def get_date(date_str: str) -> str:
    try:
        dt = datetime.fromisoformat(date_str)
    except ValueError:
        raise ValueError("Неправильный формат даты")
    return dt.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))

import re

def mask_account_card(s: str) -> str:
    """
      Маскирует номер счета или карты, переданный в виде строки.
      Определяет тип (счет или карта) по содержанию входной строки,
      извлекает номер, применяет соответствующую маскировку и возвращает
      строку с типом и замаскированным номером.

      Args:
          s (str): строка, содержащая тип (например, "Счет" или название карты)
                   и номер, который нужно замаскировать.

      Returns:
          str: строка с типом и замаскированным номером.

      Raises:
          ValueError: если входная строка не содержит номера.
      """
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
    """ Преобразует строку с датой из ISO-формата в формат "день.месяц.год".
        Args:
            date_str (str): дата в формате ISO 8601, например, "2024-03-11T02:26:18.671407".

        Returns:
            str: дата в формате "день.месяц.год".

        Raises:
            ValueError: если входная строка не соответствует формату ISO-8601.
        """
    try:
        dt = datetime.fromisoformat(date_str)
    except ValueError:
        raise ValueError("Неправильный формат даты")
    return dt.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))

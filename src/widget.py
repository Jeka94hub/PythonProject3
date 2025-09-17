def mask_account_card(info: str) -> str:
    """Обрабатывает строку с типом и номером (карта или счет), возвращая маскированную строку."""
    parts = info.split(' ',1)
    if len(parts) != 2:
        raise ValueError("Некорректный формат строки: должна содержать тип и номер.")
    type_name, number = parts

    card_types = [ "Visa","Maestro","MasterCard","Visa Classic","Visa Platinum","Visa Gold"]
    if type_name == "Счет":
        masked = get_mask_account_(number)
        return f"{type_name} {masked}"
    elif type_name in card_types:
        masked = get_mask_card_number(number)
        return f"{type_name} {masked}"
    else:
        raise ValueError(f"Неизвестный тип: {type_name}")

def get_date(date_str: str) -> str:
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%Y/%m/%d")
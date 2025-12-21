from external_api import convert_to_rubles


def get_transaction_amount(transaction: dict) -> float:
    """
    Принимает транзакцию вида:
    {
        "operationAmount": {
            "amount": "10",
            "currency": {"name": "USD", "code": "RUB"}
        }
        ...
    }

    Возвращает сумму в рублях.
    """
    operation_amount = transaction.get("operationAmount", {})
    amount_str = operation_amount.get("amount")
    currency_code = operation_amount.get("currency", {}).get("code")

    if amount_str is None:
        raise ValueError("Отсутствует 'amount' в транзакции.")
    if currency_code is None:
        # Если валюта не указана, предполагаем рубли
        currency_code = "RUB"

    # Преобразуем сумму в float (учитывая, что она строка)
    try:
        amount = float(amount_str)
    except ValueError:
        raise ValueError(f"Некорректное значение 'amount': {amount_str}")

    return convert_to_rubles(amount, currency_code)


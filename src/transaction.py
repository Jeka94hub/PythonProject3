from external_api import convert_to_rub

def get_transaction_amount(transaction: dict) -> float:
    """
    Принимает транзакцию вида:
    { "amount": 100, "currency": "USD" }

    Возвращает сумму в рублях.
    """
    amount = transaction["amount"]
    currency = transaction.get("currency", "RUB")

    return convert_to_rub(amount, currency)


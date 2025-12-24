from external_api import convert_to_rub

def get_transaction_amount_in_rub(transaction):
    """
    Принимает транзакцию и возвращает её сумму в рублях.
    Транзакция представляется как словарь с ключами 'amount' и 'currency'.
    """
    amount = transaction.get("amount")
    currency = transaction.get("currency")

    if amount is None or currency is None:
        raise ValueError("Некорректный формат транзакции. Должны быть ключи 'amount' и 'currency'.")

    return convert_to_rub(amount, currency)

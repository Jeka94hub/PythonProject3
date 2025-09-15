def get_mask_card_number(card_number: str) -> str:
    """ Маскирует номер карты в формате: XXXX XX** **** XXXX"""
    card_number = card_number.replace(" "  ,"")
    if len(card_number) < 10:
        raise ValueError("Card number too short to mask")
    return(
        f"{card_number[:4]}"
        f"{card_number[4:6]}**"
        f"**** "
        f"{card_number[6:]}"
    )


def get_mask_account(account_number: str) -> str:
    """ Маскирует номер счета в формате: **XXXX """
    account_number = account_number.replace(" " ,"")
    if len(account_number) < 4:
        raise ValueError("Account number too short to mask")
    return ( f"{account_number[:4]}")
ma
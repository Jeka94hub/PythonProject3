def get_mask_card_number(card_number: str ) -> str:
    """Маскирует номер карты в формате: XXXX XX** **** XXXX"""
    digits = card_number.replace(" ", "")
    if len(digits) != 16 or not digits.isdigit():
        raise ValueError("Card number too short to mask")

    masked = (
         digits[0:4] + " " +
         digits[4:6] + "** " +
         "**** " +
         digits[12:16]
    )
    return masked



def get_mask_account(account_number: str) -> str :
    """Маскирует номер счета в формате: **XXXX"""
    digits = account_number.replace(" ", "")
    if len(digits) < 4 or not digits.isdigit():
        raise ValueError("Account number too short to mask")
    masked = "**" + digits[-4:]
    return masked

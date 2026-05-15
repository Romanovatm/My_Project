def get_mask_card_number(card_number: str) -> str:
    """Функция для маскировки номера банковской карты"""
    if len(card_number) == 16:
        return card_number[:4] + " " + card_number[4:6] + "*" * 2 + " " + "*" * 4 + " " + card_number[12:]
    else:
        return "Некорректный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция для маскировки номера банковского счета"""
    if len(account_number) >= 4:
        return "**" + account_number[-4:]
    else:
        return "Некорректный номер счета"

def get_mask_card_number(card_number: str | int) -> str:
    """Функция для маскировки номера банковской карты"""
    if " " in str(card_number):
        card_number = "".join(str(card_number).split())
    if len(str(card_number)) == 16:
        return (
            str(card_number)[:4] + " " + str(card_number)[4:6] + "*" * 2 + " " + "*" * 4 + " " + str(card_number)[12:]
        )
    else:
        return "Некорректный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция для маскировки номера банковского счета"""
    account_number_correct = account_number.replace(" ", "")
    if len(account_number_correct) >= 4:
        return "**" + account_number_correct[-4:]
    else:
        return "Некорректный номер счета"

from masks import get_mask_card_number, get_mask_account


def mask_account_card(card_data: str) -> str:
    """Функция для маскировки данных банковской карты, исходя из ее типа, номера или счета"""
    if card_data:
        card_data_list = card_data.split()
        name_card = []

        for elem in card_data_list:
            if elem.isalpha():
                name_card.append(elem)
            else:
                continue

        name_card_str = " ".join(name_card)
        if len(card_data_list[-1]) == 16:
            return f"{name_card_str} {get_mask_card_number(card_data_list[-1])}"
        elif len(card_data_list[-1]) == 20:
            return f"{name_card_str} {get_mask_account(card_data_list[-1])}"

    return "Некорректный ввод данных"

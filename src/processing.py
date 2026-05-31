def filter_by_state(information: list, state: str = "EXECUTED") -> list:
    """Функция возвращает отсортированный список словарей по состоянию транзакций"""
    filter_list = []
    for elem in information:
        try:
            if elem["state"] == state:
                filter_list.append(elem)
        except KeyError:
            continue
    return filter_list


def sort_by_date(information: list, is_reversed: bool = True) -> list:
    """Функция возвращает отсортированный список транзакций по дате"""
    return sorted(information, reverse=is_reversed, key=lambda x: x["date"])

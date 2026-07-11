import re
from collections import Counter


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


def process_bank_search(transactions: list[dict], search: str) -> list[dict]:
    """Функция возвращает отсортированный список словарей банковских операции по заданному поиску"""
    pattern = re.compile(search, re.IGNORECASE)

    transactions_filtered = []
    for transaction in transactions:
        if transaction.get("description") and pattern.search(str(transaction["description"])):
            transactions_filtered.append(transaction)
    return transactions_filtered


def process_bank_operations(transactions: list[dict], categories: list) -> dict:
    """Функция для подсчета количества банковских операций определенного типа"""
    new_sorted_dict = {}
    counted_categories = dict(Counter(transaction["description"] for transaction in transactions))
    for key in counted_categories:
        if key in categories:
            new_sorted_dict[key] = counted_categories[key]
    return new_sorted_dict

import json


def transactions_info(path_to_json_file: str) -> list[dict]:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях.
    """
    try:
        with open(path_to_json_file, "r", encoding="UTF-8") as file:
            transactions = json.load(file)  # список словарей для работы в питоне
        if not transactions:  # если пустой
            return []
        elif type(transactions) is not list:  # если не список
            return []
        else:
            return transactions
    except FileNotFoundError:
        return []

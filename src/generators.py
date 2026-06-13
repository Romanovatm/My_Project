from typing import Iterator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Iterator[dict]:
    """
    Функция-генератор возвращает поочередно словарь транзакций по заданному параметру currency_code
    """
    for information in transactions:
        if information["operationAmount"]["currency"]["code"] == currency_code:
            yield information


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Функция-генератор возвращает поочередно описание каждой операции"""
    for information in transactions:
        yield information["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Функция-генератор возвращает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for num in range(start, stop + 1):
        if len(str(num)) <= 16:
            number_of_zeros = 16 - len(str(num))
            card_number_generate = "0" * number_of_zeros + str(num)
            yield f"{card_number_generate[:4]} {card_number_generate[4:8]} {card_number_generate[8:12]} {card_number_generate[12:16]}"
        else:
            yield "Некорректный ввод данных. Попробуйте еще раз!"
            return

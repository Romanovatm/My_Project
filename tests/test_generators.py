import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(list_of_dicts_info_transactions):
    assert list(filter_by_currency(list_of_dicts_info_transactions, "RUB")) == [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_filter_by_another_currency(list_of_dicts_info_transactions):
    assert next(filter_by_currency(list_of_dicts_info_transactions, "EUR"), {}) == {}
    assert list(filter_by_currency(list_of_dicts_info_transactions, "EUR")) == []
    assert next(filter_by_currency([], "EUR"), []) == []
    assert next(filter_by_currency(list_of_dicts_info_transactions, ""), []) == []


def test_transaction_descriptions(list_of_dicts_info_transactions):
    generator = transaction_descriptions(list_of_dicts_info_transactions)
    generator_empty = transaction_descriptions([])
    assert list(generator) == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert list(generator_empty) == []


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        ("254484298", "254484300", ["0000 0002 5448 4298", "0000 0002 5448 4299", "0000 0002 5448 4300"]),
        ("1", "3", ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (
            "9999999999999997",
            "9999999999999999",
            ["9999 9999 9999 9997", "9999 9999 9999 9998", "9999 9999 9999 9999"],
        ),
        ("000024900012310", "000024900012311", ["0000 0249 0001 2310", "0000 0249 0001 2311"]),
        ("99999999999999999", "100000000000000000", ["Некорректный ввод данных. Попробуйте еще раз!"]),
    ],
)
def test_card_number_generator(start, stop, expected):
    assert list(card_number_generator(int(start), int(stop))) == expected

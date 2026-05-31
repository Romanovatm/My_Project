import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_data, expected",
    [
        ("Visa 1234567891023456", "Visa 1234 56** **** 3456"),
        ("Visa Platinum 1234567891023456", "Visa Platinum 1234 56** **** 3456"),
        ("Счет 12345678910234560000", "Счет **0000"),
        ("jgvjgvhg 26542626436536536536363636", "Некорректный ввод данных"),
        ("nnkcjgnhsdfighsfiugh364366461sfgkhnfdugudsfiu", "Некорректный ввод данных"),
        ("", "Некорректный ввод данных"),
    ],
)
def test_mask_account_card(card_data, expected):
    assert mask_account_card(card_data) == expected


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("", "Некорректный ввод"),
        ("9999-12-31T23:59:59.999999", "31.12.9999"),
        ("0001-01-01T00:00:00.000000", "01.01.0001"),
        ("T02:26:18.671407", "Некорректный ввод"),
    ],
)
def test_get_date(date, expected):
    assert get_date(date) == expected

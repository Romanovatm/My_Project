import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_valid():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"


@pytest.mark.parametrize(
    "card_data, expected",
    [
        (1234567890123456, "1234 56** **** 3456"),
        ("12 34 56 78 90 12 34 56", "1234 56** **** 3456"),
        ("0000000000000001", "0000 00** **** 0001"),
        ("9999999999999999", "9999 99** **** 9999"),
        ("123456789012345", "Некорректный номер карты"),
        ("1234567890123456789", "Некорректный номер карты"),
    ],
)
def test_get_mask_card_number(card_data, expected):
    assert get_mask_card_number(card_data) == expected


def test_get_mask_card_number_empty_str():
    assert get_mask_card_number("") == "Некорректный номер карты"


def test_get_mask_account_valid():
    assert get_mask_account("12345678901234567890") == "**7890"


@pytest.mark.parametrize(
    "account_data, expected",
    [
        ("     67 8", "Некорректный номер счета"),
        ("1234 5678 9012 3456 78", "**5678"),
        ("BY28AKBB38193821000170000000", "**0000"),
        ("999", "Некорректный номер счета"),
        ("123456789", "**6789"),
        ("", "Некорректный номер счета"),
    ],
)
def test_get_mask_account(account_data, expected):
    assert get_mask_account(account_data) == expected

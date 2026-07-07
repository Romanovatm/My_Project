from unittest.mock import mock_open, patch

import pandas as pd

from src.utils import transactions_csv, transactions_excel, transactions_info


@patch("builtins.open", mock_open(read_data="[]"))
def test_transactions_info_empty_list():
    assert transactions_info("") == []


@patch("builtins.open", mock_open(read_data='{"number":"1"}'))
def test_transactions_info_not_list():
    assert transactions_info("") == []


@patch("builtins.open", mock_open(read_data='[{"a": "1"}, {"b": "2"}, {"c": "3"}]'))
def test_transactions_info_ok():
    assert transactions_info("") == [{"a": "1"}, {"b": "2"}, {"c": "3"}]


def test_transactions_info_file_not_found():
    assert transactions_info("../fmnvsrrn/vkkgg.json") == []


def test_transactions_csv_file_not_found():
    assert transactions_csv("../fmnvsrrn/vkkgg.csv") == []


def test_transactions_excel_file_not_found():
    assert transactions_excel("../fmnvsrrn/vkkgg.xlsx") == []


@patch(
    "builtins.open",
    mock_open(
        read_data="id;state;date;amount;currency_name;currency_code;from;to;description\n"
        "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;"
        "Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации"
    ),
)
def test_transactions_csv_ok():
    assert transactions_csv("") == [
        {
            "amount": "16210",
            "currency_code": "PEN",
            "currency_name": "Sol",
            "date": "2023-09-05T11:30:32Z",
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "id": "650703",
            "state": "EXECUTED",
            "to": "Счет 39745660563456619397",
        },
    ]


@patch("pandas.read_excel")
def test_transactions_excel_ok(mock_read_excel):
    test_data = {
        "id": [650703.0],
        "state": ["EXECUTED"],
        "date": ["2023-09-05T11:30:32Z"],
        "amount": [16210.0],
        "currency_name": ["Sol"],
        "currency_code": ["PEN"],
        "from": ["Счет 58803664561298323391"],
        "to": ["Счет 39745660563456619397"],
        "description": ["Перевод организации"],
    }
    real_df = pd.DataFrame(test_data)

    mock_read_excel.return_value = real_df

    result = transactions_excel("../data/transactions_excel.xlsx")

    assert result == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]

from unittest.mock import mock_open, patch

from src.utils import transactions_info


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

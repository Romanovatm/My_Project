from unittest.mock import patch

from src.external_api import sum_transactions_rub


def test_sum_transactions_no_rub_no_usd_no_eur():
    assert sum_transactions_rub({"operationAmount": {"currency": {"code": "BRL"}}}) == 0


def test_sum_transactions_rub():
    assert sum_transactions_rub({"operationAmount": {"currency": {"code": "RUB"}, "amount": 200}}) == 200


@patch("requests.get")
def test_sum_transactions_from_usd_to_rub(mock_get):
    mock_get.return_value.json.return_value = {
        "date": "2026-06-22",
        "historical": "",
        "info": {"rate": 73.7650, "timestamp": 1519328414},
        "query": {"amount": "8221.37", "from": "USD", "to": "RUB"},
        "result": 606449.35805,
        "success": True,
    }
    assert (
        sum_transactions_rub(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        )
        == 606449.35805
    )

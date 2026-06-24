import os

import requests
from dotenv import load_dotenv

load_dotenv()


def sum_transactions_rub(transaction: dict) -> float:
    """Конвертирует сумму транзакции в RUB, если она в USD или EUR, и возвращает итоговое значение
    во float."""
    if (
        transaction["operationAmount"]["currency"]["code"] == "USD"
        or transaction["operationAmount"]["currency"]["code"] == "EUR"
    ):
        to = "RUB"
        from_ = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        apikey = os.getenv("API_KEY")
        headers = {"apikey": apikey}
        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}",
            headers=headers,  # type: ignore
        )
        response_data = response.json()
        return float(response_data["result"])
    elif transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    return 0

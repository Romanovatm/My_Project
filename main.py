from src.generators import filter_by_currency
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import transactions_csv, transactions_excel, transactions_info
from src.widget import get_date, mask_account_card


def main() -> None:
    """
    Отвечает за основную логику проекта с пользователем и связывает функциональности между собой
    """

    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")

    user_input = input()

    if user_input == "1":
        print("Для обработки выбран JSON-файл.")
        transactions_data = transactions_info("data/operations.json")
    elif user_input == "2":
        print("Для обработки выбран CSV-файл.")
        transactions_data = transactions_csv("data/transactions.csv")
    else:
        print("Для обработки выбран XLSX-файл.")
        transactions_data = transactions_excel("data/transactions_excel.xlsx")

    while True:
        print("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")

        user_input = input().upper()

        if user_input in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Операции отфильтрованы по статусу {user_input}")
            transactions_data = filter_by_state(transactions_data, user_input)
            break
        else:
            print(f"Статус операции {user_input} недоступен.")

    print("Отсортировать операции по дате? Да/Нет")

    user_input = input().lower()

    if user_input == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        user_input = input().lower()
        if user_input == "по возрастанию":
            transactions_data = sort_by_date(transactions_data, False)
        else:
            transactions_data = sort_by_date(transactions_data)

    print("Выводить только рублевые транзакции? Да/Нет")

    user_input = input().lower()

    if user_input == "да":
        transactions_data = list(filter_by_currency(transactions_data, "RUB"))

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")

    user_input = input().lower()

    if user_input == "да":
        user_input = input("Введите слово:").lower()
        transactions_data = process_bank_search(transactions_data, user_input)

    if not transactions_data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"""Распечатываю итоговый список транзакций...
Всего банковских операций в выборке: {len(transactions_data)}""")

        for transaction in transactions_data:
            if "operationAmount" in transaction:
                print(f"{get_date(transaction["date"])} {transaction["description"]}")

                if "from" in transaction:
                    print(f"{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}")
                else:
                    print(f"{mask_account_card(transaction["to"])}")

                print(
                    f"Сумма: {transaction["operationAmount"]["amount"]} "
                    f"{transaction["operationAmount"]["currency"]["name"]}\n"
                )
            else:
                print(f"{get_date(transaction["date"])} {transaction["description"]}")

                if "from" in transaction:
                    print(f"{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}")
                else:
                    print(f"{mask_account_card(transaction["to"])}")

                print(f"Сумма: {transaction["amount"]} {transaction["currency_name"]}\n")


main()

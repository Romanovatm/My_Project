import csv
import json
import logging

import pandas as pd

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("C:/PythonProject/My_Project/logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def transactions_info(path_to_json_file: str) -> list[dict]:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях.
    """
    logger.debug("Начало работы функции")
    try:
        with open(path_to_json_file, "r", encoding="UTF-8") as file:
            transactions = json.load(file)  # список словарей для работы в питоне
            logger.debug("Успешное открытие json файла, перевод в Python object")
        if not transactions:  # если пустой
            logger.error("Файл пустой!")
            return []
        elif type(transactions) is not list:  # если не список
            logger.error("Тип входных данных не является списком")
            return []
        else:
            logger.info("Успешное  завершение функции")
            return transactions
    except FileNotFoundError:
        logger.error("Внимание! FileNotFoundError")
        return []


def transactions_csv(path_to_csv_file: str) -> list[dict]:
    """
    Функция принимает на вход путь до CSV-файла и возвращает список словарей с данными
    о финансовых транзакциях.
    """
    try:
        with open(path_to_csv_file, "r", encoding="UTF-8") as file:
            read_csv = csv.DictReader(file, delimiter=";")
            return list(read_csv)
    except FileNotFoundError:
        return []


def transactions_excel(path_to_excel_file: str) -> list[dict]:
    """
    Функция принимает на вход путь до EXCEL-файла и возвращает список словарей с данными
    о финансовых транзакциях.
    """
    try:
        excel_file = pd.read_excel(path_to_excel_file)
        return excel_file.to_dict(orient="records")
    except FileNotFoundError:
        return []

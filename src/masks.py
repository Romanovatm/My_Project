import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str | int) -> str:
    """Функция для маскировки номера банковской карты"""
    logger.debug(f"Начало работы функции. Входные данные: {card_number}")
    if " " in str(card_number):
        card_number = "".join(str(card_number).split())
        logger.debug(f"Пробелы удалены. Результат: {card_number}")
    if len(str(card_number)) == 16:
        masked_card_number = (
            str(card_number)[:4] + " " + str(card_number)[4:6] + "*" * 2 + " " + "*" * 4 + " " + str(card_number)[12:]
        )
        logger.info(f"Функция завершена успешно. Результат: {masked_card_number}")
        return masked_card_number
    else:
        logger.error(f"Внимание! Некорректный номер карты. Входные данные {card_number}")
        return "Некорректный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция для маскировки номера банковского счета"""
    logger.debug(f"Начало работы функции. Входные данные: {account_number}")
    account_number_correct = account_number.replace(" ", "")
    logger.debug("Пробелы удалены для корректной работы")
    if len(account_number_correct) >= 4:
        logger.info(f"Функция завершена успешно. Результат: {"**" + account_number_correct[-4:]}")
        return "**" + account_number_correct[-4:]
    else:
        logger.error(f"Внимание! Некорректный номер счета. Входные данные: {account_number}")
        return "Некорректный номер счета"

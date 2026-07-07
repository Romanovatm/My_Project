# Виджет банковских операций

## Описание проекта

`My_Project` — учебный Python-проект серверной части виджета банковских операций.

Проект предназначен для работы с банковскими транзакциями: маскировки карт и счетов, форматирования дат, фильтрации и сортировки операций, чтения данных из файлов разных форматов, генерации номеров карт, логирования работы функций и конвертации валютных операций в рубли через внешний API.

Код покрыт тестами `pytest`. Для проверки качества кода в проекте настроены `flake8`, `black`, `isort` и `mypy`.

## Основной функционал

В проекте реализованы следующие возможности:

- маскировка номера банковской карты;
- маскировка номера банковского счёта;
- определение типа входных данных: карта или счёт;
- форматирование даты из ISO-формата в формат `ДД.ММ.ГГГГ`;
- фильтрация банковских операций по статусу;
- сортировка операций по дате;
- чтение операций из `JSON`-файла;
- чтение транзакций из `CSV`-файла;
- чтение транзакций из `Excel`-файла;
- фильтрация транзакций по коду валюты;
- последовательное получение описаний транзакций;
- генерация номеров банковских карт в формате `XXXX XXXX XXXX XXXX`;
- логирование успешного выполнения функций и ошибок через декоратор `log`;
- вывод логов в консоль или запись логов в файл;
- конвертация суммы транзакции в рубли;
- поддержка транзакций в `RUB`, `USD` и `EUR`;
- получение API-ключа из переменных окружения через `.env`;
- обработка пустых, некорректных и отсутствующих файлов;
- тестирование функций с помощью `pytest`;
- формирование отчёта о покрытии тестами.

## Структура проекта

```text
.
├── data/
│   ├── operations.json             # JSON-файл с банковскими операциями
│   ├── transactions.csv            # CSV-файл с транзакциями
│   └── transactions_excel.xlsx     # Excel-файл с транзакциями
├── logs/
│   ├── masks.log                   # Логи функций маскировки
│   └── utils.log                   # Логи функций чтения файлов
├── src/
│   ├── __init__.py
│   ├── decorators.py               # Декоратор логирования
│   ├── external_api.py             # Конвертация суммы транзакции в рубли
│   ├── generators.py               # Генераторы транзакций и номеров карт
│   ├── masks.py                    # Маскировка карт и счетов
│   ├── processing.py               # Фильтрация и сортировка операций
│   ├── utils.py                    # Чтение JSON, CSV и Excel-файлов
│   └── widget.py                   # Работа с данными карты/счёта и датами
├── tests/
│   ├── conftest.py                 # Тестовые фикстуры
│   ├── test_decorators.py          # Тесты декоратора логирования
│   ├── test_external_api.py        # Тесты конвертации валют
│   ├── test_generators.py          # Тесты генераторов
│   ├── test_masks.py               # Тесты функций маскировки
│   ├── test_processing.py          # Тесты фильтрации и сортировки
│   ├── test_utils.py               # Тесты чтения файлов
│   └── test_widget.py              # Тесты функций виджета
├── htmlcov/                        # HTML-отчёт о покрытии тестами
├── .env.example                    # Пример файла переменных окружения
├── .flake8                         # Настройки flake8
├── .gitignore
├── logging.txt                     # Пример файла логирования
├── main.py
├── poetry.lock
├── pyproject.toml                  # Зависимости и настройки инструментов
└── README.md
```

## Используемые технологии

- Python `^3.14`;
- Poetry;
- pytest;
- pytest-cov;
- requests;
- python-dotenv;
- pandas;
- openpyxl;
- flake8;
- black;
- isort;
- mypy.

## Установка

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/Romanovatm/My_Project.git
cd My_Project
```

### 2. Установите Poetry

```bash
pip install poetry
```

### 3. Установите зависимости

```bash
poetry install
```

> В `pyproject.toml` указана версия Python `^3.14`. Перед установкой убедитесь, что используемая версия Python соответствует настройкам проекта.

## Настройка переменных окружения

Для конвертации валют через внешний API нужен API-ключ.

В проекте есть файл-пример:

```text
.env.example
```

Создайте на его основе файл `.env`.

Для Linux/macOS:

```bash
cp .env.example .env
```

Для Windows:

```bash
copy .env.example .env
```

В файле `.env` укажите API-ключ:

```env
API_KEY=your_api_key_here
```

Файл `.env` не должен попадать в публичный репозиторий, так как может содержать секретные данные.

## Использование

### Маскировка номера банковской карты

Функция `get_mask_card_number` принимает номер карты в виде строки или числа и возвращает замаскированный номер.

```python
from src.masks import get_mask_card_number

print(get_mask_card_number("1234567890123456"))
```

Результат:

```text
1234 56** **** 3456
```

Если номер карты некорректный, функция возвращает:

```text
Некорректный номер карты
```

### Маскировка номера банковского счёта

Функция `get_mask_account` принимает номер счёта и показывает только последние 4 символа.

```python
from src.masks import get_mask_account

print(get_mask_account("12345678901234567890"))
```

Результат:

```text
**7890
```

Если номер счёта некорректный, функция возвращает:

```text
Некорректный номер счета
```

### Маскировка карты или счёта по входной строке

Функция `mask_account_card` определяет, что передано: карта или счёт, — и возвращает строку с замаскированными данными.

```python
from src.widget import mask_account_card

print(mask_account_card("Visa Platinum 1234567890123456"))
print(mask_account_card("MasterCard 1234567890123456"))
print(mask_account_card("Счет 12345678901234560000"))
```

Результат:

```text
Visa Platinum 1234 56** **** 3456
MasterCard 1234 56** **** 3456
Счет **0000
```

Если данные введены некорректно, функция возвращает:

```text
Некорректный ввод данных
```

### Форматирование даты

Функция `get_date` преобразует дату из ISO-формата в формат `ДД.ММ.ГГГГ`.

```python
from src.widget import get_date

print(get_date("2024-03-11T02:26:18.671407"))
```

Результат:

```text
11.03.2024
```

Если дата некорректная, функция возвращает:

```text
Некорректный ввод
```

### Фильтрация операций по статусу

Функция `filter_by_state` возвращает список операций с указанным статусом. По умолчанию используется статус `EXECUTED`.

```python
from src.processing import filter_by_state

operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

print(filter_by_state(operations, "CANCELED"))
```

Результат:

```python
[
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}
]
```

### Сортировка операций по дате

Функция `sort_by_date` сортирует список операций по дате. По умолчанию сортировка выполняется по убыванию.

```python
from src.processing import sort_by_date

operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

print(sort_by_date(operations))
```

Для сортировки по возрастанию передайте `False` вторым аргументом:

```python
sort_by_date(operations, False)
```

### Чтение операций из JSON-файла

Функция `transactions_info` принимает путь до `JSON`-файла и возвращает список словарей с банковскими операциями.

```python
from src.utils import transactions_info

transactions = transactions_info("data/operations.json")
print(len(transactions))
```

Функция возвращает пустой список `[]`, если:

- файл не найден;
- JSON-файл содержит пустой список;
- содержимое JSON-файла не является списком.

### Чтение транзакций из CSV-файла

Функция `transactions_csv` принимает путь до `CSV`-файла и возвращает список словарей с транзакциями.

```python
from src.utils import transactions_csv

transactions = transactions_csv("data/transactions.csv")
print(transactions[0])
```

Файл `transactions.csv` читается через `csv.DictReader` с разделителем `;`.

Ожидаемые поля CSV-файла:

```text
id;state;date;amount;currency_name;currency_code;from;to;description
```

Если файл не найден, функция возвращает пустой список:

```python
[]
```

### Чтение транзакций из Excel-файла

Функция `transactions_excel` принимает путь до Excel-файла и возвращает список словарей с транзакциями.

```python
from src.utils import transactions_excel

transactions = transactions_excel("data/transactions_excel.xlsx")
print(transactions[0])
```

Для чтения Excel-файлов используются библиотеки `pandas` и `openpyxl`.

Если файл не найден, функция возвращает пустой список:

```python
[]
```

### Конвертация суммы транзакции в рубли

Функция `sum_transactions_rub` принимает словарь с данными транзакции и возвращает сумму операции в рублях в формате `float`.

```python
from src.external_api import sum_transactions_rub

transaction = {
    "operationAmount": {
        "amount": "200.00",
        "currency": {"name": "руб.", "code": "RUB"},
    }
}

print(sum_transactions_rub(transaction))
```

Результат:

```text
200.0
```

Если валюта транзакции — `RUB`, функция возвращает сумму без обращения к внешнему API.

Если валюта транзакции — `USD` или `EUR`, функция отправляет запрос к API конвертации валют и возвращает результат конвертации в рубли.

```python
from src.external_api import sum_transactions_rub

transaction = {
    "operationAmount": {
        "amount": "8221.37",
        "currency": {"name": "USD", "code": "USD"},
    }
}

print(sum_transactions_rub(transaction))
```

Для такой операции требуется корректный `API_KEY` в файле `.env`.

Если валюта не `RUB`, не `USD` и не `EUR`, функция возвращает:

```text
0
```

### Фильтрация транзакций по валюте

Функция-генератор `filter_by_currency` возвращает поочерёдно только те транзакции, у которых код валюты совпадает с переданным значением.

```python
from src.generators import filter_by_currency

transactions = [
    {
        "id": 939719570,
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
    },
    {
        "id": 873106923,
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
    },
]

usd_transactions = filter_by_currency(transactions, "USD")
print(next(usd_transactions))
```

Если транзакций с указанной валютой нет, генератор не возвращает элементы.

### Получение описаний транзакций

Функция-генератор `transaction_descriptions` возвращает описания операций по одному.

```python
from src.generators import transaction_descriptions

transactions = [
    {"description": "Перевод организации"},
    {"description": "Перевод со счета на счет"},
    {"description": "Перевод с карты на карту"},
]

for description in transaction_descriptions(transactions):
    print(description)
```

Результат:

```text
Перевод организации
Перевод со счета на счет
Перевод с карты на карту
```

### Генерация номеров банковских карт

Функция-генератор `card_number_generator` принимает начальное и конечное число диапазона и возвращает номера карт в формате `XXXX XXXX XXXX XXXX`.

```python
from src.generators import card_number_generator

for card_number in card_number_generator(1, 3):
    print(card_number)
```

Результат:

```text
0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
```

Если значение превышает 16 цифр, функция возвращает сообщение:

```text
Некорректный ввод данных. Попробуйте еще раз!
```

### Логирование выполнения функций

Декоратор `log` автоматически фиксирует успешное выполнение функции или ошибку, если она возникла.

Декоратор принимает необязательный параметр `filename`:

- если `filename` не передан, лог выводится в консоль;
- если `filename` передан, лог записывается в указанный файл в режиме добавления.

#### Логирование в консоль

```python
from src.decorators import log


@log()
def add_numbers(x: int, y: int) -> int:
    return x + y


add_numbers(2, 3)
```

Результат в консоли:

```text
add_numbers ok
```

#### Логирование ошибки

```python
from src.decorators import log


@log()
def divide(x: int, y: int) -> float:
    return x / y


divide(5, 0)
```

Результат в консоли:

```text
divide error: division by zero. Inputs: (5, 0), {}
```

Если внутри декорируемой функции возникает исключение, декоратор перехватывает его, записывает сообщение об ошибке и возвращает `None`.

#### Логирование в файл

```python
from src.decorators import log
from src.masks import get_mask_card_number

logged_mask_card_number = log("logging.txt")(get_mask_card_number)
logged_mask_card_number("1234567890123456")
```

После выполнения в файл `logging.txt` будет добавлена строка:

```text
get_mask_card_number ok
```

## Пример общего сценария работы

```python
from src.external_api import sum_transactions_rub
from src.processing import filter_by_state, sort_by_date
from src.utils import transactions_info

transactions = transactions_info("data/operations.json")
executed_transactions = filter_by_state(transactions)
sorted_transactions = sort_by_date(executed_transactions)

first_transaction = sorted_transactions[0]
amount_in_rub = sum_transactions_rub(first_transaction)

print(first_transaction)
print(amount_in_rub)
```

Этот сценарий:

1. загружает операции из JSON-файла;
2. оставляет только выполненные операции;
3. сортирует операции по дате;
4. берёт первую операцию из списка;
5. рассчитывает сумму операции в рублях.

## Тестирование

Для запуска тестов используйте команду:

```bash
poetry run pytest
```

Или, если зависимости установлены в активное окружение:

```bash
pytest
```

Тесты находятся в папке `tests/` и проверяют:

- маскировку карт и счетов;
- форматирование дат;
- фильтрацию операций по статусу;
- сортировку операций по дате;
- генераторы транзакций и номеров карт;
- декоратор логирования `log`;
- чтение данных из JSON-файла;
- чтение данных из CSV-файла;
- чтение данных из Excel-файла;
- конвертацию суммы транзакции в рубли.

В тестах для внешнего API используется `mock`, поэтому реальные запросы к сервису конвертации валют при тестировании не отправляются.

## Проверка покрытия тестами

Для запуска тестов с отчётом о покрытии:

```bash
poetry run pytest --cov=src
```

Для создания HTML-отчёта:

```bash
poetry run pytest --cov=src --cov-report=html
```

После выполнения команды отчёт будет доступен в папке:

```text
htmlcov/index.html
```

## Проверка качества кода

### Flake8

```bash
poetry run flake8 .
```

### Black

```bash
poetry run black .
```

### isort

```bash
poetry run isort .
```

### mypy

```bash
poetry run mypy .
```

## Форматы входных данных

### JSON

JSON-файл должен содержать список словарей с банковскими операциями. Для работы генераторов и конвертации валют используется вложенная структура `operationAmount`.

Пример:

```json
[
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  }
]
```

### CSV

CSV-файл должен содержать заголовки и использовать разделитель `;`.

```text
id;state;date;amount;currency_name;currency_code;from;to;description
```

### Excel

Excel-файл должен содержать таблицу с теми же полями, что и CSV-файл:

```text
id, state, date, amount, currency_name, currency_code, from, to, description
```

## Статус проекта

Проект находится в учебной разработке. Основной функционал реализован, для проверки используется набор тестов `pytest` и отчёт покрытия `pytest-cov`.


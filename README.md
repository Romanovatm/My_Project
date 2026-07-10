# Виджет банковских операций

## Описание

`My_Project` — учебное Python-приложение для обработки банковских транзакций.

Проект умеет загружать операции из файлов `JSON`, `CSV` и `XLSX`, фильтровать и сортировать их, искать операции по описанию, маскировать номера карт и счетов, формировать статистику по категориям и выводить итоговую выборку через консольный интерфейс.

Дополнительно реализованы генераторы, логирование функций, конвертация валютных операций в рубли через внешний API и автоматические тесты.

## Возможности

- маскировка номера банковской карты;
- маскировка номера банковского счёта;
- определение типа платёжных реквизитов по входной строке;
- преобразование ISO-даты в формат `ДД.ММ.ГГГГ`;
- загрузка транзакций из `JSON`, `CSV` и `XLSX`;
- фильтрация операций по статусу;
- сортировка операций по дате;
- фильтрация транзакций по коду валюты;
- поиск операций по слову или шаблону в описании;
- подсчёт количества операций по заданным категориям;
- последовательное получение описаний транзакций;
- генерация номеров банковских карт;
- конвертация сумм из `USD` и `EUR` в рубли;
- логирование успешного выполнения функций и ошибок;
- интерактивная работа с транзакциями через `main.py`;
- тестирование с помощью `pytest`;
- формирование отчёта о покрытии через `pytest-cov`.

## Структура проекта

```text
My_Project/
├── data/
│   ├── operations.json             # Операции в формате JSON
│   ├── transactions.csv            # Транзакции в формате CSV
│   └── transactions_excel.xlsx     # Транзакции в формате XLSX
├── logs/
│   ├── masks.log                   # Логи функций маскировки
│   └── utils.log                   # Логи функций чтения файлов
├── src/
│   ├── __init__.py
│   ├── decorators.py               # Декоратор логирования
│   ├── external_api.py             # Конвертация суммы в рубли
│   ├── generators.py               # Генераторы и фильтр по валюте
│   ├── masks.py                    # Маскировка карт и счетов
│   ├── processing.py               # Фильтрация, сортировка, поиск и статистика
│   ├── utils.py                    # Чтение JSON, CSV и XLSX
│   └── widget.py                   # Маскировка реквизитов и форматирование дат
├── tests/
│   ├── conftest.py
│   ├── test_decorators.py
│   ├── test_external_api.py
│   ├── test_generators.py
│   ├── test_masks.py
│   ├── test_processing.py
│   ├── test_utils.py
│   └── test_widget.py
├── htmlcov/                        # HTML-отчёт о покрытии
├── .env.example                    # Пример переменных окружения
├── .flake8                         # Настройки Flake8
├── .gitignore
├── logging.txt                     # Пример файла для декоратора log
├── main.py                         # Консольный интерфейс приложения
├── poetry.lock
├── pyproject.toml                  # Зависимости и настройки инструментов
└── README.md
```

## Технологии

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

### 1. Клонирование репозитория

```bash
git clone https://github.com/Romanovatm/My_Project.git
cd My_Project
```

### 2. Установка Poetry

```bash
pip install poetry
```

### 3. Установка зависимостей

```bash
poetry install
```

В `pyproject.toml` указано требование Python `^3.14`. Версия интерпретатора должна соответствовать этому ограничению.

## Настройка переменных окружения

Для конвертации валют используется сервис Exchange Rates Data от APILayer. API-ключ считывается из переменной окружения `API_KEY`.

Создайте файл `.env` на основе `.env.example`.

Linux/macOS:

```bash
cp .env.example .env
```

Windows:

```powershell
copy .env.example .env
```

Содержимое `.env`:

```env
API_KEY=your_api_key_here
```

Файл `.env` не следует добавлять в публичный репозиторий.

## Запуск консольного приложения

Из корневой директории проекта выполните:

```bash
poetry run python main.py
```

Либо при активированном виртуальном окружении:

```bash
python main.py
```

Программа последовательно предлагает:

1. выбрать источник транзакций: `JSON`, `CSV` или `XLSX`;
2. указать статус: `EXECUTED`, `CANCELED` или `PENDING`;
3. при необходимости отсортировать операции по дате;
4. оставить только рублёвые транзакции;
5. выполнить поиск по слову в описании;
6. вывести количество найденных операций и их основные данные.

### Пример сценария

```text
Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
```

При выводе операции программа показывает:

- дату и описание;
- замаскированные реквизиты отправителя и получателя;
- сумму и валюту операции.

## Использование модулей

### Маскировка номера карты

Функция `get_mask_card_number` принимает номер карты как строку или целое число.

```python
from src.masks import get_mask_card_number

result = get_mask_card_number("1234567890123456")
print(result)
```

Результат:

```text
1234 56** **** 3456
```

Для номера некорректной длины возвращается:

```text
Некорректный номер карты
```

### Маскировка номера счёта

```python
from src.masks import get_mask_account

result = get_mask_account("12345678901234567890")
print(result)
```

Результат:

```text
**7890
```

### Маскировка реквизитов по строке

Функция `mask_account_card` извлекает название карты или счёта и маскирует номер.

```python
from src.widget import mask_account_card

print(mask_account_card("Visa Platinum 1234567890123456"))
print(mask_account_card("Счет 12345678901234567890"))
```

Результат:

```text
Visa Platinum 1234 56** **** 3456
Счет **7890
```

### Форматирование даты

```python
from src.widget import get_date

print(get_date("2024-03-11T02:26:18.671407"))
```

Результат:

```text
11.03.2024
```

### Фильтрация по статусу

Функция `filter_by_state` по умолчанию выбирает операции со статусом `EXECUTED`.

```python
from src.processing import filter_by_state

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2024-05-12T10:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2024-05-11T10:00:00"},
]

executed = filter_by_state(operations)
canceled = filter_by_state(operations, "CANCELED")
```

Элементы без ключа `state` пропускаются.

### Сортировка по дате

```python
from src.processing import sort_by_date

sorted_operations = sort_by_date(operations)
```

По умолчанию используется сортировка по убыванию. Для сортировки по возрастанию передайте `False`:

```python
sorted_operations = sort_by_date(operations, False)
```

### Поиск операций по описанию

Функция `process_bank_search` выполняет регистронезависимый поиск по полю `description`.

```python
from src.processing import process_bank_search

transactions = [
    {"description": "Перевод со счета на счет"},
    {"description": "Открытие вклада"},
    {"description": "Перевод с карты на карту"},
]

result = process_bank_search(transactions, "счет")
```

В `result` попадёт операция с описанием `Перевод со счета на счет`.

Параметр `search` используется как регулярное выражение. Специальные символы регулярных выражений влияют на результат поиска.

### Подсчёт операций по категориям

Функция `process_bank_operations` считает количество операций, описание которых входит в переданный список категорий.

```python
from src.processing import process_bank_operations

transactions = [
    {"description": "Перевод с карты на карту"},
    {"description": "Открытие вклада"},
    {"description": "Перевод с карты на карту"},
]

categories = ["Перевод с карты на карту", "Открытие вклада"]
statistics = process_bank_operations(transactions, categories)
print(statistics)
```

Результат:

```python
{
    "Перевод с карты на карту": 2,
    "Открытие вклада": 1,
}
```

### Чтение JSON

```python
from src.utils import transactions_info

transactions = transactions_info("data/operations.json")
```

Функция возвращает пустой список `[]`, если:

- файл не найден;
- файл содержит пустой список;
- корневой JSON-объект не является списком.

### Чтение CSV

```python
from src.utils import transactions_csv

transactions = transactions_csv("data/transactions.csv")
```

Используется разделитель `;`. Ожидаемые заголовки:

```text
id;state;date;amount;currency_name;currency_code;from;to;description
```

### Чтение XLSX

```python
from src.utils import transactions_excel

transactions = transactions_excel("data/transactions_excel.xlsx")
```

Данные считываются через `pandas.read_excel` и преобразуются в список словарей.

### Фильтрация по валюте

`filter_by_currency` — функция-генератор для транзакций с вложенным полем `operationAmount`.

```python
from src.generators import filter_by_currency

rub_transactions = list(filter_by_currency(transactions, "RUB"))
```

Ожидаемая структура валюты:

```python
transaction["operationAmount"]["currency"]["code"]
```

### Получение описаний транзакций

```python
from src.generators import transaction_descriptions

for description in transaction_descriptions(transactions):
    print(description)
```

### Генерация номеров карт

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

Диапазон включает значения `start` и `stop`.

### Конвертация суммы в рубли

Функция `sum_transactions_rub`:

- возвращает сумму без запроса к API для операции в `RUB`;
- конвертирует `USD` и `EUR` в `RUB` через внешний API;
- возвращает `0` для других валют.

```python
from src.external_api import sum_transactions_rub

transaction = {
    "operationAmount": {
        "amount": "100.00",
        "currency": {
            "name": "USD",
            "code": "USD",
        },
    }
}

amount_in_rub = sum_transactions_rub(transaction)
```

Для запроса требуется корректный `API_KEY` и доступ к интернету.

### Декоратор логирования

Декоратор `log` фиксирует успешное завершение функции или возникшую ошибку.

#### Вывод в консоль

```python
from src.decorators import log


@log()
def add_numbers(x: int, y: int) -> int:
    return x + y


add_numbers(2, 3)
```

Вывод:

```text
add_numbers ok
```

#### Запись в файл

```python
from src.decorators import log


@log("logging.txt")
def add_numbers(x: int, y: int) -> int:
    return x + y
```

При исключении декоратор записывает имя функции, сообщение ошибки и переданные аргументы. Исключение не пробрасывается дальше, функция возвращает `None`.

## Форматы данных

### JSON

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

### CSV и XLSX

Табличные файлы используют плоскую структуру:

```text
id, state, date, amount, currency_name, currency_code, from, to, description
```

Для CSV применяется разделитель `;`.

## Тестирование

Запуск всех тестов:

```bash
poetry run pytest
```

Подробный вывод:

```bash
poetry run pytest -v
```

Тесты проверяют:

- маскировку карт и счетов;
- форматирование дат;
- фильтрацию и сортировку операций;
- поиск по описанию;
- подсчёт операций по категориям;
- генераторы;
- чтение `JSON`, `CSV` и `XLSX`;
- декоратор логирования;
- конвертацию валют.

В тестах внешнего API используется подмена ответа через `mock`, поэтому реальные запросы не выполняются.

## Покрытие тестами

Запуск с отображением покрытия в терминале:

```bash
poetry run pytest --cov=src
```

Создание HTML-отчёта:

```bash
poetry run pytest --cov=src --cov-report=html
```

Отчёт будет создан в файле:

```text
htmlcov/index.html
```

## Проверка качества кода

### Flake8

```bash
poetry run flake8 .
```

### Black

Проверка без изменения файлов:

```bash
poetry run black --check .
```

Автоматическое форматирование:

```bash
poetry run black .
```

### isort

Проверка порядка импортов:

```bash
poetry run isort --check-only .
```

Исправление порядка импортов:

```bash
poetry run isort .
```

### mypy

```bash
poetry run mypy .
```

## Статус проекта

Проект находится в учебной разработке. Реализованы загрузка, обработка, поиск, фильтрация и консольный вывод банковских операций. Функциональность покрывается модульными тестами и проверяется инструментами статического анализа и форматирования.

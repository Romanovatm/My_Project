from functools import wraps
from typing import Callable, ParamSpec, TypeVar

# P запоминает параметры (аргументы) исходной функции
P = ParamSpec("P")
# R запоминает тип возвращаемого значения исходной функции
R = TypeVar("R")


def log(filename: None | str = None) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Декоратор log, который автоматически логирует выполнение функции, а также ее результаты
    или возникшие ошибки. Декоратор принимает необязательный аргумент filename, который
    определяет, куда будут записываться логи (в файл или в консоль).
    """

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            result = None
            try:
                result = func(*args, **kwargs)
                log_text = f"{func.__name__} ok"
            except Exception as e:
                log_text = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
            if filename:
                with open(filename, "a", encoding="UTF-8") as file:
                    file.write(f"{log_text}\n")
            else:
                print(log_text)
            return result  # type: ignore

        return wrapper

    return decorator

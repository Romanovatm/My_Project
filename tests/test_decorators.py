from src.decorators import log
from src.masks import get_mask_card_number


def test_log_ok_console(capsys):
    decorated_function = log()(get_mask_card_number)
    decorated_function(1234567890123456)
    captured = capsys.readouterr()
    assert captured.out == "get_mask_card_number ok\n"


def test_log_error_console(capsys):
    @log()
    def some_function(x, y):
        return x / y

    some_function(5, 0)
    captured = capsys.readouterr()
    assert captured.out == "some_function error: division by zero. Inputs: (5, 0), {}\n"


def test_log_ok_file():
    decorated_function = log("logging.txt")(get_mask_card_number)
    decorated_function(1234567890123456)
    with open("logging.txt", "r") as f:
        result = f.read()
        list_result = [x for x in result.split("\n") if x != ""]
        assert list_result[-1] == "get_mask_card_number ok"


def test_log_error_file():
    @log("logging.txt")
    def some_function(x, y):
        return x / y

    some_function(5, 0)
    with open("logging.txt", "r") as f:
        result = f.read()
        list_result = [x for x in result.split("\n") if x != ""]
        assert list_result[-1] == "some_function error: division by zero. Inputs: (5, 0), {}"

import os
import pytest
from src.decorators import log



def test_log_success_console(capsys):
     @log()
     def add(a, b):
         return a + b

     result = add(2,3)
     assert result == 5

     #Перехватываем консольный вывод
     captured = capsys.readouterr()
     assert "add ok" in captured.out



def test_log_error_console(capsys):
    @log()
    def div(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(1, 0)


    captured =capsys.readouterr()
    assert "div error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0)" in captured.out



def test_log_success_file(tmp_path):
    log_file = tmp_path / "log.txt"

    @log(filename=log_file)
    def mul( a, b):
        return a * b

    result = mul(2,4)
    assert result == 8

    with open(log_file, encoding="utf-8") as f:
        content = f.read()

    assert "mul ok" in content


def test_log_error_file(tmp_path):
    log_file = tmp_path / "log.txt"

    @log(filename=log_file)
    def div(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        div( 3, 0)

    with open(log_file, encoding="utf-8") as f:
        content = f.read()

    assert "div error: ZeroDivisionError" in content
    assert "Inputs: (3, 0)" in content




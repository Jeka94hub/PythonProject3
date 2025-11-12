import functools

def log(filename=None):
    """ Декоратор для логирования начала, конца, и обишок при выполнении функции"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log_message = ""
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                _write_log(log_message, filename)
                return result
            except Exception as e:
                log_message = (
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                _write_log(log_message, filename)
                raise  # пробрасываем ошибкуу дальше
        return wrapper
    return decorator



def _write_log(message, filename=None):
    """ Вспомогательная функция для записи лога в файл или в консоль. """
    if filename:
        with open(filename,"a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)


 # пример использования
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


@log()  # Вывод в консоль
def divide(a, b):
    return a / b


if __name__ == "__main__":
    my_function(1, 2) # лог в файл
    try:
        divide(5, 0) # ошибка - лог в консоль
    except ZeroDivisionError:
        pass


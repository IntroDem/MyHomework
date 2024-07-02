from typing import Callable


def repeat(times: int = 2):
    """
    Параметризуемый декоратор, который выполняет декорируемую функцию заданное количество раз.

    :param times: Количество вызовов декорируемой функции. По умолчанию 2.
    """

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


# Пример функции для тестирования
@repeat(4)
def testing_function():
    print("python")


# (.venv) PS C:\modul3Python\pythonProject2\Homework14> python -i 4.py
# >>> testing_function()
# python
# python
# python
# python
# >>>

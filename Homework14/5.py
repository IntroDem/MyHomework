from functools import wraps


def logger(func):
    """
    Декоратор для ведения журнала вызовов декорируемой функции.

    :param func: Декорируемая функция.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        arg_names = func.__code__.co_varnames[: func.__code__.co_argcount]
        default_values = func.__defaults__ or ()
        kw_defaults = func.__kwdefaults__ or {}

        # Сопоставляем позиционные аргументы с именами и значениями по умолчанию
        args_with_names = {
            arg_names[i]: (
                args[i]
                if i < len(args)
                else default_values[i - len(arg_names) + len(default_values)]
            )
            for i in range(max(len(args), len(arg_names)))
        }

        # Добавляем ключевые аргументы
        args_with_names.update(kwargs)

        # Добавляем ключевые аргументы со значениями по умолчанию
        for k, v in kw_defaults.items():
            if k not in args_with_names:
                args_with_names[k] = v

        # Подготовка строки вызова для журнала
        call_str = f"{func_name}("
        call_str += ", ".join([f"{k}={v}" for k, v in args_with_names.items()])
        call_str += ")"

        try:
            result = func(*args, **kwargs)
            print(f"{call_str} -> {result}")
            return result
        except Exception as e:
            print(f"{call_str} .. {type(e).__name__}: {e}")
            return None

    return wrapper


# Пример функции для тестирования
@logger
def div_round(num1, num2, *, digits=0):
    return round(num1 / num2, digits)


# (.venv) PS C:\modul3Python\pythonProject2\Homework14> python -i 5.py
# >>> print(div_round(1, 3, digits=2))
# div_round(num1=1, num2=3, digits=2) -> 0.33
# 0.33
# >>> print(div_round(7, 2))
# div_round(num1=7, num2=2, digits=0) -> 4.0
# 4.0
# >>> print(div_round(5, 0))
# div_round(num1=5, num2=0, digits=0) .. ZeroDivisionError: division by zero
# None
# >>>

# 1. Проверка типов аргументов: Напишите декоратор, который будет проверять типы аргументов передаваемой
# функции и выводить предупреждение в случае несоответствия.
from colorama import init, Fore, Style
from functools import wraps
import warnings


def type_check(expected_types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    warnings.warn(
                        f"Аргумент {i+1} не является {expected_type.__name__}",
                        UserWarning,
                    )
            return func(*args, **kwargs)

        return wrapper

    return decorator


@type_check([int, str, list, float])
def foo(a, b, c, d):
    return f"{a}, {b}, {c}, {d}"


print(foo(1, "bar", [], 4.0))  # Аргументы правильные, предупреждений нет
print(foo(1, 2, [], 4.0))  # Предупреждение: второй аргумент не строка


# 2. Декоратор для изменения цвета вывода в консоли: Напишите декоратор, который будет изменять цвет текста,
# выводимого функцией в консоли.

init()


def colorize_output(color):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                return f"{color}{result}{Style.RESET_ALL}"
            else:
                return result

        return wrapper

    return decorator


@colorize_output(Fore.CYAN)
def greet(name):
    return f"Привет, {name}!"


@colorize_output(Fore.GREEN)
def bb(name):
    return f"Прощай, {name}!"


print(greet("Дмитрий"))
print(bb("Андрей"))

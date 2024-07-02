from typing import Callable, List, Union


def math_function_resolver(
    func: Callable[[float], float], *args: Union[int, float], res_to_str: bool = False
) -> List[Union[int, str]]:
    """
    Вычисляет округленные значения для различных математических функций.

    :param func: Математическая функция, принимающая один обязательный позиционно-ключевой аргумент - число x.
    :param args: Произвольное количество значений x для математической функции.
    :param res_to_str: Переключатель, определяющий тип вычисляемых значений: float (False) или str (True). По умолчанию False.
    :return: Список округленных значений математической функции для переданных значений x.
    """
    result = [round(func(x)) for x in args]

    if res_to_str:
        result = list(map(str, result))

    return result


# (.venv) PS C:\modul3Python\pythonProject2\Homework14> python -i 3.py
# >>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
# [2, 3, 4, 4, 4, 5, 6, 6, 6]
# >>> math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10))
# [2, 1, 0, 0, 0, -1, -2, -2, -2]
# >>> math_function_resolver(lambda x: 2.72**x, *range(1, 10), res_to_str=True)
# ['3', '7', '20', '55', '149', '405', '1101', '2996', '8149']
# >>>

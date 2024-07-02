from typing import Dict, Tuple, List, Optional
from ref_1 import E_series


def pick_resistors(resistance: int) -> Optional[Dict[str, Tuple[int, ...]]]:
    """
    Подбирает ближайшие номиналы сопротивления из всех рядов сопротивлений.

    Значение сопротивления в диапазоне от 100 до 999 включительно.
    :return: Словарь с ближайшими номиналами сопротивлений для каждого ряда,
             либо None, если переданное значение сопротивления вне диапазона.
    """

    # Проверяем, что значение сопротивления в заданном диапазоне
    if not (100 <= resistance <= 999):
        return None

    def closest_values(series: List[int]) -> Tuple[int, ...]:
        """
        Находит номиналы из ряда, ближайшие к заданному значению сопротивления.

        """
        min_diff = min(map(lambda x: abs(x - resistance), series))
        return tuple(filter(lambda x: abs(x - resistance) == min_diff, series))

    # Создание результата в виде словаря
    result = {series: closest_values(values) for series, values in E_series.items()}

    return result


# >>> print(pick_resistors(112))
# {'E6': (100,), 'E12': (120,), 'E24': (110,), 'E48': (110,), 'E96': (113,)}
# >>>
#
# >>> print(pick_resistors(549))
# {'E6': (470,), 'E12': (560,), 'E24': (560,), 'E48': (536, 562), 'E96': (549,)}
# >>>
# >>> print(pick_resistors(182))
# {'E6': (150,), 'E12': (180,), 'E24': (180,), 'E48': (178,), 'E96': (182,)}
# >>>
# >>> print(pick_resistors(196))
# {'E6': (220,), 'E12': (180,), 'E24': (200,), 'E48': (196,), 'E96': (196,)}
# >>>

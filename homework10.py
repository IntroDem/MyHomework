# Задача 1
# Есть три кортежа целых чисел необходимо найти элементы, которые есть во всех кортежах.

import random


def generate_random_tupls(size, low=1, high=10):
    return tuple(random.randint(low, high) for _ in range(size))


tuples_1 = generate_random_tupls(10)
tuples_2 = generate_random_tupls(10)
tuples_3 = generate_random_tupls(10)

set_1 = set(tuples_1)
set_2 = set(tuples_2)
set_3 = set(tuples_3)

print(tuples_1)
print(tuples_2)
print(tuples_3)

print(
    set_1 & set_2 & set_3,
    "Элементы которые есть во всех кортежах",
)

# Задание 2
# Есть три кортежа целых чисел необходимо найти элементы, которые уникальны для каждого списка.

unique_in_set_1 = set_1 - set_2 - set_3
print(unique_in_set_1, "Уникальные элементы первого кортежа")

unique_in_set_2 = set_2 - set_1 - set_3
print(unique_in_set_2, "Уникальные элементы второго кортежа")

unique_in_set_3 = set_3 - set_2 - set_1
print(unique_in_set_3, "Уникальные элементы третьего кортежа")

unique_all = unique_in_set_1.union(unique_in_set_2).union(unique_in_set_3)

print(unique_all, "Все уникальные элементы")


# Задание 3
# Напишите функцию print_info, которая принимает имя человека в качестве обязательного аргумента и произвольное
# количество дополнительной информации в виде именованных аргументов. Функция должна выводить переданное имя и всю
# дополнительную информацию.

# Пример использования:
# print_info("Иван", возраст=30, профессия="инженер", город="Москва")
# Вывод:
# Имя: Иван
# Возраст: 30
# Профессия: инженер
# Город: Москва


def print_info(name, **kwargs):
    print(f"Имя: {name}")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")


print_info("Иван", возраст=30, профессия="инженер", город="Москва")
print_info("Дмитрий", возраст=33, город="Брянск")

# Задание 4
# Напишите lambda функцию, которая принимает список чисел и возвращает новый список, содержащий квадраты всех
# нечетных чисел и кубы всех четных чисел.
#
# Входные данные:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Выходные данные:
# print(mapped_result)
# Вывод: [1, 8, 9, 64, 25, 216, 49, 512, 81]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

square_and_cube = lambda x: x**2 if x % 2 != 0 else x**3

mapped_result = list(map(square_and_cube, numbers))
print(numbers)
print(mapped_result)

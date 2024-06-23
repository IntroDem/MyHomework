# Задание 1
# В списке целых, заполненном случайными числами, определить минимальный и максимальный элементы, посчитать количество
# отрицательных элементов, посчитать количество положительных элементов, посчитать количество нулей. Результаты вывести
# на экран.

import random

random_numbers = [random.randint(-10, 10) for _ in range(20)]
print(random_numbers)

min_value = min(random_numbers)
print("min_value - ", min_value)

max_value = max(random_numbers)
print("max_value - ", max_value)

zero_count = random_numbers.count(0)
print("zero_count - ", zero_count)

negative_count = 0
for num in random_numbers:
    if num < 0:
        negative_count += 1
print("negative_count - ", negative_count)

positive_count = 0
for num in random_numbers:
    if num > 0:
        positive_count += 1
print("positive_count - ", positive_count)

# Задание 2
# Напишите программу, которая удаляет дубликаты из списка. Пример работы:
# Начальный список:  [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]

first_list = [10, 20, 10, 20, 30, 40, 30, 50]
print("first_list - ", first_list)

unique_list = []

for num in first_list:
    if num not in unique_list:
        unique_list.append(num)
print("unique_list - ", unique_list)

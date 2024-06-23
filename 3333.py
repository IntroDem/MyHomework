# # Функция для подсчета суммы и среднего арифметического чисел в указанном диапазоне
# def calculate_numbers(start, end):
#     # Инициализация переменных для сумм и счетчиков
#     sum_even = 0
#     count_even = 0
#     sum_odd = 0
#     count_odd = 0
#     sum_multiple_of_9 = 0
#     count_multiple_of_9 = 0
#
#     # Цикл для прохода по диапазону чисел
#     for num in range(start, end + 1):
#         # Проверка на четность
#         if num % 2 == 0:
#             sum_even += num
#             count_even += 1
#         # Проверка на нечетность
#         else:
#             sum_odd += num
#             count_odd += 1
#         # Проверка на кратность 9
#         if num % 9 == 0:
#             sum_multiple_of_9 += num
#             count_multiple_of_9 += 1
#
#     # Подсчет среднего арифметического
#     if count_even != 0:
#         avg_even = sum_even / count_even
#     else:
#         avg_even = 0
#
#     if count_odd != 0:
#         avg_odd = sum_odd / count_odd
#     else:
#         avg_odd = 0
#
#     if count_multiple_of_9 != 0:
#         avg_multiple_of_9 = sum_multiple_of_9 / count_multiple_of_9
#     else:
#         avg_multiple_of_9 = 0
#
#     # Вывод результатов
#     print("Сумма четных чисел:", sum_even)
#     print("Среднее арифметическое четных чисел:", avg_even)
#     print("Сумма нечетных чисел:", sum_odd)
#     print("Среднее арифметическое нечетных чисел:", avg_odd)
#     print("Сумма чисел, кратных 9:", sum_multiple_of_9)
#     print("Среднее арифметическое чисел, кратных 9:", avg_multiple_of_9)
#
#
# # Получение ввода от пользователя
# start_num = int(input("Введите начальное число: "))
# end_num = int(input("Введите конечное число: "))
#
# # Вызов функции для подсчета чисел
# calculate_numbers(start_num, end_num)

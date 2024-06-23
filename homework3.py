# Задание 1
# Пользователь вводит с клавиатуры два числа. Нужно посчитать отдельно сумму четных, нечетных и чисел, кратных 9 в
# указанном диапазоне, а также среднеарифметическое каждой группы.

# start, end = int(input("Enter start: ")), int((input("Enter stop: ")))
#
# if start > end:
#     start, end = end, start
#
# sum_even = 0
# count_even = 0
# sum_odd = 0
# count_odd = 0
# sum_9 = 0
# count_9 = 0
#
# for i in range(start, end + 1):
#     if i % 2 == 0:
#         sum_even += i
#         count_even += 1
#     else:
#         sum_odd += i
#         count_odd += 1
#     if i % 9 == 0:
#         sum_9 += i
#         count_9 += 1
#
# if count_even != 0:
#     even_mean = sum_even / count_even
# else:
#     even_mean = 0
#
# if count_odd != 0:
#     odd_mean = sum_odd / count_odd
# else:
#     odd_mean = 0
#
# if count_9 != 0:
#     sum_9_mean = sum_9 / count_9
# else:
#     sum_9_mean = 0
#
# print("Sum of even numbers: ", sum_even)
# print("Sum of odd numbers: ", sum_odd)
# print("Sum of multiples of 9: ", sum_9)
#
# print("Arithmetic mean of even numbers: ", even_mean)
# print("Arithmetic mean of odd numbers: ", odd_mean)
# print("Arithmetic mean of multiples of 9: ", sum_9_mean)

# Второй вариант решения через массивы. Чуть погуглив нашёл как правильно пишется синтаксис. Не сильно отличается от JS.

# start, end = int(input("Enter start: ")), int((input("Enter stop: ")))
# if start > end:
#     start, end = end, start
# even_numbers = []
# odds_numbers = []
# multiples_9_numbers = []
#
# for i in range(start, end + 1):
#     if i % 2 == 0:
#         even_numbers.append(i)
#     else:
#         odds_numbers.append(i)
#     if i % 9 == 0:
#         multiples_9_numbers.append(i)
#
# sum_even = sum(even_numbers)
# sum_odd = sum(odds_numbers)
# sum_multiples_9 = sum(multiples_9_numbers)
#
# avg_even = sum_even / len(even_numbers) if even_numbers else 0
# avg_odd = sum_odd / len(odds_numbers) if odds_numbers else 0
# avg_multiples_9 = (
#     sum_multiples_9 / len(multiples_9_numbers) if multiples_9_numbers else 0
# )
#
# print("Sum of even numbers: ", sum_even)
# print("Sum of odd numbers: ", sum_odd)
# print("Sum of multiples of 9: ", sum_multiples_9)
# print("Arithmetic mean of even numbers: ", avg_even)
# print("Arithmetic mean of odd numbers: ", avg_odd)
# print("Arithmetic mean of multiples of 9: ", avg_multiples_9)

# Задание 2
# Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все цифры 3 и 6 и вывести обратно на
# экран. Будет плюсом если вы используете управляющие операторы continue, break и else.

# num_input = input("Enter a number: ")
# filter_num = []
#
# for i in num_input:
#     num = int(i)
#     if num in (3, 6):
#         continue
#     filter_num.append(num)
# else:
#     print("The filtered numbers are:", filter_num)
#
# Вариант по примеру как решал Морозов на уроке.
#
# num_input = input("Enter a number: ")
# num_arr = [int(digit) for digit in list(num_input)]
# filtered_numbers = [num for num in num_arr if num not in (3, 6)]
# print("The filtered numbers are: ", filtered_numbers)

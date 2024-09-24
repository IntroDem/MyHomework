# Задание 1
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# на экран сумму трёх чисел или произведение трёх чисел.
action = input("Enter your action: сложение/умножение: ")

while True:
    try:
        num_1 = float(input("Enter a number one: "))
        num_2 = float(input("Enter a number two: "))
        num_3 = float(input("Enter a number three: "))
        break
    except ValueError:
        print("Please enter a number.")

sum = num_1 + num_2 + num_3
mult = num_1 * num_2 * num_3

if action == "сложение":
    print(sum)
elif action == "умножение":
    print(mult)
else:
    print("Некорректное действие")


# Задание 2
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.

# while True:
#     try:
#         number_1 = float(input("Enter a number one: "))
#         number_2 = float(input("Enter a number two: "))
#         number_3 = float(input("Enter a number three: "))
#         break
#     except ValueError:
#         print("Please enter a number.")
#
# toDo_ = input("Enter your action: max/min/mean: ")
# if toDo_ == "max":
#     res_max = number_1
#     if number_2 > res_max:
#         res_max = number_2
#     if number_3 > res_max:
#         res_max = number_3
#     print("The result is " + str(res_max))
# elif toDo_ == "min":
#     res_min = number_1
#     if number_2 < res_min:
#         res_min = number_2
#     if number_3 < res_min:
#         res_min = number_3
#     print("The result is " + str(res_min))
# elif toDo_ == "mean":
#     res_mean = (number_1 + number_2 + number_3) / 3
#     print("The result is " + str(res_mean))
# else:
#     print("Please enter a valid action.")

# Задание 3
# Пользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программа
# переводит метры в мили, дюймы или ярды.

# meters = float(input("Enter the number of meters: "))
#
# choice = input("Select the unit of measurement: i - inches, m - miles y - yard: ")
#
# if choice == "i":
#     inches = meters * 39.37
#     print("Inches: ", inches)
# elif choice == "m":
#     miles = meters * 1.609
#     print("Miles: ", miles)
# elif choice == "y":
#     yards = meters * 1.09361
#     print("Yards: ", yards)
# else:
#     print("Please enter a valid choice")

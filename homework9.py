# Задача "Генератор паролей":
# Напишите функцию, которая генерирует случайный пароль заданной длины, состоящий из букв (верхнего и нижнего регистра),
# цифр и специальных символов.

import string
import random


def get_random_password(length, complexity=3):
    result = ""

    if complexity == 1:
        chars = string.ascii_letters
    elif complexity == 2:
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length):
        result += random.choice(chars)

    return result


while True:
    try:
        password_length = int(input("Введите длину пароля: "))
        if password_length <= 0:
            print("Длина пароля должна быть больше нуля")
            continue

        password_complexity = input(
            "Введите сложность (1 - буквы, 2 - буквы и цифры, 3 - буквы цифры и пунктуация, по умолчанию 3): "
        )

        if password_complexity == "":
            password_complexity = 3
        else:
            password_complexity = int(password_complexity)

        generated_password = get_random_password(password_length, password_complexity)
        print(f"Сгенерированный пароль: {generated_password}")
        break
    except ValueError as e:
        e = "В этом поле могут быть только цифры и оно не может быть пустым"
        print(e)


# Задача "Магазин игрушек"
# В маленьком магазине игрушек "Веселые карусели" проходит акция для малышей. У каждого маленького покупателя есть
# возможность выбрать определенную игрушку со скидкой в зависимости от их возраста. Магазин предлагает следующие
# возрастные категории и скидки:
# Для детей до 3 лет - 10% скидка
# Для детей от 3 до 6 лет - 20% скидка
# Для детей от 6 до 10 лет - 30% скидка
# Для детей от 10 до 14 лет - 40% скидка
# Для детей старше 14 лет - 50% скидка
# В каждой категории скидка распространяется на все игрушки. Вам предстоит написать программу, которая с помощью
# функций, списков и оператора match case будет определять скидку для каждого покупателя в зависимости от их возраста.


def get_discount(age):
    match age:
        case age if age < 3:
            return 10
        case age if 3 <= age < 6:
            return 20
        case age if 6 <= age < 10:
            return 30
        case age if 10 <= age < 14:
            return 40
        case age if 14 <= age < 18:
            return 50
        case _:
            return 0


def discount():
    while True:
        try:
            age = int(input("Введите возраст ребёнка: "))
            if age < 0:
                print("Возраст не может быть отрицательным")
                continue
            discount_amount = get_discount(age)
            print(f"Для возраста {age} - скидка {discount_amount} %")
            break
        except ValueError:
            print("Введите корректное значение")


discount()


# Задача "Турнир по дартсу"
# В джентльменском клубе "Мастера Дартса" проходит ежемесячный турнир по дартсу. Участникам предстоит соревноваться в
# меткости и точности бросков. Организаторы решили автоматизировать процесс подсчета очков с помощью специальной
# программы.
# У каждого участника есть возможность совершить 5 бросков в каждом раунде. За каждое попадание в мишень игрок получает
# определенное количество очков. В зависимости от набранных очков после 5 бросков игроки будут распределены по разным
# категориям.
# Создайте программу, используя функции, списки и оператор match case, которая будет определять категорию каждого
# игрока в турнире по их общему количеству очков после 5 бросков.


players = [
    ("Alice", 20, 15, 10, 5, 12),
    ("Bob", 25, 30, 30, 25, 20),
    ("Charlie", 15, 15, 20, 25, 30),
]


def get_player_score(player_data):
    return sum(player_data[1:])


def determine_category(total_score):
    match total_score:
        case _ if total_score >= 120:
            return "Мастер"
        case _ if total_score >= 80:
            return "Профессионал"
        case _ if total_score >= 50:
            return "Любитель"
        case _:
            return "Новичок"


def main_darts():
    for player in players:
        player_name = player[0]
        total_score = get_player_score(player)
        category = determine_category(total_score)
        print(
            f"Игрок {player_name} набрал {total_score} очков и попадает в категорию: {category}"
        )


main_darts()

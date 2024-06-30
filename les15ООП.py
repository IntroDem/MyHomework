# Объектно ориентированное программирование.
from abc import ABC, abstractmethod


# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @abstractmethod
#     def hello(self):
#         pass
#
#
# class Mag(Human):
#     def hello(self):
#         return "Hello Mr. " + self.name
#
#
# Dmitry = Mag("Dmitry", 20)
#
# print(Dmitry.hello())


# class TheSimplestClass:
#     pass
#
#
# myFirstObject = TheSimplestClass()

# stack = []
#
#
# def push(val):
#     stack.append(val)
#
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
#
#
# push(3)
# push(2)
# push(1)
#
# print(stack[2])
#
# print(pop())
# print(pop())
# print(pop())


class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


stackObj = Stack()
stackObj2 = Stack()

stackObj.push(3)
stackObj.push(2)
stackObj.push(1)
print(stackObj.pop())
print(stackObj.pop())
print(stackObj.pop())

# Реализуйте класс «Человек». Необходимо хранить в
# полях класса: ФИО, дату рождения, контактный телефон,
# город, страну, домашний адрес. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса


class Human:
    def __init__(self, FIO, birthday, mobile, City, Country, address):
        self.FIO = FIO
        self.birthday = birthday
        self.mobile = mobile
        self.City = City
        self.Country = Country
        self.address = address

    def set_data(self, FIO, birthday, mobile, City, Country, address):
        self.FIO = FIO
        self.birthday = birthday
        self.mobile = mobile
        self.City = City
        self.Country = Country
        self.address = address

    def get_data(self):
        return {
            "ФИО": self.FIO,
            "День рождения": self.birthday,
            "Телефон": self.mobile,
            "Город": self.City,
            "Страна": self.Country,
            "Адресс": self.address,
        }

    def print_data(self):
        data = self.get_data()
        for key, value in data.items():
            print(f"{key}: {value}")

    def get_FIO(self):
        return self.FIO

    def set_FIO(self, FIO):
        self.FIO = FIO

    def get_birthday(self):
        return self.birthday

    def set_birthday(self, birthday):
        self.birthday = birthday

    def get_mobile(self):
        return self.mobile

    def set_mobile(self, mobile):
        self.mobile = mobile

    def get_City(self):
        return self.City

    def set_City(self, City):
        self.City = City

    def get_Country(self):
        return self.Country

    def set_Country(self, Country):
        self.Country = Country

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address


dmitry = Human(
    "Кузнеченков Д.В",
    "12.07.1990",
    "+7-900 111 22 33",
    "Брянск",
    "Россия",
    "ул. Брянская, д. 111",
)

print(dmitry.get_FIO())
print(dmitry.get_birthday())
print(dmitry.get_mobile())
print(dmitry.get_City())
print(dmitry.get_Country())
print(dmitry.get_address())

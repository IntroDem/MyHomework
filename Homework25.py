# Прочитайте следующие статьи и определите, какой паттерн где описан, исходя из
# примеров, описанных ниже.
# Фабричный метод: https://python-patterns.guide/gang-of-four/factory-method/
# Прототип: https://python-patterns.guide/gang-of-four/prototype/
# Одиночка: https://python-patterns.guide/gang-of-four/singleton/
# *Держите наготове переводчик. Все статьи на английском.


# Пример №1.
# Используется паттерн Прототип. Объект создаётся путём клонирования существующего объекта. Метод clone позволяет
# создать поверхностную копию объекта.
from abc import ABCMeta, abstractmethod


class IProtoType(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def clone():
        """Some kind of cloning mechanism"""


class MyClass(IProtoType):
    def __init__(self, field):
        self.field = field

    def clone(self):
        """This clone method uses a shallow copy technique"""
        return type(self)(self.field)  # a shallow copy is returned

    def __str__(self):
        return f"{id(self)}\tfield={self.field}\ttype={type(self.field)}"


# Creating an instance of MyClass
OBJECT1 = MyClass([1, 2, 3, 4])
print(f"OBJECT1 {OBJECT1}")

# Cloning OBJECT1
OBJECT2 = OBJECT1.clone()

# Modify the cloned object's field to see if it affects the original object
OBJECT2.field[1] = 101

# Comparing OBJECT1 and OBJECT2
print(f"OBJECT2 {OBJECT2}")
print(f"OBJECT1 {OBJECT1}")


# Пример №2.
# Используется паттерн Одиночка. Класс Class гарантирует что создаётся только один экземпляр объекта. Следующие
# попытки создать объект будут возвращать первый существующий экземпляр.


class Class(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Class, cls).__new__(cls)
        return cls.instance


# Creating two instances of Class
obj = Class()
new_obj = Class()

# Checking if both instances are the same
print(obj is new_obj)  # Output: True

# Setting a variable in one instance and checking it in the other
obj.var = "Class Variable"
print(new_obj.var)  # Output: Class Variable


# Пример №3.
# Используется Фабричный метод. Функция Fuction создаёт и возвращает объекты разных классов локализаций,
# в зависимости от переданного языка.
class FrenchLocalizer:
    def __init__(self):
        self.translations = {
            "car": "voiture",
            "bike": "bicyclette",
            "cycle": "cyclette",
        }

    def localize(self, msg):
        return self.translations.get(msg, msg)


class SpanishLocalizer:
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta", "cycle": "ciclo"}

    def localize(self, msg):
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    def localize(self, msg):
        return msg


def Function(language="English"):
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }
    return localizers[language]()


if __name__ == "__main__":
    f = Function("French")
    e = Function("English")
    s = Function("Spanish")

    message = ["car", "bike", "cycle"]
    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))

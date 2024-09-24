# Задание №2
# Создать базовый класс «Домашнее животное» и производные классы«Собака»,
# «Кошка», «Попугай», «Хомяк». С помощью конструктора установить имя каждого
# животного и его характеристики.
# Реализуйте для каждого из классов методы:
# ■ Sound — издает звук животного (пишем текстом в консоль);
# ■ Show — отображает имя животного;
# ■ Type — отображает название его подвида;


class Pet:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def sound(self):
        pass

    def show(self):
        print(f"Имя питомца: {self.name}")

    def type(self):
        print(f"Порода питомца: {self.kind}")


class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(name, "Собака")
        self.breed = breed

    def sound(self):
        print(f"{self.name}: 'Гав! Гав!'")

    def type(self):
        print(f"Вид питомца: {self.kind} \nПорода питомца: {self.breed}")


class Cat(Pet):
    def __init__(self, name, breed):
        super().__init__(name, "Кошка")
        self.breed = breed

    def sound(self):
        print(f"{self.name}: 'Мяу! Мяу!'")

    def type(self):
        print(f"Вид питомца: {self.kind} \nПорода питомца: {self.breed}")


class Parrot(Pet):
    def __init__(self, name, breed):
        super().__init__(name, "Попугай")
        self.breed = breed

    def sound(self):
        print(f"{self.name}: 'Чирик! Чирик!'")

    def type(self):
        print(f"Вид питомца: {self.kind} \nПорода питомца: {self.breed}")


class Hamster(Pet):
    def __init__(self, name, breed):
        super().__init__(name, "Хомяк")
        self.breed = breed

    def sound(self):
        print(f"{self.name}: 'Хрум! Хрум!'")

    def type(self):
        print(f"Вид питомца: {self.kind} \nПорода питомца: {self.breed}")


def main():
    dog = Dog(name="Рекс", breed="Лабрадор")
    cat = Cat(name="Ася", breed="Сиамская")
    parrot = Parrot(name="Полли", breed="Ара")
    hamster = Hamster(name="Моня", breed="Сирийский")

    pets = [dog, cat, parrot, hamster]

    for pet in pets:
        pet.show()
        pet.type()
        pet.sound()
        print()


if __name__ == "__main__":
    main()

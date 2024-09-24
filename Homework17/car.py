# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
class Car:
    def __init__(self):
        self.manufacturer = ""
        self.model = ""
        self.year = 0
        self.V_engine = 0.0
        self.color = ""
        self.price = 0.0

    def input_data(self):
        self.manufacturer = input("Введите производителя автомобиля: ")
        self.model = input("Введите название модели автомобиля: ")
        self.year = int(input("Введите год выпуска автомобиля: "))
        self.V_engine = float(input("Введите объем двигателя (л): "))
        self.color = input("Введите цвет автомобиля: ")
        self.price = float(input("Введите цену автомобиля: "))

    def display_data(self):
        print("\nИнформация об автомобиле:")
        print("Производитель автомобиля:", self.get_manufacturer())
        print("Модель автомобиля:", self.get_model())
        print("Год выпуска автомобиля:", self.get_year())
        print("Объем двигателя автомобиля:", self.get_V_engine())
        print("Цвет автомобиля:", self.get_color())
        print("Цена автомобиля:", self.get_price())

    # Геттеры для доступа к полям класса
    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_V_engine(self):
        return self.V_engine

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    # Сеттеры для изменения полей класса
    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_V_engine(self, V_engine):
        self.V_engine = V_engine

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price


def main():
    car = Car()

    # Ввод данных
    car.input_data()

    # Вывод данных
    car.display_data()

    # Использование сеттеров для изменения полей(пример)
    car.set_price(25000)
    print("\nИзмененная цена автомобиля:", car.get_price())


if __name__ == "__main__":
    main()

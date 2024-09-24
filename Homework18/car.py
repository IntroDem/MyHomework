# Задание 1
# К уже реализованному классу «Автомобиль» добавьте
# конструктор, а также необходимые перегруженные методы.
class Car:
    def __init__(
        self, manufacturer="", model="", year=0, V_engine=0.0, color="", price=0.0
    ):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.V_engine = V_engine
        self.color = color
        self.price = price

    def __str__(self):
        return (
            f"{self.manufacturer} {self.model} выпущенная в {self.year} году, объёмом двигателя {self.V_engine}"
            f" цвет - {self.color} , стоит {self.price}"
        )

    def __eq__(self, other):
        if isinstance(other, Car):
            return (
                self.manufacturer == other.manufacturer
                and self.model == other.model
                and self.year == other.year
                and self.V_engine == other.V_engine
                and self.color == other.color
                and self.price == other.price
            )
        return False

    def __lt__(self, other):
        if isinstance(other, Car):
            return self.price < other.price
        return False

    def __len__(self):
        from datetime import date

        return date.today().year - self.year

    def input_data(self):
        self.manufacturer = input("Введите производителя автомобиля: ")
        self.model = input("Введите название модели автомобиля: ")
        self.year = int(input("Введите год выпуска автомобиля: "))
        self.V_engine = float(input("Введите объем двигателя (л): "))
        self.color = input("Введите цвет автомобиля: ")
        self.price = float(input("Введите цену автомобиля: "))

    def display_data(self):
        print(f"\nИнформация об автомобиле {self.manufacturer} {self.model}:")
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
    car1 = Car()
    car2 = Car("Toyota", "Camry", 2015, 2.5, "white", 30000)

    # Ввод данных для car1
    car1.input_data()

    # Вывод данных
    car1.display_data()
    car2.display_data()

    # Использование сеттеров для изменения полей(пример)
    car1.set_price(25000)
    print(
        f"\nИзмененная цена автомобиля {car1.manufacturer} {car1.model}:",
        car1.get_price(),
    )

    print(f"\nИнформация о {car1.manufacturer} {car1.model}:", car1)
    print(f"Информация о {car2.manufacturer} {car2.model}:", car2)

    print("\nСравнение автомобилей:")
    print("car1 == car2:", car1 == car2)

    print("\nСравнение стоимости автомобилей:")
    print(
        f"{car1.manufacturer} {car1.model} < {car2.manufacturer} {car2.model}:",
        car1 < car2,
    )

    print(f"\nВозраст {car1.manufacturer} {car1.model}:", len(car1), "лет")
    print(f"Возраст {car2.manufacturer} {car2.model}:", len(car2), "лет")


if __name__ == "__main__":
    main()

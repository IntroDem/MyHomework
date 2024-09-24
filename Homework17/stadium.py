# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.


class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self._name = name
        self._opening_date = opening_date
        self._country = country
        self._city = city
        self._capacity = capacity

    # использовании свойств (properties)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def opening_date(self):
        return self._opening_date

    @opening_date.setter
    def opening_date(self, opening_date):
        self._opening_date = opening_date

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    def display_data(self):
        print("Информация о стадионе:")
        print("Название:", self.name)
        print("Дата открытия:", self.opening_date)
        print("Страна:", self.country)
        print("Город:", self.city)
        print("Вместимость:", self.capacity)


def main():
    # Пример создания объекта стадиона с заданными параметрами
    stadium = Stadium(
        name="Газпром Арена",
        opening_date="2017-04-22",
        country="Россия",
        city="Санкт-Петербург",
        capacity=68000,
    )

    # Вывод данных о стадионе
    stadium.display_data()

    # Пример изменения данных с использованием свойств
    stadium.capacity = 95000
    print("\nИзмененная вместимость стадиона:", stadium.capacity)


if __name__ == "__main__":
    main()

# Задание 3
# К уже реализованному классу «Стадион» добавьте
# конструктор, а также необходимые перегруженные методы.


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

    def __str__(self):
        return (
            f"Стадион '{self.name}', открыт {self.opening_date}, расположен в городе {self.city}, {self.country}. "
            f"Вместимость: {self.capacity} зрителей."
        )

    def __eq__(self, other):
        if isinstance(other, Stadium):
            return (
                self.name == other.name
                and self.opening_date == other.opening_date
                and self.country == other.country
                and self.city == other.city
                and self.capacity == other.capacity
            )
        return False

    def __lt__(self, other):
        if isinstance(other, Stadium):
            return self.capacity < other.capacity
        return False

    def __len__(self):
        from datetime import datetime

        opening_year = datetime.strptime(self.opening_date, "%Y-%m-%d").year
        return datetime.today().year - opening_year

    def display_data(self):
        print("Информация о стадионе:")
        print("Название:", self.name)
        print("Дата открытия:", self.opening_date)
        print("Страна:", self.country)
        print("Город:", self.city)
        print("Вместимость:", self.capacity)


def main():
    # Пример создания объекта стадиона с заданными параметрами
    stadium_1 = Stadium(
        name="Газпром Арена",
        opening_date="2017-04-22",
        country="Россия",
        city="Санкт-Петербург",
        capacity=68000,
    )

    stadium_2 = Stadium(
        name="Лужники",
        opening_date="1956-07-31",
        country="Россия",
        city="Москва",
        capacity=81000,
    )

    # Вывод данных о стадионах
    stadium_1.display_data()
    stadium_2.display_data()

    # Пример изменения данных с использованием свойств
    stadium_1.capacity = 95000
    print("\nИзмененная вместимость стадиона:", stadium_1.capacity)

    print(f"\nИнформация о стадионе - {stadium_1.name}:", stadium_1)
    print(f"Информация о стадионе - {stadium_2.name}:", stadium_2)

    print("\nСравнение стадионов:")
    print(f"{stadium_1.name} == {stadium_2.name}:", stadium_1 == stadium_2)

    print("\nСравнение вместимости стадионов:")
    print(f"{stadium_1.name} < {stadium_2.name}:", stadium_1 < stadium_2)

    print(f"\nВозраст стадиона - {stadium_1.name}:", len(stadium_1), "лет")
    print(f"Возраст стадиона - {stadium_2.name}:", len(stadium_2), "лет")


if __name__ == "__main__":
    main()

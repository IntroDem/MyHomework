# Задание №1
# Используя механизм множественного наследования разработайте класс “Автомобиль”.
# Должны быть классы «Колеса», «Двигатель», «Двери» и т.д


class Wheels:
    def __init__(self, wheel_manufacturer, wheels_diameter, wheels_seasonality):
        self.wheel_manufacturer = wheel_manufacturer
        self.wheels_diameter = wheels_diameter
        self.wheels_seasonality = wheels_seasonality

    def __str__(self):
        return (
            f"Марка шин: {self.wheel_manufacturer} \nДиаметр колеса: {self.wheels_diameter} \nСезонность резины: "
            f"{self.wheels_seasonality}"
        )


class Engine:
    def __init__(self, V_engine, engine_type):
        self.V_engine = V_engine
        self.engine_type = engine_type

    def __str__(self):
        return f"Объём двигателя: {self.V_engine} \nТип двигателя: {self.engine_type}"


class Transmission:
    def __init__(self, gears_count, transmission_type):
        self.gears_count = gears_count
        self.transmission_type = transmission_type

    def __str__(self):
        return f"Количество передач: {self.gears_count} \nТип трансмиссии: {self.transmission_type}"


class Doors:
    def __init__(self, door_count):
        self.door_count = door_count

    def __str__(self):
        return f"Количество дверей: {self.door_count}"


class Seats:
    def __init__(self, seat_count):
        self.seat_count = seat_count

    def __str__(self):
        return f"Количество мест: {self.seat_count}"


class Car(Wheels, Engine, Transmission, Doors, Seats):
    def __init__(
        self,
        car_manufacturer,
        car_model,
        year,
        door_count,
        gears_count,
        transmission_type,
        V_engine,
        engine_type,
        wheel_manufacturer,
        wheels_diameter,
        wheels_seasonality,
        seat_count,
    ):
        Wheels.__init__(self, wheel_manufacturer, wheels_diameter, wheels_seasonality)
        Engine.__init__(self, V_engine, engine_type)
        Transmission.__init__(self, gears_count, transmission_type)
        Seats.__init__(self, seat_count)
        Doors.__init__(self, door_count)
        self.car_manufacturer = car_manufacturer
        self.car_model = car_model
        self.year = year

    def __str__(self):
        return (
            f"Автомобиль: {self.car_manufacturer} {self.car_model} ({self.year} год)\n"
            f"{Engine.__str__(self)}\n"
            f"{Transmission.__str__(self)}\n"
            f"{Wheels.__str__(self)}\n"
            f"{Doors.__str__(self)}\n"
            f"{Seats.__str__(self)}"
        )


def main():
    car = Car(
        car_manufacturer="Toyota",
        car_model="Camry",
        year=2022,
        door_count=4,
        seat_count=5,
        gears_count=6,
        transmission_type="Автоматическая",
        V_engine=2.5,
        engine_type="Бензиновый",
        wheel_manufacturer="Michelin",
        wheels_diameter=17,
        wheels_seasonality="Летняя",
    )
    print(car)


if __name__ == "__main__":
    main()

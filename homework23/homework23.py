# Создайте класс «Самолет».Наполните его необходимыми характеристиками и
# методами. Реализуйте упаковку и распаковку объектов класса «Самолет» с
# использованием модуля json.
import json


class Airplane:
    def __init__(
        self, aircraft_number, speed, distance, lifting_capacity, number_of_seats
    ):
        self.aircraft_number = aircraft_number
        self.speed = speed
        self.distance = distance
        self.lifting_capacity = lifting_capacity
        self.number_of_seats = number_of_seats

    def get_distance(self):
        return self.distance

    def get_speed(self):
        return self.speed

    def to_dict(self):
        return {
            "aircraft_number": self.aircraft_number,
            "speed": self.speed,
            "distance": self.distance,
            "lifting_capacity": self.lifting_capacity,
            "number_of_seats": self.number_of_seats,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["aircraft_number"],
            data["speed"],
            data["distance"],
            data["lifting_capacity"],
            data["number_of_seats"],
        )


airplane = Airplane("ABC123", 900, 12000, 50000, 200)

airplane_json = json.dumps(airplane.to_dict(), indent=4)
print("Упакованный JSON:")
print(airplane_json)

with open("airplane.json", "w") as file:
    file.write(airplane_json)

with open("airplane.json", "r") as file:
    loaded_data = json.load(file)

loaded_airplane = Airplane.from_dict(loaded_data)

print("\nРаспакованный объект:")
print(f"Номер самолета: {loaded_airplane.aircraft_number}")
print(f"Скорость: {loaded_airplane.speed}")
print(f"Дальность полета: {loaded_airplane.get_distance()}")
print(f"Грузоподъемность: {loaded_airplane.lifting_capacity}")
print(f"Количество мест: {loaded_airplane.number_of_seats}")

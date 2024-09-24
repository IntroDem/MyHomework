from abc import ABC, abstractmethod


# База данных для хранения данных о пиццах и продажах
class PizzaDatabase:
    def __init__(self):
        self.pizzas_sold = 0
        self.revenue = 0.0
        self.profit = 0.0

    def add_sale(self, price, cost):
        self.pizzas_sold += 1
        self.revenue += price
        self.profit += price - cost

    def get_sales_info(self):
        return {
            "Продано пицц": self.pizzas_sold,
            "Выручка": round(self.revenue, 2),
            "Прибыль": round(self.profit, 2),
        }


# SRP: Класс Pizza отвечает только за представление пиццы.
class Pizza:
    def __init__(self, name, ingredients, base_price, cost):
        self.name = name
        self.ingredients = ingredients
        self.base_price = base_price
        self.cost = cost

    def calculate_price(self, toppings):
        return self.base_price + sum(topping.price for topping in toppings)

    def __str__(self):
        return f"Пицца: {self.name}\nИнгридиенты: {', '.join(self.ingredients)}"


# SRP: Класс Topping отвечает только за представление топпинга.
class Topping:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name


# OCP: Класс Payment является абстрактным и открыт для расширения другими типами оплаты.
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# OCP: Классы CashPayment и CardPayment расширяют класс Payment и добавляют новый функционал.
class CashPayment(Payment):
    def pay(self, amount):
        print(f"Оплата {amount} наличными.")


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Оплата {amount} картой.")


# SRP: Класс Order отвечает только за создание заказа.
class Order:
    def __init__(self, pizza, toppings):
        self.pizza = pizza
        self.toppings = toppings

    def calculate_total(self):
        return self.pizza.calculate_price(self.toppings)

    def display_order(self):
        print(self.pizza)
        if self.toppings:
            print("Топпинги: ", ", ".join([str(topping) for topping in self.toppings]))
        else:
            print("Без дополнительных топпингов.")
        print(f"Общая стоимость: {self.calculate_total()}")

    def save_order(self):
        with open("orders.txt", "a") as f:
            f.write(f"{str(self.pizza)}\n")
            if self.toppings:
                f.write(
                    f"Топпинги: {', '.join([str(topping) for topping in self.toppings])}\n"
                )
            f.write(f"Общая стоимость: {self.calculate_total()}\n\n")


# DIP: Класс PizzaShop зависит от абстракций (Order и Payment), а не от конкретных реализаций.
class PizzaShop:
    def __init__(self, database):
        self.database = database

    def process_order(self, order, payment_method):
        order.display_order()
        total_price = order.calculate_total()
        payment_method.pay(total_price)
        self.database.add_sale(total_price, order.pizza.cost)
        order.save_order()

    def sales_report(self):
        sales_info = self.database.get_sales_info()
        print(f"Продано пицц: {sales_info['Продано пицц']}")
        print(f"Выручка: {sales_info['Выручка']}")
        print(f"Прибыль: {sales_info['Прибыль']}")


# SRP: Класс UserInterface отвечает только за взаимодействие с пользователем.
class UserInterface:
    @staticmethod
    def select_pizza():
        print("Выберите пиццу:")
        print("1. Маргарита")
        print("2. Пепперони")
        print("3. Пицца BBQ")
        print("4. Гавайская")
        print("5. Вегетарианская ")
        choice = int(input("Введите ваш выбор: "))
        pizzas = [
            Pizza("Маргарита", ["томаты", "моцарелла", "базилик"], 5.0, 2.5),
            Pizza("Пепперони", ["томаты", "моцарелла", "пепперони"], 6.0, 3.0),
            Pizza("Пицца BBQ", ["соус BBQ", "курица", "лук"], 7.0, 3.5),
            Pizza("Гавайская", ["томаты", "моцарелла", "ветчина", "ананас"], 6.5, 3.2),
            Pizza(
                "Вегетарианская", ["томаты", "моцарелла", "перец", "оливки"], 5.5, 2.8
            ),
        ]
        return pizzas[choice - 1]

    @staticmethod
    def add_toppings():
        toppings_list = [
            Topping("Сладкий лук", 0.5),
            Topping("Халапеньо", 0.7),
            Topping("Перец чили", 0.6),
            Topping("Корнишоны", 0.4),
            Topping("Оливки", 0.8),
            Topping("Ветчина", 1.5),
        ]
        selected_toppings = []
        print("Добавьте начинку (введите 0, чтобы пропустить):")
        for i, topping in enumerate(toppings_list, 1):
            print(f"{i}. {topping.name} (+${topping.price})")
        while True:
            choice = int(input("Введите ваш выбор: "))
            if choice == 0:
                break
            selected_toppings.append(toppings_list[choice - 1])
        return selected_toppings

    @staticmethod
    def select_payment_method():
        print("Выберите метод оплаты:")
        print("1. Наличными")
        print("2. Картой")
        choice = int(input("Введите ваш выбор: "))
        if choice == 1:
            return CashPayment()
        else:
            return CardPayment()


def main():
    database = PizzaDatabase()
    pizza_shop = PizzaShop(database)
    ui = UserInterface()

    while True:
        pizza = ui.select_pizza()
        toppings = ui.add_toppings()
        order = Order(pizza, toppings)
        payment_method = ui.select_payment_method()
        pizza_shop.process_order(order, payment_method)

        print("\nОтчёт о продаже:")
        pizza_shop.sales_report()

        cont = input("\nХотите заказать еще пиццу? (да/нет): ")
        if cont.lower() != "да":
            break


if __name__ == "__main__":
    main()

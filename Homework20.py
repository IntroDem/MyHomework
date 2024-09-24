class Money:
    """A class to represent money with a specific currency."""

    CENTS_CURRENCIES = [
        "USD",
        "EUR",
        "GBP",
        "AUD",
        "CAD",
        "NZD",
        "SGD",
        "ZAR",
        "CHF",
        "JPY",
    ]
    KOPEСKS_CURRENCIES = [
        "RUB",
        "BYN",
        "UAH",
        "KZT",
        "UZS",
        "MDL",
        "TJS",
        "AZN",
        "GEL",
        "AMD",
    ]

    def __init__(self, units=0, cents=0, currency="RUB"):
        self.units = units
        self.cents = cents
        self.currency = currency
        self.__normalize()

    def set_units(self, units):
        self.units = units
        self.__normalize()

    def set_cents(self, cents):
        self.cents = cents
        self.__normalize()

    def set_currency(self, currency):
        self.currency = currency

    def __normalize(self):
        # Если дробная часть >= 100, преобразовать ее в целые и дробные части
        if self.cents >= 100:
            self.units += self.cents // 100
            self.cents = self.cents % 100

    def __str__(self):
        if self.currency in self.CENTS_CURRENCIES:
            fractional_name = "центов"
        elif self.currency in self.KOPEСKS_CURRENCIES:
            fractional_name = "копеек"
        else:
            fractional_name = "единиц"

        return f"{self.units} {self.currency} и {self.cents:02d} {fractional_name}"


# Примеры использования:
money1 = Money(10, 99, "USD")
print(money1)

money2 = Money()
money2.set_units(20)
money2.set_cents(150)
money2.set_currency("EUR")
print(money2)

money3 = Money(100, 120)
print(money3)

money4 = Money(2, 344, "KZT")
print(money4)

money5 = Money(11, 23, "AUD")
print(money5)

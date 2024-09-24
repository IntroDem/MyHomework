# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.


class Book:
    def __init__(self, title, publisher, author, year, genre, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.author = author
        self.genre = genre
        self.price = price

    def display_data(self):
        print("\nИнформация о книге:")
        print("Название:", self.get_title())
        print("Автор:", self.get_author())
        print("Год выпуска:", self.get_year())
        print("Издатель:", self.get_publisher())
        print("Жанр:", self.get_genre())
        print("Цена:", self.get_price())

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_price(self):
        return self.price


def main():

    book = Book(
        title="Пропаганда",
        author="Эдвард Бернейс",
        year=1928,
        publisher="Hippo",
        genre="Журналистика",
        price=500,
    )

    # Вывод данных о книге
    book.display_data()


if __name__ == "__main__":
    main()

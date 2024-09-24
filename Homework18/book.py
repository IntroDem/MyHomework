# Задание 2
# К уже реализованному классу «Книга» добавьте конструктор, а также необходимые перегруженные методы.


class Book:
    def __init__(self, title, publisher, author, year, genre, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.author = author
        self.genre = genre
        self.price = price

    def __str__(self):
        return (
            f"Книга '{self.title}' написанная автором - {self.author}, опубликована {self.publisher} в {self.year} "
            f"году, "
            f"в жанре: {self.genre}, стоит: {self.price} р."
        )

    def __eq__(self, other):
        if isinstance(other, Book):
            return (
                self.title == other.title
                and self.author == other.author
                and self.year == other.year
                and self.publisher == other.publisher
                and self.genre == other.genre
                and self.price == other.price
            )
        return False

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.price < other.price
        return False

    def __len__(self):
        from datetime import date

        return date.today().year - self.year

    def display_data(self):
        print(f"\nИнформация о книге - {self.title}:")
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

    book_1 = Book(
        title="Пропаганда",
        author="Эдвард Бернейс",
        year=1928,
        publisher="Hippo",
        genre="Журналистика",
        price=500,
    )

    book_2 = Book(
        title="1984",
        author="Джордж Оруэлл",
        year=1949,
        publisher="Сигнет Классик",
        genre="Фантастика",
        price=600,
    )

    # Вывод данных о книге
    book_1.display_data()
    book_2.display_data()

    print(f"\nИнформация о книге - {book_1.title}:", book_1)
    print(f"Информация о книге - {book_2.title}:", book_2)

    print("\nСравнение книг:")
    print(f"{book_1.title} == {book_2.title}:", book_1 == book_2)

    print("\nСравнение стоимости книг:")
    print(f"{book_1.title} < {book_2.title}:", book_1 < book_2)

    print(f"\nВозраст книги - {book_1.title}:", len(book_1), "лет")
    print(f"Возраст книги - {book_2.title}:", len(book_2), "лет")


if __name__ == "__main__":
    main()

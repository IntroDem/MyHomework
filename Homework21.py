# Задание №1
# Реализуйте класс стека для работы со строками (стек строк). Стек должен иметь
# фиксированный размер. Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки из стека. При старте
# приложения нужно отобразить меню с помощью, которого пользователь может
# выбрать необходимую операцию.


class Stack_str:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, string):
        if len(self.stack) < self.size:
            self.stack.append(string)
            print(f"Строка '{string}' запушилась в стэк")
        else:
            print("Стэк полный")

    def pop(self):
        if len(self.stack) > 0:
            pop_str = self.stack.pop()
            print(f"Строка '{pop_str}' удалилась из стэка")
        else:
            print("Стэк пустой")

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.size

    def clear(self):
        self.stack.clear()
        print("Стэк очищен")

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("Стэк пустой")


def menu():
    size = int(input("Введите размер стэка: "))
    stack = Stack_str(size)

    while True:
        print("\nМеню")
        print("1. Запушить строку в стэк")
        print("2. Удалить строку из стэка")
        print("3. Подсчет количества строк в стэке")
        print("4. Проверка пустой ли стэк")
        print("5. Проверка полный ли стэк")
        print("6. Очистить стэк")
        print("7. Получение значения без выталкивания верхней строки из стека")
        print("8. Выход")

        choice = input("Выберете пункт меню: ")

        if choice == "1":
            string = input("Введите строку для пуша: ")
            stack.push(string)

        elif choice == "2":
            stack.pop()

        elif choice == "3":
            print(f"Строк в стэке: '{stack.count()}'")

        elif choice == "4":
            if stack.is_empty():
                print("Стэк пустой")
            else:
                print("Стэк не пустой")

        elif choice == "5":
            if stack.is_full():
                print("Стэк полный")
            else:
                print("Стэк не полный")

        elif choice == "6":
            stack.clear()

        elif choice == "7":
            top_string = stack.peek()
            if top_string is not None:
                print(f"Верхняя строка в стэке - '{top_string}'")

        elif choice == "8":
            print("Выходим из программы")
            break

        else:
            print("Неверное значение, попробуйте ещё раз")


if __name__ == "__main__":
    menu()

class Stack_str:
    def __init__(self):
        self.stack = []

    def push(self, string):
        self.stack.append(string)
        print(f"Строка '{string}' запушилась в стэк")

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

    def clear(self):
        self.stack.clear()
        print("Стэк очищен")

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("Стэк пустой")
            return None


def menu():
    stack = Stack_str()

    while True:
        print("\nМеню")
        print("1. Запушить строку в стэк")
        print("2. Удалить строку из стэка")
        print("3. Подсчет количества строк в стэке")
        print("4. Проверка пустой ли стэк")
        print("5. Очистить стэк")
        print("6. Получение значения без выталкивания верхней строки из стека")
        print("7. Выход")

        choice = input("Выберете пункт меню: ")

        if choice == "1":
            string = input("Введите строку для пуша: ")
            stack.push(string)

        elif choice == "2":
            stack.pop()

        elif choice == "3":
            print(f"Строк в стэке: {stack.count()}")

        elif choice == "4":
            if stack.is_empty():
                print("Стэк пустой")
            else:
                print("Стэк не пустой")

        elif choice == "5":
            stack.clear()

        elif choice == "6":
            top_string = stack.peek()
            if top_string is not None:
                print(f"Верхняя строка в стэке: '{top_string}'")

        elif choice == "7":
            print("Выходим из программы")
            break

        else:
            print("Неверное значение, попробуйте ещё раз")


if __name__ == "__main__":
    menu()

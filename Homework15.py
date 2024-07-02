def main():
    # Создаем список для хранения оценок
    grades = []

    # Ввод оценок от пользователя
    for i in range(10):
        grade = int(input(f"Введите оценку {i + 1} (от 1 до 12): "))
        while grade < 1 or grade > 12:
            grade = int(input("Оценка должна быть от 1 до 12. Попробуйте снова: "))
        grades.append(grade)

    # Основной цикл программы
    while True:
        print("\nМеню:")
        print("1. Вывод оценок")
        print("2. Пересдача экзамена")
        print("3. Проверка стипендии")
        print("4. Вывод отсортированного списка оценок (по возрастанию)")
        print("5. Вывод отсортированного списка оценок (по убыванию)")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ")

        if choice == "1":
            print("Оценки студента:", grades)
        elif choice == "2":
            index = (
                int(input("Введите номер элемента списка для изменения (от 1 до 10): "))
                - 1
            )
            if 0 <= index < 10:
                new_grade = int(
                    input(
                        f"Введите новую оценку для элемента {index + 1} (от 1 до 12): "
                    )
                )
                while new_grade < 1 or new_grade > 12:
                    new_grade = int(
                        input("Оценка должна быть от 1 до 12. Попробуйте снова: ")
                    )
                grades[index] = new_grade
                print("Оценка успешно изменена.")
            else:
                print("Неверный номер элемента списка.")
        elif choice == "3":
            average_grade = sum(grades) / len(grades)
            if average_grade >= 10.7:
                print(f"Средний балл студента: {average_grade:.2f}. Стипендия выходит.")
            else:
                print(
                    f"Средний балл студента: {average_grade:.2f}. Стипендия не выходит."
                )
        elif choice == "4":
            sorted_grades = sorted(grades)
            print("Отсортированный список оценок (по возрастанию):", sorted_grades)
        elif choice == "5":
            sorted_grades = sorted(grades, reverse=True)
            print("Отсортированный список оценок (по убыванию):", sorted_grades)
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


main()

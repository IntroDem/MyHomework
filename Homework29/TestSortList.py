from SortList import SortList

# Положительные тесты


def test_sort_integers():
    assert SortList([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]


def test_sort_with_duplicates():
    assert SortList([3, 3, 1, 4, 1]) == [1, 1, 3, 3, 4]


def test_sort_strings():
    assert SortList(["яблоко", "банан", "груша"]) == ["банан", "груша", "яблоко"]


def test_sort_empty():
    assert SortList([]) == []


# Отрицательные тесты


def test_sort_incomparable():
    try:
        SortList([3, "банан", 4])
    except TypeError as e:
        assert (
            str(e) == "Список содержит элементы, которые нельзя сравнивать между собой"
        )


def test_sort_not_a_list():
    try:
        SortList("не список")
    except TypeError as e:
        assert str(e) == "Входные данные должны быть списком"


def test_sort_number():
    try:
        SortList(12345)
    except TypeError as e:
        assert str(e) == "Входные данные должны быть списком"


class CustomObject:
    pass


def test_sort_custom_objects():
    try:
        SortList([CustomObject(), 1])
    except TypeError as e:
        assert (
            str(e) == "Список содержит элементы, которые нельзя сравнивать между собой"
        )

def SortList(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Входные данные должны быть списком")

    try:
        return sorted(input_list)
    except TypeError as e:
        raise TypeError(
            "Список содержит элементы, которые нельзя сравнивать между собой"
        ) from e

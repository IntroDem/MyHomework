# Написать программу, принимающую на вход строку из 5 случайных элементов.
# Программа должна передать элементы строки в односвязный список, после чего
# развернуть список (аналогично list.reverse()).


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def crEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def LLprint(self):
        current_node = self.head
        while current_node:
            print(current_node.data, " ", end="")
            current_node = current_node.next
        print()


def main():
    llist = LinkedList()
    elements = input("Введите строку из 5 случайных элементов: ").split()

    for element in elements:
        llist.crEnd(element)

    print("Список до разворота:")
    llist.LLprint()

    llist.reverse()

    print("Список после разворота:")
    llist.LLprint()


if __name__ == "__main__":
    main()

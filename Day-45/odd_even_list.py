class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def odd_even_list(self):
        if self.head is None or self.head.next is None:
            return

        odd = self.head
        even = self.head.next
        even_head = even

        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head


linked_list = LinkedList()

n = int(input("Enter number of nodes: "))

for i in range(n):
    value = int(input("Enter node value: "))
    linked_list.insert(value)

print("Original linked list:")
linked_list.display()

linked_list.odd_even_list()

print("Odd positions followed by even positions:")
linked_list.display()

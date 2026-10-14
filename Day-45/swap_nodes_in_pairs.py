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

    def swap_nodes_in_pairs(self):
        current = self.head

        while current is not None and current.next is not None:
            temp1 = current.data
            current.data = current.next.data
            current.next.data = temp1

            current = current.next.next


linked_list = LinkedList()

n = int(input("Enter number of nodes: "))

for i in range(n):
    value = int(input("Enter node value: "))
    linked_list.insert(value)

print("Original linked list:")
linked_list.display()

linked_list.swap_nodes_in_pairs()

print("Linked list after swapping pairs:")
linked_list.display()

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

    def remove_kth_node_from_end(self, k):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        if k <= 0 or k > count:
            print("Invalid K value")
            return

        position = count - k + 1

        if position == 1:
            self.head = self.head.next
            return

        current = self.head

        for i in range(1, position - 1):
            current = current.next

        current.next = current.next.next


linked_list = LinkedList()

n = int(input("Enter number of nodes: "))

for i in range(n):
    value = int(input("Enter node value: "))
    linked_list.insert(value)

k = int(input("Enter K (position from the end): "))

print("Original linked list:")
linked_list.display()

linked_list.remove_kth_node_from_end(k)

print("Linked list after removal:")
linked_list.display()

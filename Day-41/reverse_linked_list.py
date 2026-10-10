
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    prev = None
    curr = head

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def display(head):
    temp = head

    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next

    print("None")


n = int(input("Enter number of nodes: "))
head = None
tail = None

for i in range(n):
    data = int(input("Enter node value: "))
    new_node = Node(data)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

print("Original linked list:")
display(head)

head = reverse_linked_list(head)

print("Reversed linked list:")
display(head)

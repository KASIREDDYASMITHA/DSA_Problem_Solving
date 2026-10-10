
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_first_node(head):
    if head is None:
        return None

    head = head.next
    return head


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

head = delete_first_node(head)

print("Linked list after deleting the first node:")
display(head)

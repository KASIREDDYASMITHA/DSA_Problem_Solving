class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def display(head):
    if head is None:
        print("Linked List is empty")
        return

    curr = head

    while curr is not None:
        print(curr.data, end=" -> ")
        curr = curr.next

    print("None")


def count_nodes(head):
    if head is None:
        return 0

    count = 0
    curr = head

    while curr is not None:
        count = count + 1
        curr = curr.next

    return count


def search(head, key):
    if head is None:
        return False

    curr = head

    while curr is not None:
        if curr.data == key:
            return True

        curr = curr.next

    return False


def insert_at_beginning(head, value):
    temp = Node(value)

    if head is None:
        return temp

    temp.next = head
    head = temp

    return head


def insert_at_end(head, value):
    temp = Node(value)

    if head is None:
        return temp

    curr = head

    while curr.next is not None:
        curr = curr.next

    curr.next = temp

    return head


def delete_at_beginning(head):
    if head is None:
        return None

    head = head.next

    return head


def delete_at_end(head):
    if head is None:
        return None

    if head.next is None:
        return None

    curr = head

    while curr.next.next is not None:
        curr = curr.next

    curr.next = None

    return head


# Creating the linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Initial Linked List:")
display(head)

# Count nodes
print("\nNumber of Nodes:")
print(count_nodes(head))

# Search for an element
key = int(input("\nEnter element to search: "))

if search(head, key):
    print("Element Found")
else:
    print("Element Not Found")

# Insert at beginning
value = int(input("\nEnter value to insert at beginning: "))
head = insert_at_beginning(head, value)

print("After Insertion at Beginning:")
display(head)

# Insert at ending
value = int(input("\nEnter value to insert at ending: "))
head = insert_at_end(head, value)

print("After Insertion at Ending:")
display(head)

# Delete at beginning
head = delete_at_beginning(head)

print("\nAfter Deletion at Beginning:")
display(head)

# Delete at ending
head = delete_at_end(head)

print("After Deletion at Ending:")
display(head)

# Final count
print("\nFinal Number of Nodes:")
print(count_nodes(head))
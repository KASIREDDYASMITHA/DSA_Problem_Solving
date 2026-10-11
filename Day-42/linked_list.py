# DSA Day 42 - Linked List (Part 4)
# Topics:
# 1. Find the middle node using slow and fast pointers
# 2. Detect a cycle using Floyd's Cycle Detection Algorithm


# Node class represents one node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a linked list from the given elements
def create_linked_list(values):
    head = None
    tail = None

    for value in values:
        new_node = Node(value)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return head


# Program 1: Find the middle node
# Slow moves one step; fast moves two steps
def find_middle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    if slow is None:
        return None

    return slow.data


# Program 2: Detect a cycle using Floyd's algorithm
def detect_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        # If both pointers meet, a cycle exists
        if slow == fast:
            return True

    # Fast reached the end; no cycle exists
    return False


# Create a cycle by connecting the last node
# to the node at the given zero-based index
def create_cycle(head, position):
    if head is None or position < 0:
        return

    current = head
    target = None
    last = None
    index = 0

    while current is not None:
        if index == position:
            target = current

        last = current
        current = current.next
        index += 1

    # Create a cycle only if the index is valid
    if target is not None:
        last.next = target


# Main program: take input at runtime
n = int(input("Enter the number of nodes: "))

values = []

if n > 0:
    values = list(map(
        int,
        input("Enter the node values separated by spaces: ").split()
    ))

    if len(values) != n:
        print("Error: Please enter exactly", n, "values.")
        exit()

head = create_linked_list(values)


# Find the middle node
middle = find_middle(head)

if middle is None:
    print("The linked list is empty.")
else:
    print("Middle node:", middle)


# Choose whether to create a cycle for testing
print("\nCycle creation options:")
print("-1 : Do not create a cycle")
print("0  : Connect the last node to the first node")
print("1  : Connect the last node to the second node")
print("2  : Connect the last node to the third node")
print("And so on...")

position = int(input("Enter the cycle position: "))

if position >= n or position < -1:
    print("Invalid cycle position.")
elif position >= 0:
    create_cycle(head, position)

    if detect_cycle(head):
        print("Cycle detected: True")
    else:
        print("Cycle detected: False")
else:
    if detect_cycle(head):
        print("Cycle detected: True")
    else:
        print("Cycle detected: False")
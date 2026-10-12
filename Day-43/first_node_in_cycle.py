
# DSA Day 43 - First Node in a Cycle

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


values = list(map(int, input("Enter linked list elements: ").split()))
cycle_position = int(input("Enter cycle position (0-based, -1 for no cycle): "))

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

# Create a cycle if a valid position is given
if head is not None and 0 <= cycle_position < len(values):
    temp = head

    for i in range(cycle_position):
        temp = temp.next

    tail.next = temp

# Detect the cycle
slow = head
fast = head
cycle_found = False

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        cycle_found = True
        break

# Find the first node of the cycle
if cycle_found:
    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    print("First node in cycle:", slow.data)
else:
    print("No cycle found")

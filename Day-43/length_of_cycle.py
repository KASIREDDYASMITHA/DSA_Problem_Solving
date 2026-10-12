
# DSA Day 43 - Length of Cycle in a Linked List

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
cycle_length = 0

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        # Count the nodes in the cycle
        cycle_length = 1
        temp = slow.next

        while temp != slow:
            cycle_length += 1
            temp = temp.next

        break

print("Length of cycle:", cycle_length)


# Day 44 - Merge Two Sorted Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Input for the first sorted list
values1 = input("Enter sorted List 1 elements: ").strip()
values1 = list(map(int, values1.split())) if values1 else []

# Input for the second sorted list
values2 = input("Enter sorted List 2 elements: ").strip()
values2 = list(map(int, values2.split())) if values2 else []

# Create the first linked list
head1 = None
tail1 = None

for value in values1:
    new_node = Node(value)

    if head1 is None:
        head1 = new_node
        tail1 = new_node
    else:
        tail1.next = new_node
        tail1 = new_node

# Create the second linked list
head2 = None
tail2 = None

for value in values2:
    new_node = Node(value)

    if head2 is None:
        head2 = new_node
        tail2 = new_node
    else:
        tail2.next = new_node
        tail2 = new_node

# Dummy node simplifies the merge
dummy = Node(0)
tail = dummy

# Compare the current nodes and select the smaller one
while head1 is not None and head2 is not None:
    if head1.data <= head2.data:
        tail.next = head1
        head1 = head1.next
    else:
        tail.next = head2
        head2 = head2.next

    tail = tail.next

# Attach all remaining nodes
if head1 is not None:
    tail.next = head1
else:
    tail.next = head2

# Display the merged sorted list
result = dummy.next

print("Merged sorted linked list:")

if result is None:
    print("Empty list")
else:
    while result is not None:
        print(result.data, end="")
        if result.next is not None:
            print(" -> ", end="")
        result = result.next

    print()

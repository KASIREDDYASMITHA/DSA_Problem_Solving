
# Day 44 - Merge Two Lists Alternately

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Input for the first linked list
values1 = input("Enter elements of List 1 separated by spaces: ").strip()
values1 = list(map(int, values1.split())) if values1 else []

# Input for the second linked list
values2 = input("Enter elements of List 2 separated by spaces: ").strip()
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

# Merge the lists alternately
dummy = Node(0)
tail = dummy

while head1 is not None and head2 is not None:
    # Save next nodes before changing links
    next1 = head1.next
    next2 = head2.next

    # Attach one node from List 1
    tail.next = head1
    head1.next = head2

    # Move tail to the newly attached List 2 node
    tail = head2

    # Advance both input pointers
    head1 = next1
    head2 = next2

# Attach the remaining nodes, if any
if head1 is not None:
    tail.next = head1
else:
    tail.next = head2

# Display the merged linked list
result = dummy.next

print("Merged linked list alternately:")

if result is None:
    print("Empty list")
else:
    while result is not None:
        print(result.data, end="")
        if result.next is not None:
            print(" -> ", end="")
        result = result.next

    print()

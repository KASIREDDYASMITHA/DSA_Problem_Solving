
# DSA Day 43 - Palindrome Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


values = list(map(int, input("Enter linked list elements: ").split()))

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

# Find the middle of the linked list
slow = head
fast = head

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

# Skip the middle node for an odd-length list
if fast is not None:
    slow = slow.next

# Reverse the second half
previous = None
current = slow

while current is not None:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node

second_half = previous
first_half = head
is_palindrome = True

# Compare both halves
while second_half is not None:
    if first_half.data != second_half.data:
        is_palindrome = False
        break

    first_half = first_half.next
    second_half = second_half.next

# Restore the second half
previous = None
current = previous

# Reversing the second half again restores its original order
current = slow
while current is not None:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node

if is_palindrome:
    print("The linked list is a palindrome")
else:
    print("The linked list is not a palindrome")

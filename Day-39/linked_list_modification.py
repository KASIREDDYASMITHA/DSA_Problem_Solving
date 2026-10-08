class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

print("Original Linked List:")

temp = head

while temp != None:
    print(temp.data)
    temp = temp.next


node1.next = node3
node3.next = node5
node5.next = None

print("\nLinked List After Modifications:")

temp = head

while temp != None:
    print(temp.data)
    temp = temp.next


print("\nDirect Access After Modifications:")
print("head.data:", head.data)
print("head.next.data:", head.next.data)
print("head.next.next.data:", head.next.next.data)
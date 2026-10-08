class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

print("Head:", head.data)
print("Second Node:", head.next.data)
print("Third Node:", head.next.next.data)
print("Fourth Node:", head.next.next.next.data)
print("Last Node Next:", head.next.next.next.next)
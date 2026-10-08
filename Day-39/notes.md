# DSA Day 39 - Linked List-1

## 1. Introduction to Linked List

A linked list is a linear data structure in which elements are stored in the form of nodes.

Unlike arrays, the nodes of a linked list do not need to be stored in continuous memory locations.

Each node contains:

1. Data
2. Reference to the next node

Example:

```text
[10] -> [20] -> [30] -> [40] -> None
```

Here:

* `10`, `20`, `30`, and `40` are data values.
* Each node is connected to the next node.
* `None` represents the end of the linked list.

---

## 2. Array

Before learning linked lists, we need to understand arrays.

Important characteristics of arrays:

* All elements are of the same data type.
* Elements are stored in continuous memory locations.
* Elements can be accessed using an index.

Example:

```text
[10, 20, 30, 40]
```

---

## 3. Limitations of Arrays

Arrays have some limitations when elements need to be inserted or deleted.

### Insertion at the Beginning

Suppose we have:

```text
[10, 20, 30, 40]
```

If we insert `5` at the beginning:

```text
[5, 10, 20, 30, 40]
```

The existing elements need to be shifted.

Therefore, insertion at the beginning requires shifting elements.

Time Complexity:

```text
O(n)
```

---

## 4. Deletion From the Beginning

Suppose we have:

```text
[10, 20, 30, 40]
```

If we delete `10`:

```text
[20, 30, 40]
```

The remaining elements need to be shifted.

Time Complexity:

```text
O(n)
```

---

## 5. Insertion in the Middle

Suppose we want to insert `25` between `20` and `30`.

Before:

```text
[10, 20, 30, 40]
```

After:

```text
[10, 20, 25, 30, 40]
```

The elements after the insertion position need to be shifted.

Time Complexity:

```text
O(n)
```

---

## 6. Continuous Memory

Arrays store elements in continuous memory locations.

For example:

```text
[10] [20] [30] [40]
```

The elements are stored next to each other in memory.

A linked list does not require continuous memory locations.

The nodes can be stored at different memory locations and connected using references.

---

# 7. What is a Node?

A node is the basic building block of a linked list.

A node contains two main parts:

```text
+---------+---------+
|  data   |  next   |
+---------+---------+
```

### Data

The `data` part stores the actual value.

Example:

```text
10
```

### Next

The `next` part stores the reference to the next node.

Example:

```text
node1.next = node2
```

The last node's `next` contains:

```text
None
```

This represents the end of the linked list.

---

# 8. Node Structure in Python

We can create a node using a class.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Explanation:

* `Node` is the class.
* `data` stores the value of the node.
* `next` stores the reference to the next node.
* Initially, `next` is `None`.

---

# 9. Creating Nodes

We can create nodes using the `Node` class.

```python
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
```

Now four nodes have been created.

Initially, every node has:

```text
next = None
```

---

# 10. Connecting Nodes

We can connect nodes using the `next` reference.

```python
node1.next = node2
node2.next = node3
node3.next = node4
```

The linked list becomes:

```text
[10] -> [20] -> [30] -> [40] -> None
```

The connections are:

```text
node1 -> node2
node2 -> node3
node3 -> node4
node4 -> None
```

---

# 11. Head

The first node of a linked list is called the `head`.

Example:

```python
head = node1
```

The structure becomes:

```text
head
 |
 v
[10] -> [20] -> [30] -> [40] -> None
```

The `head` is used as the starting point for accessing or traversing the linked list.

---

# 12. Accessing Node Data

Suppose the linked list is:

```text
head -> 10 -> 20 -> 30 -> 40 -> None
```

We can access the first node's data using:

```python
print(head.data)
```

Output:

```text
10
```

---

## Accessing the Second Node

```python
print(head.next.data)
```

Output:

```text
20
```

---

## Accessing the Third Node

```python
print(head.next.next.data)
```

Output:

```text
30
```

---

## Accessing the Fourth Node

```python
print(head.next.next.next.data)
```

Output:

```text
40
```

The `next` reference is used to move from one node to the next node.

---

# 13. Understanding `head.next`

If:

```text
head -> 10 -> 20 -> 30 -> 40 -> None
```

Then:

```python
head
```

refers to the first node.

```python
head.data
```

gives:

```text
10
```

```python
head.next
```

refers to the second node.

```python
head.next.data
```

gives:

```text
20
```

Similarly:

```python
head.next.next.data
```

gives:

```text
30
```

---

# 14. Traversing a Linked List

Traversal means visiting every node of the linked list one by one.

Example:

```text
10 -> 20 -> 30 -> 40 -> None
```

We can traverse the list using a temporary variable.

```python
temp = head

while temp != None:
    print(temp.data)
    temp = temp.next
```

Output:

```text
10
20
30
40
```

---

# 15. Understanding `temp`

Initially:

```python
temp = head
```

So `temp` points to the first node.

Example:

```text
temp
 |
 v
10 -> 20 -> 30 -> 40 -> None
```

After:

```python
temp = temp.next
```

`temp` moves to the next node.

```text
     temp
      |
      v
10 -> 20 -> 30 -> 40 -> None
```

Again:

```python
temp = temp.next
```

Now:

```text
          temp
           |
           v
10 -> 20 -> 30 -> 40 -> None
```

This continues until:

```python
temp == None
```

Then the traversal stops.

---

# 16. Basic Traversal Program

```python
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

temp = head

while temp != None:
    print(temp.data)
    temp = temp.next
```

Output:

```text
10
20
30
40
```

---

# 17. Modifying Links

One important concept in a linked list is that we can change the links between nodes.

Consider:

```text
10 -> 20 -> 30 -> 40 -> 50 -> None
```

Suppose the nodes are:

```python
node1 = 10
node2 = 20
node3 = 30
node4 = 40
node5 = 50
```

If we change the links:

```python
node1.next = node3
node3.next = node5
node5.next = None
```

The reachable linked list becomes:

```text
10 -> 30 -> 50 -> None
```

The nodes `20` and `40` are no longer reachable from `head`.

---

# 18. Example of Modifying Links

```python
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

print("Linked List After Modification:")

temp = head

while temp != None:
    print(temp.data)
    temp = temp.next
```

Output:

```text
Original Linked List:
10
20
30
40
50

Linked List After Modification:
10
30
50
```

---

# 19. Important Linked List Diagram

```text
head
 |
 v
+----+------+     +----+------+     +----+------+     +----+------+
| 10 | next | --> | 20 | next | --> | 30 | next | --> | 40 | None |
+----+------+     +----+------+     +----+------+     +----+------+
```

Each node contains:

```text
data
next
```

The `next` connects one node to another.

---

# 20. Array vs Linked List

| Array                                              | Linked List                                   |
| -------------------------------------------------- | --------------------------------------------- |
| Elements are stored in continuous memory locations | Nodes do not need continuous memory locations |
| Elements are accessed using indexes                | Nodes are accessed by following links         |
| Insertion can require shifting                     | Links can be changed                          |
| Deletion can require shifting                      | Links can be changed                          |
| Uses indexes                                       | Uses references/links                         |
| First element is accessed using index              | First node is accessed using head             |

---

# 21. Important Terms

### Node

The basic unit of a linked list.

### Data

The value stored inside a node.

### Next

The reference to the next node.

### Head

The first node of the linked list.

### None

Represents the end of the linked list.

### Traversal

Visiting nodes one by one.

### Link

The connection between one node and another node.

---

# 22. Important Python Statements

### Create a node

```python
node1 = Node(10)
```

### Connect two nodes

```python
node1.next = node2
```

### Set the head

```python
head = node1
```

### Access data

```python
head.data
```

### Move to next node

```python
temp = temp.next
```

### Check end of list

```python
temp != None
```

---

# 23. Time Complexity

### Traversal

Every node may need to be visited.

```text
O(n)
```

### Accessing a Node

Linked lists do not provide direct index-based access like arrays.

To reach a node, we generally follow the links from the head.

```text
O(n)
```

### Insertion/Deletion

After reaching the required position or having the required node reference, changing links can be done without shifting all the remaining elements.

---

# 24. Key Points to Remember

1. A linked list consists of nodes.
2. A node contains data and a next reference.
3. The first node is called the head.
4. The last node points to `None`.
5. Nodes do not need to be stored in continuous memory locations.
6. The `next` reference connects nodes.
7. Traversal starts from the head.
8. `temp = temp.next` moves to the next node.
9. `head.data` accesses the first node's data.
10. `head.next.data` accesses the second node's data.
11. `head.next.next.data` accesses the third node's data.
12. Changing `next` references can change the structure of the linked list.
13. Nodes that are no longer reachable from `head` are not included when traversing the list.

---

# 25. Final Example

```python
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

print("First Node:", head.data)
print("Second Node:", head.next.data)
print("Third Node:", head.next.next.data)
print("Fourth Node:", head.next.next.next.data)

print("\nLinked List:")

temp = head

while temp != None:
    print(temp.data)
    temp = temp.next
```

Output:

```text
First Node: 10
Second Node: 20
Third Node: 30
Fourth Node: 40

Linked List:
10
20
30
40
```

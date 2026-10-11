# DSA Day 42 – Linked List 

## 1. Finding the Middle Node of a Linked List

### Problem Statement
Find the middle node of a linked list without calculating the length of the linked list.

### Approach: Two-Pointer Technique

We use two pointers:
- **Slow pointer:** Moves one node at a time.
- **Fast pointer:** Moves two nodes at a time.

### Algorithm
1. Initialize both `slow` and `fast` to the head node.
2. Move `slow` one step using `slow = slow.next`.
3. Move `fast` two steps using `fast = fast.next.next`.
4. Continue while `fast` and `fast.next` are not `None`.
5. When the loop ends, `slow` points to the middle node.

### Example 1: Odd Number of Nodes

Linked list:

`10 -> 20 -> 30 -> 40 -> 50 -> None`

The middle node is `30`.

### Example 2: Even Number of Nodes

Linked list:

`10 -> 20 -> 30 -> 40 -> None`

The algorithm returns `30`, the second of the two middle nodes.

### Python Code

```python
slow = head
fast = head

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

# slow points to the middle node
```

### Complexity
- Time Complexity: O(n)
- Auxiliary Space Complexity: O(1)

Here, `n` is the number of nodes. We traverse the list using two pointers without storing its length.

---

## 2. Detecting a Cycle in a Linked List

### Problem Statement
Determine whether a linked list contains a cycle.

A cycle exists when a node's `next` pointer points back to a previously visited node instead of pointing to `None`.

### Floyd's Cycle Detection Algorithm

Floyd's Cycle Detection Algorithm is also known as the **Tortoise and Hare Algorithm**.

It uses two pointers:
- **Slow pointer (Tortoise):** Moves one node at a time.
- **Fast pointer (Hare):** Moves two nodes at a time.

### Algorithm
1. If `head` is `None` or `head.next` is `None`, return `False`.
2. Initialize `slow` and `fast` to `head`.
3. Move `slow` one step and `fast` two steps.
4. If `slow == fast`, return `True` because a cycle exists.
5. Continue while `fast` and `fast.next` are not `None`.
6. If `fast` reaches `None`, return `False` because no cycle exists.

### Example 1: Cycle Exists

`10 -> 20 -> 30 -> 40`

Suppose the next pointer of node `40` points back to node `20`.

The slow and fast pointers eventually meet. Therefore, the algorithm returns `True`.

### Example 2: No Cycle

`10 -> 20 -> 30 -> 40 -> None`

The fast pointer eventually reaches `None`. Therefore, the algorithm returns `False`.

### Python Code

```python
slow = head
fast = head

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        # A cycle exists
        return True

# No cycle exists
return False
```

### Complexity
- Time Complexity: O(n)
- Auxiliary Space Complexity: O(1)

The algorithm uses two pointers and does not need a separate set or list to store visited nodes.

---

## 3. Difference Between the Two Problems

| Feature | Finding Middle Node | Cycle Detection |
|---|---|---|
| Purpose | Find the middle node | Check whether a cycle exists |
| Slow pointer | Moves one step | Moves one step |
| Fast pointer | Moves two steps | Moves two steps |
| Main result | Middle node | `True` or `False` |
| Time complexity | O(n) | O(n) |
| Auxiliary space | O(1) | O(1) |

## 4. Important Conditions

### Finding the Middle
Use this condition:

`fast is not None and fast.next is not None`

It prevents accessing the next node of a missing node.

### Detecting a Cycle
Check whether the two pointers meet **after moving them**:

`if slow == fast:`

The initial assignment `slow = head` and `fast = head` is not itself evidence of a cycle.

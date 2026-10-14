# DSA Day 45 - Linked List-7

## Topics Covered

Today I learned three linked list problems:

1. Remove Kth Node from the End
2. Swap Nodes in Pairs
3. Odd Even List

## 1. Remove Kth Node from the End

Remove the Kth node counting from the end of a singly linked list.

**Key formula:**

Kth node from the end = (N - K + 1)th node from the beginning

**Approach:** Count the total number of nodes, calculate the position from the beginning, and delete that node.

**Example:**

Input: `10 -> 20 -> 30 -> 40 -> 50`, K = 2

Output: `10 -> 20 -> 30 -> 50`

**Time Complexity:** O(N)

**Space Complexity:** O(1)

## 2. Swap Nodes in Pairs

Swap every two adjacent nodes in a linked list. If one node remains at the end, leave it unchanged.

**Approach:** Take two adjacent nodes and swap their data values using a temporary variable, following the class notes.

**Example:**

Input: `1 -> 2 -> 3 -> 4`

Output: `2 -> 1 -> 4 -> 3`

**Time Complexity:** O(N)

**Space Complexity:** O(1)

## 3. Odd Even List

Arrange nodes at odd positions first, followed by nodes at even positions. The original relative order within each group must be maintained.

**Example:**

Input: `1 -> 2 -> 3 -> 4 -> 5`

Output: `1 -> 3 -> 5 -> 2 -> 4`

**Approach:** Maintain separate odd-position and even-position links, then connect the odd list to the even list.

**Time Complexity:** O(N)

**Space Complexity:** O(1)

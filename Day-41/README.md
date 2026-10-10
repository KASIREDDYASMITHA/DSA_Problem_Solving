# DSA Day 41 - Linked List-3

## Topics Covered

Today, I learned four linked list operations:

1. Delete the first node in a linked list.
2. Delete the last node in a linked list.
3. Reverse a linked list.
4. Find the middle node in a linked list.

## 1. Delete the First Node

Delete the first node by moving the head pointer to the second node.

**Example:**

Input: `10 -> 20 -> 30 -> None`

Output: `20 -> 30 -> None`

**Approach:**
- If the list is empty, return `None`.
- Update `head` to `head.next`.
- Return the updated head.

**Time Complexity:** O(1)

**Space Complexity:** O(1)

## 2. Delete the Last Node

Delete the last node by reaching the second-last node and setting its `next` to `None`.

**Example:**

Input: `10 -> 20 -> 30 -> None`

Output: `10 -> 20 -> None`

**Approach:**
- If the list is empty or contains only one node, return `None`.
- Traverse until the second-last node.
- Set its `next` to `None`.
- Return the head.

**Time Complexity:** O(n)

**Space Complexity:** O(1)

## 3. Reverse a Linked List

Reverse a linked list by changing the direction of every node's `next` pointer.

**Example:**

Input: `10 -> 20 -> 30 -> None`

Output: `30 -> 20 -> 10 -> None`

**Approach:**
- Initialize `prev = None`, `curr = head`, and `next_node = None`.
- Store the next node before changing the current link.
- Point `curr.next` to `prev`.
- Move `prev` and `curr` forward.
- Return `prev` as the new head.

**Time Complexity:** O(n)

**Space Complexity:** O(1)

## 4. Find the Middle Node

Find the middle node using two pointers: `slow` and `fast`.

**Example 1:**

Input: `10 -> 20 -> 30 -> 40 -> 50 -> None`

Output: `30`

**Example 2:**

Input: `10 -> 20 -> 30 -> 40 -> None`

Output: `30`

**Approach:**
- Initialize both pointers at the head.
- Move `slow` one step at a time.
- Move `fast` two steps at a time.
- When `fast` reaches the end, `slow` points to the middle.

For an even number of nodes, this implementation returns the second middle node.

**Time Complexity:** O(n)

**Space Complexity:** O(1)


# DSA Day 43 - Linked List-5

## Topics Covered

Today I practiced three linked-list problems:

1. Length of Cycle
2. First Node in Cycle
3. Palindrome Linked List

## 1. Length of Cycle

Find the number of nodes present in a cycle in a linked list. If no cycle exists, the length is 0.

**Approach:** Use Floyd's slow and fast pointers to detect the cycle. After the pointers meet, traverse the cycle once to count its nodes.

**Time Complexity:** O(n)  
**Auxiliary Space:** O(1)

## 2. First Node in Cycle

Find the node where the cycle begins in a linked list.

**Approach:** Use Floyd's slow and fast pointers to detect the cycle. After they meet, reset the slow pointer to the head and move both pointers one step at a time. Their next meeting point is the cycle's starting node.

**Time Complexity:** O(n)  
**Auxiliary Space:** O(1)

## 3. Palindrome Linked List

A linked list is a palindrome if its elements are the same when read forward and backward.

Examples:
- 1 -> 2 -> 3 -> 2 -> 1: Palindrome
- 1 -> 2 -> 3 -> 4: Not a palindrome

**Approach:**
1. Find the middle of the linked list using slow and fast pointers.
2. Reverse the second half.
3. Compare the elements of both halves.
4. Restore the original linked list.

**Time Complexity:** O(n)  
**Auxiliary Space:** O(1)



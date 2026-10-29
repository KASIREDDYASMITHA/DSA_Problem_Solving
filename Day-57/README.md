# DSA Day 57 - Backtracking

## Topics Covered

Today, I practiced two backtracking problems:

1. Combination Sum
2. Palindrome Partitioning

## 1. Combination Sum

**Problem:** Given an array of distinct positive integers and a target, print all unique combinations whose sum equals the target.

**Approach:**
- Use recursion and backtracking.
- Add an element to the current combination.
- Reuse the same element by passing the same index in the recursive call.
- Stop when the sum equals or exceeds the target.
- Remove the last element and explore other choices.

**Example:**

Input:
- Array: [2, 3, 6, 7]
- Target: 7

Output:
- [2, 2, 3]
- [7]

## 2. Palindrome Partitioning

**Problem:** Given a string, print all possible partitions such that every substring is a palindrome.

**Approach:**
- Start from the current index.
- Try every possible substring.
- Check whether the substring is a palindrome.
- Add valid substrings to the current partition.
- Recursively process the remaining string.
- Backtrack by removing the last substring.

**Example:**

Input:
- String: aab

Output:
- ['a', 'a', 'b']
- ['aa', 'b']

## Key Concepts Learned

- Recursion
- Backtracking
- Base conditions
- Substring selection
- Palindrome checking
- Choose, Explore, Undo

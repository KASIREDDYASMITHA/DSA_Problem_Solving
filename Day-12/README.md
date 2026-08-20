# DSA Day 12 - Two Pointer Technique

## 📅 Day 12

Today I learned the **Two Pointer Technique**, an optimization technique used to solve problems efficiently by using two indices/pointers to traverse a data structure.

## 📚 Topics Covered

- Two Pointer Technique
- Types of Two Pointer Technique
- Same Direction Two Pointers
- Opposite Direction Two Pointers
- Applications of Two Pointers
- Reversing an Array
- Reversing an Array In-Place
- Checking Whether a String is a Palindrome
- Time Complexity
- Space Complexity

## 🔹 Two Pointer Technique

The Two Pointer Technique is an optimization method where two indices/pointers are used to traverse data structures such as:

- Arrays
- Strings
- Linked Lists

Instead of using nested loops with `O(n²)` time complexity, many problems can be solved efficiently in `O(n)` time.

## 🔹 Types of Two Pointer Technique

### 1. Opposite Direction

The two pointers start from opposite ends and move towards each other.

Example:

```text
left  →        ←  right
[ 1 ][ 3 ][ 7 ][ 4 ][ 5 ]
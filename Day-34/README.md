# DSA Day 34

## Topics Covered

Today I learned advanced applications of Binary Search on rotated sorted arrays.

### 1. Search in Rotated Sorted Array
- A sorted array can be rotated at an unknown index.
- Even after rotation, one half of the array is always sorted.
- We identify the sorted half using `low`, `mid`, and `high`.
- Then we check whether the target lies inside that sorted half.
- Time Complexity: O(log n)
- Space Complexity: O(1)

### 2. Minimum Element in Rotated Sorted Array
- A rotated sorted array contains two sorted portions.
- The minimum element is present around the rotation point.
- Binary Search is used to find the minimum efficiently.
- If the left part is sorted, the minimum can be in the right unsorted part.
- Time Complexity: O(log n)
- Space Complexity: O(1)

## Programs

1. Search_Rotated_Sorted_Array.py
2. Minimum_Element_Rotated_Sorted_Array.py

## Key Idea

Instead of checking every element one by one, Binary Search eliminates half of the search space in every step.

## Example

Sorted array:

[0, 1, 2, 4, 5, 6, 7]

After rotation:

[4, 5, 6, 7, 0, 1, 2]

The array is no longer completely sorted, but one half is always sorted.


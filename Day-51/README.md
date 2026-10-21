# Day 51 — Merge Sort

## Topics Covered
- Divide and Conquer
- Merge procedure
- Base condition
- Merging two sorted arrays
- Complete Merge Sort algorithm

## 1. What is Merge Sort?

Merge Sort is a sorting algorithm based on the Divide and Conquer technique. It divides an array into smaller parts, sorts them, and combines them to obtain a sorted array.

## 2. Divide and Conquer

The algorithm works in three steps:

1. **Divide:** Split the array into two halves.
2. **Conquer:** Recursively sort both halves.
3. **Combine:** Merge the two sorted halves into one sorted array.

## 3. Base Condition

When the subarray contains only one element, stop dividing it.

A single-element array is already sorted.

## 4. Merge Procedure

The merge procedure takes two sorted arrays and combines them into one sorted array.

Example:

Input:
- Array 1: `[2, 3, 4, 5]`
- Array 2: `[9, 10, 11, 12]`

Output:
`[2, 3, 4, 5, 9, 10, 11, 12]`

The procedure compares the current elements of both arrays and adds the smaller element to the result.

## 5. Algorithm

1. Find the middle index.
2. Divide the array into left and right halves.
3. Recursively sort both halves.
4. Merge the sorted halves.
5. Stop recursion when the left index is greater than or equal to the right index.

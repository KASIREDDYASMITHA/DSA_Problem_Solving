# Day 16- DSA Problem Solving

## Topics Covered

Today I learned array problems based on:

- Two Pointer Technique
- Removing duplicates from a sorted array
- Subarrays
- Maximum Sum Subarray of Size K
- Brute Force Approach
- Sliding Window concept

---

## 1. Remove Duplicates From Sorted Array

### Problem

Given a sorted array, remove duplicate elements and keep only the unique elements.

### Approach

I used the Two Pointer Approach.

- `i` is used to compare the current element with the next element.
- `j` keeps track of the position where the next unique element should be stored.
- Since the array is sorted, duplicate elements appear next to each other.
- If `arr[i] != arr[i + 1]`, the element is unique and is stored at `arr[j]`.

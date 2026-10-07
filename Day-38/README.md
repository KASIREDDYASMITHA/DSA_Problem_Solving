# DSA Day 38 - Binary Search 

## Topics Covered

Today I learned the Binary Search on Answer technique and solved three problems:

1. Capacity to Ship Packages Within D Days
2. Split Array - Minimize Largest Subarray Sum
3. Painter's Partition Problem

## What is Binary Search?

Binary Search is a technique where we do not search for an element in an array.

Instead, we search for the minimum or maximum possible answer within a range.

The general process is:

- Find the minimum possible answer.
- Find the maximum possible answer.
- Take the middle value.
- Check whether the middle value is possible.
- If it is possible, try to find a better smaller answer.
- If it is not possible, increase the answer.
- Continue until the optimal answer is found.

## 1. Capacity to Ship Packages Within D Days

Given package weights and a number of days, find the minimum ship capacity required to ship all packages within the given number of days.

### Example

Weights:

10 20 30 40 50

Days:

3

The answer is the minimum capacity that can ship all packages within 3 days.

### Search Range

Minimum capacity = maximum package weight

Maximum capacity = sum of all package weights

## 2. Split Array - Minimize Largest Subarray Sum

Given an array and k subarrays, split the array into k contiguous subarrays such that the largest subarray sum is as small as possible.

### Example

Array:

7 2 5 10 8

K:

2

The goal is to minimize the largest sum among the two subarrays.

### Search Range

Minimum possible answer = maximum element

Maximum possible answer = sum of all elements

## 3. Painter's Partition Problem

Given board lengths and k painters, assign contiguous boards to painters so that all boards are painted in the minimum possible time.

### Example

Boards:

10 20 30 40

Painters:

2

The goal is to minimize the maximum time taken by any painter.

### Search Range

Minimum possible time = longest board

Maximum possible time = sum of all boards

## Brute Force Approach

In the brute-force approach, every possible answer from the minimum value to the maximum value is checked.

For every possible answer:

- Calculate how many days, subarrays, or painters are required.
- If the required number is within the limit, the answer is valid.
- Return the first valid answer.

## Binary Search Approach

Instead of checking every possible answer, binary search is used on the answer range.

If the current answer is possible:

- Store it as the answer.
- Search the left half for a smaller answer.

If the current answer is not possible:

- Search the right half.

This reduces the search space much faster.

## Important Pattern

These problems follow the same pattern:

```text
low = maximum element
high = sum of elements

while low <= high:

    mid = middle value

    check whether mid is possible

    if possible:
        answer = mid
        search left
    else:
        search right
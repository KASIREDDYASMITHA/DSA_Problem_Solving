# DSA Day 36 - Peak Element and Bitonic Point

## Topics Covered

Today I learned two important array problems:

1. Peak Element
2. Bitonic Point

For both problems, I learned two approaches:

- Linear Search
- Binary Search

I also learned:

- How binary search can be applied to problems that are not completely sorted
- How to identify increasing and decreasing slopes
- How to reduce the search space
- Boundary element handling
- Time Complexity
- Space Complexity

---

# Problem 1: Peak Element

## Definition

A **Peak Element** is an element that is greater than its neighboring elements.

For an element at index `i`:

```text
arr[i] > arr[i - 1]
AND
arr[i] > arr[i + 1]


## Definition of Bitonic Point

A **Bitonic Point** is the maximum element in a bitonic array, where the array first increases and then decreases.

In simple words, it is the point where the increasing sequence changes into a decreasing sequence.

For example:

[1, 3, 5, 8, 6, 4, 2]

Here:

1 < 3 < 5 < 8

and

8 > 6 > 4 > 2

Therefore, `8` is the **Bitonic Point**.

```text
1 < 3 < 5 < 8 > 6 > 4 > 2
            ↑
       Bitonic Point
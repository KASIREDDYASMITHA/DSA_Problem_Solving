# Day 52 - Quick Sort

## Topic
Quick Sort Algorithm

## What I Learned
- Quick Sort is a divide-and-conquer sorting algorithm.
- The pivot element is placed in its correct position in the sorted array.
- Elements smaller than or equal to the pivot are placed on its left, and greater elements are placed on its right in the partition method used here.
- Quick Sort recursively sorts the left and right subarrays.
- Quick Sort is generally not stable.
- Merge Sort is generally stable.

## How Quick Sort Works
1. Choose a pivot element.
2. Partition the array around the pivot.
3. Place the pivot in its correct sorted position.
4. Apply Quick Sort to the left subarray.
5. Apply Quick Sort to the right subarray.
6. Continue until the subarrays contain zero or one element.

## Example
Input:
`[10, 7, 8, 9, 1, 5]`

Output:
`[1, 5, 7, 8, 9, 10]`

## Partitioning
Partitioning rearranges elements around the pivot so that the pivot reaches its correct position for the current subarray.

## Time Complexity
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n²)

## Space Complexity
- Average recursion space: O(log n)
- Worst-case recursion space: O(n)

## Stability
- Quick Sort: Generally unstable.
- Merge Sort: Generally stable.

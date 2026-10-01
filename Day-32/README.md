# Day 32 - Binary Search 1

## Topics Covered

- Linear Search
- Time Complexity of Linear Search
- Binary Search
- Binary Search condition
- Search Space Reduction
- `low`, `high`, and `mid`
- First Occurrence
- Last Occurrence
- Safe calculation of `mid`

## Programs

1. Linear Search
2. Binary Search
3. First Occurrence using Binary Search
4. Last Occurrence using Binary Search

## Key Learning

- Linear Search checks elements one by one.
- Binary Search works only on sorted data.
- Binary Search reduces the search space by half in every iteration.
- `mid = low + (high - low) // 2` is used to calculate the middle index safely.
- For First Occurrence, after finding the key, continue searching towards the left.
- For Last Occurrence, after finding the key, continue searching towards the right.

## Complexity

- Linear Search: O(n)
- Binary Search: O(log n)
- First Occurrence: O(log n)
- Last Occurrence: O(log n)


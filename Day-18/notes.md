# DSA Day 18 - Sliding Window Technique

## 1. Sliding Window Technique

Sliding Window is a technique used to solve problems involving continuous subarrays or subarrays/windows of an array.

Instead of repeatedly processing the same elements, we maintain a window using two pointers such as:

- `start`
- `end`

The window represents the current range of elements being considered.

---

# 2. Variable Size Sliding Window

In a variable size sliding window, the window size is not fixed.

The window size changes dynamically based on a given condition.

The window can:

- Expand
- Shrink

depending on the condition of the problem.

When the value of `k` or the required window size is not directly given in the question, a variable size sliding window may be used depending on the problem.

---

# 3. General Flow of Variable Size Sliding Window

The general idea is:

```text
start = 0

for end = 0; end < n; end++:

    add arr[end]

    while window is invalid:

        remove arr[start]
        start++

    update answer
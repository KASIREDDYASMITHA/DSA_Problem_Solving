# DSA Day 14 - Two Pointer Technique

## 📚 Topics Covered

Today I learned the **Two Pointer Technique** and how it can be used to optimize array problems involving pairs and triplets.

### 1. Two Pointer Technique

* Using `left` and `right` pointers.
* Starting `left` from the beginning and `right` from the end.
* Sorting the array before applying the standard opposite-end Two Pointer approach.
* Moving pointers based on the current sum.

### Pointer Movement Rule

```text
sum == target  → Answer found

sum < target   → left++

sum > target   → right--
```

---

## 2. Two Sum

### Brute Force

Used two nested loops to check every possible pair.

```text
Time Complexity: O(n²)
Space Complexity: O(1)
```

### Two Pointer

Sorted the array and used `left` and `right` pointers.

```text
Time Complexity: O(n log n)
Space Complexity: O(1)
```

---

## 3. Sum Triplet

Problem:

```text
arr[i] + arr[j] + arr[k] == target
```

### Brute Force

Used three nested loops.

```text
Time Complexity: O(n³)
Space Complexity: O(1)
```

### Optimized Two Pointer Approach

* Sort the array.
* Fix one element `arr[i]`.
* Calculate:

```text
newTarget = target - arr[i]
```

* Use `left` and `right` pointers to find the remaining two elements.

```text
Time Complexity: O(n²)
Space Complexity: O(1)
```

This improves the brute-force approach from:

```text
O(n³) → O(n²)
```

---

## 4. Closest Pair Sum

Problem:

Find two elements whose sum is closest to the given target.

Difference is calculated using:

```text
diff = abs(target - sum)
```

### Brute Force

Checked every possible pair.

```text
Time Complexity: O(n²)
Space Complexity: O(1)
```

### Two Pointer Approach

* Sort the array.
* Start `left = 0`.
* Start `right = n - 1`.
* Calculate the current pair sum.
* Track the minimum difference.
* Move pointers according to the target.

```text
Time Complexity: O(n log n)
Space Complexity: O(1)
```

---

## 📊 Complexity Summary

| Problem          | Approach    |       Time | Space |
| ---------------- | ----------- | ---------: | ----: |
| Two Sum          | Brute Force |      O(n²) |  O(1) |
| Two Sum          | Two Pointer | O(n log n) |  O(1) |
| Sum Triplet      | Brute Force |      O(n³) |  O(1) |
| Sum Triplet      | Two Pointer |      O(n²) |  O(1) |
| Closest Pair Sum | Brute Force |      O(n²) |  O(1) |
| Closest Pair Sum | Two Pointer | O(n log n) |  O(1) |

---

## 💡 Key Learning

The main idea learned today:

> **Use the sorted order of an array to intelligently move two pointers instead of checking every possible combination.**

For pair problems:

```text
left = 0
right = n - 1

while left < right:

    sum = arr[left] + arr[right]

    if sum == target:
        found

    elif sum < target:
        left++

    else:
        right--
```

For triplet problems:

```text
Fix one element
        ↓
Convert remaining problem into Two Sum
        ↓
Apply Two Pointer
```

---

## 💻 Programs Practiced

### `sum_triplet.py`

Contains:

* Sum Triplet using Brute Force
* Sum Triplet using Two Pointer Optimization

### `closest_pair_sum.py`

Contains:

* Closest Pair Sum using Brute Force
* Closest Pair Sum using Two Pointer Optimization


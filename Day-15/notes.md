# DSA Day 15 - Two Pointer Technique

## Two Pointer Technique

The Two Pointer Technique is used to solve array problems efficiently by using two pointers.

The pointers are moved according to the condition of the problem.

---

# 1. Container With Most Water

## Problem

Given an array of heights, choose two lines that can form a container containing the maximum amount of water.

For two lines at positions `i` and `j`:

```text
length = j - i
breadth = min(arr[i], arr[j])
area = length * breadth
```

The maximum area among all possible pairs is the answer.

---

# 2. Container With Most Water - Brute Force Approach

In the Brute Force Approach, we check every possible pair of lines.

We use two loops:

```text
for i = 0 to n-1
    for j = i+1 to n-1
```

For every pair:

```text
length = j - i
breadth = min(arr[i], arr[j])
area = length * breadth
```

Then update the maximum area.

## Algorithm

1. Initialize `result = -infinity`.
2. Start `i` from `0`.
3. Start `j` from `i + 1`.
4. Calculate the length.
5. Find the smaller height.
6. Calculate the area.
7. Update the maximum result.
8. Repeat for all possible pairs.
9. Return the result.

## Pseudocode

```text
function maxArea(arr[])
{
    result = -infinity

    for(i = 0; i < n; i++)
    {
        for(j = i + 1; j < n; j++)
        {
            length = j - i
            breadth = Math.min(arr[i], arr[j])
            area = length * breadth
            result = Math.max(result, area)
        }
    }

    return result
}
```

## Complexity

```text
Time Complexity  = O(n²)
Space Complexity = O(1)
```

---

# 3. Container With Most Water - Two Pointer Approach

The Brute Force Approach takes `O(n²)` time.

We can optimize it using the Two Pointer Technique.

Initialize:

```text
left = 0
right = arr.length - 1
```

Calculate:

```text
length = right - left
breadth = min(arr[left], arr[right])
area = length * breadth
```

Update the maximum result.

## Pointer Movement

If:

```text
arr[left] < arr[right]
```

move the left pointer:

```text
left++
```

Otherwise:

```text
right--
```

The pointer at the smaller height is moved because the smaller height limits the container.

Continue until:

```text
left < right
```

becomes false.

## Pseudocode

```text
function maxArea(arr[])
{
    result = -infinity

    left = 0
    right = arr.length - 1

    while(left < right)
    {
        length = right - left
        breadth = Math.min(arr[left], arr[right])
        area = length * breadth

        result = Math.max(result, area)

        if(arr[left] < arr[right])
        {
            left++
        }
        else
        {
            right--
        }
    }

    return result
}
```

The faculty notes use this exact left/right pointer structure.

## Complexity

```text
Time Complexity  = O(n)
Space Complexity = O(1)
```

---

# 4. Brute Force vs Two Pointer

| Approach    | Time Complexity | Space Complexity |
| ----------- | --------------- | ---------------- |
| Brute Force | O(n²)           | O(1)             |
| Two Pointer | O(n)            | O(1)             |

The Two Pointer Approach is more efficient because it avoids checking every possible pair.

---

# 5. Merge Two Sorted Arrays

Given two sorted arrays, merge them into one sorted array.

Example:

```text
arr1 = [1, 2, 7]
arr2 = [3, 4, 5, 6]
```

Result:

```text
[1, 2, 3, 4, 5, 6, 7]
```

We use three pointers:

```text
i = 0
j = 0
k = 0
```

Where:

* `i` points to the current element of `arr1`.
* `j` points to the current element of `arr2`.
* `k` points to the current position in the result array.

The result array size is:

```text
n1 + n2
```

where:

```text
n1 = length of arr1
n2 = length of arr2
```

---

# 6. Merge Process

Compare:

```text
arr1[i] and arr2[j]
```

If:

```text
arr1[i] < arr2[j]
```

store `arr1[i]` in the result array and move:

```text
i++
k++
```

Otherwise, store `arr2[j]` and move:

```text
j++
k++
```

Continue until one of the arrays is completely processed.

---

# 7. Remaining Elements

After the main loop, one array may still have remaining elements.

If elements are remaining in `arr2`:

```text
while(j < n2)
{
    res[k] = arr2[j]
    j++
    k++
}
```

If elements are remaining in `arr1`:

```text
while(i < n1)
{
    res[k] = arr1[i]
    i++
    k++
}
```

Finally, return the result.

## Pseudocode

```text
function mergeTwoSortedArrays(arr1[], arr2[])
{
    n1 = arr1.length
    n2 = arr2.length

    i = 0
    j = 0
    k = 0

    res[] = new Array(n1 + n2)

    while(i < n1 && j < n2)
    {
        if(arr1[i] < arr2[j])
        {
            res[k] = arr1[i]
            i++
            k++
        }
        else
        {
            res[k] = arr2[j]
            j++
            k++
        }
    }

    while(j < n2)
    {
        res[k] = arr2[j]
        j++
        k++
    }

    while(i < n1)
    {
        res[k] = arr1[i]
        i++
        k++
    }

    return res
}
```

This follows the merge approach in your faculty notes using `i`, `j`, and `k`.

## Complexity

```text
Time Complexity  = O(n1 + n2)
Space Complexity = O(n1 + n2)
```

---

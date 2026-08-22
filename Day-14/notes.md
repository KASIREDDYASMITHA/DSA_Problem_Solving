# DSA Day 14 - Two Pointer Technique

## Topic: Two Pointer Technique

Today I learned the **Two Pointer Technique** and how it can be used to optimize problems involving pairs and triplets in an array.

The main problems covered today are:

1. Two Sum
2. Two Sum using Two Pointer
3. Sum Triplet
4. Sum Triplet using Brute Force
5. Sum Triplet using Two Pointer
6. Closest Pair Sum
7. Closest Pair Sum using Brute Force
8. Closest Pair Sum using Two Pointer

---

# 1. Two Pointer Technique

The **Two Pointer Technique** is an algorithmic technique where two indexes/pointers are used to traverse an array.

The two pointers are generally called:

```text
left
right
```

For a sorted array:

```text
left  -> starts from the beginning
right -> starts from the end
```

Example:

```text
Array:

2  5  7  12  13  14  14  16  27
^                              ^
left                           right
```

The pointers move toward each other depending on the current sum.

---

# 2. Important Condition

For two elements:

```text
arr[left] + arr[right]
```

compare the sum with the target.

There are three possible cases.

## Case 1: Sum == Target

```text
arr[left] + arr[right] == target
```

The required pair has been found.

Example:

```text
arr = [2, 5, 7, 12, 13, 14, 16, 27]
target = 18
```

If:

```text
arr[left] = 5
arr[right] = 13
```

Then:

```text
5 + 13 = 18
```

Therefore the target is found.

---

## Case 2: Sum < Target

If:

```text
arr[left] + arr[right] < target
```

the current sum is too small.

Since the array is sorted, increase the left pointer:

```text
left++
```

This tries to obtain a larger sum.

Example:

```text
arr = [2, 5, 7, 12, 13]
target = 18
```

Suppose:

```text
left = 0
right = 4

2 + 13 = 15
```

Since:

```text
15 < 18
```

move:

```text
left++
```

---

## Case 3: Sum > Target

If:

```text
arr[left] + arr[right] > target
```

the current sum is too large.

Since the array is sorted, decrease the right pointer:

```text
right--
```

This tries to obtain a smaller sum.

Example:

```text
arr = [2, 5, 7, 12, 13]
target = 18
```

Suppose:

```text
left = 1
right = 4

5 + 13 = 18
```

If instead the sum were:

```text
7 + 13 = 20
```

then:

```text
20 > 18
```

so:

```text
right--
```

---

# 3. Why Sorting Is Important

The Two Pointer technique depends on the array being sorted.

Example:

```text
Original array:

2 7 5 14 4 12 27 16 13
```

After sorting:

```text
2 5 7 12 13 14 14 16 27
```

Now we know:

* Moving `left` to the right increases the value.
* Moving `right` to the left decreases the value.

Therefore we can intelligently decide which pointer to move.

---

# 4. Two Sum

## Problem

Given an integer array `arr[]` and an integer `target`, determine whether there exists a pair of elements whose sum is equal to the target.

Condition:

```text
arr[i] + arr[j] = target
```

Return:

```text
true
```

if such a pair exists.

Otherwise return:

```text
false
```

---

# 5. Two Sum - Brute Force Approach

The brute-force approach checks every possible pair.

We use two loops:

```text
for i
    for j
```

The condition is:

```text
arr[i] + arr[j] == target
```

## Pseudocode

```text
function twoSum(arr[], target)
{
    for(i = 0; i < arr.length - 1; i++)
    {
        for(j = i + 1; j < arr.length; j++)
        {
            if(arr[i] + arr[j] == target)
                return true
        }
    }

    return false
}
```

The faculty notes use this nested-loop approach for the basic Two Sum solution.

## Time Complexity

There are two nested loops.

Therefore:

```text
Time Complexity = O(n²)
```

## Space Complexity

Only a constant amount of extra space is used.

```text
Space Complexity = O(1)
```

---

# 6. Two Sum - Two Pointer Approach

The Two Sum problem can be optimized using the Two Pointer Technique.

First sort the array.

Then:

```text
left = 0
right = arr.length - 1
```

The faculty notes specify sorting the array and then comparing the two-pointer sum with the target.

## Pseudocode

```text
function twoSum(arr[], target)
{
    left = 0
    right = arr.length - 1

    arr.sort()

    while(left < right)
    {
        if(arr[left] + arr[right] == target)
            return true

        else if(arr[left] + arr[right] < target)
            left++

        else
            right--
    }

    return false
}
```

---

# 7. Two Sum Example 1

Input:

```text
arr = [2, 7, 5, 14, 4, 12, 27, 16, 13]
target = 18
```

After sorting:

```text
[2, 4, 5, 7, 12, 13, 14, 16, 27]
```

Start:

```text
left = 0
right = 8
```

Check:

```text
2 + 27 = 29
```

Since:

```text
29 > 18
```

move:

```text
right--
```

Continue until:

```text
5 + 13 = 18
```

Therefore:

```text
Pair exists
```

---

# 8. Two Sum Example 2

Input:

```text
arr = [2, 4, 5, 7, 12]
target = 20
```

Largest possible pair:

```text
7 + 12 = 19
```

No pair can produce `20`.

Therefore:

```text
false
```

---

# 9. Two Sum Complexity

Sorting:

```text
O(n log n)
```

Two Pointer traversal:

```text
O(n)
```

Overall:

```text
O(n log n)
```

Space:

```text
O(1)
```

So:

```text
Brute Force Two Sum  = O(n²)
Two Pointer Two Sum   = O(n log n)
```

---

# 10. Set

A **set** is an unordered collection of distinct elements.

Example:

```text
{2, 4, 7, 9}
```

Duplicate values are not stored as separate elements.

Example:

```text
Input:

[2, 4, 4, 7, 7, 9]

Set:

{2, 4, 7, 9}
```

The class notes define a set as an unordered collection of distinct elements.

---

# 11. Sum Triplet

## Problem

Given an integer array `arr[]` and an integer `target`, determine whether there exists a triplet `(a, b, c)` such that:

```text
a + b + c = target
```

Return:

```text
true
```

if a triplet exists.

Otherwise:

```text
false
```

---

# 12. Sum Triplet - Brute Force

The brute-force solution uses three loops.

We select three different elements:

```text
arr[i]
arr[j]
arr[k]
```

and check:

```text
arr[i] + arr[j] + arr[k] == target
```

The structure is:

```text
for i
    for j
        for k
            check sum
```

## Pseudocode

```text
function threeSum(arr[], target)
{
    for(i = 0; i < n; i++)
    {
        for(j = i + 1; j < n; j++)
        {
            for(k = j + 1; k < n; k++)
            {
                if(arr[i] + arr[j] + arr[k] == target)
                    return true
            }
        }
    }

    return false
}
```

---

# 13. Sum Triplet Example 1

Input:

```text
arr = [2, 5, 7, 12, 13]
target = 20
```

Check possible triplets.

One valid triplet is:

```text
2 + 5 + 13 = 20
```

Therefore:

```text
true
```

---

# 14. Sum Triplet Example 2

Input:

```text
arr = [1, 4, 7, 10]
target = 30
```

No three elements produce `30`.

Therefore:

```text
false
```

---

# 15. Sum Triplet Brute Force Complexity

There are three nested loops.

Therefore:

```text
Time Complexity = O(n³)
```

Space:

```text
Space Complexity = O(1)
```

The major disadvantage is that the number of comparisons grows very quickly as `n` increases.

---

# 16. Sum Triplet - Optimized Two Pointer Approach

The brute-force approach takes:

```text
O(n³)
```

We can optimize it using the Two Pointer Technique.

First sort the array:

```text
arr.sort()
```

Then fix one element:

```text
arr[i]
```

For the remaining two elements, calculate:

```text
newTarget = target - arr[i]
```

Now the problem becomes a Two Sum problem.

We need:

```text
arr[left] + arr[right] == newTarget
```

The faculty notes use exactly this approach: sort the array, fix `i`, calculate `newTarget`, then use `left` and `right`.

---

# 17. Sum Triplet Two Pointer Algorithm

Step 1:

```text
arr.sort()
```

Step 2:

```text
for i = 0 to n - 3
```

Step 3:

```text
left = i + 1
right = n - 1
```

Step 4:

```text
newTarget = target - arr[i]
```

Step 5:

Check:

```text
arr[left] + arr[right]
```

against:

```text
newTarget
```

---

# 18. Sum Triplet Pointer Movement

If:

```text
arr[left] + arr[right] == newTarget
```

then:

```text
Triplet found
```

Return:

```text
true
```

---

If:

```text
arr[left] + arr[right] < newTarget
```

then:

```text
left++
```

because a larger value is required.

---

If:

```text
arr[left] + arr[right] > newTarget
```

then:

```text
right--
```

because a smaller value is required.

---

# 19. Sum Triplet Pseudocode

```text
function threeSum(arr[], target)
{
    arr.sort()

    for(i = 0; i < n - 2; i++)
    {
        left = i + 1
        right = arr.length - 1

        newTarget = target - arr[i]

        while(left < right)
        {
            if(arr[left] + arr[right] == newTarget)
                return true

            else if(arr[left] + arr[right] < newTarget)
                left++

            else
                right--
        }
    }

    return false
}
```

---

# 20. Sum Triplet Example

Given:

```text
arr = [2, 7, 5, 14, 4, 12, 27, 16, 13]
target = 28
```

Sort:

```text
[2, 4, 5, 7, 12, 13, 14, 16, 27]
```

Take:

```text
arr[i] = 2
```

Then:

```text
newTarget = 28 - 2
newTarget = 26
```

Now find two numbers whose sum is `26`.

For example:

```text
12 + 14 = 26
```

Therefore:

```text
2 + 12 + 14 = 28
```

Triplet exists.

---

# 21. Sum Triplet Complexity

Sorting:

```text
O(n log n)
```

Outer loop:

```text
O(n)
```

Two Pointer search for each fixed element:

```text
O(n)
```

Overall:

```text
Time Complexity = O(n²)
```

Space:

```text
Space Complexity = O(1)
```

Therefore the optimization changes:

```text
Brute Force = O(n³)
```

to:

```text
Two Pointer = O(n²)
```

This is a significant improvement.

---

# 22. Closest Pair Sum

## Problem

Given an integer array `arr[]` and an integer `target`, find a pair of elements whose sum is closest to the target.

Instead of necessarily finding an exact target, we find the pair whose difference from the target is minimum.

Formula:

```text
difference = abs(target - sum)
```

The pair with the smallest difference is the answer.

---

# 23. Closest Pair Sum Example

Given:

```text
arr = [1, 3, 4, 7, 10]
target = 15
```

Possible pairs include:

```text
1 + 3 = 4
1 + 4 = 5
1 + 7 = 8
1 + 10 = 11
3 + 4 = 7
3 + 7 = 10
3 + 10 = 13
4 + 7 = 11
4 + 10 = 14
7 + 10 = 17
```

Compare with target `15`.

For:

```text
4 + 10 = 14
```

difference:

```text
abs(15 - 14) = 1
```

For:

```text
7 + 10 = 17
```

difference:

```text
abs(15 - 17) = 2
```

Therefore:

```text
Closest Pair Sum = 14
```

Pair:

```text
(4, 10)
```

---

# 24. Closest Pair Sum - Brute Force

Use two nested loops.

For every pair:

```text
sum = arr[i] + arr[j]
```

Calculate:

```text
diff = abs(target - sum)
```

Maintain:

```text
bestDiff
bestSum
```

Initially:

```text
bestDiff = infinity
bestSum = 0
```

If:

```text
diff < bestDiff
```

update:

```text
bestDiff = diff
bestSum = sum
```

Finally:

```text
return bestSum
```

---

# 25. Closest Pair Sum Brute Force Pseudocode

```text
function closestPairSum(arr[], target)
{
    n = arr.length

    bestDiff = infinity
    bestSum = 0

    for(i = 0; i < n; i++)
    {
        for(j = i + 1; j < n; j++)
        {
            sum = arr[i] + arr[j]

            diff = abs(target - sum)

            if(diff < bestDiff)
            {
                bestDiff = diff
                bestSum = sum
            }
        }
    }

    return bestSum
}
```

---

# 26. Closest Pair Sum Brute Force Complexity

Two nested loops are used.

Therefore:

```text
Time Complexity = O(n²)
```

Extra space:

```text
Space Complexity = O(1)
```

---

# 27. Closest Pair Sum - Two Pointer Approach

We can optimize the closest pair problem using the Two Pointer Technique.

First sort the array.

Then:

```text
left = 0
right = n - 1
```

Calculate:

```text
sum = arr[left] + arr[right]
```

Then calculate:

```text
diff = abs(target - sum)
```

Update the best answer if the current difference is smaller.

---

# 28. Closest Pair Pointer Movement

If:

```text
sum < target
```

we need a larger sum.

Therefore:

```text
left++
```

---

If:

```text
sum > target
```

we need a smaller sum.

Therefore:

```text
right--
```

---

If:

```text
sum == target
```

then the exact target has been found.

The difference is:

```text
0
```

which is the minimum possible difference.

---

# 29. Closest Pair Two Pointer Pseudocode

```text
function closestPairSum(arr[], target)
{
    arr.sort()

    left = 0
    right = arr.length - 1

    bestDiff = infinity
    bestSum = 0

    while(left < right)
    {
        sum = arr[left] + arr[right]

        diff = abs(target - sum)

        if(diff < bestDiff)
        {
            bestDiff = diff
            bestSum = sum
        }

        if(sum < target)
            left++

        else
            right--
    }

    return bestSum
}
```

---

# 30. Closest Pair Example 1

Input:

```text
arr = [1, 3, 4, 7, 10]
target = 15
```

Sorted:

```text
[1, 3, 4, 7, 10]
```

Start:

```text
left = 0
right = 4
```

Current sum:

```text
1 + 10 = 11
```

Since:

```text
11 < 15
```

move:

```text
left++
```

Next:

```text
3 + 10 = 13
```

Still:

```text
13 < 15
```

Move:

```text
left++
```

Next:

```text
4 + 10 = 14
```

Difference:

```text
abs(15 - 14) = 1
```

This becomes the current best answer.

Therefore:

```text
Closest Pair Sum = 14
```

---

# 31. Closest Pair Example 2

Given:

```text
arr = [2, 5, 8, 12]
target = 15
```

Start:

```text
2 + 12 = 14
```

Difference:

```text
1
```

Move left because:

```text
14 < 15
```

Next:

```text
5 + 12 = 17
```

Difference:

```text
2
```

Move right because:

```text
17 > 15
```

Next:

```text
5 + 8 = 13
```

Difference:

```text
2
```

The best sum remains:

```text
14
```

Therefore:

```text
Closest Pair Sum = 14
```

---

# 32. Closest Pair Two Pointer Complexity

Sorting:

```text
O(n log n)
```

Two Pointer traversal:

```text
O(n)
```

Overall:

```text
Time Complexity = O(n log n)
```

Space:

```text
Space Complexity = O(1)
```

---

# 33. Complexity Comparison

| Problem          | Approach    | Time Complexity | Space Complexity |
| ---------------- | ----------- | --------------- | ---------------- |
| Two Sum          | Brute Force | O(n²)           | O(1)             |
| Two Sum          | Two Pointer | O(n log n)      | O(1)             |
| Sum Triplet      | Brute Force | O(n³)           | O(1)             |
| Sum Triplet      | Two Pointer | O(n²)           | O(1)             |
| Closest Pair Sum | Brute Force | O(n²)           | O(1)             |
| Closest Pair Sum | Two Pointer | O(n log n)      | O(1)             |

---

# 34. Why Two Pointer Is Faster

Consider Sum Triplet.

Brute Force:

```text
for i
    for j
        for k
```

This results in:

```text
O(n³)
```

The optimized method fixes one element and uses two pointers for the remaining two elements.

Therefore:

```text
O(n²)
```

The improvement is:

```text
O(n³) -> O(n²)
```

---

# 35. General Two Pointer Pattern

For a sorted array:

```text
arr.sort()

left = 0
right = n - 1

while left < right:

    currentSum = arr[left] + arr[right]

    if currentSum == target:
        return true

    elif currentSum < target:
        left += 1

    else:
        right -= 1
```

The core decision is:

```text
sum < target
    -> left++

sum > target
    -> right--

sum == target
    -> answer found
```

---

# 36. Important Conditions

The following conditions are important when using this technique.

### Condition 1

The array should generally be sorted before applying this sum-based Two Pointer approach.

### Condition 2

The pointers should move toward each other.

```text
left++
right--
```

### Condition 3

Use:

```text
while(left < right)
```

to ensure the same element is not used twice in a pair.




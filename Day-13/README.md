# DSA Day 13 - Two Pointer Technique


# Topics Covered

Today I learned:

1. Separate Zeros and Ones using an Extra Array
2. Separate Zeros and Ones using Counting
3. Separate Zeros and Ones using Two Pointer Technique
4. Two Sum Problem
5. Two Sum using Brute Force
6. Two Sum using HashSet
7. Time Complexity and Space Complexity comparison
8. Understanding the Two Pointer Technique
9. Understanding HashSet / Set

---

# 1. Separate Zeros and Ones

## Problem Statement

Given a binary array containing only `0`s and `1`s, rearrange the array such that:

* All `0`s appear on the left side.
* All `1`s appear on the right side.

The array should be rearranged so that all zeros are grouped on the left and all ones are grouped on the right.

### Example

Input:

```text
[1, 0, 1, 1, 0, 0, 1]
```

Output:

```text
[0, 0, 0, 1, 1, 1, 1]
```

Another example:

```text
Input:
[0, 0, 1, 1, 1, 0]

Output:
[0, 0, 0, 1, 1, 1]
```

---

# Approach 1 - Using Extra Array

## Idea

Create a new array of the same size as the original array.

Use two positions:

* `j` starts from the beginning of the result array.
* `k` starts from the end of the result array.

Traverse the original array.

If the current element is `0`:

```text
res[j] = arr[i]
j++
```

If the current element is `1`:

```text
res[k] = arr[i]
k--
```

Therefore:

* Zeros are placed from the left.
* Ones are placed from the right.

The faculty notes use a new array of size `n` and two positions for placing zeros and ones.

---

## Algorithm

1. Find the length of the array.
2. Create a new array of size `n`.
3. Initialize:

   * `j = 0`
   * `k = n - 1`
4. Traverse the original array.
5. If the element is `0`, place it at `res[j]`.
6. Increment `j`.
7. If the element is `1`, place it at `res[k]`.
8. Decrement `k`.
9. Return the result array.

---

## Example

```text
Input:
[1, 0, 0, 1, 1, 0]
```

Zeros are placed from the left.

Ones are placed from the right.

Result:

```text
[0, 0, 0, 1, 1, 1]
```

---

## Complexity

```text
Time Complexity  : O(n)
Space Complexity : O(n)
```

The extra space is required because a new result array is created.

---

## Program

File:

```text
01_separate_zeros_ones_extra_array.py
```

---

# Approach 2 - Using Counting

## Idea

Instead of creating another array, count how many zeros and ones are present in the original array.

Maintain:

```text
zero_count = 0
one_count = 0
```

Traverse the array.

If the element is `0`:

```text
zero_count++
```

Otherwise:

```text
one_count++
```

After counting:

* Fill the first `zero_count` positions with `0`.
* Fill the remaining positions with `1`.

This approach modifies the original array.

The faculty notes describe counting zeros and ones and then manually filling zeros for `zero_count` positions and ones for the remaining positions.

---

## Algorithm

1. Find the length of the array.
2. Initialize:

   * `zero_count = 0`
   * `one_count = 0`
3. Traverse the array.
4. Count the number of zeros.
5. Count the number of ones.
6. Fill the first `zero_count` positions with `0`.
7. Fill the remaining positions with `1`.
8. Print the result.

---

## Example

```text
Input:
[1, 0, 1, 0, 0, 1]
```

Count:

```text
Zeros = 3
Ones  = 3
```

Fill:

```text
[0, 0, 0, 1, 1, 1]
```

---

## Complexity

```text
Time Complexity  : O(n)
Space Complexity : O(1)
```

No extra array is created.

---

## Program

File:

```text
02_separate_zeros_ones_counting.py
```

---

# Approach 3 - Two Pointer Technique

## Idea

Use two pointers:

```text
left  = 0
right = n - 1
```

The `left` pointer starts from the beginning.

The `right` pointer starts from the end.

We want:

```text
0 0 0 0 1 1 1 1
```

Therefore:

* `left` should find a misplaced `1`.
* `right` should find a misplaced `0`.
* Swap them.

The faculty notes use exactly this two-pointer structure.

---

## Pointer Movement

### Left Pointer

Move `left` forward while:

```text
arr[left] == 0
```

Because the zero is already in the correct position.

---

### Right Pointer

Move `right` backward while:

```text
arr[right] == 1
```

Because the one is already in the correct position.

---

### Swap

When:

```text
arr[left] == 1
```

and

```text
arr[right] == 0
```

the elements are in the wrong positions.

Swap them:

```python
arr[left], arr[right] = arr[right], arr[left]
```

Then move both pointers:

```text
left++
right--
```

---

## Algorithm

1. Initialize `left = 0`.
2. Initialize `right = n - 1`.
3. Continue while `left < right`.
4. Move `left` while the current element is `0`.
5. Move `right` while the current element is `1`.
6. Swap `arr[left]` and `arr[right]`.
7. Increment `left`.
8. Decrement `right`.
9. Continue until the pointers meet.

---

## Example

Consider:

```text
[0, 1, 1, 0, 1, 0]
```

Initially:

```text
left = 0
right = 5
```

`arr[left]` is `0`, so move `left`.

`arr[right]` is `0`, so it is already a misplaced element for the right side.

The left pointer eventually finds a `1`.

The right pointer finds a `0`.

Swap them.

The process continues until all zeros are on the left and all ones are on the right.

Final result:

```text
[0, 0, 0, 1, 1, 1]
```

---

## Complexity

```text
Time Complexity  : O(n)
Space Complexity : O(1)
```

This approach does not create another array.

---

## Program

File:

```text
03_separate_zeros_ones_two_pointer.py
```

---

# Comparison of Three Approaches

| Approach    | Time Complexity | Space Complexity |
| ----------- | --------------: | ---------------: |
| Extra Array |            O(n) |             O(n) |
| Counting    |            O(n) |             O(1) |
| Two Pointer |            O(n) |             O(1) |

---

# Important Observation

All three approaches take:

```text
O(n)
```

time.

But their space requirements are different.

### Extra Array

```text
O(n) space
```

because another array is created.

### Counting

```text
O(1) space
```

because only counters are used.

### Two Pointer

```text
O(1) space
```

because only two pointers are used and the original array is modified.

---

# 2. Two Sum Problem

## Problem Statement

Given:

* An unordered integer array `arr`
* An integer `target`

Determine whether there exists a pair of elements whose sum is equal to the target.

Return:

```text
True
```

if such a pair exists.

Otherwise return:

```text
False
```

The faculty notes describe checking pairs of elements and returning true when their sum equals the target.

---

# Example 1

Input:

```text
arr = [2, 7, 11, 15]
target = 9
```

There is a pair:

```text
2 + 7 = 9
```

Output:

```text
True
```

---

# Example 2

Input:

```text
arr = [2, 7, 11, 15]
target = 20
```

Check the possible pairs.

No pair gives `20`.

Output:

```text
False
```

---

# Approach 1 - Two Sum Using Brute Force

## Idea

Check every possible pair.

Use two loops:

```text
i = 0 to n - 2
j = i + 1 to n - 1
```

For every pair, check:

```text
arr[i] + arr[j] == target
```

If the condition is true:

```text
return True
```

If all pairs are checked and no pair is found:

```text
return False
```

The faculty notes show this nested-loop approach.

---

## Algorithm

1. Start with the first element.
2. Compare it with every element after it.
3. Check whether their sum equals the target.
4. If yes, return `True`.
5. Move to the next element.
6. Continue checking all pairs.
7. If no pair is found, return `False`.

---

## Example

```text
arr = [2, 7, 11, 15]
target = 9
```

Check:

```text
2 + 7 = 9
```

Therefore:

```text
True
```

---

## Number of Possible Pairs

For `n` elements, the number of possible pairs is:

```text
nC2
```

Formula:

```text
nC2 = n! / (2! × (n-2)!)
```

Therefore:

```text
nC2 = n(n-1) / 2
```

This grows approximately as:

```text
O(n²)
```

Therefore the brute-force approach has quadratic time complexity.

---

## Complexity

```text
Time Complexity  : O(n²)
Space Complexity : O(1)
```

---

## Program

File:

```text
04_two_sum_bruteforce.py
```

---

# Approach 2 - Two Sum Using HashSet

## Idea

Instead of checking every possible pair, use a `set`.

For every element:

```text
complement = target - arr[i]
```

Then check whether the complement is already present in the set.

If the complement exists:

```text
True
```

Otherwise add the current element to the set.

---

# What is a Complement?

The complement is the value required to make the current element equal to the target.

Formula:

```text
complement = target - current_element
```

---

## Example

Consider:

```text
arr = [2, 7, 11, 15]
target = 9
```

### First Element

```text
current = 2
```

Calculate:

```text
complement = 9 - 2
           = 7
```

Check whether `7` exists in the set.

Initially:

```text
set = {}
```

`7` is not present.

Add `2`:

```text
set = {2}
```

---

### Second Element

```text
current = 7
```

Calculate:

```text
complement = 9 - 7
           = 2
```

Check the set:

```text
set = {2}
```

`2` exists.

Therefore a pair exists:

```text
2 + 7 = 9
```

Return:

```text
True
```

---

# Algorithm

1. Create an empty set.
2. Traverse the array.
3. Calculate:

```text
complement = target - arr[i]
```

4. Check whether the complement exists in the set.
5. If it exists, return `True`.
6. Otherwise add the current element to the set.
7. Continue until the array ends.
8. If no pair is found, return `False`.

---

# Why HashSet is Used

A Python `set` is an unordered collection of distinct elements.

Example:

```python
s = set()

s.add(10)
s.add(20)
s.add(10)

print(s)
```

The duplicate `10` is not stored twice.

The faculty notes define a set as an unordered collection of distinct elements.

---

# Complexity

```text
Time Complexity  : O(n)
Space Complexity : O(n)
```

The set may store up to `n` elements.

---

## Program

File:

```text
05_two_sum_hashset.py
```

---

# Two Sum Comparison

| Approach    | Time Complexity | Space Complexity |
| ----------- | --------------: | ---------------: |
| Brute Force |           O(n²) |             O(1) |
| HashSet     |            O(n) |             O(n) |

---

# Brute Force vs HashSet

## Brute Force

Advantages:

* Simple to understand.
* Does not require extra data structures.
* Uses constant extra space.

Disadvantages:

* Checks many pairs.
* Time complexity is `O(n²)`.

---

## HashSet

Advantages:

* Faster for large arrays.
* Time complexity is approximately `O(n)`.
* Avoids checking every possible pair.

Disadvantages:

* Requires extra memory.
* Space complexity is `O(n)`.

---

# 3. Two Pointer Technique - Key Concept

The Two Pointer Technique uses two indices/pointers to process an array efficiently.

Commonly:

```text
left  → beginning of array
right → end of array
```

The pointers are moved according to the problem conditions.

In today's Zero/One problem:

```text
left  → searches for misplaced 1
right → searches for misplaced 0
```

Then the misplaced values are swapped.

---

# Important Patterns Learned Today

## Pattern 1 - Two Pointers from Both Ends

```text
left = 0
right = n - 1
```

Use this pattern when elements from opposite ends need to be processed.

Example:

```text
Separating zeros and ones
```

---

## Pattern 2 - Complement + Set

For Two Sum:

```text
complement = target - arr[i]
```

Then:

```text
if complement in set:
    pair exists
```

Otherwise:

```text
set.add(arr[i])
```

---

# Time and Space Complexity Summary

| Problem            | Approach    |  Time | Space |
| ------------------ | ----------- | ----: | ----: |
| Separate 0s and 1s | Extra Array |  O(n) |  O(n) |
| Separate 0s and 1s | Counting    |  O(n) |  O(1) |
| Separate 0s and 1s | Two Pointer |  O(n) |  O(1) |
| Two Sum            | Brute Force | O(n²) |  O(1) |
| Two Sum            | HashSet     |  O(n) |  O(n) |

---

# Important Concepts to Remember

### 1. Binary Array

An array containing only:

```text
0 and 1
```

is called a binary array.

---

### 2. Two Pointers

Two pointers are indices used to process an array from different positions.

Example:

```text
left = 0
right = n - 1
```

---

### 3. Swap

Swapping exchanges the values of two positions.

Python:

```python
arr[left], arr[right] = arr[right], arr[left]
```

---

### 4. Set

A set is an unordered collection of distinct elements.

Example:

```python
s = set()
s.add(10)
s.add(20)
```

---

### 5. Complement

For Two Sum:

```text
complement = target - current_element
```

---

### 6. Brute Force

Brute force means checking all possible possibilities.

For Two Sum:

```text
Check every possible pair.
```

---

# Common Mistakes to Avoid

## Mistake 1

Using an extra array when the problem can be solved in-place with constant space.

---

## Mistake 2

Forgetting to move both pointers after swapping.

Correct:

```python
left += 1
right -= 1
```

---

## Mistake 3

For Two Sum, checking the current element against itself.

The HashSet approach avoids this by checking the complement before adding the current element.

---

## Mistake 4

Forgetting to break after finding a valid pair in the brute-force approach.

---

# Programs Created Today

```text
01_separate_zeros_ones_extra_array.py
02_separate_zeros_ones_counting.py
03_separate_zeros_ones_two_pointer.py
04_two_sum_bruteforce.py
05_two_sum_hashset.py
```

---

# Folder Structure

```text
Day-13/
│
├── README.md
│
├── 01_separate_zeros_ones_extra_array.py
│
├── 02_separate_zeros_ones_counting.py
│
├── 03_separate_zeros_ones_two_pointer.py
│
├── 04_two_sum_bruteforce.py
│
└── 05_two_sum_hashset.py
```

---

# Day 13 Learning Summary

Today I learned how to solve the problem of separating zeros and ones using three different approaches:

```text
1. Extra Array
2. Counting
3. Two Pointer
```

I also learned the Two Sum problem using:

```text
1. Brute Force
2. HashSet
```

The main lesson from today's class was that the same problem can have multiple solutions, but the best solution depends on both:

```text
Time Complexity
Space Complexity
```

For separating zeros and ones, the Two Pointer approach achieves:

```text
Time  : O(n)
Space : O(1)
```

For Two Sum, the HashSet approach improves the time complexity from:

```text
Brute Force : O(n²)
```

to approximately:

```text
HashSet : O(n)
```

at the cost of:

```text
O(n)
```

extra space.

---

# Key Takeaways

```text
✓ Learned Two Pointer Technique
✓ Learned how to separate 0s and 1s
✓ Learned Extra Array approach
✓ Learned Counting approach
✓ Learned Two Pointer approach
✓ Learned Two Sum problem
✓ Learned Brute Force approach
✓ Learned HashSet approach
✓ Learned Complement concept
✓ Learned Set concept
✓ Compared Time Complexity
✓ Compared Space Complexity
✓ Practiced Python implementations
```

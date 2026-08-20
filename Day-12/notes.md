# DSA Class 12 - Two Pointer Technique

## 1. Two Pointer Technique

Two Pointer Technique is an optimization method where we use two indices/pointers to traverse data structures like arrays, strings, or linked lists efficiently.

Instead of using nested loops with `O(n²)` time complexity, many problems can be solved in `O(n)` time using two pointers.

The two pointers are moved according to the requirement of the problem.

---

## 2. Types of Two Pointer Technique

There are two main types of the Two Pointer Technique:

### Type 1 - Opposite Direction

In this type, both pointers move in opposite directions.

One pointer starts from the beginning and the other pointer starts from the end.

Example:

```text
left →              ← right

[ 1 ][ 3 ][ 7 ][ 4 ][ 5 ]
```

For an array:

```text
left = 0
right = n - 1
```

The `left` pointer moves towards the right and the `right` pointer moves towards the left.

This type of two-pointer technique can be used for:

* Array problems
* String problems
* Reversing an array
* Palindrome problems

---

### Type 2 - Same Direction

In this type, both pointers move in the same direction.

Example:

```text
i →
j →

[ 1 ][ 3 ][ 7 ][ 4 ][ 5 ]
```

Both pointers start from the beginning and move towards the end according to the problem requirement.

---

## 3. Applications of Two Pointer Technique

The Two Pointer Technique can be used to solve:

* Array problems
* String problems
* Linked List problems

It is especially useful when two positions in a data structure need to be tracked at the same time.

---

# 4. Problem - Reverse Array

Given an array of integers, reverse the array.

### Example

Input:

```text
[1, 3, 7, 4, 5]
```

Output:

```text
[5, 4, 7, 3, 1]
```

There are different ways to reverse an array.

---

# 5. Reverse Array Using an Extra Array

When we know the size of the array, we can create another array of the same size.

Example:

```text
n = 5

res = new Array(n)
```

Then we traverse the original array from the last element to the first element and store the elements in the new array.

For example:

```text
Original Array:

[1][3][7][4][5]

Reversed Array:

[5][4][7][3][1]
```

### Algorithm

1. Create a result array of size `n`.
2. Set `j = 0`.
3. Traverse the original array from `n - 1` to `0`.
4. Store each element in the result array.
5. Increment `j`.
6. Return the result array.

### Complexity

```text
Time Complexity = O(n)
Space Complexity = O(n)
```

The space complexity is `O(n)` because an extra array is created.

---

# 6. Reverse Array Using Two Pointers

An array can also be reversed in-place using the Two Pointer Technique.

Initialize:

```text
left = 0
right = n - 1
```

Example:

```text
[1][3][7][4][5]
 ↑           ↑
left        right
```

While:

```text
left < right
```

swap the elements at `left` and `right`.

### Swap

```text
temp = arr[left]
arr[left] = arr[right]
arr[right] = temp
```

Then move the pointers:

```text
left++
right--
```

Continue until `left` is no longer less than `right`.

---

## 7. Example of Two Pointer Array Reversal

Initial array:

```text
[1][3][7][4][5]
 ↑           ↑
left        right
```

First swap:

```text
[5][3][7][4][1]
    ↑       ↑
   left    right
```

Second swap:

```text
[5][4][7][3][1]
       ↑
   pointers meet
```

Final reversed array:

```text
[5][4][7][3][1]
```

---

## 8. Algorithm for In-Place Array Reversal

1. Set `left = 0`.
2. Set `right = n - 1`.
3. Repeat while `left < right`.
4. Swap `arr[left]` and `arr[right]`.
5. Increment `left`.
6. Decrement `right`.
7. Return the array.

### Complexity

```text
Time Complexity = O(n)
Space Complexity = O(1)
```

Only a temporary variable is required for swapping, so no extra array is created.

---

# 9. Comparison of Both Array Reversal Approaches

| Approach     | Time Complexity | Space Complexity |
| ------------ | --------------- | ---------------- |
| Extra Array  | O(n)            | O(n)             |
| Two Pointers | O(n)            | O(1)             |

Both approaches take `O(n)` time, but the Two Pointer Technique is more space efficient because it reverses the original array in-place.

---

# 10. Upper Bound and Lower Bound

When the upper bound and lower bound of an algorithm are the same:

```text
O(n), Ω(n) → Θ(n)
```

Therefore, the time complexity can be represented as:

```text
Θ(n)
```

This means the algorithm has a linear growth rate.

---

# 11. Palindrome

A palindrome is a string that reads the same from the beginning and from the end.

Examples:

```text
madam
level
racecar
```

These strings are palindromes.

Example of a string that is not a palindrome:

```text
hello
```

---

# 12. Check Whether a String is a Palindrome Using Two Pointers

We can use two pointers to check whether a string is a palindrome.

Initialize:

```text
left = 0
right = str.length - 1
```

Example:

```text
m a d a m
↑       ↑
left   right
```

Compare the characters at `left` and `right`.

If they are different:

```text
return false
```

If they are equal:

```text
left++
right--
```

Continue until:

```text
left < right
```

becomes false.

If all corresponding characters are equal, return:

```text
true
```

---

# 13. Palindrome Algorithm

1. Set `left = 0`.
2. Set `right = str.length - 1`.
3. While `left < right`:

   * Compare `str[left]` and `str[right]`.
   * If they are not equal, return `false`.
   * Increment `left`.
   * Decrement `right`.
4. If all characters match, return `true`.

---

# 14. Palindrome Example

String:

```text
madam
```

First comparison:

```text
m a d a m
↑       ↑

m == m
```

Move the pointers:

```text
m a d a m
  ↑   ↑

a == a
```

Move the pointers again:

```text
m a d a m
    ↑

d
```

All corresponding characters match.

Therefore:

```text
true
```

---

# 15. Palindrome Complexity

For a string of length `n`:

```text
Time Complexity = O(n)
Space Complexity = O(1)
```

The string is checked using two pointers without creating another array.

---

# 16. Key Points to Remember

* Two Pointer Technique is an optimization technique.
* It uses two indices/pointers to traverse a data structure.
* It can be used with arrays, strings, and linked lists.
* There are two main types:

  * Opposite Direction
  * Same Direction
* In the opposite-direction approach, one pointer starts from the beginning and the other starts from the end.
* Two pointers can be used to reverse an array.
* An array can be reversed in-place using two pointers.
* In-place array reversal requires `O(1)` extra space.
* Two pointers can also be used to check whether a string is a palindrome.
* Many problems that require nested loops can be optimized using the Two Pointer Technique.
* The goal of the technique is to improve time or space efficiency depending on the problem.

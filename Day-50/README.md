# Day 50 — DSA Learning

## Topic: Recursion 

### Concepts Covered
- Reverse a string using recursion.
- Find the maximum element in an array using recursion.
- Understand divide and conquer.
- Divide an array until each subarray contains one element.
- Combine the results using the maximum operation.

### 1. Reverse a String Using Recursion

**Approach:**
- Start from the last character of the string.
- Add the current character to the result.
- Recursively process the previous character.
- Stop when the index becomes less than zero.

**Base Case:** Index is less than zero.

**Example:**
- Input: `hello`
- Output: `olleh`

### 2. Find Maximum Element Using Recursion

**Approach:**
- Start from the last index of the array.
- Compare the current element with the maximum of the remaining elements.
- Return the larger value.
- Stop when only the first element remains.

**Base Case:** Index becomes zero.

**Example:**
- Input: `[10, 25, 7, 40, 15]`
- Output: `40`

### 3. Find Maximum Using Divide and Conquer

**Approach:**
- Divide the array into two halves.
- Continue dividing until each part contains one element.
- Find the maximum of the left half.
- Find the maximum of the right half.
- Combine both results using `max(left_max, right_max)`.

**Base Case:** A subarray contains one element.

**Example:**
- Input: `[12, 5, 30, 18, 9]`
- Output: `30`

### Time and Space Complexity

| Problem | Time Complexity | Auxiliary Space |
|---|---|---|
| Reverse string using recursion | O(n) | O(n) |
| Maximum using index recursion | O(n) | O(n) |
| Maximum using divide and conquer | O(n) | O(log n) |

Here, `n` is the number of characters or array elements. The divide-and-conquer space complexity assumes balanced splitting and excludes the input array.

### Key Takeaways
- Every recursive solution needs a base case.
- Each recursive call should move toward the base case.
- Recursion can process strings and arrays.
- Divide and conquer solves smaller subproblems and combines their results.

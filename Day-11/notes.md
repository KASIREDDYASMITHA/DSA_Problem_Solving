# Day 11 — Time Complexity and Space Complexity

## 1. Time Complexity

Time Complexity describes how the running time of an algorithm grows with respect to the input size `n`.

We usually express time complexity using **Big-O notation**.

Examples:

* `O(1)` → Constant time
* `O(log n)` → Logarithmic time
* `O(n)` → Linear time
* `O(n log n)` → Linearithmic time
* `O(n²)` → Quadratic time

The goal is not to calculate the exact running time in seconds.

The goal is to understand how the number of operations grows when the input size increases.

---

# 2. Common Time Complexities

## O(1) — Constant Time

The number of operations does not depend on the input size.

Example:

```cpp
int x = 10;
cout << x;
```

Even if `n` becomes very large, the number of operations remains approximately constant.

Therefore:

```text
Time Complexity = O(1)
```

---

## O(n) — Linear Time

The algorithm performs work proportional to `n`.

Example:

```cpp
for(int i = 0; i < n; i++)
{
    cout << i << " ";
}
```

The loop runs approximately `n` times.

Therefore:

```text
Time Complexity = O(n)
```

---

## O(n²) — Quadratic Time

A loop inside another loop often gives `O(n²)`.

Example:

```cpp
for(int i = 0; i < n; i++)
{
    for(int j = 0; j < n; j++)
    {
        cout << "Hello";
    }
}
```

Outer loop:

```text
n times
```

Inner loop:

```text
n times
```

Total:

```text
n × n = n²
```

Therefore:

```text
Time Complexity = O(n²)
```

---

# 3. O(log n) — Logarithmic Time

When the loop variable increases or decreases exponentially, the complexity can become `O(log n)`.

Example:

```cpp
for(int i = 1; i <= n; i = i * 2)
{
    cout << i << " ";
}
```

Values of `i`:

```text
1
2
4
8
16
32
...
```

After `k` iterations:

```text
i = 2^k
```

When `i` reaches `n`:

```text
2^k = n
```

Taking log base 2:

```text
k = log₂(n)
```

Therefore:

```text
Time Complexity = O(log n)
```

Another common form:

```cpp
for(int i = n; i >= 1; i = i / 2)
{
    cout << i << " ";
}
```

This is also:

```text
O(log n)
```

---

# 4. O(n log n)

If an `O(log n)` loop is executed `n` times, the overall complexity becomes:

```text
O(n log n)
```

Example:

```cpp
for(int i = 0; i < n; i++)
{
    for(int j = 1; j <= n; j = j * 2)
    {
        cout << "Hello";
    }
}
```

Outer loop:

```text
O(n)
```

Inner loop:

```text
O(log n)
```

Therefore:

```text
O(n) × O(log n)
= O(n log n)
```

---

# 5. Nested Loop — Important Rule

For nested loops, determine how many times each loop executes.

Example:

```cpp
for(int i = 1; i <= n; i++)
{
    for(int j = 1; j <= n; j = j * 2)
    {
        cout << "Hello";
    }
}
```

Outer loop:

```text
n iterations
```

Inner loop:

```text
log₂(n) iterations
```

Therefore:

```text
T.C = O(n log n)
```

---

# 6. Geometric Progression in Time Complexity

A geometric progression can appear when the number of iterations grows like:

```text
1 + 2 + 4 + 8 + 16 + ...
```

The sum of a geometric progression is:

```text
Sₙ = a(rⁿ - 1) / (r - 1)
```

For:

```text
a = 1
r = 2
```

we get:

```text
Sₙ = 1 + 2 + 4 + 8 + ... + 2ᵏ
```

The sum is:

```text
2^(k+1) - 1
```

Ignoring constants:

```text
O(2ᵏ)
```

If:

```text
2ᵏ = n
```

then:

```text
k = log₂(n)
```

Therefore:

```text
2ᵏ = n
```

So the total becomes:

```text
O(n)
```

---

# 7. Example: O(n) from Increasing Inner Loop

Consider:

```cpp
for(int i = 1; i <= n; i = i * 2)
{
    for(int j = 1; j <= i; j++)
    {
        cout << "Hello";
    }
}
```

Values of `i` are:

```text
1, 2, 4, 8, 16, ...
```

The inner loop executes:

```text
1 + 2 + 4 + 8 + ... + n
```

This is a geometric progression.

The sum is approximately:

```text
2n - 1
```

Ignoring constants:

```text
O(n)
```

Therefore:

```text
Time Complexity = O(n)
```

---

# 8. Important Difference: Sequential vs Nested Loops

## Sequential loops

Example:

```cpp
for(int i = 0; i < n; i++)
{
    cout << i;
}

for(int j = 0; j < n; j++)
{
    cout << j;
}
```

Complexity:

```text
O(n) + O(n)
= O(2n)
= O(n)
```

Constants are ignored in Big-O.

---

## Nested loops

Example:

```cpp
for(int i = 0; i < n; i++)
{
    for(int j = 0; j < n; j++)
    {
        cout << "Hello";
    }
}
```

Complexity:

```text
O(n) × O(n)
= O(n²)
```

So:

```text
Sequential → Add
Nested → Multiply
```

---

# 9. Space Complexity

Space Complexity is the amount of memory used by an algorithm with respect to the input size `n`.

It tells us:

* How much extra memory the program needs.
* How memory usage grows when input size increases.

---

# 10. Types of Memory Used

Total memory used by a program can involve:

1. Input Space
2. Auxiliary Space

---

# 11. Input Space

Input space is the memory required to store the input.

Example:

```cpp
int arr[n];
```

The array itself stores the input.

In many interview discussions, input space is considered separately from auxiliary space.

---

# 12. Auxiliary Space

Auxiliary space is the extra memory used by the algorithm apart from the input.

This is usually the space complexity we focus on when analyzing an algorithm.

Examples of auxiliary memory:

* Variables
* Extra arrays
* HashMap
* HashSet
* Stack
* Queue
* Recursion stack
* Other dynamically allocated memory

---

# 13. O(1) Space Complexity

If the algorithm uses only a fixed number of variables regardless of input size, its auxiliary space is:

```text
O(1)
```

Example:

```cpp
int sum = 0;

for(int i = 0; i < n; i++)
{
    sum += arr[i];
}
```

The array `arr` is the input.

The algorithm only uses:

```text
sum
i
```

These are constant extra variables.

Therefore:

```text
Auxiliary Space = O(1)
```

---

# 14. Extra Array — O(n) Space

If we create an additional array of size `n`:

```cpp
int temp[n];
```

then the extra memory grows with `n`.

Therefore:

```text
Auxiliary Space = O(n)
```

---

# 15. 2D Array — O(n²) Space

If we create a 2D array:

```cpp
int matrix[n][n];
```

Number of elements:

```text
n × n = n²
```

Therefore:

```text
Space Complexity = O(n²)
```

---

# 16. HashMap — O(n) Space

If we create a HashMap and store `n` elements:

```cpp
unordered_map<int, int> mp;
```

and the map stores approximately `n` elements, the additional space is:

```text
O(n)
```

---

# 17. HashSet — O(n) Space

If we create a HashSet and store `n` elements:

```cpp
unordered_set<int> st;
```

then the auxiliary space is:

```text
O(n)
```

---

# 18. Stack / Queue — O(n) Space

If we create a new stack or queue and store `n` elements:

```cpp
stack<int> st;
```

or:

```cpp
queue<int> q;
```

then:

```text
Auxiliary Space = O(n)
```

---

# 19. Recursion Stack

Recursion uses memory for function calls.

Each recursive call creates a stack frame.

Example:

```cpp
void fun(int n)
{
    if(n == 0)
        return;

    fun(n - 1);
}
```

There are approximately `n` recursive calls.

Therefore:

```text
Recursion Stack Space = O(n)
```

Recursion is one of the common reasons for additional space usage.

---

# 20. O(log n) Space

Some recursive divide-and-conquer algorithms create recursion depth of `log n`.

Example idea:

```text
n
n/2
n/4
n/8
...
1
```

The number of levels is:

```text
O(log n)
```

Therefore:

```text
Recursion Stack Space = O(log n)
```

---

# 21. O(n²) Space

`O(n²)` auxiliary space commonly occurs when we create structures such as:

* `n × n` matrices
* DP tables of size `n × n`
* Graph adjacency matrices

Example:

```cpp
int dp[n][n];
```

Therefore:

```text
Space Complexity = O(n²)
```

---

# 22. Common Sources of O(n) Space

The following commonly require `O(n)` additional space when they store `n` elements:

### 1. Creating a HashMap

```text
O(n)
```

### 2. Creating a HashSet

```text
O(n)
```

### 3. Creating a new array of size n

```text
O(n)
```

### 4. Creating a new Stack or Queue of size n

```text
O(n)
```

### 5. Recursion stack of depth n

```text
O(n)
```

---

# 23. Common Sources of O(n²) Space

Common examples include:

### 1. Matrix

```cpp
int matrix[n][n];
```

```text
O(n²)
```

### 2. DP Table

```cpp
int dp[n][n];
```

```text
O(n²)
```

### 3. Graph Adjacency Matrix

For `n` vertices:

```text
O(n²)
```

---

# 24. Example: O(1) Space

```cpp
int sum = 0;

for(int i = 0; i < n; i++)
{
    sum += arr[i];
}
```

Extra variables:

```text
sum
i
```

The number of variables does not increase with `n`.

Therefore:

```text
Auxiliary Space = O(1)
```

---

# 25. Example: O(n) Space

```cpp
int temp[n];

for(int i = 0; i < n; i++)
{
    temp[i] = arr[i];
}
```

An additional array of size `n` is created.

Therefore:

```text
Auxiliary Space = O(n)
```

---

# 26. Example: O(n²) Space

```cpp
int matrix[n][n];

for(int i = 0; i < n; i++)
{
    for(int j = 0; j < n; j++)
    {
        matrix[i][j] = 0;
    }
}
```

The matrix contains:

```text
n² elements
```

Therefore:

```text
Auxiliary Space = O(n²)
```

---

# 27. Important Interview Questions

## Question 1

What is the space complexity of:

```cpp
int sum = 0;

for(int i = 0; i < n; i++)
{
    sum += arr[i];
}
```

Answer:

```text
O(1)
```

Reason:

Only constant extra variables are used.

---

## Question 2

What is the space complexity of an extra array of size `n`?

Answer:

```text
O(n)
```

---

## Question 3

What is the space complexity of a 2D array of size `n × n`?

Answer:

```text
O(n²)
```

---

## Question 4

What is the space complexity of recursion with depth `n`?

Answer:

```text
O(n)
```

Because every recursive call requires a stack frame.

---

## Question 5

What is the space complexity of a recursion tree/depth of `log n`?

Answer:

```text
O(log n)
```

---

# 28. Important Rule for Space Complexity

When analyzing auxiliary space, ask:

> "What extra memory is being created as input size increases?"

For example:

```text
Only variables
→ O(1)

Extra array of size n
→ O(n)

HashMap storing n elements
→ O(n)

Stack/Queue storing n elements
→ O(n)

Recursion depth n
→ O(n)

2D matrix n × n
→ O(n²)

DP table n × n
→ O(n²)
```

---

# 29. Time Complexity vs Space Complexity

## Time Complexity

Measures how the number of operations grows with input size.

Example:

```text
Loop from 1 to n
→ O(n)
```

## Space Complexity

Measures how extra memory grows with input size.

Example:

```text
Extra array of size n
→ O(n)
```

---

# 30. Quick Revision Table

| Situation                      | Complexity |
| ------------------------------ | ---------- |
| Single operation               | O(1)       |
| Single loop up to n            | O(n)       |
| Loop dividing/multiplying by 2 | O(log n)   |
| Nested n × n loops             | O(n²)      |
| n loops × log n loop           | O(n log n) |
| Extra variable                 | O(1)       |
| Extra array of size n          | O(n)       |
| HashMap with n elements        | O(n)       |
| HashSet with n elements        | O(n)       |
| Stack/Queue with n elements    | O(n)       |
| Recursion depth n              | O(n)       |
| n × n matrix                   | O(n²)      |
| n × n DP table                 | O(n²)      |
| n × n adjacency matrix         | O(n²)      |

---

# 31. Key Rules to Remember

### Rule 1

Ignore constants.

```text
O(2n) → O(n)
O(5n) → O(n)
O(100n) → O(n)
```

### Rule 2

For sequential code, add complexities.

```text
O(n) + O(n)
= O(2n)
= O(n)
```

### Rule 3

For nested loops, multiply when the iteration counts are independent.

```text
O(n) × O(n)
= O(n²)
```

### Rule 4

If a loop doubles or halves its value:

```text
i = i * 2
```

or:

```text
i = i / 2
```

think:

```text
O(log n)
```

### Rule 5

Extra array/hashmap/hashset/stack/queue containing `n` elements generally means:

```text
O(n) auxiliary space
```

### Rule 6

A recursion stack must be counted in auxiliary space.

---

# 32. Day 11 Summary

Today's main topics:

* Time Complexity
* Big-O notation
* O(1)
* O(log n)
* O(n)
* O(n log n)
* O(n²)
* Nested loops
* Sequential loops
* Geometric Progression
* Logarithmic loops
* Space Complexity
* Input Space
* Auxiliary Space
* Extra arrays
* 2D arrays
* HashMap
* HashSet
* Stack
* Queue
* Recursion Stack
* DP tables
* Graph adjacency matrices

The main goal is to determine:

```text
1. How much time does the algorithm take as n increases?
2. How much extra memory does the algorithm require as n increases?
```

---

## Day 11 Quick Formula Sheet

```text
1 + 1 + 1 + ... + 1 (n times)
= O(n)

1 + 2 + 3 + ... + n
= n(n + 1) / 2
= O(n²)

1 + 2 + 4 + 8 + ... + n
= O(n)

1 + 2 + 4 + 8 + ... + 2^k
= O(2^k)

2^k = n
=> k = log₂n

Therefore:
number of iterations = O(log n)
```

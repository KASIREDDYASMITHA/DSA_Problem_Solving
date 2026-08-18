# Day 10 - Detailed Notes

## 1. Time Complexity

Time Complexity is used to describe how the running time of an algorithm grows with respect to the input size `n`.

Instead of measuring the exact time in seconds, we count the number of basic operations performed by the algorithm.

We represent this using asymptotic notation such as:

```text
O(1)
O(log n)
O(√n)
O(n)
O(n log n)
O(n²)
O(2ⁿ)
O(n!)
```

---

# 2. Big-O Notation

Big-O notation represents an upper bound on the growth of an algorithm's running time.

For DSA, it is commonly used to describe how an algorithm behaves as `n` becomes large.

Example:

```text
3n + 5
```

The constant `3` and constant `5` are ignored for asymptotic growth.

Therefore:

```text
O(3n + 5) = O(n)
```

---

# 3. Growth Order of Functions

The functions discussed in class can be arranged from slower growth to faster growth:

```text
O(1)
< O(log n)
< O(√n)
< O(n)
< O(n log n)
< O(n²)
< O(2ⁿ)
< O(n!)
```

The larger the growth rate, the more expensive the algorithm becomes for large values of `n`.

---

# 4. O(1) - Constant Complexity

If an operation executes a fixed number of times regardless of `n`, its complexity is constant.

Example:

```python
print("hello")
```

Complexity:

```text
O(1)
```

---

# 5. O(log n) - Logarithmic Complexity

If the input size is repeatedly divided or the loop variable is repeatedly multiplied by a constant, the complexity is logarithmic.

Example pattern:

```text
n
n/2
n/4
n/8
...
1
```

The number of iterations is approximately:

```text
log₂ n
```

Therefore:

```text
O(log n)
```

Example:

```python
i = n

while i >= 1:
    print("hello")
    i = i // 2
```

The faculty notes also demonstrate a loop where `i` is repeatedly reduced by half.

---

# 6. O(√n) - Square Root Complexity

If a loop runs approximately `√n` times:

```text
O(√n)
```

Example:

```python
for i in range(int(n ** 0.5)):
    print("hello")
```

The faculty notes include this `√n` loop pattern.

---

# 7. O(n) - Linear Complexity

If a loop runs `n` times:

```text
O(n)
```

Example:

```python
for i in range(1, n + 1):
    print("hello")
```

Even if the loop increments by 2:

```python
for i in range(1, n + 1, 2):
    print("hello")
```

the complexity remains:

```text
O(n)
```

because constant factors are ignored.

The faculty notes include both ordinary increment and increment-by-2 examples.

---

# 8. O(n²) - Quadratic Complexity

Two independent loops, each running `n` times:

```python
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print("hello")
```

Number of operations:

```text
n × n
= n²
```

Therefore:

```text
O(n²)
```

The faculty notes explicitly demonstrate this nested-loop multiplication approach.

---

# 9. Dependent Nested Loop

Consider:

```python
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("hello")
```

For:

```text
i = 1 → 1 operation
i = 2 → 2 operations
i = 3 → 3 operations
...
i = n → n operations
```

Total:

```text
1 + 2 + 3 + ... + n
```

Using:

```text
n(n + 1) / 2
```

we get:

```text
O(n²)
```

---

# 10. O(n log n)

Consider:

```python
for i in range(1, n + 1):
    for j in range(i, n + 1):
        print("hello")
```

For each value of `i`, the inner loop performs approximately:

```text
n/i
```

operations.

Therefore:

```text
n/1 + n/2 + n/3 + ... + n/n
```

Taking `n` common:

```text
n(1 + 1/2 + 1/3 + ... + 1/n)
```

The harmonic sum grows as:

```text
log n
```

Therefore:

```text
O(n log n)
```

---

# 11. Dominant Term

When multiple terms are present, the term with the highest growth rate dominates.

Example:

```text
n² + n³
```

Compare:

```text
n²
n³
```

`n³` grows faster.

Therefore:

```text
n² + n³ = O(n³)
```

Another example:

```text
n³ + n² + n + 10
```

The dominant term is:

```text
n³
```

Therefore:

```text
O(n³)
```

---

# 12. Important Theorem

If `f(n)` and `g(n)` are asymptotically non-negative functions, then:

```text
f(n) + g(n) = O(max(f(n), g(n)))
```

This means that when adding two functions, the function with the larger growth rate determines the final Big-O complexity.

Example:

```text
f(n) = n²
g(n) = n³
```

Then:

```text
f(n) + g(n)
= n² + n³
= O(n³)
```

---

# 13. Nested Loop Analysis Rules

### Case 1: Independent nested loops

```python
for i in range(n):
    for j in range(n):
        # O(1)
        pass
```

Complexity:

```text
O(n × n)
= O(n²)
```

---

### Case 2: Dependent inner loop

```python
for i in range(1, n + 1):
    for j in range(1, i + 1):
        # O(1)
        pass
```

Complexity:

```text
1 + 2 + 3 + ... + n
= n(n + 1)/2
= O(n²)
```

---

### Case 3: Inner loop depends on `i`

```python
for i in range(1, n + 1):
    for j in range(i, n + 1):
        # O(1)
        pass
```

Complexity:

```text
O(n log n)
```

---

# 14. Important Observations

### Constant increment

```text
i = i + 1
i = i + 2
i = i + 5
```

These remain:

```text
O(n)
```

---

### Multiplication/division

```text
i = i × 2
```

or

```text
i = i / 2
```

generally produces:

```text
O(log n)
```

---

### Nested loops

For independent loops:

```text
O(n) × O(n)
= O(n²)
```

---

### Sequential operations

For:

```text
O(n) + O(n²)
```

the dominant term is:

```text
O(n²)
```

---

# 15. Quick Complexity Table

| Pattern                         | Complexity |
| ------------------------------- | ---------- |
| Single statement                | O(1)       |
| Loop runs fixed number of times | O(1)       |
| Loop from 1 to n                | O(n)       |
| Loop increasing by constant     | O(n)       |
| Loop repeatedly dividing by 2   | O(log n)   |
| Loop up to √n                   | O(√n)      |
| Two independent n loops         | O(n²)      |
| Dependent loop: 1 + 2 + ... + n | O(n²)      |
| `n(1 + 1/2 + ... + 1/n)`        | O(n log n) |

---

# 16. Day 10 Summary

Today I learned how to analyze the time complexity of different programs by counting their iterations.

The main concepts I practiced were:

* Big-O notation
* Growth rates
* Constant complexity
* Logarithmic complexity
* Square-root complexity
* Linear complexity
* Linearithmic complexity
* Quadratic complexity
* Nested loops
* Dependent loops
* Dominant terms
* Sum of asymptotically non-negative functions

The main idea I learned:

> Do not focus on the exact number of operations. Focus on how the number of operations grows when `n` becomes large.

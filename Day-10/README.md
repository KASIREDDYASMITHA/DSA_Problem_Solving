# Day 10 - Time and Space Complexity

## 📚 Topic

**Data Structures and Algorithms - Time and Space Complexity**

Today I learned how to analyze the efficiency of algorithms using:

* Time Complexity
* Asymptotic Analysis
* Big-O notation
* Growth of functions
* Loop analysis
* Nested loop analysis
* Logarithmic loops
* Dependent nested loops
* Dominant terms

---

## 🎯 Learning Objectives

By the end of Day 10, I learned how to:

* Understand the time taken by an algorithm as input size increases.
* Calculate the number of times a loop executes.
* Analyze single loops and nested loops.
* Identify logarithmic, linear, quadratic, and linearithmic complexities.
* Find the dominant term in an expression.
* Compare functions according to their growth rate.
* Apply Big-O notation to represent algorithmic complexity.

---

## 🧠 Topics Covered

### 1. Time Complexity

Time complexity describes how the running time of an algorithm grows as the input size `n` increases.

We usually represent time complexity using **Big-O notation**.

Examples:

```text
O(1)       → Constant
O(log n)   → Logarithmic
O(√n)      → Square Root
O(n)       → Linear
O(n log n) → Linearithmic
O(n²)      → Quadratic
O(2ⁿ)      → Exponential
O(n!)      → Factorial
```

---

### 2. Growth Rate

The growth rate of functions can be arranged from slower growth to faster growth as:

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

As `n` becomes larger, functions with faster growth become significantly more expensive.

---

### 3. Dominant Term

When an expression contains multiple terms, the term with the highest growth rate dominates the overall complexity.

For example:

```text
n² + n³
```

Since `n³` grows faster than `n²`:

```text
n² + n³ = O(n³)
```

Therefore, we keep the dominant term.

---

### 4. Sum of Functions

If `f(n)` and `g(n)` are asymptotically non-negative functions:

```text
f(n) + g(n) = O(max(f(n), g(n)))
```

Example:

```text
n² + n³ = O(n³)
```

because `n³` is the dominant term.

---

### 5. Loop Analysis

The number of iterations of a loop determines its time complexity.

Examples:

```python
for i in range(1, n + 1):
    print("hello")
```

Time Complexity:

```text
O(n)
```

A loop that increases by a constant amount such as `i = i + 2` is also linear:

```text
O(n)
```

---

### 6. Logarithmic Loop

When the loop variable is repeatedly divided by a constant, the number of iterations is logarithmic.

Example:

```text
n → n/2 → n/4 → n/8 → ...
```

Therefore:

```text
O(log n)
```

---

### 7. Square Root Loop

A loop that executes up to `√n` times has:

```text
O(√n)
```

Example:

```python
for i in range(int(n ** 0.5)):
    print("hello")
```

---

### 8. Nested Loops

If two independent loops each run `n` times:

```python
for i in range(n):
    for j in range(n):
        print("hello")
```

The total number of operations is:

```text
n × n = n²
```

Therefore:

```text
O(n²)
```

The faculty notes also use nested loops to demonstrate this multiplication approach.

---

### 9. Dependent Nested Loops

Consider:

```python
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("hello")
```

The inner loop executes:

```text
1 + 2 + 3 + ... + n
```

Using the sum formula:

```text
n(n + 1) / 2
```

Therefore:

```text
O(n²)
```

---

### 10. Inner Loop Depending on Outer Loop

Example:

```python
for i in range(1, n + 1):
    for j in range(i, n + 1):
        print("hello")
```

The inner loop executes approximately:

```text
n/i
```

times for each value of `i`.

Therefore the total becomes related to:

```text
n(1 + 1/2 + 1/3 + ... + 1/n)
```

which gives:

```text
O(n log n)
```

---

## 📝 Key Rules Learned

### Rule 1: Ignore Constants

```text
O(5n) = O(n)
O(100n) = O(n)
```

### Rule 2: Keep the Dominant Term

```text
O(n² + n) = O(n²)
O(n³ + n² + n) = O(n³)
```

### Rule 3: Sequential Loops Add

```text
O(n) + O(n) = O(n)
```

### Rule 4: Nested Independent Loops Multiply

```text
O(n) × O(n) = O(n²)
```

### Rule 5: Multiplication/Division of Loop Variable Often Produces Logarithmic Complexity

```text
i = i × 2
```

or

```text
i = i / 2
```

generally gives:

```text
O(log n)
```

---

## 💡 Day 10 Takeaway

Today I learned that analyzing an algorithm is not only about whether the program produces the correct output. We also need to understand how efficiently it runs as the input size increases.

The most important skill I practiced today was identifying the number of loop iterations and converting that into Big-O notation.

### Important Growth Order

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


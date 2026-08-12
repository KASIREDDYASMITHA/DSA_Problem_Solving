# DSA Day 04 Notes

## Topic 1: Power of Two Check

A number is said to be a power of 2 if it can be represented as:

```text
2^n
```

where:

```text
n >= 0
```

### Examples

```text
2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
```

Therefore:

```text
1, 2, 4, 8, 16, 32, 64...
```

are powers of 2.

---

## Important Observation

Every power of 2 except `1` is an even number.

But every even number is NOT necessarily a power of 2.

### Example 1

```text
8
```

8 is even and:

```text
8 = 2^3
```

Therefore, 8 is a power of 2.

### Example 2

```text
10
```

10 is even, but it cannot be represented as `2^n`.

Therefore, 10 is not a power of 2.

---

## Approach

The approach used in class is:

1. Check whether `n <= 0`.
2. If yes, return false / print that it is not a power of 2.
3. While `n % 2 == 0`, divide `n` by 2.
4. After the loop, check whether `n == 1`.
5. If `n == 1`, the original number is a power of 2.
6. Otherwise, it is not a power of 2.

---

## Why `n % 2 == 0`?

The `%` operator gives the remainder.

For example:

```text
8 % 2 = 0
16 % 2 = 0
10 % 2 = 0
7 % 2 = 1
```

Therefore:

```python
n % 2 == 0
```

means the number is divisible by 2.

---

## Why divide by 2 repeatedly?

Suppose:

```text
n = 16
```

We repeatedly divide by 2:

```text
16 / 2 = 8
8 / 2 = 4
4 / 2 = 2
2 / 2 = 1
```

We finally get:

```text
1
```

Therefore, 16 is a power of 2.

Now consider:

```text
n = 12
```

```text
12 / 2 = 6
6 / 2 = 3
```

Now 3 is not divisible by 2.

Since the final value is not 1:

```text
12 is not a power of 2
```

---

# Topic 2: Pattern Printing

Pattern printing is used to practice:

- `for` loops
- nested loops
- rows
- columns
- string construction
- controlling the number of elements printed

---

# Pattern 1: Stars in a Single Line

### Example

For:

```text
n = 5
```

Output:

```text
*****
```

### Logic

Start with an empty string:

```python
s = ""
```

Add one star during every iteration:

```python
s = s + "*"
```

After 5 iterations:

```text
*****
```

---

# Pattern 2: Square Pattern

For:

```text
n = 4
```

Output:

```text
****
****
****
****
```

### Logic

There are 4 rows.

Every row contains 4 stars.

Therefore:

```text
Rows = n
Stars in each row = n
```

This requires nested loops.

The outer loop controls rows.

The inner loop controls stars.

---

# Pattern 3: Right-Angled Star Triangle

For:

```text
n = 5
```

Output:

```text
*
**
***
****
*****
```

### Logic

The number of stars depends on the row number.

```text
Row 1 → 1 star
Row 2 → 2 stars
Row 3 → 3 stars
Row 4 → 4 stars
Row 5 → 5 stars
```

Therefore, the inner loop runs up to `i`.

---

# Pattern 4: Inverted Right-Angled Star Triangle

For:

```text
n = 5
```

Output:

```text
*****
****
***
**
*
```

### Logic

The number of stars decreases after every row.

```text
Row 1 → 5 stars
Row 2 → 4 stars
Row 3 → 3 stars
Row 4 → 2 stars
Row 5 → 1 star
```

The outer loop runs from `n` down to `1`.

---

# Pattern 5: Floyd's Triangle

Floyd's Triangle is a number pattern.

For:

```text
n = 4
```

Output:

```text
1
2 3
4 5 6
7 8 9 10
```

### Rules

1. Numbers start from 1.
2. Numbers continue increasing.
3. Row `i` contains `i` numbers.
4. The number is incremented after every print.

### Example

Start:

```text
num = 1
```

First row:

```text
1
```

Second row:

```text
2 3
```

Third row:

```text
4 5 6
```

Fourth row:

```text
7 8 9 10
```

---

# Loop Concepts Learned

## For Loop

Used when we know or can define the range of iterations.

Example:

```python
for i in range(1, n + 1):
    print(i)
```

---

## While Loop

Used in the Power of Two problem.

Example:

```python
while n % 2 == 0:
    n = n // 2
```

---

## Nested Loop

A loop inside another loop.

Example:

```python
for i in range(n):
    for j in range(n):
        print("*")
```

The outer loop controls the rows and the inner loop controls the elements.

---

# Important Python Syntax

### Add a character to a string

```python
s = s + "*"
```

### Repeat a string

```python
s = "*" * n
```

### Integer division

```python
n = n // 2
```

### Modulus

```python
n % 2
```

### Range

```python
range(1, n + 1)
```

starts from 1 and goes up to `n`.

### Reverse range

```python
range(n, 0, -1)
```

starts from `n` and decreases until 1.

---

# Day 4 Summary

Today I learned:

- Power of Two checking
- Modulus operator
- Integer division
- `while` loop
- Single-line star pattern
- Square pattern
- Right-angled star pattern
- Inverted right-angled star pattern
- Floyd's Triangle
- Nested loops
- String construction
- Running variables
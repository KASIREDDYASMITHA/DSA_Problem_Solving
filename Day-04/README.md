# DSA Day 04 – Power of Two & Pattern Printing

## Topics Covered

1. Power of Two Check
2. Pattern Printing
   - Stars in a Single Line
   - Square Pattern
   - Right-Angled Star Triangle
   - Inverted Right-Angled Star Triangle
   - Floyd's Triangle

---

## Learning Objectives

- Understand how `while` loops can be used to solve basic DSA problems.
- Practice `for` loops.
- Practice nested `for` loops.
- Understand how to construct patterns using strings.
- Understand how the number of stars changes from row to row.
- Understand how a running number can be used to print Floyd's Triangle.
- Practice converting pseudocode into Python.

---

## Programs

| No. | Program | File |
|---|---|---|
| 1 | Power of Two Check | `programs/01_power_of_two.py` |
| 2 | Stars in a Single Line | `programs/02_single_line_stars.py` |
| 3 | Square Pattern | `programs/03_square_pattern.py` |
| 4 | Right-Angled Star Triangle | `programs/04_right_angled_triangle.py` |
| 5 | Inverted Right-Angled Star Triangle | `programs/05_inverted_right_angled_triangle.py` |
| 6 | Floyd's Triangle | `programs/06_floyds_triangle.py` |

---

# 1. Power of Two

A number is said to be a power of 2 if it can be represented as:

`2^n`

where:

`n >= 0`

### Examples

- `2^0 = 1` → Power of 2
- `2^1 = 2` → Power of 2
- `2^3 = 8` → Power of 2
- `2^4 = 16` → Power of 2
- `10` → Not a Power of 2

### Approach

1. If `n <= 0`, it is not a power of 2.
2. While `n` is divisible by 2, divide it by 2.
3. After the loop, check whether `n == 1`.
4. If `n == 1`, the original number was a power of 2.
5. Otherwise, it was not a power of 2.

### Example

For `n = 16`:

```text
16 → 8 → 4 → 2 → 1
```

Output:

```text
Power of 2
```

For `n = 12`:

```text
12 → 6 → 3
```

Output:

```text
Not a Power of 2
```

---

# 2. Stars in a Single Line

For `n = 5`:

```text
*****
```

The program uses a loop to add `*` to a string `n` times.

---

# 3. Square Pattern

For `n = 4`:

```text
****
****
****
****
```

There are:

- `n` rows
- `n` stars in every row

The outer loop controls the rows.

The inner loop controls the stars in each row.

---

# 4. Right-Angled Star Triangle

For `n = 5`:

```text
*
**
***
****
*****
```

The number of stars increases by one in every row.

- Row 1 → 1 star
- Row 2 → 2 stars
- Row 3 → 3 stars
- Row 4 → 4 stars
- Row 5 → 5 stars

---

# 5. Inverted Right-Angled Star Triangle

For `n = 5`:

```text
*****
****
***
**
*
```

The number of stars decreases by one in every row.

- Row 1 → 5 stars
- Row 2 → 4 stars
- Row 3 → 3 stars
- Row 4 → 2 stars
- Row 5 → 1 star

---

# 6. Floyd's Triangle

Floyd's Triangle starts from `1` and continuously increases the number.

For `n = 4`:

```text
1
2 3
4 5 6
7 8 9 10
```

Rules:

- The numbers start from `1`.
- Numbers are printed continuously.
- Row 1 contains 1 number.
- Row 2 contains 2 numbers.
- Row 3 contains 3 numbers.
- Row 4 contains 4 numbers.
- The running number is increased after every number is printed.

---

# Important Concepts

## Modulus Operator

```python
n % 2
```

The modulus operator gives the remainder.

Example:

```text
8 % 2 = 0
10 % 2 = 0
7 % 2 = 1
```

Therefore:

```python
n % 2 == 0
```

checks whether a number is divisible by 2.

---

## Integer Division

```python
n // 2
```

performs integer division.

Example:

```text
16 // 2 = 8
8 // 2 = 4
4 // 2 = 2
2 // 2 = 1
```

---

## Nested Loops

A loop inside another loop is called a nested loop.

Example:

```python
for i in range(n):
    for j in range(n):
        print("*")
```

Generally:

- Outer loop → rows
- Inner loop → columns/elements

---

# Time Complexity

## Power of Two

The value is divided by 2 repeatedly.

Time Complexity:

`O(log n)`

Space Complexity:

`O(1)`

## Square Pattern

For `n` rows and `n` stars per row:

Time Complexity:

`O(n^2)`

Space Complexity:

`O(n)` when a row string is constructed.

---

# Key Takeaways

1. Use a `while` loop when the number of iterations depends on the changing value.
2. Use nested loops for row-and-column based patterns.
3. The outer loop generally controls rows.
4. The inner loop generally controls elements in each row.
5. A running variable can maintain a value across iterations.
6. Pattern printing is useful for understanding loops and nested loops.
# DSA Day 5 – Pattern Printing

## Topic

Pattern Printing – 2

Day 5 focuses on printing different patterns using nested loops.

### Concepts Covered

1. Hollow Square Pattern
2. Number Pattern
3. Left Half Pyramid Pattern
4. Reverse Left Half Pyramid Pattern
5. Triangle Pattern

---

## 1. Hollow Square Pattern

A hollow square has stars on:

* The first row
* The last row
* The first column
* The last column

The inner portion contains spaces.

### Example for n = 5

```text
* * * * *
*       *
*       *
*       *
* * * * *
```

### Logic

* Print `n` stars for the first row.
* For the middle `n - 2` rows:

  * Print a star.
  * Print `n - 2` spaces.
  * Print another star.
* Print `n` stars for the last row.

### Program

See:

`01_hollow_square.py`

---

## 2. Number Pattern

The number pattern prints increasing numbers in every row.

### Example for n = 5

```text
1
12
123
1234
12345
```

### Logic

* Outer loop controls the rows.
* Inner loop runs from `1` to the current row number.
* Print the value of `j`.

### Program

See:

`02_number_pattern.py`

---

## 3. Left Half Pyramid Pattern

The Left Half Pyramid contains spaces followed by stars.

### Example for n = 5

```text
    *
   **
  ***
 ****
*****
```

### Logic

For every row:

1. Print `n - i` spaces.
2. Print `i` stars.
3. Move to the next line.

### Program

See:

`03_left_half_pyramid.py`

---

## 4. Reverse Left Half Pyramid Pattern

The Reverse Left Half Pyramid starts with the maximum number of stars and decreases by one star in every row.

### Example for n = 5

```text
*****
 ****
  ***
   **
    *
```

### Logic

* Outer loop runs from `n` down to `1`.
* Print `n - i` spaces.
* Print `i` stars.
* Move to the next line.

### Program

See:

`04_reverse_left_half_pyramid.py`

---

## 5. Triangle Pattern

The Triangle Pattern contains leading spaces followed by stars separated by spaces.

### Example for n = 5

```text
    *
   * *
  * * *
 * * * *
* * * * *
```

### Logic

For every row:

1. Print `n - i` spaces.
2. Print `i` stars with a space after each star.
3. Move to the next line.

### Program

See:

`05_triangle_pattern.py`

---

# Important Pattern Printing Concept

Pattern problems generally use nested loops.

```text
Outer loop  → controls rows
Inner loop  → controls what is printed in each row
```

For example:

```python
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()
```

Here:

* `i` controls the current row.
* `j` controls how many stars are printed.
* `print()` moves the cursor to the next line.

---

# Day 5 Summary

| Pattern                   | Main Logic                        |
| ------------------------- | --------------------------------- |
| Hollow Square             | Boundary stars + inner spaces     |
| Number Pattern            | Print numbers from `1` to `i`     |
| Left Half Pyramid         | Spaces decrease, stars increase   |
| Reverse Left Half Pyramid | Spaces increase, stars decrease   |
| Triangle                  | Leading spaces + increasing stars |





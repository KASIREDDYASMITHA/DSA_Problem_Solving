# DSA Day 8 - 2D Array Traversals

**2D Array Traversals**

Today I learned different techniques for traversing elements of a 2D array.

The main traversal techniques covered today are:

1. Circular Traversal
2. Diamond Traversal
3. Spiral Traversal

I also practiced handling boundary elements carefully and debugging a Diamond Traversal solution for the `3 × 3` case.

---

# 1. Circular Traversal

Circular Traversal means traversing the **boundary elements** of a square matrix in a circular order.

The traversal is performed in four parts:

1. First Row
2. Last Column
3. Last Row
4. First Column

### Traversal Order

```text
First Row
    ↓
Last Column
    ↓
Last Row
    ↓
First Column
```

### Example

For the following matrix:

```text
1  2  3
4  5  6
7  8  9
```

The circular traversal is:

```text
1 → 2 → 3 → 6 → 9 → 8 → 7 → 4
```

The center element `5` is not included because it is not part of the boundary.

### Important Point

**Corner elements should be counted only once.**

Therefore, the loops are started carefully:

* First row → all columns
* Last column → start from row `1`
* Last row → start from column `n - 2`
* First column → start from row `n - 2` and stop at row `1`

This avoids counting the corner elements multiple times.

### Example Sum

```text
1 + 2 + 3 + 6 + 9 + 8 + 7 + 4 = 40
```

### Python Program

File:

```text
circular_traversal.py
```

---

# 2. Diamond Traversal

Diamond Traversal traverses the elements forming a **diamond shape** inside a square matrix.

The traversal is divided into four parts:

1. Top → Right
2. Right → Bottom
3. Bottom → Left
4. Left → Top

The middle position of the matrix is used to determine the starting point.

```python
mid = (n - 1) // 2
```

### Traversal Directions

```text
1. Top → Right
2. Right → Bottom
3. Bottom → Left
4. Left → Top
```

---

## 2.1 Top → Right

The traversal starts from:

```python
i = 0
j = mid
```

Then both row and column are increased:

```text
i = i + 1
j = j + 1
```

---

## 2.2 Right → Bottom

The traversal starts from the middle row and the last column.

The movement is:

```text
i = i + 1
j = j - 1
```

So the traversal moves diagonally downward and toward the left.

---

## 2.3 Bottom → Left

The traversal starts from:

```text
i = n - 2
j = mid - 1
```

The movement is:

```text
i = i - 1
j = j - 1
```

---

## 2.4 Left → Top

The movement is:

```text
i = i - 1
j = j + 1
```

This completes the diamond boundary.

---

# 3. Diamond Traversal Example

For the matrix:

```text
1  2  3
4  5  6
7  8  9
```

The diamond boundary is:

```text
    2
   / \
  4   6
   \ /
    8
```

The traversal elements are:

```text
2 → 6 → 8 → 4
```

Therefore:

```text
2 + 6 + 8 + 4 = 20
```

The center element `5` is not included.

---

# 4. Handling the 3 × 3 Case

While implementing Diamond Traversal, I found that the original implementation did not correctly handle the `3 × 3` matrix case.

The corrected implementation handles this case separately.

For a `3 × 3` matrix, the first three traversal sections already visit all required diamond boundary elements.

Therefore, the fourth traversal is executed only when:

```python
if n > 3:
```

This prevents unnecessary traversal for the `3 × 3` case.

### Important Observation

The Diamond Traversal implementation is intended for **odd-sized square matrices**, because it depends on a middle row and middle column.

The middle position is calculated using:

```python
mid = (n - 1) // 2
```

### Python Programs

Corrected version:

```text
diamond_traversal.py
```

Original version:

```text
diamond_traversal_original.py
```

The original version is kept separately to understand the debugging process and the correction made for the `3 × 3` case.

---

# 5. Spiral Traversal

Spiral Traversal means traversing all elements of a 2D array in a spiral pattern.

The traversal is controlled using four boundaries:

```text
top
bottom
left
right
```

Initially:

```python
top = 0
bottom = n - 1
left = 0
right = m - 1
```

A `count` variable is used to keep track of the number of elements already visited.

```python
count = 0
```

The traversal continues until:

```text
count == n × m
```

---

## 5.1 Spiral Traversal Steps

The traversal is performed in four directions.

### L1: Left → Right

Traverse the top row from the left boundary to the right boundary.

```text
Left → Right
```

After completing the row:

```python
top = top + 1
```

---

### L2: Top → Bottom

Traverse the right column from the updated top boundary to the bottom boundary.

```text
Top → Bottom
```

After completing the column:

```python
right = right - 1
```

---

### L3: Right → Left

Traverse the bottom row from the updated right boundary toward the left boundary.

```text
Right → Left
```

After completing the row:

```python
bottom = bottom - 1
```

---

### L4: Bottom → Top

Traverse the left column from the updated bottom boundary toward the top boundary.

```text
Bottom → Top
```

After completing the column:

```python
left = left + 1
```

These four steps continue until all elements have been visited.

---

# 6. Spiral Traversal Example

For the matrix:

```text
1   2   3   4
5   6   7   8
9  10  11  12
```

The spiral traversal is:

```text
1 → 2 → 3 → 4 → 8 → 12 → 11 → 10 → 9 → 5 → 6 → 7
```

The traversal starts from the top-left corner and moves clockwise toward the center.

### Python Program

File:

```text
spiral_traversal.py
```

---

# 7. Circular vs Diamond vs Spiral Traversal

| Traversal          | Main Idea                                    | Movement              |
| ------------------ | -------------------------------------------- | --------------------- |
| Circular Traversal | Traverse boundary elements                   | Horizontal + Vertical |
| Diamond Traversal  | Traverse diamond-shaped boundary             | Diagonal              |
| Spiral Traversal   | Traverse the complete matrix in spiral order | Horizontal + Vertical |

---

# 8. Important Concepts Learned

### 1. Boundary Traversal

In Circular Traversal, only the boundary elements of the matrix are considered.

Example:

```text
1  2  3
4  5  6
7  8  9
```

Boundary elements:

```text
1 2 3 6 9 8 7 4
```

---

### 2. Avoiding Duplicate Elements

When traversing boundaries, corner elements can easily be counted more than once.

Therefore, loop starting and ending conditions must be handled carefully.

For example:

```python
for i in range(1, n):
```

is used for the last column instead of starting from `0`.

---

### 3. Using Middle Position

Diamond Traversal uses:

```python
mid = (n - 1) // 2
```

to find the middle column.

---

### 4. Using Boundaries

Spiral Traversal uses four variables:

```python
top
bottom
left
right
```

These boundaries shrink after every traversal.

---

### 5. Handling Special Cases

The `3 × 3` case in Diamond Traversal showed the importance of testing algorithms with small input sizes.

A solution that appears correct for larger matrices may still fail for smaller edge cases.

---

# 9. Programs Included

The following programs are included in this Day 8 folder:

```text
circular_traversal.py
diamond_traversal.py
diamond_traversal_original.py
spiral_traversal.py
```

### `circular_traversal.py`

Calculates the sum of the boundary elements using Circular Traversal.

### `diamond_traversal.py`

Calculates the sum of the diamond boundary and handles the `3 × 3` case.

### `diamond_traversal_original.py`

Original Diamond Traversal implementation used to identify the `3 × 3` issue.

### `spiral_traversal.py`

Prints all elements of a 2D array in spiral order.

---

# 10. Complexity

## Circular Traversal

The traversal visits only the boundary elements.

```text
Time Complexity: O(n)
```

The input matrix requires:

```text
Space Complexity: O(n²)
```

---

## Diamond Traversal

The traversal visits the boundary elements of the diamond.

```text
Time Complexity: O(n)
```

The input matrix requires:

```text
Space Complexity: O(n²)
```

---

## Spiral Traversal

Every element of the matrix is visited exactly once.

For an `n × m` matrix:

```text
Time Complexity: O(n × m)
```

The matrix itself requires:

```text
Space Complexity: O(n × m)
```

---

# 11. Key Takeaways

* Learned different traversal techniques for 2D arrays.
* Learned Circular Traversal of matrix boundaries.
* Learned how to avoid duplicate corner elements.
* Learned Diamond Traversal using diagonal movement.
* Learned how to calculate the middle position of an odd-sized matrix.
* Identified and fixed the `3 × 3` Diamond Traversal issue.
* Learned Spiral Traversal using `top`, `bottom`, `left`, and `right` boundaries.
* Practiced converting traversal logic into Python programs.
* Learned the importance of testing algorithms with different matrix sizes.

---

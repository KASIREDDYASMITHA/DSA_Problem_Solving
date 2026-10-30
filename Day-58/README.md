# DSA Day 58 - Backtracking (6)

## Topics Covered

1. Rat in a Maze
2. Longest Increasing Path Length

## 1. Rat in a Maze

**Approach:** Backtracking and Recursion

Find all possible paths from the starting cell to the destination in a maze.

- `0` represents a blocked cell.
- `1` represents an open cell.
- Starting position: `(0, 0)`
- Destination: `(n-1, n-1)`
- `T` - Top
- `D` - Down
- `R` - Right
- `L` - Left

**Key Concepts:**
- Boundary checking
- Recursive traversal
- Marking visited cells
- Restoring cells during backtracking

**File:** `rat_in_a_maze.py`

## 2. Longest Increasing Path Length

**Approach:** Recursion and Backtracking

Find the maximum length of a strictly increasing path in a matrix.

Movement is allowed in four directions:
- Top
- Down
- Left
- Right

The next cell must contain a value greater than the current cell.

**Key Concepts:**
- Matrix traversal
- Recursive function calls
- Strictly increasing condition
- Finding the maximum path length using `max()`

**File:** `longest_increasing_path.py`

## Complexity

Both programs use recursive exploration.

- Rat in a Maze: Exponential worst-case time complexity.
- Longest Increasing Path: Exponential worst-case time complexity in the direct recursive implementation.

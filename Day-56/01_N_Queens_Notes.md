# Day 56 - Backtracking 4

## Topic: N-Queens Problem

### 1. Problem Statement
The N-Queens Problem involves placing N queens on an N x N chessboard so that no two queens attack each other.

A queen can attack horizontally, vertically, and diagonally. Therefore, no two queens should share the same row, column, or diagonal.

### 2. Board Representation
- `0` -> No Queen
- `1` -> Queen

Example of a 4 x 4 board:

```text
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0
```

Each row contains exactly one queen, and no two queens attack each other.

### 3. Approach: Brute Force with Backtracking

1. Start from row 0.
2. Try every column in the current row.
3. Call `isSafe(row, col, board, n)` to check whether a queen can be placed.
4. If the position is safe, set `board[row][col] = 1`.
5. Recursively call `solve()` for the next row.
6. After exploring that choice, reset `board[row][col] = 0` to backtrack.
7. If all N rows are completed, a solution has been found.

### 4. solve() Function

Purpose:
To place queens row by row and explore valid arrangements.

Pseudocode:

```text
solve(board, row, n):

    if row == n:
        print(board)
        return

    for col from 0 to n - 1:

        if isSafe(row, col, board, n):
            board[row][col] = 1

            solve(board, row + 1, n)

            board[row][col] = 0
```

The last assignment removes the queen so that other possible positions can be explored.

### 5. isSafe() Function

Purpose:
To determine whether a queen can be placed at the given row and column.

Since queens are placed from the first row downward, check only the cells above the current position.

#### A. Column Check

Check whether any queen exists in the same column above the current row.

```text
for i from row - 1 down to 0:
    if board[i][col] == 1:
        return false
```

#### B. Upper-Left Diagonal Check

Move diagonally upward and to the left.

```text
i = row - 1
j = col - 1

while i >= 0 and j >= 0:
    if board[i][j] == 1:
        return false

    i = i - 1
    j = j - 1
```

#### C. Upper-Right Diagonal Check

Move diagonally upward and to the right.

```text
i = row - 1
j = col + 1

while i >= 0 and j < n:
    if board[i][j] == 1:
        return false

    i = i - 1
    j = j + 1
```

If none of these checks finds a queen, return `true`.

### 6. Backtracking

Backtracking means making a choice, exploring its consequences, and undoing that choice when necessary.

In this problem:

```python
board[row][col] = 1
solve(board, row + 1, n)
board[row][col] = 0
```

- `1` places the queen.
- `solve()` explores the next row.
- `0` removes the queen so another position can be tested.

### 7. Base Case

```text
if row == n:
    print(board)
    return
```

When `row == n`, queens have been placed successfully in all N rows. The current board is a valid solution.

### 8. Important Points

- The board has N rows and N columns.
- Exactly one queen is placed in each row.
- A queen must not share a column or diagonal with another queen.
- `isSafe()` checks whether a position is valid.
- `solve()` uses recursion to move to the next row.
- Backtracking removes a queen after exploring a choice.
- For N = 2 and N = 3, no valid solutions exist.
- For N = 4, there are two valid solutions.

### 9. Complexity

**Space Complexity:** O(N²) for the board, with O(N) additional recursion depth.

**Time Complexity:** The algorithm explores possible placements using backtracking. A commonly used upper-bound estimate for this row-by-row approach is O(N!), ignoring the O(N) safety-check cost. A more explicit conservative bound including safety checks is O(N × N!).
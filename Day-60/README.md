# DSA Day 60 - Backtracking: Sudoku Solver

## Topic
Backtracking - Sudoku Solver

## What I Learned
- Solving a Sudoku puzzle using backtracking.
- Checking whether a number can be placed safely in a cell.
- Validating rows, columns, and 3x3 subgrids.
- Moving to the next cell using row and column indices.
- Using recursion to solve the Sudoku puzzle.
- Resetting a cell to 0 when a choice does not lead to a solution.

## Key Functions
- `is_safe(board, row, col, num)` - Checks whether a number can be placed safely.
- `solve(board, row, col)` - Solves the Sudoku using recursion and backtracking.
- `sudoku(board)` - Starts the solving process.

## Approach
1. Start from the first cell.
2. Skip cells that are already filled.
3. Try numbers from 1 to 9 in empty cells.
4. Check whether each number is valid.
5. Recursively solve the remaining cells.
6. If a choice fails, reset the cell to 0 and try another number.
7. Return the solved board when all rows are completed.

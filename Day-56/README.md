# Day 56 - Backtracking 4: N-Queens Problem

## Topics Covered
- N-Queens Problem
- Backtracking
- Brute-force approach
- Board representation using 0 and 1
- `solve()` function
- `isSafe()` function
- Column checking
- Upper-left diagonal checking
- Upper-right diagonal checking

## Problem Overview
The N-Queens Problem involves placing N queens on an N x N chessboard so that no two queens attack each other.

- `0` represents an empty cell.
- `1` represents a queen.

## Approach
1. Start with the first row.
2. Try placing a queen in each column.
3. Check whether the position is safe using `isSafe()`.
4. If the position is safe, place the queen and move to the next row.
5. If no valid position is available, backtrack and remove the previously placed queen.
6. Continue until a valid solution is found or all possibilities have been explored.

## Safety Checks
- Check the same column above the current position.
- Check the upper-left diagonal.
- Check the upper-right diagonal.

Only rows above the current row need to be checked because the algorithm places queens row by row, starting from the first row.

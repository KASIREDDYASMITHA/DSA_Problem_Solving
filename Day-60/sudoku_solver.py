# DSA Day 60
# Topic: Backtracking - Sudoku Solver


def is_safe(board, row, col, num):

    # Check the row
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Find the starting position of the 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    # Check the 3x3 subgrid
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve(board, row, col):

    # Base case: all nine rows are completed
    if row == 9:
        return True

    # Calculate the next cell
    next_row = row
    next_col = col + 1

    # Move to the next row when the column reaches 9
    if col == 9:
        next_row = row + 1
        next_col = 0

    # Skip cells that are already filled
    if board[row][col] != 0:
        return solve(board, next_row, next_col)

    # Try numbers from 1 to 9
    for num in range(1, 10):

        # Check whether the number can be placed safely
        if is_safe(board, row, col, num):

            # Place the number
            board[row][col] = num

            # Recursively solve the next cell
            if solve(board, next_row, next_col):
                return True

            # Backtrack: reset the cell
            board[row][col] = 0

    # No valid number was found
    return False


def sudoku(board):

    if solve(board, 0, 0):
        return board

    return None


# Sample Sudoku puzzle
# 0 represents an empty cell

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


# Solve the Sudoku puzzle
result = sudoku(board)


# Display the result
if result is not None:
    print("Solved Sudoku:")
    for row in result:
        print(row)
else:
    print("No solution exists for this Sudoku puzzle.")
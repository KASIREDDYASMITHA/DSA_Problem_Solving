
# DSA Day 53: N-Queens Problem
# Approach: Backtracking

n = int(input("Enter the size of the chessboard: "))

board = [-1] * n
solutions = []


def is_safe(row, col):
    for previous_row in range(row):
        previous_col = board[previous_row]

        # Check the same column
        if previous_col == col:
            return False

        # Check both diagonals
        if abs(previous_col - col) == abs(previous_row - row):
            return False

    return True


def solve_n_queens(row):
    # Base case: all queens have been placed
    if row == n:
        solutions.append(board.copy())
        return

    # Try placing a queen in each column
    for col in range(n):
        if is_safe(row, col):
            board[row] = col

            # Move to the next row
            solve_n_queens(row + 1)

            # Backtrack: remove the queen
            board[row] = -1


if n <= 0:
    print("Enter a positive board size.")
else:
    solve_n_queens(0)

    print("Total solutions:", len(solutions))

    for solution_number, solution in enumerate(solutions, start=1):
        print("\nSolution", solution_number)

        for row in range(n):
            for col in range(n):
                if solution[row] == col:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()

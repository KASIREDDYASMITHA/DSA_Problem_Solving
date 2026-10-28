# Day 56: N-Queens Problem
# Find all valid solutions using backtracking

def isSafe(row, col, board, n):

    # Column check
    for i in range(row - 1, -1, -1):
        if board[i][col] == 1:
            return False

    # Upper-left diagonal check
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    # Upper-right diagonal check
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False

        i -= 1
        j += 1

    return True


def solve(board, row, n):

    global solution_count

    # Base case
    if row == n:
        solution_count += 1

        print("\nSolution", solution_count)

        for i in range(n):
            print(board[i])

        return

    # Try placing a queen in every column
    for col in range(n):

        if isSafe(row, col, board, n):
            board[row][col] = 1

            solve(board, row + 1, n)

            # Backtrack
            board[row][col] = 0


n = int(input("Enter the value of N: "))

if n <= 0:
    print("N must be a positive integer.")
else:
    board = [[0 for col in range(n)] for row in range(n)]

    solution_count = 0

    solve(board, 0, n)

    if solution_count == 0:
        print("No solution exists.")
    else:
        print("\nTotal number of solutions:", solution_count)
# Day 58 - Longest Increasing Path Length
# Approach: Recursion and Backtracking

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

matrix = []

print("Enter the matrix elements:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)


def longest_path(matrix, row, col, prev):
    n = len(matrix)
    m = len(matrix[0])

    # Check boundaries and increasing condition
    if (
        row < 0
        or row >= n
        or col < 0
        or col >= m
        or matrix[row][col] <= prev
    ):
        return 0

    # Current cell contributes one to the path length
    res = 1

    # Move Top
    res = max(
        res,
        1 + longest_path(matrix, row - 1, col, matrix[row][col])
    )

    # Move Down
    res = max(
        res,
        1 + longest_path(matrix, row + 1, col, matrix[row][col])
    )

    # Move Left
    res = max(
        res,
        1 + longest_path(matrix, row, col - 1, matrix[row][col])
    )

    # Move Right
    res = max(
        res,
        1 + longest_path(matrix, row, col + 1, matrix[row][col])
    )

    return res


if n <= 0 or m <= 0:
    print("Number of rows and columns must be positive.")
elif any(len(row) != m for row in matrix):
    print("Invalid input: enter exactly m values in each row.")
else:
    answer = 0

    # Start the search from every cell
    for i in range(n):
        for j in range(m):
            res = longest_path(matrix, i, j, float("-inf"))
            answer = max(answer, res)

    print("Longest Increasing Path Length:", answer)
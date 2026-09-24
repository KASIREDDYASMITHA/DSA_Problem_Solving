# Rotate Matrix 90 Degrees Clockwise
# Approach: Transpose + Reverse Each Row

n = int(input("Enter the size of the matrix: "))

matrix = []

print("Enter matrix elements row by row:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 1: Transpose the matrix
for i in range(n):
    for j in range(i + 1, n):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp

# Step 2: Reverse each row
for i in range(n):
    left = 0
    right = n - 1

    while left < right:
        temp = matrix[i][left]
        matrix[i][left] = matrix[i][right]
        matrix[i][right] = temp

        left += 1
        right -= 1

# Print rotated matrix
print("Rotated matrix:")
for i in range(n):
    print(*matrix[i])
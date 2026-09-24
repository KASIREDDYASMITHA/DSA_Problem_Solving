# Set Matrix Zeroes
# Approach 1: Marker Matrix

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements row by row:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Create marker matrix
mark = [[False] * m for i in range(n)]

# Find zeros and mark their rows and columns
for i in range(n):
    for j in range(m):

        if matrix[i][j] == 0:

            # Mark entire column
            for k in range(n):
                mark[k][j] = True

            # Mark entire row
            for k in range(m):
                mark[i][k] = True

# Update matrix
for i in range(n):
    for j in range(m):

        if mark[i][j] == True:
            matrix[i][j] = 0

# Print result
print("Matrix after setting zeroes:")
for i in range(n):
    print(*matrix[i])
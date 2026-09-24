# Set Matrix Zeroes
# Approach 2: Row and Column Marker Arrays

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements row by row:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Create row and column markers
row = [False] * n
col = [False] * m

# Find zeros
for i in range(n):
    for j in range(m):

        if matrix[i][j] == 0:
            row[i] = True
            col[j] = True

# Set marked rows and columns to zero
for i in range(n):
    for j in range(m):

        if row[i] == True or col[j] == True:
            matrix[i][j] = 0

# Print result
print("Matrix after setting zeroes:")
for i in range(n):
    print(*matrix[i])
# Search in a Row-wise and Column-wise Sorted 2D Matrix
# Approach: Staircase Search

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements row by row:")
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

target = int(input("Enter target element: "))

# Start from the top-right corner
i = 0
j = n - 1

while i < m and j >= 0:

    # Target found
    if matrix[i][j] == target:
        print(True)
        break

    # Current element is greater than target
    elif matrix[i][j] > target:
        j -= 1

    # Current element is smaller than target
    else:
        i += 1

else:
    print(False)
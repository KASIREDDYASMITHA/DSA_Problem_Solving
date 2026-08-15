n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

arr = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(int(input(f"Enter element [{i}][{j}]: ")))
    arr.append(row)

sum = 0

# First column
for i in range(n):
    sum = sum + arr[i][0]

# Last row
# Start from 1 because arr[n-1][0] is already included
for j in range(1, m):
    sum = sum + arr[n - 1][j]

print("Sum of L Traversal:", sum)
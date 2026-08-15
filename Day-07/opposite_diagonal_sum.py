
n = int(input("Enter size of matrix: "))

arr = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input(f"Enter element [{i}][{j}]: ")))
    arr.append(row)

sum = 0

for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            sum = sum + arr[i][j]

print("Sum of opposite diagonal elements:", sum)
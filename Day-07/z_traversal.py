n = int(input("Enter size of matrix: "))

arr = []

print("Enter the matrix:")

for i in range(n):
    arr.append(list(map(int, input().split())))

sum = 0

# Top row
for j in range(n):
    sum = sum + arr[0][j]

# Opposite diagonal
i = 1
j = n - 2

while i < n - 1 and j > 0:
    sum = sum + arr[i][j]
    i = i + 1
    j = j - 1

# Bottom row
for j in range(n):
    sum = sum + arr[n - 1][j]

print(sum)
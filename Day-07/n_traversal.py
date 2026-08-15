n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

total = 0

# First column: bottom to top
for i in range(n - 1, -1, -1):
    total = total + arr[i][0]

# Main diagonal
for i in range(1, n):
    total = total + arr[i][i]

# Last column: bottom to top
for i in range(n - 2, -1, -1):
    total = total + arr[i][n - 1]

print(total)
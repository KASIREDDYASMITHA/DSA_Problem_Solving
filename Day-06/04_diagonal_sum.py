
n = int(input())

arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

diagonal_sum = 0

for i in range(n):
    diagonal_sum = diagonal_sum + arr[i][i]

print(diagonal_sum)
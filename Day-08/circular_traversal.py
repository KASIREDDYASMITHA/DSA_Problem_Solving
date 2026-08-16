
# DSA Day 8
# Circular Traversal of a Square Matrix

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

total = 0

# -------------------------
# 1. First Row
# -------------------------
for j in range(n):
    total += arr[0][j]

# -------------------------
# 2. Last Column
# -------------------------
for i in range(1, n):
    total += arr[i][n - 1]

# -------------------------
# 3. Last Row
# -------------------------
for j in range(n - 2, -1, -1):
    total += arr[n - 1][j]

# -------------------------
# 4. First Column
# -------------------------
for i in range(n - 2, 0, -1):
    total += arr[i][0]

print(total)
# DSA Day 8
# Diamond Traversal
# Works for all odd-sized square matrices including 3 x 3

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

total = 0
mid = (n - 1) // 2

# -------------------------
# 1. Top -> Right
# -------------------------
i = 0
j = mid

while i < mid and j < n:
    total += arr[i][j]
    i += 1
    j += 1

# -------------------------
# 2. Right -> Bottom
# -------------------------
i = mid
j = n - 1

while i < n and j >= mid:
    total += arr[i][j]
    i += 1
    j -= 1

# -------------------------
# 3. Bottom -> Left
# -------------------------
i = n - 2
j = mid - 1

while i >= mid and j >= 0:
    total += arr[i][j]
    i -= 1
    j -= 1

# -------------------------
# 4. Left -> Top
# -------------------------
# For a 3 x 3 matrix, the first
# three loops already visit all
# required diamond boundary cells.

if n > 3:
    i = mid - 1
    j = 0

    while i >= 0 and j < mid:
        total += arr[i][j]
        i -= 1
        j += 1

print(total)
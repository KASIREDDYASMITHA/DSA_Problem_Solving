# DSA Day 8
# Spiral Traversal of a 2D Array

n = int(input())
m = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

top = 0
bottom = n - 1
left = 0
right = m - 1

count = 0

while count < n * m:

    # -------------------------
    # L1: Left -> Right
    # -------------------------
    for j in range(left, right + 1):
        print(arr[top][j], end=" ")
        count += 1

    top += 1

    # -------------------------
    # L2: Top -> Bottom
    # -------------------------
    for i in range(top, bottom + 1):
        print(arr[i][right], end=" ")
        count += 1

    right -= 1

    # -------------------------
    # L3: Right -> Left
    # -------------------------
    for j in range(right, left - 1, -1):
        print(arr[bottom][j], end=" ")
        count += 1

    bottom -= 1

    # -------------------------
    # L4: Bottom -> Top
    # -------------------------
    for i in range(bottom, top - 1, -1):
        print(arr[i][left], end=" ")
        count += 1

    left += 1
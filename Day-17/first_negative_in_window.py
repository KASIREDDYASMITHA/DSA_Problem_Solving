# DSA Day 17
# Amazon Asked Question
# First Negative Number in Every Window of Size K
# Brute Force Approach

n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

k = int(input("Enter k: "))

res = []
idx = 0

for i in range(n - k + 1):
    temp = 0

    for j in range(i, i + k):
        if arr[j] < 0:
            temp = arr[j]
            break

    res.append(temp)
    idx += 1

print("First Negative Elements:", res)
# Day 23 - Product of Array Except Self
# Approach 1: Brute Force Approach

arr = list(map(int, input("Enter array elements: ").split()))

n = len(arr)

res = [1] * n

for i in range(n):
    for j in range(n):
        if i != j:
            res[i] = res[i] * arr[j]

print("Product of array except self:", res)
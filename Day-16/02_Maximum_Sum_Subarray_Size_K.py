# Maximum Sum Subarray of Size K
# Brute Force Approach

n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))

k = int(input("Enter k: "))

res = float('-inf')

for i in range(0, n - k + 1):
    sum = 0

    for j in range(i, i + k):
        sum = sum + arr[j]

    res = max(sum, res)

print("Maximum sum of", k, "consecutive elements:", res)
# DSA Day 17
# Maximum Sum Subarray of Size K
# Sliding Window Technique

n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

k = int(input("Enter k: "))

start = 0
windowSum = 0
maxSum = float('-inf')

for end in range(n):
    windowSum = windowSum + arr[end]

    windowSize = end - start + 1

    if windowSize < k:
        continue

    if windowSize == k:
        maxSum = max(maxSum, windowSum)

        windowSum = windowSum - arr[start]
        start = start + 1

print("Maximum Sum:", maxSum)
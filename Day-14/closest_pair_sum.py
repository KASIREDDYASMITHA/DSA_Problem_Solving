# DSA Day 14
# Closest Pair Sum
# Brute Force and Two Pointer Approach


# ==================================================
# 1. CLOSEST PAIR SUM - BRUTE FORCE
# ==================================================

n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))

target = int(input("Enter target: "))

bestDiff = float('inf')
bestSum = 0

for i in range(n):

    for j in range(i + 1, n):

        currentSum = arr[i] + arr[j]

        diff = abs(target - currentSum)

        if diff < bestDiff:
            bestDiff = diff
            bestSum = currentSum

print("Closest Pair Sum =", bestSum)


# ==================================================
# 2. CLOSEST PAIR SUM - TWO POINTER APPROACH
# ==================================================

n = int(input("\nEnter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))

target = int(input("Enter target: "))

arr.sort()

left = 0
right = n - 1

bestDiff = float('inf')
bestSum = 0

while left < right:

    currentSum = arr[left] + arr[right]

    diff = abs(target - currentSum)

    if diff < bestDiff:
        bestDiff = diff
        bestSum = currentSum

    if currentSum < target:
        left += 1

    else:
        right -= 1

print("Closest Pair Sum =", bestSum)
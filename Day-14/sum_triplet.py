# DSA Day 14
# Sum Triplet
# Brute Force and Two Pointer Approach


# ==================================================
# 1. SUM TRIPLET - BRUTE FORCE
# ==================================================

arr = list(map(int, input("Enter the array elements: ").split()))
target = int(input("Enter the target sum: "))

found = False
n = len(arr)

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):

            if arr[i] + arr[j] + arr[k] == target:
                print("Triplet:", arr[i], arr[j], arr[k])
                found = True

if not found:
    print("No triplet found")


# ==================================================
# 2. SUM TRIPLET - TWO POINTER APPROACH
# ==================================================

n = int(input("\nEnter number of elements: "))

arr = [int(input("Enter element: ")) for _ in range(n)]

target = int(input("Enter target: "))

arr.sort()

found = False

for i in range(n - 2):

    left = i + 1
    right = n - 1

    newTarget = target - arr[i]

    while left < right:

        currentSum = arr[left] + arr[right]

        if currentSum == newTarget:

            print("Triplet:", arr[i], arr[left], arr[right])

            found = True
            break

        elif currentSum < newTarget:
            left += 1

        else:
            right -= 1

    if found:
        break

if not found:
    print("No triplet found")
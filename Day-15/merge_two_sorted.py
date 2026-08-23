# Container With Most Water
# Day 15 - DSA
#
# Two Approaches:
# 1. Brute Force
# 2. Two Pointer


arr = list(map(int, input("Enter elements: ").split()))


# --------------------------------------------------
# Approach 1: Brute Force
# --------------------------------------------------

n = len(arr)
brute_force_result = 0

for i in range(n):
    for j in range(i + 1, n):

        length = j - i
        breadth = min(arr[i], arr[j])

        area = length * breadth

        brute_force_result = max(brute_force_result, area)

print("Brute Force Approach:", brute_force_result)


# --------------------------------------------------
# Approach 2: Two Pointer
# --------------------------------------------------

two_pointer_result = float('-inf')

left = 0
right = len(arr) - 1

while left < right:

    length = right - left
    breadth = min(arr[left], arr[right])

    area = length * breadth

    two_pointer_result = max(two_pointer_result, area)

    if arr[left] < arr[right]:
        left += 1
    else:
        right -= 1

print("Two Pointer Approach:", two_pointer_result)
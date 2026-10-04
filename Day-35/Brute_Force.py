# ============================================================
# DSA Day 35
# Question 1: Find the Element That Appears Once
# Approach 1: Brute Force
# ============================================================

# Problem:
# Every element appears twice except one element.
# Find the element that appears only once.
#
# Example:
# Input:
# 1 1 2 2 3 3 4
#
# Output:
# 4


arr = list(map(int, input("Enter sorted array elements: ").split()))

answer = -1

for i in range(len(arr)):
    count = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count = count + 1

    if count == 1:
        answer = arr[i]
        break

print("Single Element:", answer)
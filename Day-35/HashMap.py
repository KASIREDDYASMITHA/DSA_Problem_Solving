# ============================================================
# DSA Day 35
# Question 1: Find the Element That Appears Once
# Approach 2: HashMap
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

frequency = {}

for num in arr:

    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1

answer = -1

for num in frequency:

    if frequency[num] == 1:
        answer = num
        break

print("Single Element:", answer)
# ============================================================
# DSA Day 35
# Question 1: Find the Element That Appears Once
# Approach 3: Binary Search
# ============================================================

# Problem:
# Given a sorted array where every element appears twice
# except one element, find the element that appears once.
#
# Example:
# Input:
# 1 1 2 2 3 3 4
#
# Output:
# 4


arr = list(map(int, input("Enter sorted array elements: ").split()))

low = 0
high = len(arr) - 1

if len(arr) == 1:

    answer = arr[0]

else:

    while low < high:

        mid = low + (high - low) // 2

        # Make mid even
        if mid % 2 == 1:
            mid = mid - 1

        # The pair is correct.
        # Therefore, the single element is on the right.
        if arr[mid] == arr[mid + 1]:
            low = mid + 2

        # The pair is not correct.
        # Therefore, the single element is at mid or on the left.
        else:
            high = mid

    answer = arr[low]

print("Single Element:", answer)
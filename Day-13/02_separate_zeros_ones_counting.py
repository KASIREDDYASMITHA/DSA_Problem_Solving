# Day 13 - Separate Zeros and Ones
# Approach 2: Using Counting

# Problem:
# Given a binary array containing only 0s and 1s,
# rearrange the array so that all 0s appear on the left
# and all 1s appear on the right.

n = int(input("Enter n: "))

arr = [int(input("Enter element: ")) for _ in range(n)]

zero_count = 0
one_count = 0

# Count zeros and ones
for i in range(n):

    if arr[i] == 0:
        zero_count += 1

    else:
        one_count += 1

# Fill zeros
for i in range(zero_count):
    arr[i] = 0

# Fill ones
for i in range(zero_count, n):
    arr[i] = 1

print("Original/Result array:", arr)

# Time Complexity: O(n)
# Space Complexity: O(1)
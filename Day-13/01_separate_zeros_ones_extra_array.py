# Day 13 - Separate Zeros and Ones
# Approach 1: Using Extra Array

# Problem:
# Given a binary array containing only 0s and 1s,
# rearrange the array so that all 0s appear on the left
# and all 1s appear on the right.

n = int(input("Enter n: "))

arr = [int(input("Enter element: ")) for _ in range(n)]

# Create a new array of size n
res = [0] * n

j = 0
k = n - 1

# Traverse the original array
for i in range(n):

    if arr[i] == 0:
        # Place 0 from the left side
        res[j] = arr[i]
        j += 1

    else:
        # Place 1 from the right side
        res[k] = arr[i]
        k -= 1

print("Original array:", arr)
print("Result:", res)

# Time Complexity: O(n)
# Space Complexity: O(n)
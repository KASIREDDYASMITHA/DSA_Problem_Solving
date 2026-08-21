# Day 13 - Separate Zeros and Ones
# Approach 3: Two Pointer Technique

# Problem:
# Given a binary array containing only 0s and 1s,
# rearrange the array so that all 0s appear on the left
# and all 1s appear on the right.

n = int(input("Enter n: "))

arr = [int(input("Enter element: ")) for _ in range(n)]

left = 0
right = n - 1

while left < right:

    # Move left while it is already correctly placed at 0
    while left < right and arr[left] == 0:
        left += 1

    # Move right while it is already correctly placed at 1
    while left < right and arr[right] == 1:
        right -= 1

    # Swap misplaced elements
    arr[left], arr[right] = arr[right], arr[left]

    left += 1
    right -= 1

print("Result:", arr)

# Time Complexity: O(n)
# Space Complexity: O(1)
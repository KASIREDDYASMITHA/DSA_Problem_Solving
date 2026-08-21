# Day 13 - Two Sum
# Approach 1: Brute Force

# Problem:
# Given an integer array and a target,
# determine whether there exists a pair of elements
# whose sum is equal to the target.

n = int(input("Enter n: "))

arr = [int(input("Enter element: ")) for _ in range(n)]

target = int(input("Enter Target: "))

found = False

# Check every possible pair
for i in range(n - 1):

    for j in range(i + 1, n):

        if arr[i] + arr[j] == target:
            found = True
            break

    # Stop outer loop if pair is found
    if found:
        break

print(found)

# Time Complexity: O(n^2)
# Space Complexity: O(1)
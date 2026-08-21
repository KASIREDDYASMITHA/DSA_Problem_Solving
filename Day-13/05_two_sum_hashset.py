# Day 13 - Two Sum
# Approach 2: Using HashSet

# Problem:
# Given an integer array and a target,
# determine whether there exists a pair of elements
# whose sum is equal to the target.

n = int(input("Enter n: "))

arr = [int(input("Enter element: ")) for _ in range(n)]

target = int(input("Enter Target: "))

# Create an empty set
s = set()

found = False

# Traverse the array
for i in range(n):

    # Find the value needed to reach the target
    complement = target - arr[i]

    # Check whether complement already exists
    if complement in s:
        found = True
        break

    # Add current element to the set
    s.add(arr[i])

print(found)

# Time Complexity: O(n)
# Space Complexity: O(n)
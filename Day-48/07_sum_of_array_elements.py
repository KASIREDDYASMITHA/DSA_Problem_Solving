
# DSA Day 48
# Sum of Array Elements Using Recursion

# Approach:
# Add the current element to the sum of remaining elements.
# Base case: index reaches the array length.

arr = list(map(int, input("Enter array elements: ").split()))


def sum_array(arr, index):
    if index == len(arr):
        return 0

    return arr[index] + sum_array(arr, index + 1)


print("Sum of array elements:", sum_array(arr, 0))

# Example:
# Input: 10 20 30 40
# Output: 100

# Time Complexity: O(n)
# Auxiliary Space: O(n)

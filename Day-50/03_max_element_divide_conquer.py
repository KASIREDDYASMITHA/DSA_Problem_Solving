
# Day 50 - Find Maximum Using Divide and Conquer

# Approach:
# Divide the array into two halves.
# Find the maximum of each half recursively.
# Combine both results using max().
# Base case: only one element remains.

def find_maximum(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    left_maximum = find_maximum(arr, left, mid)
    right_maximum = find_maximum(arr, mid + 1, right)

    return max(left_maximum, right_maximum)


n = int(input("Enter the number of elements: "))

if n <= 0:
    print("Please enter at least one element.")
else:
    arr = []

    for i in range(n):
        element = int(input("Enter an element: "))
        arr.append(element)

    result = find_maximum(arr, 0, n - 1)

    print("Maximum element:", result)

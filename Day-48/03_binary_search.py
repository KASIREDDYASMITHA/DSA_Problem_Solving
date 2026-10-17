
# DSA Day 48
# Binary Search Using Recursion

# Approach:
# Search the middle element.
# If the target is smaller, search the left half.
# If the target is larger, search the right half.
# Base case: low > high means the target is absent.

arr = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter target element: "))


def binary_search(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)


result = binary_search(arr, 0, len(arr) - 1, target)

if result == -1:
    print("Element not found")
else:
    print("Element found at index:", result)

# Example:
# Array: 10 20 30 40 50
# Target: 40
# Output: Element found at index: 3

# Time Complexity: O(log n)
# Auxiliary Space: O(log n)

# Important: The input array must be sorted.

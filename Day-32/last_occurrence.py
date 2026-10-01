# Last Occurrence using Binary Search
# The array must be sorted.
# When the key is found, store the index
# and continue searching towards the right.
#
# Example:
# Array: 1 2 2 2 3 4
# Key: 2
# Last occurrence: index 3

n = int(input("Enter array size: "))

arr = list(map(int, input("Enter sorted array elements: ").split()))

key = int(input("Enter key: "))

low = 0
high = n - 1

result = -1

while low <= high:

    mid = low + (high - low) // 2

    # Key found
    if key == arr[mid]:

        # Store the current position
        result = mid

        # Continue searching towards the right
        low = mid + 1

    # Key is smaller than middle element
    elif key < arr[mid]:

        high = mid - 1

    # Key is greater than middle element
    else:

        low = mid + 1

print("Last occurrence index:", result)
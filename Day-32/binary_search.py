# Binary Search
# Binary Search works only on a sorted array.
# The search space becomes half after every comparison.

# Example input:
# Enter array size: 8
# Enter sorted array elements: 2 5 8 12 16 23 38 56
# Enter key: 23

n = int(input("Enter array size: "))

arr = list(map(int, input("Enter sorted array elements: ").split()))

key = int(input("Enter key to search: "))

low = 0
high = n - 1

result = -1

while low <= high:

    # Calculate middle index safely
    mid = low + (high - low) // 2

    # Key is found
    if key == arr[mid]:
        result = mid
        break

    # Key is smaller, so search in the left half
    elif key < arr[mid]:
        high = mid - 1

    # Key is greater, so search in the right half
    else:
        low = mid + 1

print("Index:", result)
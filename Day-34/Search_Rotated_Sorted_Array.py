# Search in Rotated Sorted Array
arr = list(map(int, input("Enter the elements of the rotated sorted array: ").split()))
target = int(input("Enter the target element: "))

low = 0
high = len(arr) - 1

answer = -1

while low <= high:

    mid = low + (high - low) // 2

    # Target found
    if arr[mid] == target:
        answer = mid
        break

    # Check whether left half is sorted
    if arr[low] <= arr[mid]:

        # Target lies in the sorted left half
        if target >= arr[low] and target < arr[mid]:
            high = mid - 1

        # Target lies in the right half
        else:
            low = mid + 1

    # Right half is sorted
    else:

        # Target lies in the sorted right half
        if target > arr[mid] and target <= arr[high]:
            low = mid + 1

        # Target lies in the left half
        else:
            high = mid - 1

print("Target index:", answer)
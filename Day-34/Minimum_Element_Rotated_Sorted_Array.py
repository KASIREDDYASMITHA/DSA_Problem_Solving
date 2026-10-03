# Find Minimum Element in Rotated Sorted Array

arr = list(map(int, input("Enter the elements of the rotated sorted array: ").split()))

low = 0
high = len(arr) - 1

while low < high:

    mid = low + (high - low) // 2

    # Current portion is completely sorted
    if arr[low] < arr[mid] and arr[mid] < arr[high]:
        print("Minimum element:", arr[low])
        break

    # Left part is sorted
    # Minimum is present in the right unsorted region
    if arr[mid] > arr[high]:
        low = mid + 1

    # Minimum can be at mid or in the left part
    else:
        high = mid

else:
    print("Minimum element:", arr[low])
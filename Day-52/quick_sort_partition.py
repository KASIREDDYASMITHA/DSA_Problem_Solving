
# Day 52 - Quick Sort Partition
# Place the pivot in its correct position.

arr = list(map(int, input("Enter array elements separated by spaces: ").split()))

low = 0
high = len(arr) - 1

if len(arr) > 0:
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    pivot_index = i + 1

    print("Array after partition:", arr)
    print("Pivot element:", pivot)
    print("Pivot index:", pivot_index)
else:
    print("Array is empty.")

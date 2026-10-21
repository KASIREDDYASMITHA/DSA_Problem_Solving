
# Day 51: Merge Sort
# Approach: Divide and Conquer

def mergeSort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)

    i = left
    j = mid + 1
    temp = []

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for k in range(len(temp)):
        arr[left + k] = temp[k]


arr = list(map(int, input("Enter array elements: ").split()))

mergeSort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)

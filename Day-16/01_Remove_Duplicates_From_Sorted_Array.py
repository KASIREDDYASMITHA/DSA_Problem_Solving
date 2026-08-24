# Remove Duplicates From Sorted Array
# Two Pointer Approach

n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter sorted elements: ").split()))

j = 0

for i in range(0, n - 1):
    if arr[i] != arr[i + 1]:
        arr[j] = arr[i]
        j += 1

arr[j] = arr[n - 1]

print("Array after removing duplicates:")

for i in range(j + 1):
    print(arr[i], end=" ")
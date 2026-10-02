# Day 33 - Ceil using Binary Search

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

low = 0
high = n - 1
res = -1

while low <= high:

    mid = low + (high - low) // 2

    if arr[mid] >= target:
        res = mid
        high = mid - 1

    else:
        low = mid + 1

print("Ceil Index:", res)

if res != -1:
    print("Ceil Value:", arr[res])
# Day 33 - Upper Bound using Binary Search

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

low = 0
high = n - 1
res = n

while low <= high:

    mid = low + (high - low) // 2

    if arr[mid] > target:
        res = mid
        high = mid - 1

    else:
        low = mid + 1

print("Upper Bound:", res)
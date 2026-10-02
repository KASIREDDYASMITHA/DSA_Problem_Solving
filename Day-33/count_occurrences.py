# Day 33 - Count Occurrences using Binary Search

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

# First Occurrence

low = 0
high = n - 1
first = -1

while low <= high:

    mid = low + (high - low) // 2

    if arr[mid] == target:
        first = mid
        high = mid - 1

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

# Last Occurrence

low = 0
high = n - 1
last = -1

while low <= high:

    mid = low + (high - low) // 2

    if arr[mid] == target:
        last = mid
        low = mid + 1

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

# Count Occurrences

if first == -1:
    count = 0
else:
    count = last - first + 1

print("First Occurrence:", first)
print("Last Occurrence:", last)
print("Count Occurrences:", count)
# Bitonic Point - Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

user_input = input("Enter bitonic array elements separated by spaces: ")
arr = list(map(int, user_input.split()))

n = len(arr)

low = 0
high = n - 1

while low < high:
    mid = low + (high - low) // 2

    if arr[mid] < arr[mid + 1]:
        low = mid + 1
    else:
        high = mid

bitonic_index = low
bitonic_point = arr[bitonic_index]

print("Bitonic Point Index :", bitonic_index)
print("Bitonic Point (Maximum Element) :", bitonic_point)
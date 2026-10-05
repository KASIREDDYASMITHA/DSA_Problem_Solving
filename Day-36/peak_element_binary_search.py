# Peak Element - Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

user_input = input("Enter array elements separated by spaces: ")
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

peak_index = low

print("Peak Element Index :", peak_index)
print("Peak Element Value :", arr[peak_index])
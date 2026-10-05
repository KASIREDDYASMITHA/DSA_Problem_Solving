# Bitonic Point - Linear Search
# Time Complexity: O(n)
# Space Complexity: O(1)

user_input = input("Enter bitonic array elements separated by spaces: ")
arr = list(map(int, user_input.split()))

n = len(arr)

bitonic_point = arr[n - 1]

for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        bitonic_point = arr[i]
        break

print("Bitonic Point (Maximum Element) :", bitonic_point)
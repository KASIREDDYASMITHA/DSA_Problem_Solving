# Rotate Array K Times
# Reversal Algorithm

arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))

n = len(arr)

k = k % n

# Reverse entire array
left = 0
right = n - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

# Reverse first k elements
left = 0
right = k - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

# Reverse remaining elements
left = k
right = n - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("Rotated array:", arr)
# Rotate Array K Times
# Auxiliary Array Approach

arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))

n = len(arr)

k = k % n

res = [0] * n

for i in range(n):
    res[(i + k) % n] = arr[i]

print("Rotated array:", res)
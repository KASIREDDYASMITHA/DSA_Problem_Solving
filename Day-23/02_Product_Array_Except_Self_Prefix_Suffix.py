# Day 23 - Product of Array Except Self
# Approach 2: Prefix + Suffix Product Approach

arr = list(map(int, input("Enter array elements: ").split()))

n = len(arr)

left = [1] * n
right = [1] * n
res = [1] * n

# Calculate prefix products
for i in range(1, n):
    left[i] = arr[i - 1] * left[i - 1]

# Calculate suffix products
for i in range(n - 2, -1, -1):
    right[i] = arr[i + 1] * right[i + 1]

# Multiply prefix and suffix products
for i in range(n):
    res[i] = left[i] * right[i]

print("Product of array except self:", res)
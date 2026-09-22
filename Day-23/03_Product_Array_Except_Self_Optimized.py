# Day 23 - Product of Array Except Self
# Approach 3: Optimized Prefix + Suffix Approach

arr = list(map(int, input("Enter array elements: ").split()))

n = len(arr)

res = [1] * n

# Calculate prefix products
for i in range(1, n):
    res[i] = res[i - 1] * arr[i - 1]

# Calculate suffix products and update result
suffix = 1

for i in range(n - 1, -1, -1):
    res[i] = res[i] * suffix
    suffix = suffix * arr[i]

print("Product of array except self:", res)
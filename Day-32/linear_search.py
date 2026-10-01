# Linear Search
# Linear Search checks every element one by one.
# If the key is found, print its index.
# If the key is not found, print -1.

# Example input:
# Enter array size: 8
# Enter array elements: 2 5 8 12 16 23 38 56
# Enter key: 23

n = int(input("Enter array size: "))

arr = list(map(int, input("Enter array elements: ").split()))

key = int(input("Enter key to search: "))

result = -1

for i in range(n):
    if arr[i] == key:
        result = i
        break

print("Index:", result)
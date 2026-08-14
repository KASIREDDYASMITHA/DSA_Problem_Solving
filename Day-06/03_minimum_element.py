arr = [7, 3, 9, 2, 5]

res = float('inf')

for i in range(len(arr)):
    if arr[i] < res:
        res = arr[i]

print("Minimum element:", res)
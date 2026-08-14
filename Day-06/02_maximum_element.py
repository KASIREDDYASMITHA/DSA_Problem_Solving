arr = [10, 25, 5, 45, 30, 15]

res = float('-inf')

for i in range(len(arr)):
    if arr[i] > res:
        res = arr[i]

print("Maximum element is:", res)
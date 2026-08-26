
# First Negative Number in Every Window of Size K
# Sliding Window


arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter window size: "))

n = len(arr)

res = [0] * (n - k + 1)

start = 0
idx = 0
first = 0

for end in range(n):

    wSize = end - start + 1

    if wSize < k:
        continue

    if wSize == k:

        while first < start or (first <= end and arr[first] >= 0):
            first += 1

        if first <= end:
            res[idx] = arr[first]
        else:
            res[idx] = 0

        idx += 1
        start += 1

print("Result:", res)
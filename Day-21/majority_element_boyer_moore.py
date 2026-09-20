# Majority Element
# Approach 4: Boyer-Moore Voting Algorithm

arr = list(map(int, input("Enter array elements: ").split()))

n = len(arr)

count = 0
candidate = 0

# Find candidate
for i in range(n):
    if count == 0:
        candidate = arr[i]

    if candidate == arr[i]:
        count += 1
    else:
        count -= 1

# Verify candidate
temp = 0

for i in range(n):
    if arr[i] == candidate:
        temp += 1

if temp > n / 2:
    print("Majority Element:", candidate)
else:
    print("Majority Element:", -1)
# Sliding Window Technique using Two Pointers

arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter target sum: "))

start = 0
current_sum = 0
found = False

for end in range(len(arr)):
    current_sum += arr[end]


while current_sum > k:
    current_sum -= arr[start]
    start += 1
    
    if current_sum == k:
        found = True
        break

print(found)

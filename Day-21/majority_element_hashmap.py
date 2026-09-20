# Majority Element
# Approach 2: HashMap

nums = list(map(int, input("Enter array elements: ").split()))

n = len(nums)

frequency = {}

for num in nums:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

found = False

for num in frequency:
    if frequency[num] > n // 2:
        print("Majority Element:", num)
        found = True
        break

if not found:
    print("Majority Element:", -1)
# Majority Element
# Approach 3: Sorting

nums = list(map(int, input("Enter array elements: ").split()))

nums.sort()

n = len(nums)

found = False

for i in range(n // 2 + 1):
    if nums[i] == nums[i + n // 2]:
        print("Majority Element:", nums[i])
        found = True
        break

if not found:
    print("Majority Element:", -1)
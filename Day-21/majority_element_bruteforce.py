# Majority Element
# Approach 1: Brute Force

nums = list(map(int, input("Enter array elements: ").split()))

n = len(nums)

for i in range(n):
    count = 0

    for j in range(n):
        if nums[i] == nums[j]:
            count += 1

    if count > n // 2:
        print("Majority Element:", nums[i])
        break
else:
    print("Majority Element:", -1)
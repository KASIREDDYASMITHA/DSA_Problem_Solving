
# Day 66 - Delete and Earn
# Approach: Points Array Construction

nums = [5, 2, 3, 5, 4, 2, 6, 3, 3]

max_value = max(nums)

# Create points array initialized with zeros
pts = [0] * (max_value + 1)

# Calculate total points for each number
for i in range(len(nums)):

    pts[nums[i]] = pts[nums[i]] + nums[i]

print("Original Array:", nums)

print("Points Array:", pts)


# Day 66 - House Robber II
# Approach: Recursion

def solve(nums, start, end):

    if start > end:
        return 0

    take = nums[start] + solve(nums, start + 2, end)

    skip = solve(nums, start + 1, end)

    return max(take, skip)


def rob(nums):

    n = len(nums)

    if n == 0:
        return 0

    if n == 1:
        return nums[0]

    # Case 1: Exclude the last house
    case1 = solve(nums, 0, n - 2)

    # Case 2: Exclude the first house
    case2 = solve(nums, 1, n - 1)

    return max(case1, case2)


nums = [2, 7, 9, 3, 1]

print("Maximum Money:", rob(nums))

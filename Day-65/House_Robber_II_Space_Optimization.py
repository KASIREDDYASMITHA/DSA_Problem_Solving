
# Day 66 - House Robber II
# Approach: Space Optimization

def solve(nums, start, end):

    prev2 = 0
    prev1 = 0

    for i in range(start, end + 1):

        take = nums[i] + prev2

        skip = prev1

        current = max(take, skip)

        prev2 = prev1

        prev1 = current

    return prev1


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


# Day 66 - House Robber II
# Approach: Memoization (Top-Down DP)

def solve(nums, start, end, dp):

    if start > end:
        return 0

    if dp[start] != -1:
        return dp[start]

    take = nums[start] + solve(nums, start + 2, end, dp)

    skip = solve(nums, start + 1, end, dp)

    dp[start] = max(take, skip)

    return dp[start]


def rob(nums):

    n = len(nums)

    if n == 0:
        return 0

    if n == 1:
        return nums[0]

    # Case 1: Exclude the last house
    dp1 = [-1] * n
    case1 = solve(nums, 0, n - 2, dp1)

    # Case 2: Exclude the first house
    dp2 = [-1] * n
    case2 = solve(nums, 1, n - 1, dp2)

    return max(case1, case2)


nums = [2, 7, 9, 3, 1]

print("Maximum Money:", rob(nums))

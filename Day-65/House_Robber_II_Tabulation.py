
# Day 66 - House Robber II
# Approach: Tabulation (Bottom-Up DP)

def solve(nums, start, end):

    size = end - start + 1

    dp = [0] * (size + 2)

    for i in range(end, start - 1, -1):

        index = i - start

        take = nums[i] + dp[index + 2]

        skip = dp[index + 1]

        dp[index] = max(take, skip)

    return dp[0]


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

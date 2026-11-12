
# DSA Day 64
# Problem: House Robber
# Approaches:
# 1. Recursion
# 2. Top-Down DP (Memoization)


# 1. Recursion
def house_robber_recursion(nums):
    n = len(nums)

    def solve(i):
        if i < 0:
            return 0

        if i == 0:
            return nums[0]

        rob = nums[i] + solve(i - 2)

        skip = solve(i - 1)

        return max(rob, skip)

    return solve(n - 1)


# 2. Top-Down DP (Memoization)
def house_robber_memoization(nums):
    n = len(nums)

    dp = [-1] * n

    def solve(i):
        if i < 0:
            return 0

        if i == 0:
            return nums[0]

        if dp[i] != -1:
            return dp[i]

        rob = nums[i] + solve(i - 2)

        skip = solve(i - 1)

        dp[i] = max(rob, skip)

        return dp[i]

    return solve(n - 1)


# Main Program
nums = list(map(int, input("Enter the house amounts separated by spaces: ").split()))

if len(nums) == 0:
    print("Maximum money: 0")
else:
    print("\nHouse Robber Problem")

    print("Recursion:", house_robber_recursion(nums))

    print("Memoization:", house_robber_memoization(nums))

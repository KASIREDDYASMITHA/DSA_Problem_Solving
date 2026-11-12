
# DSA Day 64
# Problem: Minimum Cost Climbing Stairs
# Approaches:
# 1. Recursion
# 2. Top-Down DP (Memoization)
# 3. Bottom-Up DP (Tabulation)
# 4. Space Optimization


# 1. Recursion
def min_cost_recursion(cost):
    n = len(cost)

    def solve(i):
        if i == 0:
            return cost[0]

        if i == 1:
            return cost[1]

        return cost[i] + min(solve(i - 1), solve(i - 2))

    return min(solve(n - 1), solve(n - 2))


# 2. Top-Down DP (Memoization)
def min_cost_memoization(cost):
    n = len(cost)
    dp = [-1] * n

    def solve(i):
        if i == 0:
            return cost[0]

        if i == 1:
            return cost[1]

        if dp[i] != -1:
            return dp[i]

        dp[i] = cost[i] + min(solve(i - 1), solve(i - 2))

        return dp[i]

    return min(solve(n - 1), solve(n - 2))


# 3. Bottom-Up DP (Tabulation)
def min_cost_tabulation(cost):
    n = len(cost)

    dp = [0] * n

    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

    return min(dp[n - 1], dp[n - 2])


# 4. Space Optimization
def min_cost_space_optimization(cost):
    n = len(cost)

    prev2 = cost[0]
    prev1 = cost[1]

    for i in range(2, n):
        current = cost[i] + min(prev1, prev2)

        prev2 = prev1
        prev1 = current

    return min(prev1, prev2)


# Main Program
cost = list(map(int, input("Enter the stair costs separated by spaces: ").split()))

if len(cost) < 2:
    print("Enter at least two stair costs.")
else:
    print("\nMinimum Cost Climbing Stairs")

    print("Recursion:", min_cost_recursion(cost))

    print("Memoization:", min_cost_memoization(cost))

    print("Tabulation:", min_cost_tabulation(cost))

    print("Space Optimization:", min_cost_space_optimization(cost))

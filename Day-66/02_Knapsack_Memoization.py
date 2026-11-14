
# Day 66 - 0/1 Knapsack Using Memoization

def solve(profit, weight, n, capacity, dp):

    # Base condition
    if n == 0 or capacity == 0:
        return 0

    # Check whether the result is already calculated
    if dp[n][capacity] != -1:
        return dp[n][capacity]

    # If current item's weight is greater than capacity
    if weight[n - 1] > capacity:

        dp[n][capacity] = solve(
            profit,
            weight,
            n - 1,
            capacity,
            dp
        )

    else:

        # Don't take the current item
        dontTake = solve(
            profit,
            weight,
            n - 1,
            capacity,
            dp
        )

        # Take the current item
        take = profit[n - 1] + solve(
            profit,
            weight,
            n - 1,
            capacity - weight[n - 1],
            dp
        )

        dp[n][capacity] = max(dontTake, take)

    return dp[n][capacity]


# Main program
profit = [60, 100, 120]
weight = [10, 20, 30]

capacity = 50
n = len(profit)

# Create DP table initialized with -1
dp = [[-1 for j in range(capacity + 1)]
      for i in range(n + 1)]

result = solve(profit, weight, n, capacity, dp)

print("Maximum Profit:", result)

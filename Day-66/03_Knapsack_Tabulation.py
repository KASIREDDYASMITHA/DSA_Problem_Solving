
# Day 66 - 0/1 Knapsack Using Tabulation

profit = [60, 100, 120]
weight = [10, 20, 30]

capacity = 50
n = len(profit)

# Create DP table
dp = [[0 for j in range(capacity + 1)]
      for i in range(n + 1)]

# First row and first column are already initialized to 0

# Fill the DP table
for i in range(1, n + 1):

    for j in range(1, capacity + 1):

        # If current item's weight is greater than capacity
        if weight[i - 1] > j:

            dp[i][j] = dp[i - 1][j]

        else:

            # Don't take the current item
            dontTake = dp[i - 1][j]

            # Take the current item
            take = profit[i - 1] + dp[i - 1][j - weight[i - 1]]

            dp[i][j] = max(dontTake, take)


# Final answer
print("Maximum Profit:", dp[n][capacity])

# Display DP table
print("\nDP Table:")

for i in range(n + 1):
    print(dp[i])

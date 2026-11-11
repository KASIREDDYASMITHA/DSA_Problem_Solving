
# Minimum Cost Climbing Stairs using Dynamic Programming

cost = list(map(int, input("Enter the stair costs separated by spaces: ").split()))

n = len(cost)

if n < 2:
    print("Please enter at least two stair costs.")

else:
    dp = [0] * n

    # Base cases
    dp[0] = cost[0]
    dp[1] = cost[1]

    # Calculate minimum cost for remaining stairs
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

    # Minimum cost to reach the top
    result = min(dp[n - 1], dp[n - 2])

    print("Minimum cost to reach the top:", result)

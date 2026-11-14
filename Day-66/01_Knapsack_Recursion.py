
# Day 66 - 0/1 Knapsack Using Recursion

def solve(profit, weight, n, capacity):

    # Base condition
    if n == 0 or capacity == 0:
        return 0

    # If current item's weight is greater than capacity
    if weight[n - 1] > capacity:
        return solve(profit, weight, n - 1, capacity)

    else:
        # Don't take the current item
        dontTake = solve(profit, weight, n - 1, capacity)

        # Take the current item
        take = profit[n - 1] + solve(
            profit,
            weight,
            n - 1,
            capacity - weight[n - 1]
        )

        return max(dontTake, take)


# Main program
profit = [60, 100, 120]
weight = [10, 20, 30]

capacity = 50
n = len(profit)

result = solve(profit, weight, n, capacity)

print("Maximum Profit:", result)

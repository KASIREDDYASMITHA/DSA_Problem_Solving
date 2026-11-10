
# DSA Day 62 - Fibonacci Using Bottom-Up DP
# Tabulation Approach

# Function to calculate Fibonacci number
def fib(n):

    # Create DP array
    dp = [0] * (n + 1)

    # Base conditions
    dp[0] = 0

    if n >= 1:
        dp[1] = 1

    # Calculate Fibonacci values using iteration
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    # Return final result
    return dp[n]


# Taking input from user
n = int(input("Enter the value of n: "))

# Displaying result
print("Fibonacci number:", fib(n))

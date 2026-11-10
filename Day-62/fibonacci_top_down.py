
# DSA Day 62 - Fibonacci Using Top-Down DP
# Memoization Approach

# Function to initialize DP array
def fib(n):
    dp = [-1] * (n + 1)

    return fun(n, dp)


# Recursive function with memoization
def fun(n, dp):

    # Base condition
    if n == 0 or n == 1:
        return n

    # Check whether the result is already calculated
    if dp[n] != -1:
        return dp[n]

    # Calculate and store the result
    dp[n] = fun(n - 1, dp) + fun(n - 2, dp)

    return dp[n]


# Taking input from user
n = int(input("Enter the value of n: "))

# Displaying result
print("Fibonacci number:", fib(n))

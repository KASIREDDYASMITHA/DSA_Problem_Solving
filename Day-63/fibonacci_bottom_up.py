
# Fibonacci Series using Bottom-Up Dynamic Programming

n = int(input("Enter the value of n: "))

if n < 0:
    print("Please enter a non-negative number.")

else:
    dp = [0] * (n + 1)

    dp[0] = 0

    if n >= 1:
        dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print("Fibonacci number:", dp[n])

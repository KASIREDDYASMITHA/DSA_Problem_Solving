# Stock Span Problem
# Approach: Brute Force

n = int(input("Enter number of days: "))

price = list(map(int, input("Enter stock prices: ").split()))

res = [0] * n

# First day always has span 1
res[0] = 1

# Traverse from the second day
for i in range(1, n):

    count = 1

    # Check previous days
    for j in range(i - 1, -1, -1):

        if price[j] <= price[i]:
            count += 1
        else:
            break

    res[i] = count

print("Stock Span:", res)
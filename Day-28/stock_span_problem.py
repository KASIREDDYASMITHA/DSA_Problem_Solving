# Day 28
# Problem: Stock Span Problem
# Approach: Stack

n = int(input("Enter number of days: "))

price = list(map(int, input("Enter stock prices: ").split()))

res = [0] * n

# Create an empty stack
st = []

res[0] = 1
st.append(0)

for i in range(1, n):

    # Remove indices whose prices are less than
    # or equal to the current price
    while len(st) > 0 and price[st[-1]] <= price[i]:
        st.pop()

    # If stack is empty, all previous days
    # have smaller or equal prices
    if len(st) == 0:
        res[i] = i + 1

    # Otherwise, calculate the distance
    # from the nearest greater price
    else:
        res[i] = i - st[-1]

    # Push current day's index
    st.append(i)

print("Stock Span:", res)

# Time Complexity: O(n)
# Space Complexity: O(n)
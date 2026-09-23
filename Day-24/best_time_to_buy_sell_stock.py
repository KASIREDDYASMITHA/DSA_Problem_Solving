# Best Time to Buy and Sell Stock
# Greedy Approach

prices = list(map(int, input("Enter stock prices: ").split()))

minPrice = float('inf')
maxProfit = 0

for i in range(len(prices)):

    if prices[i] < minPrice:
        minPrice = prices[i]

    else:
        profit = prices[i] - minPrice

        if profit > maxProfit:
            maxProfit = profit

print("Maximum Profit:", maxProfit)
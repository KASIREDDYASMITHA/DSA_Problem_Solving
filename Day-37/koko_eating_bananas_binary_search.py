import math

piles = [int(x) for x in input("Enter the banana piles separated by spaces: ").split()]
h = int(input("Enter the maximum hours available: "))

low = 1
high = max(piles)
ans = high

while low <= high:
    mid = low + (high - low) // 2

    total_hours = 0

    for pile in piles:
        total_hours += math.ceil(pile / mid)

    if total_hours <= h:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print("Minimum eating speed required (Binary Search):", ans)
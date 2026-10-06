import math

piles = [int(x) for x in input("Enter the banana piles separated by spaces: ").split()]
h = int(input("Enter the maximum hours available: "))

max_pile = max(piles)
ans = max_pile

for speed in range(1, max_pile + 1):
    total_hours = 0

    for pile in piles:
        total_hours += math.ceil(pile / speed)

    if total_hours <= h:
        ans = speed
        break

print("Minimum eating speed required (Brute Force):", ans)
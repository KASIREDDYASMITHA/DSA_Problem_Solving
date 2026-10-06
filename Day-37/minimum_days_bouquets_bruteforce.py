bloomDay = [int(x) for x in input("Enter the bloom days separated by spaces: ").split()]
m = int(input("Enter the number of bouquets needed: "))
k = int(input("Enter the number of adjacent flowers per bouquet: "))

if m * k > len(bloomDay):
    print("Minimum days required: -1")
else:
    min_day = min(bloomDay)
    max_day = max(bloomDay)
    ans = -1

    for day in range(min_day, max_day + 1):
        bouquets = 0
        consecutive_flowers = 0

        for flower_day in bloomDay:
            if flower_day <= day:
                consecutive_flowers += 1
            else:
                bouquets += consecutive_flowers // k
                consecutive_flowers = 0

        bouquets += consecutive_flowers // k

        if bouquets >= m:
            ans = day
            break

    print("Minimum days required (Brute Force):", ans)
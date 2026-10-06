bloomDay = [int(x) for x in input("Enter the bloom days separated by spaces: ").split()]
m = int(input("Enter the number of bouquets needed: "))
k = int(input("Enter the number of adjacent flowers per bouquet: "))

if m * k > len(bloomDay):
    print("Minimum days required: -1")
else:
    low = min(bloomDay)
    high = max(bloomDay)
    ans = high

    while low <= high:
        mid = low + (high - low) // 2

        bouquets = 0
        consecutive_flowers = 0

        for flower_day in bloomDay:
            if flower_day <= mid:
                consecutive_flowers += 1
            else:
                bouquets += consecutive_flowers // k
                consecutive_flowers = 0

        bouquets += consecutive_flowers // k

        if bouquets >= m:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    print("Minimum days required (Binary Search):", ans)
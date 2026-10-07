weights = list(map(int, input("Enter package weights separated by space: ").split()))
days = int(input("Enter number of days allowed: "))

low = max(weights)
high = sum(weights)
ans = high

while low <= high:
    mid = low + (high - low) // 2

    required_days = 1
    current_weight = 0

    for weight in weights:
        if current_weight + weight <= mid:
            current_weight += weight
        else:
            required_days += 1
            current_weight = weight

    if required_days <= days:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print("Minimum ship capacity required:", ans)
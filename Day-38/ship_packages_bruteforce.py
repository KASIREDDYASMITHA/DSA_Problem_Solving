#ship_packages_bruteforce

weights = list(map(int, input("Enter package weights separated by space: ").split()))
days = int(input("Enter number of days allowed: "))

low = max(weights)
high = sum(weights)

ans = high

for capacity in range(low, high + 1):
    required_days = 1
    current_weight = 0

    for weight in weights:
        if current_weight + weight <= capacity:
            current_weight += weight
        else:
            required_days += 1
            current_weight = weight

    if required_days <= days:
        ans = capacity
        break

print("Minimum ship capacity required:", ans)
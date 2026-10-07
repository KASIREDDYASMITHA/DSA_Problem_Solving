boards = list(map(int, input("Enter board lengths separated by space: ").split()))
k = int(input("Enter number of painters (k): "))

low = max(boards)
high = sum(boards)

ans = high

for max_time in range(low, high + 1):
    painters_needed = 1
    current_time = 0

    for board in boards:
        if current_time + board <= max_time:
            current_time += board
        else:
            painters_needed += 1
            current_time = board

    if painters_needed <= k:
        ans = max_time
        break

print("Minimum time required to paint all boards:", ans)
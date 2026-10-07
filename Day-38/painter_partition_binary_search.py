boards = list(map(int, input("Enter board lengths separated by space: ").split()))
k = int(input("Enter number of painters (k): "))

low = max(boards)
high = sum(boards)
ans = high

while low <= high:
    mid = low + (high - low) // 2

    painters_needed = 1
    current_time = 0

    for board in boards:
        if current_time + board <= mid:
            current_time += board
        else:
            painters_needed += 1
            current_time = board

    if painters_needed <= k:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print("Minimum time required to paint all boards:", ans)
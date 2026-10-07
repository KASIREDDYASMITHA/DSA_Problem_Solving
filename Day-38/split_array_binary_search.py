nums = list(map(int, input("Enter array numbers separated by space: ").split()))
k = int(input("Enter number of subarrays (k): "))

low = max(nums)
high = sum(nums)
ans = high

while low <= high:
    mid = low + (high - low) // 2

    required_subarrays = 1
    current_sum = 0

    for num in nums:
        if current_sum + num <= mid:
            current_sum += num
        else:
            required_subarrays += 1
            current_sum = num

    if required_subarrays <= k:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print("Minimum largest subarray sum:", ans)
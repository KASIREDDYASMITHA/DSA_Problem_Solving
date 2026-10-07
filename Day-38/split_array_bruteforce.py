nums = list(map(int, input("Enter array numbers separated by space: ").split()))
k = int(input("Enter number of subarrays (k): "))

low = max(nums)
high = sum(nums)

ans = high

for max_sum in range(low, high + 1):
    required_subarrays = 1
    current_sum = 0

    for num in nums:
        if current_sum + num <= max_sum:
            current_sum += num
        else:
            required_subarrays += 1
            current_sum = num

    if required_subarrays <= k:
        ans = max_sum
        break

print("Minimum largest subarray sum:", ans)
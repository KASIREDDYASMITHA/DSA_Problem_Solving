# Container With Most Water
# Two Pointer Approach

arr = list(map(int, input().split()))

result = float('-inf')

left = 0
right = len(arr) - 1

while left < right:
    length = right - left

    breadth = min(arr[left], arr[right])

    area = length * breadth

    result = max(result, area)

    if arr[left] < arr[right]:
        left += 1
    else:
        right -= 1

print(result)
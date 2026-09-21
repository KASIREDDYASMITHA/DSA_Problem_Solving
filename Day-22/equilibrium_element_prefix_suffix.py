# Day 22 - Equilibrium Element
# Approach 2: Prefix Sum + Suffix Sum
#
# Problem:
# Find an index where the sum of elements on the left side
# is equal to the sum of elements on the right side.
#
# Approach:
# - left[i] stores the sum of elements from index 0 to i.
# - right[i] stores the sum of elements from index i to n-1.
# - For every index, compare left[i] and right[i].
#
# Note:
# In this approach, the current element is included in both
# prefix and suffix sums.
#
# Pseudocode:
# 1. Take the array as input.
# 2. Create a left array of size n.
# 3. Create a right array of size n.
# 4. Store prefix sums in the left array.
# 5. Store suffix sums in the right array.
# 6. Compare left[i] and right[i] for every index.
# 7. If they are equal, print the index.
# 8. If no equilibrium index exists, print -1.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

arr = list(map(int, input().split()))

n = len(arr)

left = [0] * n
right = [0] * n

# Calculate prefix sums
left[0] = arr[0]

for i in range(1, n):
    left[i] = left[i - 1] + arr[i]

# Calculate suffix sums
right[n - 1] = arr[n - 1]

for i in range(n - 2, -1, -1):
    right[i] = right[i + 1] + arr[i]

# Find equilibrium index
for i in range(n):
    if left[i] == right[i]:
        print(i)
        break
else:
    print(-1)
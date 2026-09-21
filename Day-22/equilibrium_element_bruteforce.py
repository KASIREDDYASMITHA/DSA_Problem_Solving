# Day 22 - Equilibrium Element
# Approach 1: Brute Force
#
# Problem:
# Find an index where the sum of elements on the left side
# is equal to the sum of elements on the right side.
#
# The element at the equilibrium index is not included
# in either side.
#
# Example:
# Input:
# 1 3 5 2 2
#
# Output:
# 2
#
# Explanation:
# Left sum  = 1 + 3 = 4
# Right sum = 2 + 2 = 4
#
# Therefore, index 2 is the equilibrium index.
#
# Pseudocode:
# 1. Take the array as input.
# 2. Traverse every index.
# 3. Calculate the sum of elements before the index.
# 4. Calculate the sum of elements after the index.
# 5. Compare the left sum and right sum.
# 6. If both are equal, print the index.
# 7. If no equilibrium index exists, print -1.
#
# Time Complexity: O(n^2)
# Space Complexity: O(1)

arr = list(map(int, input().split()))

n = len(arr)

for i in range(n):

    lsum = 0

    # Calculate left sum
    for j in range(0, i):
        lsum = lsum + arr[j]

    rsum = 0

    # Calculate right sum
    for j in range(i + 1, n):
        rsum = rsum + arr[j]

    if lsum == rsum:
        print(i)
        break

else:
    print(-1)
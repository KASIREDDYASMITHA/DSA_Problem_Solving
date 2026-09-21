# Day 22 - Equilibrium Element
# Approach 3: Total Sum + Running Left Sum
#
# Problem:
# Find an index where the sum of elements on the left side
# is equal to the sum of elements on the right side.
#
# Approach:
# First calculate the total sum of the array.
#
# At every index:
#
# rightSum = totalSum - leftSum - arr[i]
#
# Here:
# - totalSum = sum of all elements
# - leftSum = sum of elements before the current index
# - arr[i] = current element
#
# After checking the current index, add arr[i] to leftSum
# so that it becomes the left sum for the next index.
#
# Pseudocode:
# 1. Take the array as input.
# 2. Calculate the total sum of the array.
# 3. Set leftSum = 0.
# 4. Traverse the array.
# 5. Calculate rightSum using:
#       rightSum = totalSum - leftSum - arr[i]
# 6. Compare leftSum and rightSum.
# 7. If they are equal, print the index.
# 8. Add arr[i] to leftSum.
# 9. If no equilibrium index exists, print -1.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

arr = list(map(int, input().split()))

n = len(arr)

# Calculate total sum
totalSum = 0

for i in range(n):
    totalSum = totalSum + arr[i]

# Initialize left sum
leftSum = 0

# Find equilibrium index
for i in range(n):

    # Calculate right sum
    rightSum = totalSum - leftSum - arr[i]

    # Compare left sum and right sum
    if leftSum == rightSum:
        print(i)
        break

    # Add current element to left sum
    leftSum = leftSum + arr[i]

else:
    print(-1)
# ============================================================
# DSA Day 35
# Question 2: Integer Square Root
# Approach: Binary Search
# ============================================================

# Problem:
# Given a non-negative integer x, find the square root of x
# rounded down to the nearest integer.
#
# Example:
# Input:
# 8
#
# Output:
# 2
#
# Because:
# 2 * 2 = 4 <= 8
# 3 * 3 = 9 > 8
#
# Therefore answer = 2


n = int(input("Enter a non-negative integer: "))

if n == 0:

    answer = 0

else:

    low = 1
    high = n
    answer = 0

    while low <= high:

        mid = low + (high - low) // 2

        if mid * mid <= n:

            answer = mid
            low = mid + 1

        else:

            high = mid - 1

print("Integer Square Root:", answer)
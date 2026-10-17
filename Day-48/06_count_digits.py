
# DSA Day 48
# Count Digits Using Recursion

# Approach:
# count_digits(n) = 1 + count_digits(n // 10)
# Base case: n < 10

n = int(input("Enter an integer: "))


def count_digits(n):
    if n < 10:
        return 1

    return 1 + count_digits(n // 10)


n = abs(n)
print("Number of digits:", count_digits(n))

# Example 1:
# Input: 4567
# Output: 4

# Example 2:
# Input: 0
# Output: 1

# Time Complexity: O(d)
# Auxiliary Space: O(d)
# d = number of digits

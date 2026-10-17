
# DSA Day 48
# Sum of Digits Using Recursion

# Approach:
# sum_digits(n) = n % 10 + sum_digits(n // 10)
# Base case: n == 0

n = int(input("Enter an integer: "))


def sum_digits(n):
    if n == 0:
        return 0

    return n % 10 + sum_digits(n // 10)


n = abs(n)
print("Sum of digits:", sum_digits(n))

# Example 1:
# Input: 1234
# Output: 10

# Example 2:
# Input: -567
# Output: 18

# Time Complexity: O(d)
# Auxiliary Space: O(d)
# d = number of digits

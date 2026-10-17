
# DSA Day 48
# Power of a Number Using Recursion

# Approach:
# power(x, n) = x * power(x, n - 1)
# Base case: power(x, 0) = 1

x = float(input("Enter the base: "))
n = int(input("Enter a non-negative exponent: "))


def power(x, n):
    if n == 0:
        return 1

    return x * power(x, n - 1)


if n < 0:
    print("Please enter a non-negative exponent.")
else:
    print("Result:", power(x, n))

# Example:
# Base: 2
# Exponent: 4
# Output: 16.0

# Time Complexity: O(n)
# Auxiliary Space: O(n)

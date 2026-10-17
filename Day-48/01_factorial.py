
# DSA Day 48
# Factorial of a Number Using Recursion

# Approach:
# factorial(n) = n * factorial(n - 1)
# Base case: factorial(0) = 1

n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative integers.")
else:
    def factorial(n):
        if n == 0:
            return 1

        return n * factorial(n - 1)

    print("Factorial:", factorial(n))

# Example:
# Input: 5
# Output: Factorial: 120

# Time Complexity: O(n)
# Auxiliary Space: O(n)

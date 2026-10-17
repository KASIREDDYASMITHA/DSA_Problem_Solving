
# DSA Day 48
# Recursion Time Complexity and Back Substitution

# Recurrence 1:
# T(n) = 1 + n * T(n - 1), for n >= 1
# T(0) = 1
#
# Expansion:
# T(n) = 1 + n * T(n - 1)
#      = 1 + n * (1 + (n - 1) * T(n - 2))
#      = 1 + n + n * (n - 1) * T(n - 2)
#
# This recurrence grows factorially.
# Time Complexity: O(n!)

# Recurrence 2:
# T(n) = T(n - 1) + n, for n >= 2
# T(1) = 1
#
# Expansion:
# T(n) = T(n - 1) + n
#      = T(n - 2) + (n - 1) + n
#      = T(1) + 2 + 3 + ... + n
#
# Sum of first n integers is O(n^2).
# Time Complexity: O(n^2)


# Program 1: Demonstrate repeated recursive calls
def fun1(n):
    if n == 0:
        return

    for k in range(1, n + 1):
        fun1(n - 1)


n = int(input("Enter n for fun1: "))

if n < 0:
    print("Enter a non-negative integer.")
else:
    fun1(n)
    print("fun1 completed for n =", n)


# Program 2: Calculate the recurrence T(n) = T(n - 1) + n
def recurrence(n):
    if n == 1:
        return 1

    return recurrence(n - 1) + n


n = int(input("Enter n for the second recurrence (n >= 1): "))

if n < 1:
    print("Enter an integer greater than or equal to 1.")
else:
    print("T(n) =", recurrence(n))

# Note:
# fun1 demonstrates the first recurrence's recursive-call pattern.
# The second function calculates the second recurrence's value.

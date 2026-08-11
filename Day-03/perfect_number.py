# Day 3 - Perfect Number

# A perfect number is a number whose positive divisors,
# excluding the number itself, add up to the number.
#
# Example:
# 6 -> 1 + 2 + 3 = 6
#
# 28 -> 1 + 2 + 4 + 7 + 14 = 28


# Approach 1: Brute Force
# Time Complexity: O(n)
# Space Complexity: O(1)

n = int(input("Enter a number: "))

s = 0

for i in range(1, n):
    if n % i == 0:
        s += i

if s == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")


# Approach 2: Optimized using Square Root
# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)

import math

n = int(input("Enter a number: "))

if n <= 1:
    print("Not a Perfect Number")
else:
    s = 1

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            s += i

            pair = n // i

            if pair != i:
                s += pair

    if s == n:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")
# Day 3 - Prime Number

# Approach 1: Brute Force
# Time Complexity: O(n)
# Space Complexity: O(1)

n = int(input("Enter n: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")


# Approach 2: Optimized using Square Root
# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)

import math


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


n = int(input("Enter a number: "))

if is_prime(n):
    print("Prime")
else:
    print("Not Prime")
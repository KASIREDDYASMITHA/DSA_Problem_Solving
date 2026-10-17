
# DSA Day 48
# Basic Backtracking Example: Generate Binary Strings

# Approach:
# Try 0 at the current position.
# Recursively explore the next position.
# Undo the choice and try 1.
# Base case: the string reaches the required length.

n = int(input("Enter the length of binary strings: "))


def generate_binary_strings(n, current):
    if len(current) == n:
        print(current)
        return

    current.append(0)
    generate_binary_strings(n, current)
    current.pop()

    current.append(1)
    generate_binary_strings(n, current)
    current.pop()


if n < 0:
    print("Enter a non-negative integer.")
else:
    generate_binary_strings(n, [])

# Example:
# Input: 2
# Output:
# [0, 0]
# [0, 1]
# [1, 0]
# [1, 1]

# Time Complexity: O(2^n)
# Auxiliary Space: O(n), excluding output

# DSA Day 46 - Recursion Print Patterns
# Understand statement execution before and after recursive calls.

# --------------------------------------------------
# Pattern 1: Print before the recursive call
# Example: n = 3
# Output: 3 2 1
# --------------------------------------------------

def print_before(n):
    if n == 0:
        return

    print(n, end=" ")
    print_before(n - 1)


# --------------------------------------------------
# Pattern 2: Print after the recursive call
# Example: n = 3
# Output: 1 2 3
# --------------------------------------------------

def print_after(n):
    if n == 0:
        return

    print_after(n - 1)
    print(n, end=" ")


# --------------------------------------------------
# Pattern 3: Print before and after the recursive call
# Example: n = 2
# Output: 2 1 1 2
# --------------------------------------------------

def print_before_and_after(n):
    if n == 0:
        return

    print(n, end=" ")
    print_before_and_after(n - 1)
    print(n, end=" ")


# --------------------------------------------------
# Pattern 4: Two recursive calls
# Example: n = 2
# Output: 2 1 1 2 1 1
# --------------------------------------------------

def print_with_two_calls(n):
    if n == 0:
        return

    print(n, end=" ")
    print_with_two_calls(n - 1)
    print(n, end=" ")
    print_with_two_calls(n - 1)


# Read input at runtime
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    print("\nPattern 1 - Print before recursion:")
    print_before(n)
    print()

    print("\nPattern 2 - Print after recursion:")
    print_after(n)
    print()

    print("\nPattern 3 - Print before and after recursion:")
    print_before_and_after(n)
    print()

    print("\nPattern 4 - Two recursive calls:")
    print_with_two_calls(n)
    print()
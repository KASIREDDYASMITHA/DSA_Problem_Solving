# DSA Day 46 - Recursion Basics
# Topics: Base case, recursive call, mathematical recursion, and GCD

# --------------------------------------------------
# Program 1: Print numbers from n to 1 using recursion
# --------------------------------------------------

def print_numbers(n):
    # Base case: stop when n becomes 0
    if n == 0:
        return

    # Print the current number before the recursive call
    print(n)

    # Recursive call with a smaller input
    print_numbers(n - 1)


print("Program 1: Print numbers from n to 1")
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    print_numbers(n)


# --------------------------------------------------
# Program 2: f(x) = 2 + f(x - 1), when x >= 1
# Base case: f(x) = 1 otherwise
# --------------------------------------------------

def mathematical_function(x):
    # Base case: f(0) = 1
    if x <= 0:
        return 1

    # Recursive case
    return 2 + mathematical_function(x - 1)


print("\nProgram 2: Mathematical Recursion")
x = int(input("Enter an integer: "))
print("f(", x, ") =", mathematical_function(x), sep="")


# --------------------------------------------------
# Program 3: GCD using recursive subtraction
# --------------------------------------------------

def gcd_recursive(x, y):
    # Handle zero inputs
    if x == 0:
        return y
    if y == 0:
        return x

    # Base case: both numbers are equal
    if x == y:
        return x

    # Recursive case: subtract the smaller number
    if x > y:
        return gcd_recursive(x - y, y)

    return gcd_recursive(x, y - x)


print("\nProgram 3: GCD Using Recursive Subtraction")
a = int(input("Enter the first non-negative integer: "))
b = int(input("Enter the second non-negative integer: "))

if a < 0 or b < 0:
    print("Please enter non-negative integers.")
elif a == 0 and b == 0:
    print("GCD is undefined for 0 and 0.")
else:
    print("GCD =", gcd_recursive(a, b))

"""
DSA Day 9
Topic: Time and Space Complexity

Examples:
1. O(1) - Constant
2. O(n) - Linear
3. O(n/2) - Linear
4. O(log n) - Logarithmic
5. O(n^2) - Quadratic
6. Sum of first n natural numbers
"""


# --------------------------------------------------
# 1. O(1) - Constant Time
# --------------------------------------------------

def constant_operations(x, y):
    """
    A fixed number of operations are performed.

    Time Complexity: O(1)
    """
    a = x + y
    b = x * y
    c = a - b

    return c


# --------------------------------------------------
# 2. O(n) - Linear Time
# --------------------------------------------------

def linear_loop(n):
    """
    Loop runs n times.

    Time Complexity: O(n)
    """
    for i in range(1, n + 1):
        print(i)


# --------------------------------------------------
# 3. O(n/2) -> O(n)
# --------------------------------------------------

def half_loop(n):
    """
    Loop increments by 2.

    Number of iterations is approximately n/2.

    Time Complexity: O(n)
    """
    for i in range(1, n + 1, 2):
        print(i)


# --------------------------------------------------
# 4. O(log n) - Logarithmic Time
# --------------------------------------------------

def logarithmic_loop(n):
    """
    Value is multiplied by 2 in every iteration.

    Time Complexity: O(log n)
    """
    i = 1

    while i <= n:
        print(i)
        i = i * 2


# --------------------------------------------------
# 5. O(n^2) - Quadratic Time
# --------------------------------------------------

def nested_loop(n):
    """
    Outer loop runs n times.
    Inner loop runs n times.

    Total operations = n * n

    Time Complexity: O(n^2)
    """
    count = 0

    for i in range(n):
        for j in range(n):
            count += 1

    return count


# --------------------------------------------------
# 6. Sum using a Loop - O(n)
# --------------------------------------------------

def sum_using_loop(n):
    """
    Calculates:
    1 + 2 + 3 + ... + n

    Time Complexity: O(n)
    """
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


# --------------------------------------------------
# 7. Sum using Formula - O(1)
# --------------------------------------------------

def sum_using_formula(n):
    """
    Formula:
    1 + 2 + 3 + ... + n = n(n + 1) / 2

    Time Complexity: O(1)
    """
    return n * (n + 1) // 2


# --------------------------------------------------
# Main Program
# --------------------------------------------------

if __name__ == "__main__":

    print("O(1) Example:")
    print(constant_operations(5, 3))

    print("\nO(n) Example:")
    linear_loop(5)

    print("\nO(n/2) Example:")
    half_loop(6)

    print("\nO(log n) Example:")
    logarithmic_loop(16)

    print("\nO(n^2) Example:")
    print("Number of operations:", nested_loop(4))

    print("\nSum using loop:")
    print(sum_using_loop(10))

    print("\nSum using formula:")
    print(sum_using_formula(10))
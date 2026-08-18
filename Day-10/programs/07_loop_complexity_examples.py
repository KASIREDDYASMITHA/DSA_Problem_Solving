# Day 10 - Different Loop Complexity Examples


# Example 1: O(n)
def linear_loop(n):
    for i in range(1, n + 1):
        print("hello")


# Example 2: O(n) even though increment is 2
def linear_increment_by_two(n):
    for i in range(1, n + 1, 2):
        print("hello")


# Example 3: O(sqrt(n))
def square_root_loop(n):
    i = 0

    while i < n ** 0.5:
        print("hello")
        i += 1


# Example 4: O(n^2)
def quadratic_loop(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("hello")


# Example 5: O(n^2) dependent nested loop
def dependent_nested_loop(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("hello")


# Example 6: O(n log n)
def linearithmic_loop(n):
    for i in range(1, n + 1):
        j = i

        while j <= n:
            print("hello")
            j *= 2


n = 10

linear_loop(n)
linear_increment_by_two(n)
square_root_loop(n)
quadratic_loop(n)
dependent_nested_loop(n)
linearithmic_loop(n)
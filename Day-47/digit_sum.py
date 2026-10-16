# Take the number as input from the user.
n = int(input("Enter a non-negative number: "))

# Take the base as input from the user.
r = int(input("Enter the base: "))

# Check whether the inputs are valid.
if n < 0 or r < 2:
    print("Enter a non-negative number and a base greater than or equal to 2.")
else:
    # Recursively calculate the sum of digits in base r.
    def foo(n, r):
        if n > 0:
            return (n % r) + foo(n // r, r)
        else:
            return 0

    result = foo(n, r)
    print("Sum of digits in the given base:", result)

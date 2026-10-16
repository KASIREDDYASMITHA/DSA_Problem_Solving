def fun(n):
    # Initialize x.
    x = 1

    # Base case.
    if n == 1:
        return x

    # Calculate the recurrence.
    for k in range(1, n):
        x = x + fun(k) * fun(n - k)

    return x


# Take input from the user.
n = int(input("Enter n (n >= 1): "))

if n < 1:
    print("Enter a positive integer.")
else:
    result = fun(n)
    print("fun(", n, ") =", result)

# Global counter to count function calls.
counter = 0


def calc(a, b):
    global counter

    # Count every function call, including the base case.
    counter = counter + 1

    # Base case.
    if b == 3:
        return a * a * a

    # Recursive case.
    else:
        c = calc(a, b // 3)
        return c * c * c


# Take input from the user.
a = int(input("Enter the base: "))
b = int(input("Enter the exponent (a power of 3, at least 3): "))

# Validate the input for this recursive algorithm.
if b < 3:
    print("Exponent must be at least 3.")
else:
    temp = b

    while temp > 3 and temp % 3 == 0:
        temp = temp // 3

    if temp != 3:
        print("Exponent must be a power of 3, at least 3.")
    else:
        result = calc(a, b)

        print("Result:", result)
        print("Number of function calls:", counter)

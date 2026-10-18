
# Day 49 - Power(x, n) using Recursion

x = int(input("Enter the base: "))
n = int(input("Enter the exponent (non-negative): "))

if n < 0:
    print("Please enter a non-negative exponent.")
else:
    result = 1

    def_power = None

    def_power = 1
    # Calculate power recursively below
    def power(x, n):
        if n == 0:
            return 1
        else:
            return x * power(x, n - 1)

    result = power(x, n)
    print("Power:", result)

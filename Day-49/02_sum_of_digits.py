
# Day 49 - Sum of Digits using Recursion

n = int(input("Enter a non-negative number: "))

if n < 0:
    print("Please enter a non-negative number.")
else:
    def sum_of_digits(n):
        if n == 0:
            return 0
        else:
            return n % 10 + sum_of_digits(n // 10)

    print("Sum of digits:", sum_of_digits(n))

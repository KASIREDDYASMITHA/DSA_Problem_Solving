
# Day 49 - Count Digits using Recursion

n = int(input("Enter an integer: "))

n = abs(n)

def count_digits(n):
    if n <= 9:
        return 1
    else:
        return 1 + count_digits(n // 10)

print("Number of digits:", count_digits(n))

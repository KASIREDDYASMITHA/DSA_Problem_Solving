
# Fibonacci Series using Space Optimization

n = int(input("Enter the value of n: "))

if n < 0:
    print("Please enter a non-negative number.")

elif n == 0:
    print("Fibonacci number:", 0)

elif n == 1:
    print("Fibonacci number:", 1)

else:
    first = 0
    second = 1

    for i in range(2, n + 1):
        res = first + second

        first = second
        second = res

    print("Fibonacci number:", res)

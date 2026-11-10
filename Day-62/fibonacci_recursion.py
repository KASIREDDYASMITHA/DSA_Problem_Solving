
# DSA Day 62 - Fibonacci Using Recursion

# Function to calculate Fibonacci number
def fib(n):

    # Base condition
    if n == 0 or n == 1:
        return n

    # Recursive calls
    else:
        return fib(n - 1) + fib(n - 2)


# Taking input from user
n = int(input("Enter the value of n: "))

# Displaying result
print("Fibonacci number:", fib(n))

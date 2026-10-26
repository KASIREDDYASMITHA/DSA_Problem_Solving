# DSA Day 54 - Backtracking
# Program: Generate all binary strings of length n

n = int(input("Enter the length of the binary string: "))

def fun(n, i, temp):
    if i == n:
        print(temp)
        return

    fun(n, i + 1, temp + "0")
    fun(n, i + 1, temp + "1")


print("Binary strings are:")
fun(n, 0, "")
n = int(input("Enter n: "))

# First row
for i in range(n):
    print("*", end=" ")
print()

# Middle rows
for i in range(n - 2):
    print("*", end=" ")

    for j in range(n - 2):
        print(" ", end=" ")

    print("*")

# Last row
for i in range(n):
    print("*", end=" ")
print()
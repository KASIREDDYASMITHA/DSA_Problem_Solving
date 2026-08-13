n = int(input("Enter n: "))

for i in range(n, 0, -1):

    # Print spaces
    for j in range(1, n - i + 1):
        print(" ", end="")

    # Print stars
    for j in range(1, i + 1):
        print("*", end="")

    print()
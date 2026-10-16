import sys
# Allow the deep recursion used in the faculty example.
sys.setrecursionlimit(20000)

# Store the number of print executions.
print_count = 0


def Count(x, y):
    global print_count

    if y != 1:
        if x != 1:
            # This represents print("*").
            print_count = print_count + 1

            # Recursively divide x by 2.
            Count(x // 2, y)
        else:
            # Decrease y and restart with x = 1024.
            y = y - 1
            Count(1024, y)


# Take input from the user.
x = int(input("Enter x: "))
y = int(input("Enter y: "))

# Count the executions.
Count(x, y)

print("Number of print executions:", print_count)

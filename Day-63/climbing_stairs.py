
# Climbing Stairs - Number of Ways

def climbStairs(n):

    if n < 0:
        return 0

    if n == 0:
        return 1

    else:
        return climbStairs(n - 1) + climbStairs(n - 2)


n = int(input("Enter the number of stairs: "))

if n < 0:
    print("Please enter a non-negative number.")
else:
    print("Number of ways:", climbStairs(n))

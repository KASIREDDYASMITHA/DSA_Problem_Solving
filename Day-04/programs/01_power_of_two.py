# Power of Two Check

n = int(input("Enter a number: "))

if n <= 0:
    print("Not a Power of 2")
else:
    while n % 2 == 0:
        n = n // 2

    if n == 1:
        print("Power of 2")
    else:
        print("Not a Power of 2")
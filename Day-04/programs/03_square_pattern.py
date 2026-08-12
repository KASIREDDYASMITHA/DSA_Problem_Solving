# Square Pattern of Stars

n = int(input("Enter a number: "))

for i in range(n):
    s = ""

    for j in range(n):
        s = s + "*"

    print(s)
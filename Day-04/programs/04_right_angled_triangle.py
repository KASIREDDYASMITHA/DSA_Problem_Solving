# Right-Angled Star Triangle

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    s = ""

    for j in range(1, i + 1):
        s = s + "*"

    print(s)
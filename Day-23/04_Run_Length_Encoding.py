# Day 23 - Run-Length Encoding

s = input("Enter a string: ")

if len(s) == 0:
    print("")
else:
    result = ""
    count = 1

    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            count += 1
        else:
            result = result + s[i] + str(count)
            count = 1

    print("Encoded string:", result)
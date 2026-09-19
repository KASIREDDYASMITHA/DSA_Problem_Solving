
# Longest Substring Without Repeating Characters - Brute Force

s = input("Enter a string: ")

res = 0

for i in range(len(s)):
    s1 = ""

    for j in range(i, len(s)):
        s1 = s1 + s[j]

        # Check whether s1 has duplicate characters
        seen = set()
        duplicate = False

        for ch in s1:
            if ch in seen:
                duplicate = True
                break

            seen.add(ch)

        if duplicate:
            break
        else:
            res = max(res, len(s1))

print("Length of longest substring:", res)
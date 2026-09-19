
# Longest Substring With Exactly K Unique Characters - Brute Force

s = input("Enter string: ")
k = int(input("Enter k: "))

result = 0

for i in range(len(s)):
    for j in range(i, len(s)):

        # Generate substring
        substring = s[i:j + 1]

        # Create set of unique characters
        unique = set()

        for ch in substring:
            unique.add(ch)

        # Check exactly k unique characters
        if len(unique) == k:
            if len(substring) > result:
                result = len(substring)

print("Longest substring length:", result)
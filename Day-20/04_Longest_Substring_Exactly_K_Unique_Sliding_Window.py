
# Longest Substring With Exactly K Unique Characters - Sliding Window

s = input("Enter string: ")
k = int(input("Enter k: "))

mp = {}
start = 0
result = 0

for end in range(len(s)):
    ch = s[end]

    # Increase frequency of current character
    if ch in mp:
        mp[ch] = mp[ch] + 1
    else:
        mp[ch] = 1

    # If unique characters are more than k,
    # move start forward
    while len(mp) > k:
        left = s[start]

        mp[left] = mp[left] - 1

        if mp[left] == 0:
            del mp[left]

        start = start + 1

    # Check if current window has exactly k unique characters
    if len(mp) == k:
        result = max(result, end - start + 1)

print("Longest substring length:", result)
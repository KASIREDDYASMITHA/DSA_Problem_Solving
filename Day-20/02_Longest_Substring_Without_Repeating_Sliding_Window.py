# Longest Substring Without Repeating Characters - Sliding Window

s = input("Enter a string: ")

mp = {}
start = 0
ans = 0

for end in range(len(s)):
    ch = s[end]

    # Increase frequency of current character
    if ch in mp:
        mp[ch] = mp[ch] + 1
    else:
        mp[ch] = 1

    # If duplicate exists, move start forward
    while mp[ch] > 1:
        left = s[start]

        mp[left] = mp[left] - 1

        if mp[left] == 0:
            del mp[left]

        start = start + 1

    # Current window = start to end
    ans = max(ans, end - start + 1)

print("Length of longest substring:", ans)
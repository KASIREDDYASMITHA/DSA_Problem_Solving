# Day 22 - Valid Anagram
# Approach 2: HashMap / Dictionary
#
# Problem:
# Given two strings s and t, check whether t is an anagram of s.
#
# Example:
# s = "listen"
# t = "silent"
# Output: True
#
# Approach:
# Store the frequency of every character in the first string.
# Then decrease the frequency using the characters of the second string.
#
# Pseudocode:
# 1. Take two strings as input.
# 2. If their lengths are different, print False.
# 3. Create an empty hashmap.
# 4. Count the frequency of every character in the first string.
# 5. Traverse the second string.
# 6. Decrease the frequency of each character.
# 7. If a character does not exist or its frequency becomes negative,
#    print False.
# 8. Check whether all frequencies are zero.
# 9. If all frequencies are zero, print True.
#
# Time Complexity: O(n)
# Space Complexity: O(k)
# k = number of distinct characters

s = input("Enter first string: ")
t = input("Enter second string: ")

if len(s) != len(t):
    print(False)
else:
    hashmap = {}

    # Store character frequencies from the first string
    for ch in s:
        if ch in hashmap:
            hashmap[ch] += 1
        else:
            hashmap[ch] = 1

    # Compare with the second string
    for ch in t:
        if ch in hashmap:
            hashmap[ch] -= 1

            if hashmap[ch] < 0:
                print(False)
                break
        else:
            print(False)
            break

    else:
        # Check whether all frequencies became zero
        if all(value == 0 for value in hashmap.values()):
            print(True)
        else:
            print(False)
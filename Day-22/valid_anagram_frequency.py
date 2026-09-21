# Day 22 - Valid Anagram
# Approach 3: Frequency Counting
#
# Problem:
# Given two strings s and t, check whether t is an anagram of s.
#
# This approach assumes that the strings contain only lowercase
# English letters from 'a' to 'z'.
#
# Example:
# s = "anagram"
# t = "nagaram"
# Output: True
#
# Pseudocode:
# 1. Take two strings as input.
# 2. If their lengths are different, print False.
# 3. Create a frequency array of size 26.
# 4. For every character in s, increase its frequency.
# 5. For every character in t, decrease its frequency.
# 6. Check whether all frequencies are zero.
# 7. If all are zero, print True.
# 8. Otherwise, print False.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# Because the frequency array always has 26 elements.

s = input("Enter first string: ")
t = input("Enter second string: ")

if len(s) != len(t):
    print(False)
else:
    freq = [0] * 26

    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1
        freq[ord(t[i]) - ord('a')] -= 1

    if all(x == 0 for x in freq):
        print(True)
    else:
        print(False)
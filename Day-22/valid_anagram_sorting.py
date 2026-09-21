# Day 22 - Valid Anagram
# Approach 1: Sorting
#
# Problem:
# Given two strings s and t, check whether t is an anagram of s.
#
# Anagram:
# Two strings are anagrams if they contain the same characters
# with the same frequency, but the order can be different.
#
# Example:
# s = "listen"
# t = "silent"
# Output: True
#
# Pseudocode:
# 1. Take two strings as input.
# 2. If their lengths are different, print False.
# 3. Sort both strings.
# 4. Compare the sorted strings.
# 5. If they are equal, print True, otherwise print False.
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)

s = input("Enter first string: ")
t = input("Enter second string: ")

if len(s) != len(t):
    print(False)
else:
    s = sorted(s)
    t = sorted(t)

    print(s == t)
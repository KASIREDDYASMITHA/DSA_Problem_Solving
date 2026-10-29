# Day 57 - DSA
# Topic: Backtracking
# Problem: Palindrome Partitioning

s = input("Enter a string: ")

current = []


def is_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1

    return True


def generate(s, start, current):
    if start == len(s):
        print(current)
        return

    for end in range(start, len(s)):
        if is_palindrome(s, start, end):
            current.append(s[start:end + 1])

            generate(s, end + 1, current)

            current.pop()


print("All possible palindrome partitions:")
generate(s, 0, current)
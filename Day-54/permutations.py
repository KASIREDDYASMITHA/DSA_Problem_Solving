# DSA Day 54 - Backtracking
# Program: Generate all permutations of a string

s = input("Enter a string: ")

n = len(s)

used = [False] * n

def permutations(temp):
    if len(temp) == n:
        print(temp)
        return

    for i in range(n):
        if used[i] == False:
            used[i] = True

            permutations(temp + s[i])

            used[i] = False


print("Permutations are:")
permutations("")
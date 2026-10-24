
# DSA Day 53: Generate All Subsequences
# Approach: Recursion and Backtracking

string = input("Enter a string: ")
subsequences = []


def generate_subsequences(index, temp):
    # Base case: all characters have been considered
    if index == len(string):
        subsequences.append(temp)
        return

    # Choice 1: Do not take the current character
    generate_subsequences(index + 1, temp)

    # Choice 2: Take the current character
    generate_subsequences(index + 1, temp + string[index])


generate_subsequences(0, "")

# Display subsequences in lexicographical order
subsequences.sort()

print("All subsequences:")
for subsequence in subsequences:
    if subsequence == "":
        print("(empty)")
    else:
        print(subsequence)

print("Total subsequences:", len(subsequences))

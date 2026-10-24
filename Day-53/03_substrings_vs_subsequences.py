
# DSA Day 53: Substrings vs Subsequences

string = input("Enter a string: ")

# Generate all non-empty substrings
substrings = []

for start in range(len(string)):
    for end in range(start + 1, len(string) + 1):
        substrings.append(string[start:end])

# Generate all non-empty subsequences
subsequences = []


def generate_subsequences(index, temp):
    if index == len(string):
        if temp != "":
            subsequences.append(temp)
        return

    # Skip the current character
    generate_subsequences(index + 1, temp)

    # Take the current character
    generate_subsequences(index + 1, temp + string[index])


generate_subsequences(0, [])

# Sort and remove duplicates for display
substrings = sorted(set(substrings))
subsequences = sorted(set(subsequences))

print("Substrings:")
for item in substrings:
    print(item)

print("\nSubsequences:")
for item in subsequences:
    print(item)

print("\nNumber of distinct non-empty substrings:", len(substrings))
print("Number of distinct non-empty subsequences:", len(subsequences))


# DSA Day 53: Backtracking Basics
# Example: Generate all subsets of a list

numbers = [1, 2, 3]
subsets = []


def backtrack(index, current):
    # Base case: all elements have been considered
    if index == len(numbers):
        subsets.append(current.copy())
        return

    # Choice 1: Do not take the current element
    backtrack(index + 1, current)

    # Choice 2: Take the current element
    current.append(numbers[index])
    backtrack(index + 1, current)

    # Backtrack: undo the last choice
    current.pop()


backtrack(0, [])

print("All subsets:")
for subset in subsets:
    print(subset)

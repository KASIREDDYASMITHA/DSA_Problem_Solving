# Day 55 - DSA
# Topic: Combinations of Size K
# Approach: Backtracking

def generate_combinations(arr, k):
    result = []
    fun(arr, 0, k, [], result)
    return result


def fun(arr, start, k, current, result):

    # Base case
    if len(current) == k:
        result.append(current.copy())
        return

    # Choose elements and explore combinations
    for i in range(start, len(arr)):

        current.append(arr[i])

        fun(arr, i + 1, k, current, result)

        # Backtrack: remove the last chosen element
        current.pop()


n = int(input("Enter the number of array elements: "))

arr = []

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

k = int(input("Enter the combination size k: "))

if k < 0 or k > len(arr):
    print("Invalid value of k")
else:
    combinations = generate_combinations(arr, k)

    print("Combinations of size", k, ":")

    for combination in combinations:
        print(combination)

    print("Total combinations:", len(combinations))
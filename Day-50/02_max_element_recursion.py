
# Day 50 - Find Maximum Element Using Recursion

# Approach:
# Compare the current element with the maximum
# of the elements before it.
# Base case: index becomes zero.

def find_maximum(arr, index):
    if index == 0:
        return arr[0]

    previous_maximum = find_maximum(arr, index - 1)

    return max(arr[index], previous_maximum)


n = int(input("Enter the number of elements: "))

if n <= 0:
    print("Please enter at least one element.")
else:
    arr = []

    for i in range(n):
        element = int(input("Enter an element: "))
        arr.append(element)

    result = find_maximum(arr, n - 1)

    print("Maximum element:", result)


# Day 49 - Maximum Element in Array using Recursion

n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

def find_max(arr, n):
    if n == 1:
        return arr[0]
    else:
        maximum = find_max(arr, n - 1)

        if arr[n - 1] > maximum:
            return arr[n - 1]
        else:
            return maximum

if n <= 0:
    print("Please enter at least one element.")
else:
    print("Maximum element:", find_max(arr, n))

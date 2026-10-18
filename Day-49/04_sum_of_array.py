
# Day 49 - Sum of Array Elements using Recursion

n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

def sum_array(arr, n):
    if n == 0:
        return 0
    else:
        return arr[n - 1] + sum_array(arr, n - 1)

print("Sum of array elements:", sum_array(arr, n))

# Subarray with Given Sum
# Brute Force Approach

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

k = int(input("Enter k: "))

found = False

for i in range(n):

    sum = 0

    for j in range(i, n):

        sum = sum + arr[j]

        if sum == k:
            found = True
            break

    if found:
        break

print(found)
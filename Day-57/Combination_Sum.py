# Day 57 - DSA
# Topic: Backtracking
# Problem: Combination Sum

arr = list(map(int, input("Enter distinct positive integers separated by spaces: ").split()))
target = int(input("Enter target sum: "))

current = []


def generate(arr, target, start, total, current):
    if total == target:
        print(current)
        return

    if total > target:
        return

    for i in range(start, len(arr)):
        current.append(arr[i])

        generate(arr, target, i, total + arr[i], current)

        current.pop()


print("Combinations whose sum equals the target:")
generate(arr, target, 0, 0, current)
n = int(input("Enter size: "))

arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

res = [0] * n

j = 0

for i in range(n - 1, -1, -1):
    res[j] = arr[i]
    j = j + 1

print("Original Array:", arr)
print("Reversed Array:", res)

# Day 51: Merge Two Sorted Arrays

arr1 = list(map(int, input("Enter elements of first sorted array: ").split()))
arr2 = list(map(int, input("Enter elements of second sorted array: ").split()))

i = 0
j = 0
res = []

while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
        res.append(arr1[i])
        i += 1
    else:
        res.append(arr2[j])
        j += 1

while i < len(arr1):
    res.append(arr1[i])
    i += 1

while j < len(arr2):
    res.append(arr2[j])
    j += 1

print("Merged sorted array:", res)

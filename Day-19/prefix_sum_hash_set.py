# Prefix Sum + Hash Set

arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter target sum: "))

s = set()
prefixSum = 0

# Initially add 0 prefix sum
s.add(0)

found = False

for i in range(len(arr)):
    prefixSum = prefixSum + arr[i]

    if prefixSum - k in s:
        found = True
        break

    s.add(prefixSum)

print(found)
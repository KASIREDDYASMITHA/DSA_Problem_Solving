#Hash Map / Dictionary - Frequency Counting

arr = list(map(int, input("Enter array elements: ").split()))

mp = {}

for num in arr:
    mp[num] = mp.get(num, 0) + 1

print(mp)
# Peak Element - Linear Search
# Time Complexity: O(n)
# Space Complexity: O(1)

user_input = input("Enter array elements separated by spaces: ")
arr = list(map(int, user_input.split()))

n = len(arr)
peak_index = -1

if n == 1:
    peak_index = 0

elif arr[0] > arr[1]:
    peak_index = 0

elif arr[n - 1] > arr[n - 2]:
    peak_index = n - 1

else:
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            peak_index = i
            break

if peak_index != -1:
    print("Peak Element Index :", peak_index)
    print("Peak Element Value :", arr[peak_index])
else:
    print("No peak element found")
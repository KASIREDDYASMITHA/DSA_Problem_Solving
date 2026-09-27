# Day 28
# Problem: Nearest Smaller Element to the Left
# Approach: Monotonic Stack

n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter array elements: ").split()))

res = [0] * n

# Create an empty stack
st = []

for i in range(n):

    # Remove elements greater than or equal to current element
    while len(st) > 0 and st[-1] >= arr[i]:
        st.pop()

    # If stack is empty, no smaller element exists on the left
    if len(st) == 0:
        res[i] = -1
    else:
        # Top of stack is nearest smaller element
        res[i] = st[-1]

    # Push current element
    st.append(arr[i])

print("Nearest Smaller Element to Left:", res)

# Time Complexity: O(n)
# Space Complexity: O(n)
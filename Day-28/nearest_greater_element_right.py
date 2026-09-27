# Day 28
# Problem: Nearest Greater Element to the Right
# Approach: Monotonic Stack

n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter array elements: ").split()))

res = [0] * n

# Create an empty stack
st = []

# Traverse from right to left
for i in range(n - 1, -1, -1):

    # Remove smaller or equal elements
    while len(st) > 0 and st[-1] <= arr[i]:
        st.pop()

    # If stack is empty, no greater element exists
    if len(st) == 0:
        res[i] = -1
    else:
        res[i] = st[-1]

    # Push current element to stack
    st.append(arr[i])

print("Nearest Greater Element to Right:", res)

# Time Complexity: O(n)
# Space Complexity: O(n)
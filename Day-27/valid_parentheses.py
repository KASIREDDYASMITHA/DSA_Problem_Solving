# Valid Parentheses
# Approach: Stack

s = input("Enter the string: ")

# If length is odd, it cannot be valid
if len(s) % 2 == 1:
    print(False)

else:
    # Create an empty stack
    st = []

    valid = True

    # Traverse the string
    for ch in s:

        # Opening brackets
        if ch == '(' or ch == '[' or ch == '{':
            st.append(ch)

        # Closing brackets
        else:
            # No opening bracket available
            if len(st) == 0:
                valid = False
                break

            # Remove the top element
            temp = st.pop()

            # Check matching brackets
            if ch == ')' and temp != '(':
                valid = False
                break

            if ch == ']' and temp != '[':
                valid = False
                break

            if ch == '}' and temp != '{':
                valid = False
                break

    # Stack should be empty at the end
    if len(st) != 0:
        valid = False

    print(valid)
# Evaluate Reverse Polish Notation
# DSA Day 29 - Stack

tokens = input("Enter the tokens separated by spaces: ").split()

stack = []

for token in tokens:

    if token in ["+", "-", "*", "/"]:

        b = stack.pop()
        a = stack.pop()

        if token == "+":
            stack.append(a + b)

        elif token == "-":
            stack.append(a - b)

        elif token == "*":
            stack.append(a * b)

        else:
            # Division truncating toward zero
            result = abs(a) // abs(b)

            if (a < 0) != (b < 0):
                result = -result

            stack.append(result)

    else:
        stack.append(int(token))

print("Result:", stack[-1])
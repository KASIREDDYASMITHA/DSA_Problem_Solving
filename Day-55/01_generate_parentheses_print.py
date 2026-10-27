# Day 55 - DSA
# Topic: Generate Parentheses using Backtracking
# Approach: Recursion and Backtracking

def generate_parentheses(n):
    fun(0, 0, "", n)


def fun(open_count, close_count, result, n):

    # Base case
    if len(result) == 2 * n:
        print(result)
        return

    # Choose an opening parenthesis
    if open_count < n:
        fun(open_count + 1, close_count, result + "(", n)

    # Choose a closing parenthesis
    if close_count < open_count:
        fun(open_count, close_count + 1, result + ")", n)


n = int(input("Enter the number of pairs: "))

print("Valid parentheses combinations:")
generate_parentheses(n)
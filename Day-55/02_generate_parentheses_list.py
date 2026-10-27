# Day 55 - DSA
# Topic: Generate Parentheses and Store Results
# Approach: Backtracking with a Result List

def generate_parentheses(n):
    temp = []
    fun(0, 0, "", n, temp)
    return temp


def fun(open_count, close_count, result, n, temp):

    # Base case
    if len(result) == 2 * n:
        temp.append(result)
        return

    # Choose an opening parenthesis
    if open_count < n:
        fun(
            open_count + 1,
            close_count,
            result + "(",
            n,
            temp
        )

    # Choose a closing parenthesis
    if close_count < open_count:
        fun(
            open_count,
            close_count + 1,
            result + ")",
            n,
            temp
        )


n = int(input("Enter the number of pairs: "))

result = generate_parentheses(n)

print("Valid parentheses combinations:")
print(result)

print("Total combinations:", len(result))
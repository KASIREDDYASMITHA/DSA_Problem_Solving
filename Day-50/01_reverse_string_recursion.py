
# Day 50 - Reverse a String Using Recursion

# Approach:
# Start from the last character and move backward.
# Base case: index becomes less than zero.

def reverse_string(text, index):
    if index < 0:
        return ""

    return text[index] + reverse_string(text, index - 1)


string = input("Enter a string: ")

result = reverse_string(string, len(string) - 1)

print("Reversed string:", result)

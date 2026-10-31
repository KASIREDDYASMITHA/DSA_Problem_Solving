# DSA Day 59 - Backtracking
# Problem: Letter Combinations of a Phone Number

digits = input("Enter the digit string (2-9): ")

mapping = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

valid = True

for digit in digits:
    if digit not in mapping:
        valid = False
        break

if not valid:
    print("Enter digits from 2 to 9 only.")

elif digits == "":
    print("No combinations available.")

else:
    count = 0

    def generate(digits, index, result, mapping):
        global count

        if index == len(digits):
            print(result)
            count += 1
            return

        letters = mapping[digits[index]]

        for i in range(len(letters)):
            generate(
                digits,
                index + 1,
                result + letters[i],
                mapping
            )

    generate(digits, 0, "", mapping)

    print("Total combinations:", count)
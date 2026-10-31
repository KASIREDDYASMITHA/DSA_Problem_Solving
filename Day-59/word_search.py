# DSA Day 59 - Backtracking
# Problem: Word Search

board = [
    ["E", "S", "E"],
    ["F", "C", "C"]
]

word = input("Enter the word to search: ")


def search(board, word, row, col, index):
    rows = len(board)
    cols = len(board[0])

    if index == len(word):
        return True

    if row < 0 or row >= rows or col < 0 or col >= cols:
        return False

    if board[row][col] != word[index]:
        return False

    original = board[row][col]
    board[row][col] = "#"

    found = (
        search(board, word, row - 1, col, index + 1)
        or search(board, word, row + 1, col, index + 1)
        or search(board, word, row, col - 1, index + 1)
        or search(board, word, row, col + 1, index + 1)
    )

    board[row][col] = original

    return found


def word_search(board, word):
    if word == "":
        return True

    rows = len(board)
    cols = len(board[0])

    for row in range(rows):
        for col in range(cols):
            if search(board, word, row, col, 0):
                return True

    return False


print("Board:")

for row in board:
    print(row)

if word_search(board, word):
    print("Word found: True")
else:
    print("Word found: False")
# ---------------------------------------------------------
# Program: Word Search
# Description:
# This program checks whether a word exists in a character
# grid using backtracking.
# ---------------------------------------------------------

def dfs(board, row, col, word, index):
    if index == len(word):
        return True

    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return False

    if board[row][col] != word[index]:
        return False

    temp = board[row][col]
    board[row][col] = "#"

    found = (
        dfs(board, row + 1, col, word, index + 1) or
        dfs(board, row - 1, col, word, index + 1) or
        dfs(board, row, col + 1, word, index + 1) or
        dfs(board, row, col - 1, word, index + 1)
    )

    board[row][col] = temp
    return found


def exist(board, word):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if dfs(board, row, col, word, 0):
                return True
    return False


board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

word = "ABCCED"

print("Board:")
for row in board:
    print(row)

print("Word:", word)

if exist(board, word):
    print("Word exists in board.")
else:
    print("Word does not exist in board.")

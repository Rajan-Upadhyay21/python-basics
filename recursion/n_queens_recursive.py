# ---------------------------------------------------------
# Program: N-Queens Problem using Recursion and Backtracking
# Description:
# This program solves the N-Queens problem, where N queens
# must be placed on an N x N chessboard such that no two
# queens attack each other.
# ---------------------------------------------------------

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def is_safe(board, row, col, n):
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == "Q":
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col, n):
    # Base case: all queens are placed
    if col == n:
        print("One valid solution:")
        print_board(board)
        return True

    solution_found = False

    # Try placing queen in each row of current column
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"

            # Recur for next column
            if solve_n_queens(board, col + 1, n):
                solution_found = True

            # Backtrack
            board[row][col] = "."

    return solution_found


# Board size
n = 4

# Creating empty board
board = [["." for _ in range(n)] for _ in range(n)]

print(f"Solving {n}-Queens Problem:\n")
has_solution = solve_n_queens(board, 0, n)

if not has_solution:
    print("No solution exists.")

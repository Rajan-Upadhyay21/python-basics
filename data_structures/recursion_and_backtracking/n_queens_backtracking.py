# ---------------------------------------------------------
# Program: N-Queens Problem
# Description:
# This program solves the N-Queens problem
# using backtracking.
# ---------------------------------------------------------

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == "Q":
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == "Q":
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col, n):
    if col == n:
        print("One valid solution:")
        print_board(board)
        return True

    solution_found = False

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"

            if solve_n_queens(board, col + 1, n):
                solution_found = True

            board[row][col] = "."

    return solution_found


n = 4
board = [["." for _ in range(n)] for _ in range(n)]

print(f"Solving {n}-Queens Problem:\n")
has_solution = solve_n_queens(board, 0, n)

if not has_solution:
    print("No solution exists.")

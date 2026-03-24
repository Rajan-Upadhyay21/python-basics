# ---------------------------------------------------------
# Program: Maze Solver using Recursion and Backtracking
# Description:
# This program finds a path from the top-left corner to the
# bottom-right corner of a maze using recursion.
# 1 = open path
# 0 = blocked cell
# ---------------------------------------------------------

def print_solution(solution):
    print("Path found:")
    for row in solution:
        print(" ".join(str(cell) for cell in row))
    print()


def is_valid_move(maze, x, y, n):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1


def solve_maze(maze, x, y, solution, n):
    # If destination is reached
    if x == n - 1 and y == n - 1 and maze[x][y] == 1:
        solution[x][y] = 1
        return True

    if is_valid_move(maze, x, y, n):
        # Avoid revisiting the same cell
        if solution[x][y] == 1:
            return False

        # Mark current cell as part of solution path
        solution[x][y] = 1

        # Move down
        if solve_maze(maze, x + 1, y, solution, n):
            return True

        # Move right
        if solve_maze(maze, x, y + 1, solution, n):
            return True

        # Move up
        if solve_maze(maze, x - 1, y, solution, n):
            return True

        # Move left
        if solve_maze(maze, x, y - 1, solution, n):
            return True

        # Backtrack if no move works
        solution[x][y] = 0
        return False

    return False


# Maze definition
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

n = len(maze)
solution = [[0 for _ in range(n)] for _ in range(n)]

print("Maze:")
for row in maze:
    print(row)

print()

if solve_maze(maze, 0, 0, solution, n):
    print_solution(solution)
else:
    print("No path found in the maze.")

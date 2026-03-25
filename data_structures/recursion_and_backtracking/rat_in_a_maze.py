# ---------------------------------------------------------
# Program: Rat in a Maze
# Description:
# This program finds one valid path in a maze
# using backtracking.
# ---------------------------------------------------------

def is_safe(maze, x, y, n, solution):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and solution[x][y] == 0


def solve_maze(maze, x, y, n, solution):
    if x == n - 1 and y == n - 1:
        solution[x][y] = 1
        return True

    if is_safe(maze, x, y, n, solution):
        solution[x][y] = 1

        if solve_maze(maze, x + 1, y, n, solution):
            return True

        if solve_maze(maze, x, y + 1, n, solution):
            return True

        if solve_maze(maze, x - 1, y, n, solution):
            return True

        if solve_maze(maze, x, y - 1, n, solution):
            return True

        solution[x][y] = 0

    return False


maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

n = len(maze)
solution = [[0 for _ in range(n)] for _ in range(n)]

if solve_maze(maze, 0, 0, n, solution):
    print("Path found:")
    for row in solution:
        print(row)
else:
    print("No path found.")

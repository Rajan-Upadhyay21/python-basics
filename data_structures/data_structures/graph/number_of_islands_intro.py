# ---------------------------------------------------------
# Program: Number of Islands
# Description:
# This program counts the number of islands in a grid
# using DFS.
# ---------------------------------------------------------

def dfs(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])

    if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
        return

    grid[row][col] = "0"

    dfs(grid, row + 1, col)
    dfs(grid, row - 1, col)
    dfs(grid, row, col + 1)
    dfs(grid, row, col - 1)


def num_islands(grid):
    if not grid:
        return 0

    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                dfs(grid, row, col)
                count += 1

    return count


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "1"],
    ["0", "0", "1", "0", "1"],
    ["0", "0", "0", "1", "1"]
]

print("Number of islands:", num_islands(grid))

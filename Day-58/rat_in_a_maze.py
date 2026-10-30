# Day 58 - Rat in a Maze
# Approach: Backtracking

n = int(input("Enter the size of the maze (n): "))

maze = []

print("Enter the maze values (0 for blocked, 1 for open):")

for i in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

paths = []


def find_paths(maze, n, row, col, path):
    # Check whether the current position is outside the maze
    if row < 0 or row >= n or col < 0 or col >= n:
        return

    # Check whether the cell is blocked or already visited
    if maze[row][col] == 0:
        return

    # Check whether the destination is reached
    if row == n - 1 and col == n - 1:
        paths.append(path)
        return

    # Mark the current cell as visited
    maze[row][col] = 0

    # Move Top
    find_paths(maze, n, row - 1, col, path + "T")

    # Move Down
    find_paths(maze, n, row + 1, col, path + "D")

    # Move Right
    find_paths(maze, n, row, col + 1, path + "R")

    # Move Left
    find_paths(maze, n, row, col - 1, path + "L")

    # Restore the cell during backtracking
    maze[row][col] = 1


if n <= 0:
    print("Maze size must be positive.")
elif any(len(row) != n for row in maze):
    print("Invalid input: enter exactly n values in each row.")
elif any(value not in (0, 1) for row in maze for value in row):
    print("Invalid input: maze values must be 0 or 1.")
elif maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
    print("No path exists.")
else:
    find_paths(maze, n, 0, 0, "")

    if len(paths) == 0:
        print("No path exists.")
    else:
        print("Possible paths:")
        for path in paths:
            print(path)
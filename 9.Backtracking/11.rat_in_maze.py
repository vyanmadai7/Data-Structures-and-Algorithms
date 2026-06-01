def ratInMaze(maze):
    n = len(maze)
    res = []

    def backtrack(i, j, path):
        if i == n - 1 and j == n - 1 and maze[i][j] == 1:
            res.append(path[:])
            return

        if i < 0 or j < 0 or i >= n or j >= n or maze[i][j] == 0:
            return

        maze[i][j] = 0

        backtrack(i + 1, j, path + "D")
        backtrack(i - 1, j, path + "U")
        backtrack(i, j + 1, path + "R")
        backtrack(i, j - 1, path + "L")

        maze[i][j] = 1

    if maze[0][0] == 1:
        backtrack(0, 0, "")

    return res
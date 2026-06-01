def solveSudoku(board):

    def is_valid(r, c, ch):
        for i in range(9):
            if board[r][i] == ch or board[i][c] == ch:
                return False

        sr, sc = 3 * (r // 3), 3 * (c // 3)
        for i in range(sr, sr + 3):
            for j in range(sc, sc + 3):
                if board[i][j] == ch:
                    return False
        return True

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for ch in "123456789":
                        if is_valid(i, j, ch):
                            board[i][j] = ch
                            if backtrack():
                                return True
                            board[i][j] = "."
                    return False
        return True

    backtrack()
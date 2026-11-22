class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]


        cols = [False] * n
        # rows = [False] * n
        mainDiagonal = [False] * (2 * n - 1)
        secondDiagonal = [False] * (2 * n - 1)
 

        def getMainIdx(row, col):
            return row - col
        def getSecondIdx(row, col):
            return row + col

        def backtrack(row, col):
            if not (0 <= col < n):
                return

            mainIdx = getMainIdx(row, col)
            secondIdx = getSecondIdx(row, col)

            if cols[col] or mainDiagonal[mainIdx] or secondDiagonal[secondIdx]:
                return

            board[row][col] = 'Q'
            cols[col] = mainDiagonal[mainIdx] = secondDiagonal[secondIdx] = True

            if row == n - 1:
                res.append([''.join(row) for row in board])
            else:
                for newCol in range(n):
                    if newCol != col:
                        backtrack(row + 1, newCol)

            board[row][col] = '.'
            cols[col] = mainDiagonal[mainIdx] = secondDiagonal[secondIdx] = False

        res = []
        for col in range(n):
            backtrack(0, col)

        return res
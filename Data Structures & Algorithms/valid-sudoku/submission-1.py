class Solution:
    def boxIdx(self, i, j):
        return i // 3 * 3 + j // 3
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        rows = [[False] * 9 for _ in range(n)]
        cols = [[False] * 9 for _ in range(n)]
        boxes = [[False] * 9 for _ in range(n)]

        for i in range(n):
            for j in range(n):
                val = board[i][j]
                if val == ".":
                    continue
                num = int(val) - 1

                if rows[i][num] or cols[j][num] or boxes[self.boxIdx(i, j)][num]:
                    return False

                rows[i][num] = True
                cols[j][num] = True
                boxes[self.boxIdx(i, j)][num] = True
        
        return True



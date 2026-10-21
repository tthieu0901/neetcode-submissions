class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)] 
        cols = [set() for _ in range(9)] 
        boxes = [set() for _ in range(9)]

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                val = board[i][j]
                if val == ".":
                    continue

                boxIdx = i // 3 * 3 + j // 3
                if val in rows[i] or val in cols[j] or val in boxes[boxIdx]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxes[boxIdx].add(val)

        return True
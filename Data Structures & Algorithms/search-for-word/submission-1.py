class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(n)]
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col, idx):
            if not (0 <= row < m and 0 <= col < n):
                return False

            if visited[row][col]:
                return False

            visited[row][col] = True

            if board[row][col] == word[idx]:
                if idx == len(word) - 1: return True
                for dx, dy in d:
                    if dfs(row + dx, col + dy, idx + 1): return True

            visited[row][col] = False
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0): return True

        return False      
            
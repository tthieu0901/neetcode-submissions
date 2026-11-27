class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return
            
            if grid[i][j] != "1":
                return

            # mark as visited
            grid[i][j] = "."

            for dx, dy in d:
                dfs(i + dx, j + dy)

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j)

        return cnt
                






class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i, j):
            # mark as visited
            grid[i][j] = -1
            area = 1
            for dx, dy in d:
                next_i, next_j = i + dx, j + dy
                if (0 <= next_i < m and 0 <= next_j < n) and grid[next_i][next_j] == 1:
                    area += dfs(next_i, next_j)
            return area

        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))

        return maxArea
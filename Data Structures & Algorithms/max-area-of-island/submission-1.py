class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return 0
            
            if grid[i][j] != 1:
                return 0

            # mark as visited
            grid[i][j] = -1
            area = 1
            for dx, dy in d:
                area += dfs(i + dx, j + dy)
            return area

        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))

        return maxArea
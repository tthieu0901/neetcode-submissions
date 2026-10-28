class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        lefts = [0] * n
        rights = [0] * n

        for i in range(n - 1):
            lefts[i + 1] = max(height[i], lefts[i])

        for i in range(n - 1, 0, -1):
            rights[i - 1] = max(height[i], rights[i])


        total = 0
        for i in range(n):
            total += max(min(lefts[i], rights[i]) - height[i], 0)
        return total    
            


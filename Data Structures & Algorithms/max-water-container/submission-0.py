class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        left = 0
        right = n - 1

        res  = 0
        while left < right:
            hLeft = heights[left]
            hRight = heights[right]

            res = max(res, min(hLeft, hRight) * (right - left))

            if hLeft < hRight:
                left += 1
            else:
                right -= 1

        return res

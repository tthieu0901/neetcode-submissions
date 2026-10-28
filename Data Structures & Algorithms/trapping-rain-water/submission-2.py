class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []

        n = len(height)

        total = 0
        for i in range(n):
            while stack and height[stack[-1]] <= height[i]: # height[i] >= height[stack[-1]] means found right wall
                cur = height[stack.pop()]

                if stack: # if have left wall
                    left = height[stack[-1]]
                    right = height[i]

                    h = min(left, right) - cur
                    w = i - stack[-1] - 1

                    total += h * w

            stack.append(i)

        return total

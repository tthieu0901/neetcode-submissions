class Solution:
    def rob(self, nums: List[int]) -> int:
        def backtrack(left, right):
            if left > right:
                return 0
            
            if left == right: return nums[left]
            n = right - left + 1
            dp = [0] * n
            dp[0] = nums[left]
            dp[1] = max(nums[left], nums[left + 1])

            for i in range(2, n):
                dp[i] = max(nums[left + i] + dp[i - 2], dp[i - 1])

            return dp[-1]
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        return max(backtrack(0, n - 2), backtrack(1, n - 1))

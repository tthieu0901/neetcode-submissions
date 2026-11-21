class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])

        return dp[len(nums)]
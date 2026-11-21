class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def backtrack(idx):
            if idx >= len(nums):
                return 0

            if memo[idx] != -1:
                return memo[idx]

            memo[idx] = max(nums[idx] + backtrack(idx + 2), backtrack(idx + 1)) 
            return memo[idx]

        return backtrack(0)
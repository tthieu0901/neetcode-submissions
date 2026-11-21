class Solution:
    def rob(self, nums: List[int]) -> int:
        def backtrack(idx, maxIdx, memo):
            if idx >= maxIdx:
                return 0
            if memo[idx] != -1:
                return memo[idx]

            memo[idx] = max(nums[idx] + backtrack(idx + 2, maxIdx, memo), backtrack(idx + 1, maxIdx, memo))
            return memo[idx]

        if not nums: return 0
        if len(nums) == 1: return nums[0]

        n = len(nums)
        memo1 = [-1] * n
        memo2 = [-1] * n
        return max(backtrack(0, n - 1, memo1), backtrack(1, n, memo2))

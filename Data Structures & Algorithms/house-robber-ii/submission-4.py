class Solution:
    def rob(self, nums: List[int]) -> int:
        def backtrack(nums):
            n = len(nums)
            if n == 0: return 0
            if n == 1: return nums[0]
            prev = nums[0]
            cur = max(nums[0], nums[1])

            for i in range(2, n):
                tmp = cur
                cur = max(nums[i] + prev, cur)
                prev = tmp

            return cur

        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        return max(backtrack(nums[:n - 1]), backtrack(nums[1:]))

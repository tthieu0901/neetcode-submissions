class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        res = 0
        for i, num in enumerate(nums):
            if num - 1 not in s:
                l = 1
                while num + l in s:
                    l += 1
                
                res = max(res, l)

        return res
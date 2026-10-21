class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in nums:
            l = 0
            if num - 1 not in s:
                while num in s:
                    l += 1
                    num += 1

            res = max(res, l)

        return res
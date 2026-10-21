class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        s = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in s: # start number
                cnt = 0
                while num in s:
                    num += 1    
                    cnt += 1

                res = max(cnt, res)

        return res
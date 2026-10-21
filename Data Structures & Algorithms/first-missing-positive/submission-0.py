from math import inf
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minNum = inf
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if num > 0 and num <= n:
                minNum = min(num, minNum)
            else:
                nums[i] = 0

        if minNum == inf or minNum > 1:
            return 1

        for i in range(n):
            num = abs(nums[i])
            if num == 0 or num == inf:
                continue
            
            if nums[num - 1] == 0:
                nums[num - 1] = -inf
            elif nums[num - 1] > 0:
                nums[num - 1] = -nums[num - 1]

        while minNum - 1 < n and nums[minNum - 1] < 0:
            minNum += 1

        return minNum
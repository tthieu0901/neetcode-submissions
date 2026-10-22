class Solution:
    def twoSum(self, nums, target, start) :
        s = set()

        k = nums[start]

        res = set()
        for i in range(start + 1, len(nums)):
            num = nums[i]

            if target - num in s:
                res.add(tuple(sorted([k, num, target - num])))

            s.add(num)
        
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums) - 1):
            res.update(self.twoSum(nums, -nums[i], i))

        return list(res)
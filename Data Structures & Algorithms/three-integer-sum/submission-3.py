class Solution:
    def twoSum(self, nums, target, start) :
        left = start + 1
        right = len(nums) - 1

        res = set()
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                res.add((nums[start], nums[left], nums[right]))
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1 # by pass the duplicate value
            elif s < target:
                left += 1
            else:
                right -= 1

        return res
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums) - 1):
            res.update(self.twoSum(nums, -nums[i], i))

        return list(res)
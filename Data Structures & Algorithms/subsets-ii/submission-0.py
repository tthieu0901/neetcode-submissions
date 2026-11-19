class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        arr = []

        nums.sort()
        
        def dfs(idx):
            if idx == len(nums):
                res.append(arr[:])
                return

            arr.append(nums[idx])
            dfs(idx + 1)
            arr.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            dfs(idx + 1)


        dfs(0)
        return res
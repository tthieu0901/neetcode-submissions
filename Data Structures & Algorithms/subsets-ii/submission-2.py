class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        arr = []

        nums.sort()
        
        def dfs(idx):
            res.append(arr[:])

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
            
                arr.append(nums[i])
                dfs(i + 1)
                arr.pop()


        dfs(0)
        return res
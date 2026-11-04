class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        res = []
        def solve(nums, idx):
            if idx == len(nums):
                res.append(arr[:])
                return
                
            arr.append(nums[idx])
            solve(nums, idx + 1)

            arr.pop()
            solve(nums, idx + 1)

        solve(nums, 0)
        return res

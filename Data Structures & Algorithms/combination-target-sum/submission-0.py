class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        arr = []
        def backtrack(idx, target):
            if target < 0 or idx >= len(nums):
                return

            if target == 0:
                res.append(arr[:])
                return

            backtrack(idx + 1, target)

            arr.append(nums[idx])
            backtrack(idx, target - nums[idx])
            arr.pop()

        backtrack(0, target)
        return res
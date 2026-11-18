class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        arr = []
        found = [False] * len(nums)
        def backtrack(idx):
            if idx == len(nums):
                res.append(arr[:])
                return

            for i, num in enumerate(nums):
                if found[i]:
                    continue
                found[i] = True
                arr.append(num)
                backtrack(idx + 1)
                arr.pop()
                found[i] = False

        backtrack(0)
        return res
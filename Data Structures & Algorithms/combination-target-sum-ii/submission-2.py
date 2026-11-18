class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        arr = []

        candidates.sort()
        def backtrack(idx, target):
            if target == 0:
                res.append(arr[:])
                return

            if idx >= len(candidates) or target < 0:
                return

            arr.append(candidates[idx])
            backtrack(idx + 1, target - candidates[idx])
            arr.pop()
            while idx < len(candidates) - 1 and candidates[idx] == candidates[idx + 1]: 
                idx += 1
            backtrack(idx + 1, target)

        backtrack(0, target)
        return res 
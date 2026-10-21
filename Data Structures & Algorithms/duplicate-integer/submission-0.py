class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setVal = set()

        for num in nums:
            if num not in setVal:
                setVal.add(num)
            else:
                return True

        return False

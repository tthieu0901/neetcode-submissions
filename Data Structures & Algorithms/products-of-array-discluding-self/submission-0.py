class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preProduct = [1] * n
        postProduct = [1] * n

        for i in range(n - 1):
            preProduct[i + 1] = preProduct[i] * nums[i]
        
        for i in range(n - 1, 0, -1):
            postProduct[i - 1] = postProduct[i] * nums[i]

        res = [1] * n
        for i in range(n):
            res[i] = preProduct[i] * postProduct[i]    

        return res
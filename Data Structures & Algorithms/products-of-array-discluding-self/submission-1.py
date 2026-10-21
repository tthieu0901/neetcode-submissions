class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 1, 2, 8]
        # [48, 24, 6, 1]

        n = len(nums)
        left = [1] * n
        right = [1] * n

        for i in range(n - 1):
            left[i + 1] = left[i] * nums[i]

        for i in range(n - 1, 0, -1):
            right[i - 1] = right[i] * nums[i]

        return [left[i] * right[i] for i in range(n)]

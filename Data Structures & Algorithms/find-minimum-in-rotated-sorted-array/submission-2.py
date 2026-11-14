class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if right - left + 1 <= 2:
                return min(nums[left], nums[right])
            if nums[left] <= nums[right]:
                return nums[left]

            mid = left + (right - left) // 2

            if nums[left] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        return -1

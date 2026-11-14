class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binSearch(left, right):
            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    return mid

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[left] < nums[right]:
                return binSearch(left, right)

            if nums[mid] < target <= nums[right]:
                return binSearch(mid + 1, right)

            if nums[left] <= target < nums[mid]:
                return binSearch(left, mid - 1)

            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1

        return -1
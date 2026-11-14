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

        while left < right:

            if nums[left] < nums[right]:
                pivot = left
                break

            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        leftSearch = binSearch(0, pivot - 1)
        return leftSearch if leftSearch != -1 else binSearch(pivot, len(nums) - 1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            mid = (left + right) // 2
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left = mid + 1 if numbers[mid] + numbers[right] < target else left + 1
            else:
                right = mid - 1 if numbers[left] + numbers[mid] > target else right - 1

        return [-1, -1]
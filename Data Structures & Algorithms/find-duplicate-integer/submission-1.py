class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        slow = 0
        fast = 0

        while slow == 0 or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        dup = 0
        while dup != slow:
            dup = nums[dup]
            slow = nums[slow]

        return dup
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def parition(l, r):
            pivot = r
            i = l

            for j in range(l, r):
                if nums[j] <= nums[pivot]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[pivot] = nums[pivot], nums[i]
            return i
        n = len(nums)
        L, R = 0, n - 1

        pivot = n
        k = n - k
        while pivot != k:
            pivot = parition(L, R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1

        return nums[k]

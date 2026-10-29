class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        left = 1
        right = max(piles)

        while left < right:
            k = left + (right - left) // 2
            totalHour = sum(math.ceil(pile / k) for pile in piles)
            if totalHour <= h:
                right = k
            else:
                left = k + 1

        return left
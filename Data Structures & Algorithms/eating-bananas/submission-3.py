class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0

        left = 1
        right = max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            time = sum(math.ceil(pile / mid) for pile in piles)
            
            if time > h:
                res = mid
                left = mid + 1
            else:
                right = mid - 1


        return res + 1
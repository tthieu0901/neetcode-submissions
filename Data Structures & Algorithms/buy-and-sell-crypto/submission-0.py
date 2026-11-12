class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevMin = prices[0]
        res = 0
        for i in range(1, len(prices)):
            res = max(res, max(0, prices[i] - prevMin))
            prevMin = min(prevMin, prices[i])

        return res
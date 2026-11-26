class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = [[None] * (amount + 1) for  _ in range(n)] 
        def backtrack(idx, left):
            if left == 0:
                return 0

            if left < 0 or idx == n:
                return -1

            if memo[idx][left] != None:
                return memo[idx][left]

            minValue = -1
            for nCoin in range(0, left // coins[idx] + 1):
                coin = backtrack(idx + 1, left - coins[idx] * nCoin)
                if coin != -1:
                    minValue = coin + nCoin if minValue == -1 else min(minValue, nCoin + coin)
            
            memo[idx][left] = minValue
            return memo[idx][left]

        return backtrack(0, amount)
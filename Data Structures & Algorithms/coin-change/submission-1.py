class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = [None] * (amount + 1)
        def backtrack(amount):
            if amount == 0:
                return 0

            if memo[amount] != None:
                return memo[amount]
            
            res = math.inf
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + backtrack(amount - coin))

            memo[amount] = res
            return memo[amount]

        res = backtrack(amount)
        return res if res != math.inf else -1
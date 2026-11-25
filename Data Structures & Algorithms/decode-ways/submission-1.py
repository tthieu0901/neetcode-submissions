class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(n):
            if s[i] == '0':
                continue

            dp[i + 1] += dp[i]
            if i + 1 < n and (s[i] < '2' or (s[i] == '2' and s[i + 1] <= '6')):
                dp[i + 2] += dp[i]
        return dp[-1]
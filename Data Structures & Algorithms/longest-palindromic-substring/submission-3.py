class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        maxLen = 1
        start = 0
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                end = i + l - 1
                if s[i] == s[end] and (i + 1 >= end - 1 or dp[i + 1][end - 1]):
                    dp[i][end] = True
                    if l > maxLen:
                        maxLen = l
                        start = i
        return s[start:start + maxLen]
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        dp = [[False] * n for _ in range(n)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = s[i] == s[j] and (i + 1 > j - 1 or dp[i + 1][j - 1])
                if dp[i][j]:
                    cnt += 1

        return cnt
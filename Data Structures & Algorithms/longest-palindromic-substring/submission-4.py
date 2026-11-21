class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen = 1
        start = 0

        memo = [[False] * n for _ in range(n)]
        for l in range(1, n + 1):
            for left in range(n - l + 1):
                right = left + l - 1
                if s[left] == s[right] and (left + 1 >= right - 1 or memo[left + 1][right - 1]):
                    memo[left][right] = True
                    curLen = right - left  + 1
                    if curLen > maxLen:
                        maxLen = curLen
                        start = left
        return s[start:start + maxLen]
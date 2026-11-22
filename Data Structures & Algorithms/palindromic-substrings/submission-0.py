class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = [[False] * n for _ in range(n)]
        def isPalindrome(l, r):
            if memo[l][r]:
                return True

            memo[l][r] = s[l] == s[r] and (l + 1 > r - 1 or isPalindrome(l + 1, r - 1))
            return memo[l][r]

        cnt = 0
        for i in range(n):
            for j in range(i, n):
                if isPalindrome(i, j):
                    cnt += 1

        return cnt
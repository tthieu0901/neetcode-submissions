class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [-1] * n
        def decode(idx):
            if idx >= n:
                return 1
            if s[idx] == '0':
                return 0
            if memo[idx] != -1:
                return memo[idx]

            total = 0
            total += decode(idx + 1)
            if idx + 1 < n and (s[idx] < '2' or (s[idx] == '2' and s[idx + 1] <= '6')):
                total += decode(idx + 2)
            memo[idx] = total
            return memo[idx]
        
        return decode(0)
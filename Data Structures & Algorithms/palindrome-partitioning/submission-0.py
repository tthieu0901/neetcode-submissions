class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        arr = []
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        n = len(s)
        dp = [[False] * n  for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for l in range(1, n + 1):
            for i in range(n - l + 1):
                left = i
                right = i + l - 1
                if s[left] == s[right]: 
                    if left + 1 < right - 1 and not dp[left + 1][right - 1]:
                        continue
                    dp[left][right] = True 


        def backtrack(left):
            if left >= n:
                res.append(arr[:])
                return
            
            for right in range(left, n):
                if isPalindrome(left, right):
                    arr.append(s[left: right + 1])
                    backtrack(right + 1)
                    arr.pop()

        backtrack(0)
        return res
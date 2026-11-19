class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]
        dp[1] = ["()"]

        def dfs(n):
            if dp[n]:
                return dp[n] 

            for i in range(1, n // 2 + 1):
                for left in dfs(i):
                    for right in dfs(n - i):
                        if left + right not in dp[n]:
                            dp[n].append(left + right)
                        
                        if right + left not in dp[n]:
                            dp[n].append(right + left)

            for combination in dfs(n - 1):           
                dp[n].append("(" + combination + ")")
            
            return dp[n]

        return dfs(n)
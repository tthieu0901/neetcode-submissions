class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        arr = []

        def dfs(openN, closeN):
            if openN == closeN == n:
                res.append("".join(arr))
                return

            if openN < n:
                arr.append("(")
                dfs(openN + 1, closeN)
                arr.pop()

            if closeN < openN:
                arr.append(")")
                dfs(openN, closeN + 1)
                arr.pop()

        dfs(0, 0)
        return res
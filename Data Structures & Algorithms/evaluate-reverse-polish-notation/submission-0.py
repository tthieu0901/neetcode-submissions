class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def isOperator(token):
            return token in ("+", "-", "*", "/")

        for token in tokens:
            if isOperator(token):
                b = stack.pop()
                a = stack.pop()

                res = 0
                if token == "+":
                    res = a + b
                elif token == "-":
                    res = a - b
                elif token == "*":
                    res = a * b
                else:
                    res = abs(a) // abs(b)
                    if a * b < 0:
                        res *= -1

                stack.append(res)
            else:
                stack.append(int(token)) 

        return stack[-1]
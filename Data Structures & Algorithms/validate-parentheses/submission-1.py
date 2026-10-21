class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def isOpen(ch):
            return ch in ('(', '[', '{')

        def match(a, b):
            return (
                a == '(' and b == ')'
                or a == '[' and b == ']'
                or a == '{' and b == '}'
            )
            

        for ch in s:
            if isOpen(ch):
                stack.append(ch)
            else:
                if not stack: return False
                lastOpen = stack.pop()
                if not match(lastOpen, ch):
                    return False

        return not stack


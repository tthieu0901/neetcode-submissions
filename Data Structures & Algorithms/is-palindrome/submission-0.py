class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        def isValid(ch):
            return 'A' <= ch <= 'Z' or 'a' <= ch <= 'z' or '0' <= ch <= '9'

        while start <= end:
            if not isValid(s[start]):
                start += 1
                continue

            if not isValid(s[end]):
                end -= 1
                continue

            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1
        
        return True
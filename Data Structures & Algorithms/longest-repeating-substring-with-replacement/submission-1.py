class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0

        curChar = s[0]
        res = 0
        oldK = k
        while right < len(s):
            if s[right] != curChar:
                if k > 0:
                    k -= 1
                else:
                    curChar = s[right]
                    left = right
                    k = oldK
                    while left >= 0 and (s[left] == s[right] or k > 0):
                        if s[left] != s[right] and k > 0:
                            k -= 1
                        left -= 1
                    left += 1
            res = max(res, right - left + 1)
            right += 1
        
        return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        n = len(s)

        beg = 0
        end = 0

        res = 0
        while end < n:
            if s[end] in lastSeen and lastSeen[s[end]] >= beg:
                beg = lastSeen[s[end]] + 1

            lastSeen[s[end]] = end
            res = max(res, end - beg + 1)
            end += 1

        return res
        
            
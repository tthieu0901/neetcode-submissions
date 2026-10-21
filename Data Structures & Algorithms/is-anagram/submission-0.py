class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = defaultdict(int)
        for ch in s:
            d1[ch] += 1

        d2 = defaultdict(int)
        for ch in t:
            d2[ch] += 1
        
        return d1 == d2


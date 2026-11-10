class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = defaultdict(int)

        for ch in s1:
            freq[ch] += 1

        left = 0
        right = 0
        while right < len(s2):
            freq[s2[right]] -= 1
            
            if right - left + 1 > len(s1):
                freq[s2[left]] += 1
                left += 1

            if all(val == 0 for val in freq.values()):
                return True    

            right += 1

        return False

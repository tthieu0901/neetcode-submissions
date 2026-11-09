class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countMap = defaultdict(int)
        n = len(s)
        maxFreq = 0
        res = 0
        left = 0
        for right, ch in enumerate(s):
            countMap[ch] += 1
            maxFreq = max(maxFreq, countMap[ch])

            while (right - left + 1) - maxFreq > k:
                countMap[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
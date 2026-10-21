class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return sorted(freq, key=lambda num: freq[num], reverse=True)[:k]
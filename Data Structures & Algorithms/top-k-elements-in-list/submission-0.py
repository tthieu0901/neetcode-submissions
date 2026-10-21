class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        l = [(freq, num) for num, freq in d.items()]
        l.sort(reverse=True)

        return [p[1] for p in l[:k]]
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        heapq.heapify(h)

        for point in points:
            heapq.heappush(h, (-math.sqrt(point[0] ** 2 + point[1] ** 2), point))
            if len(h) > k:
                heapq.heappop(h)
        return [x[1] for x in h]


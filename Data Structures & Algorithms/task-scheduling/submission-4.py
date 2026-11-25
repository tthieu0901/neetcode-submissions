class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1

        cnts = sorted(freq.values(), reverse=True)
        maxCnt = cnts[0]
        idle = (maxCnt - 1) * n
        for i, cnt in enumerate(cnts):
            if i > 0:
                idle -= min(cnt, maxCnt - 1)
        return max(0, idle) + len(tasks)


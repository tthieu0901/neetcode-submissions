class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1

        h = [(-value, key) for key, value in freq.items()]
        heapq.heapify(h)
        
        time = 0
        q = deque()
        while h or q:
            time += 1
 
            if not h:
                time = q[0][1]
            else:
                item = heapq.heappop(h)
                task, cnt = item[1], -item[0]
                cnt -= 1
                if cnt > 0:
                    q.append(((-cnt, task), time + n))
                
            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])


        return time


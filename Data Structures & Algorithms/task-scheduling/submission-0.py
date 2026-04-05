class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count_tasks = defaultdict(int)
        for task in tasks:
            count_tasks[task] -= 1

        maxHeap = [c for c in count_tasks.values()]
        heapq.heapify(maxHeap)

        q = deque() # (freq, time remaining)
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                f = 1 + heapq.heappop(maxHeap)
                if f:
                    q.append((f, time + n))
            while q and q[0][1] == time:
                freq, time = q.popleft()
                heapq.heappush(maxHeap, freq)
        return time
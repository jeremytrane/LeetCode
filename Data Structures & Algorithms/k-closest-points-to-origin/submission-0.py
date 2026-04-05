class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        points = [(math.sqrt((x**2) + (y**2)), x, y) for x, y in points]
        heapq.heapify(points)
        for i in range(k):
            distance = heapq.heappop(points)
            res.append((distance[1], distance[2]))
        return res
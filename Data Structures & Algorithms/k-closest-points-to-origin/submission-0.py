class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        values = []

        for i, j in points:
            values.append(i**2 + j **2)

        for i in range(len(points)):
            heapq.heappush(heap, (values[i], points[i]))
        
        ret = []
        for i in range(k):
            _, ans = heapq.heappop(heap)
            ret.append(ans)

        return ret
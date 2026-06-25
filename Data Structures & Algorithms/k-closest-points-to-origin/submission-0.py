class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x,y):
            return x**2 + y**2
        maxHeap = []
        for x, y in points:
            heapq.heappush(maxHeap, [-distance(x,y), x, y])
            if len(maxHeap) > k:
                # pop the point with the biggest distance from origin
                heapq.heappop(maxHeap)
        return [[x,y] for _, x, y in maxHeap]
            
            


"""
[x,y]

sqrt((x1 - x2)^2 + (y1 - y2)^2))

Create a max heap using the Euclidean Distance of size k
If size exceeds k, pop the point with the highest distance
"""
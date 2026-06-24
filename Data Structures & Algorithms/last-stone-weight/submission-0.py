class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)
            if x < y:
                heapq.heappush(maxHeap, -(y-x))
        return 0 if len(maxHeap) == 0 else -maxHeap[0]    

"""
Need to always get the two heaviest stones from the list
Max heap
"""
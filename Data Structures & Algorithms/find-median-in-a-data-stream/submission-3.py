class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        # check for validity
        if self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            
            tmp = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -tmp)
        
        # check for size constraints
        len_minheap = len(self.minHeap)
        len_maxheap = len(self.maxHeap)
        if abs(len_minheap - len_maxheap) > 1:
            if len_minheap > len_maxheap:
                tmp = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -tmp)
            else:
                tmp = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -tmp)
        
        

    def findMedian(self) -> float:
        #print(self.minHeap)
        #print(self.maxHeap)
        len_minheap = len(self.minHeap)
        len_maxheap = len(self.maxHeap)
        if abs(len_minheap - len_maxheap) == 1:
            if len_minheap > len_maxheap:
                return self.minHeap[0]
            else:
                return -self.maxHeap[0]
        else:
            minNum = self.minHeap[0]
            maxNum = -self.maxHeap[0]
            return (maxNum + minNum) / 2

"""
Two heaps, 1 min heap and 1 max heap

max heap to store the lower half
min heap to store the upper half

1. add to max heap
2. Check for validity
    - root max heap <= root min_heap
    if violated, pop max heap and insert to min heap
3. Check for size constraints
    max(min heap, max heap) - min(min heap, max heap) <= 1
    If violated, pop from the bigger heap and append to the smaller heap
4. If len is the same, pop from each heap, sum, and div by 2
    Else, pop from the bigger heap
"""
        
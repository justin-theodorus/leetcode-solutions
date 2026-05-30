class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        max_heap = []
        for key, val in count.items():
            heapq.heappush(max_heap, (-val, key))
        ans = []
        for i in range(k):
            _, key = heapq.heappop(max_heap)
            ans.append(key)
        return ans


# top 1 = most frequent
# top 2 = 2nd most frequent
# nums[i] -1000 to 1000

# count frequency of each element
# put in max-heap
# pop from max-heap k times
# max size of the heap should be k
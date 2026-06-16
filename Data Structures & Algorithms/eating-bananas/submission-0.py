class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_sum(k):
            total = 0
            for i in range(len(piles)):
                if piles[i] <= k:
                    total += 1
                else:
                    total += piles[i] // k
                    if piles[i] % k > 0:
                        total += 1
            return total
        
        l = 1
        r = k = max(piles)

        while l <= r:
            mid = l + ((r - l) // 2)
            if get_sum(mid) <= h:
                k = mid
                r = mid - 1
            else:
                l = mid + 1
        return k
"""
k is at most max(piles)

sum of ceil(piles[i] / k) must be <= h
"""
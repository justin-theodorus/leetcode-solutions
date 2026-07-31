class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        res = 0
        cumDelta = 0
        for i in range(len(gas)):
            delta = gas[i] - cost[i]
            if cumDelta < 0:
                cumDelta = 0
                res = i
            cumDelta += delta
        return res
            
"""
gas[i] -> + fuel
cost[i] -> - fuel

-1 if sum(cost) > sum(gas)


gas = [1,2,3,4]
cost = [2,2,4,1]
delta = [-1,0,-1,3]

Find a starting point where if you traverse left, the cumulative delta
cannot ever be negative. 

Otherwise, reset the cumulative and find a new starting point.

If it reaches the end of the array with positive net, the wraparound
is guaranteed to also be positive/zero becasue sum(gas) >= sum(cost)
"""
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curTriplet = [0,0,0]

        first = target[0]
        second = target[1]
        third = target[2]
        
        def checkMatch(triplet):
            match = False
            idx = 0
            while idx < 3:
                if triplet[idx] > target[idx]:
                    return False
                if triplet[idx] == target[idx]:
                    match = True
                idx += 1
            return match
                


        for triplet in triplets:
            if checkMatch(triplet):
                curTriplet[0] = max(curTriplet[0], triplet[0])
                curTriplet[1] = max(curTriplet[1], triplet[1])
                curTriplet[2] = max(curTriplet[2], triplet[2])
            
            if curTriplet[0] > first or curTriplet[1] > second or curTriplet[2] > third:
                return False
            elif curTriplet == target:
                return True
            
        
        return curTriplet == target
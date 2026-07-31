class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        minHand = min(hand)
        maxHand = max(hand)
        seen = defaultdict(int)

        for h in hand:
            seen[h] += 1
        
        l = minHand
        while l <= maxHand:
            if seen[l] == 0:
                l += 1
                continue
            
            for r in range(l, l + groupSize):
                if seen[r] == 0:
                    return False
                seen[r] -= 1
        return True
                
                
        

class Solution:
    def isHappy(self, n: int) -> bool:
        def getSum(num):
            total = 0
            while num > 0:
                total += ((num % 10) ** 2)
                num //= 10
            
            return total
        
        seen = set()
        target = set([1, 10, 100, 1000])
        while n not in seen or n not in target:
            if n in seen:
                return False
            if n in target:
                return True
            
            seen.add(n)
            n = getSum(n)
            
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l, r = 1, x
        res = 0

        while l <= r:
            mid = (l + r) // 2
            squared = mid * mid
            if squared > x:
                r = mid - 1
            elif squared < x:
                l = mid + 1
                res = mid
            else:
                return mid
        return res
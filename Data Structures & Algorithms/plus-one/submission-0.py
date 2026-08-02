class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []
        n = len(digits)
        digits[-1] += 1
        extra = False

        for i in range(n - 1, -1, -1):
            if extra:
                digits[i] += 1
                extra = False
            if digits[i] >= 10:
                extra = True
                digits[i] -= 10
        return [1] + digits if extra else digits
        
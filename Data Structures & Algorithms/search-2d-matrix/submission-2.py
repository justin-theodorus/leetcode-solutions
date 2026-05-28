class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        for i in range(len(matrix)):
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] > target:
                row = i-1
                break
            
            if i == len(matrix) - 1:
                row = len(matrix) - 1
        
        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            mid = (l+r) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

        
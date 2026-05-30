class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def check(r, c, placed):
            for row, col in placed:
                if r == row or c == col or r + c == row + col or r - c == row - col:
                    return False
            return True

        def backtrack(all, curr, r, c, placed):
            if r == n:
                tmp = []
                for cur in curr:
                    tmp.append("".join(cur))
                all.append(tmp[:])
                return
            if c >= n:
                return

            if check(r, c, placed):
                curr[r][c] = 'Q'
                placed.add((r,c))
                backtrack(all, curr, r + 1, 0, placed)
                placed.remove((r,c))
                curr[r][c] = '.'
            backtrack(all, curr, r, c + 1, placed)
        all = []
        initial = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(all, initial, 0, 0, set())
        return all

# block same row
# block same col
# block same sum
# block same diff
class Trie:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def add(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.word = True
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        trie = Trie()
        res, visit = set(), set()
        for w in words:
            trie.add(w)

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or (r, c) in visit or
                board[r][c] not in node.children
            ):
                return
            
            visit.add((r, c))
            char = board[r][c]
            node = node.children[board[r][c]]
            word += char
            if node.word:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie, "")
        
        return list(res)
        
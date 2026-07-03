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
    
    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        trie = Trie()
        found = Trie()
        for w in words:
            trie.add(w)

        def dfs(r, c, visited, node, path):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                (r, c) in visited or board[r][c] not in node.children):
                return
            
            char = board[r][c]
            next_node = node.children[char]
            path += char
            if next_node.word:
                found.add(path)
            
            visited.add((r, c))
            dfs(r + 1, c, visited, next_node, path)
            dfs(r - 1, c, visited, next_node, path)
            dfs(r, c + 1, visited, next_node, path)
            dfs(r, c - 1, visited, next_node, path)
            visited.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, set(), trie, "")
        
        ans = []
        for word in words:
            if found.search(word):
                ans.append(word)
        return ans
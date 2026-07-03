class WordDictionary:

    def __init__(self):
        self.children = {}
        self.word = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self
        for idx, c in enumerate(word):
            if c == '.':
                for key in curr.children:
                    if curr.children[key].search(word[idx + 1:]):
                        return True
                return False
            else:
                if c not in curr.children:
                    return False
                curr = curr.children[c]
        return curr.word
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                nei[pattern].append(word)
        
        queue = deque([beginWord])
        visited = set([beginWord])
        res = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for match in nei[pattern]:
                        if match not in visited:
                            visited.add(match)
                            queue.append(match)
            res += 1
        return 0
                        


# *at: [cat]
# c*t: [cat]
# ca*: [cat]


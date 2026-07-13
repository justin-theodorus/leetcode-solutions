class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # create mapping
        if endWord not in wordList:
            return 0
        mapping = defaultdict(list)
        for word in wordList:
            for idx in range(len(word)):
                key = word[:idx] + "_" + word[idx + 1:]
                mapping[key].append(word)
        
        q = deque([beginWord])
        visit = set([beginWord])
        ans = 1
        while q:
            for i in range(len(q)):
                curWord = q.popleft()
                if curWord == endWord:
                    return ans
                for idx in range(len(curWord)):
                    key = curWord[:idx] + "_" + curWord[idx + 1:]
                    for newWord in mapping[key]:
                        if newWord not in visit:
                            visit.add(newWord)
                            q.append(newWord)
            ans += 1
        return 0
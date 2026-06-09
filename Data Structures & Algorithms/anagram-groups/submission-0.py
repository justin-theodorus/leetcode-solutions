class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            count = Counter(s)
            key = tuple(sorted(count.items()))
            seen[key].append(s)
        return list(seen.values())

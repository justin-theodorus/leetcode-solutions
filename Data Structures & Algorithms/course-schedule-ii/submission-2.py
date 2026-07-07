class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for a, b in prerequisites:
            adjList[a].append(b)
            # b must be taken before a
        
        ans = []
        visited = set()
        path = set()

        def dfs(lesson):
            if lesson in path:
                return False
            if lesson in visited:
                return True
            path.add(lesson)
            for nextLesson in adjList[lesson]:
                if not dfs(nextLesson):
                    return False
            ans.append(lesson)
            visited.add(lesson)
            path.discard(lesson)

            return True
        for lesson in range(numCourses):
            if lesson not in visited:
                if not dfs(lesson):
                    return []
        return ans



"""
Topo Sort:
Visit all Neighbors first before appending the current Node to the path
"""
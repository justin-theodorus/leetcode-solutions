class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for a, b in prerequisites:
            adjList[b].append(a)
        
        visited = set()
        path = set()
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            
            path.add(course)
            visited.add(course)
            for nextCourse in adjList[course]:
                if not dfs(nextCourse):
                    return False
            path.remove(course)
            return True
        
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return False
        
        return True
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return list(range(0, numCourses))
        
        adj = defaultdict(list)
        
        for a, b in prerequisites:
            adj[b].append(a)
        
        ans, visited, cycle = [], set(), set()

        def dfs(i):
            # cycle
            if i in cycle:
                return False
            if i in visited:
                return True
            
            cycle.add(i)

            for j in adj[i]:
                if not dfs(j):
                    return False
            cycle.remove(i)
            visited.add(i)
            ans.append(i)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return ans[::-1]



# courses: 0 to numCourses - 1
# return list. If not possible, return []
# [0, 1] = 1 must be taken before 0
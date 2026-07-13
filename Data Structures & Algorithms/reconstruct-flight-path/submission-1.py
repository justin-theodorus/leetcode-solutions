class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        for source, dest in sorted(tickets)[::-1]:
            adjList[source].append(dest)
        
        ans = []
        def dfs(airport):
            while adjList[airport]:
                nextAirport = adjList[airport].pop()
                dfs(nextAirport)
            ans.append(airport)
        dfs("JFK")
        return ans[::-1]
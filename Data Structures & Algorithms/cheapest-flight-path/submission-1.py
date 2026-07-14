class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # build adjacency list
        adj = defaultdict(list)
        for source, dest, price in flights:
            adj[source].append((price, dest))
        
        # init
        # start with 0 cost at src
        pq = [(0, src, k + 1)] # (price, airport, stops_remaining)
        # Track the maximum remaining stops we've seen for each node to prune searches
        stops_remaining_at_node = [-1 for _ in range(n)]
        
        while pq:
            curPrice, curAirport, curK = heapq.heappop(pq)
            
            if curAirport == dst:
                return curPrice

            # If we reach a node with fewer (or equal) stops remaining than a previous visit,
            # and since Dijkstra guarantees we reached it with a higher or equal price, 
            # this path is not better.
            if curK <= stops_remaining_at_node[curAirport]:
                continue
            
            stops_remaining_at_node[curAirport] = curK

            if curK > 0:
                for nextPrice, nextAirport in adj[curAirport]:
                    heapq.heappush(pq, (curPrice + nextPrice, nextAirport, curK - 1))

        return -1
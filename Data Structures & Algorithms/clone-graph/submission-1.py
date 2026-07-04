"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        created = {}
        # val -> Node
        def dfs(curr):
            if not curr:
                return
            if curr.val not in created:
                created[curr.val] = Node(curr.val)
            else:
                return created[curr.val]
            new_curr = created[curr.val]
            for neighbor in curr.neighbors:
                dfs(neighbor)
                new_curr.neighbors.append(created[neighbor.val])
            
            return new_curr
        return dfs(node)

"""
Input: 1 node, the starting node
Node values are numbered from 1 to n

Input node is always the first node and has value 1

"End" nodes must be created first before parent nodes are created

Topological
"""
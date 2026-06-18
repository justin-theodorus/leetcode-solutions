"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        created_node = defaultdict(lambda: Node(0))
        created_node[None] = None
        curr = head

        while curr:
            created_node[curr].val = curr.val
            created_node[curr].next = created_node[curr.next]
            created_node[curr].random = created_node[curr.random]

            curr = curr.next
        return created_node[head]


        

"""
possible to access a node not yet created when traversing

need to maintain a hashmap:
Node -> Node

3,7,4,5
d,3,7,4,5
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def bfs(head1, head2):
            pq1 = deque([head1])
            pq2 = deque([head2])

            while pq1 and pq2:
                for i in range(len(pq2)):
                    node1 = pq1.popleft()
                    node2 = pq2.popleft()

                    if node1 is None and node2 is None:
                        continue

                    if node1 is None or node2 is None:
                        return False

                    if node1.val != node2.val:
                        return False
                    
                    pq1.append(node1.left)
                    pq1.append(node1.right)
                    pq2.append(node2.left)
                    pq2.append(node2.right)
            return True
        
        def dfs(node):
            if not node:
                return False
            found = False
            if node.val == subRoot.val:
                found = bfs(node, subRoot)
            if found: return True

            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        
        def dfs(node):
            if not node:
                return None
            if p.val <= node.val <= q.val:
                return node
            
            if p.val < node.val and q.val < node.val:
                return dfs(node.left)
            else:
                return dfs(node.right)
        return dfs(root)
            


"""
node is ancestor if
p.val and q.val < node.val
p.val < node.val < q.val or vice versa
node.val < p.val and q.val
"""
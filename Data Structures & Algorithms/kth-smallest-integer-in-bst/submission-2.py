# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, cur):
            if not node:
                return

            dfs(node.left, cur)

            cur.append(node.val)

            dfs(node.right, cur)
        cur = []
        dfs(root, cur)
        return cur[k-1]
"""
left, parent, right
preorder traversal?
dfs
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        good = 0
        def dfs(node, max_val):
            nonlocal good
            if node.val >= max_val:
                good += 1
                max_val = node.val
            if node.left:
                dfs(node.left, max_val)
            if node.right:
                dfs(node.right, max_val)
        
        dfs(root, float("-inf"))
        return good

"""
root is always a good node

traverse each node once
track the max value seen up until that node
if an update happens, its a good node
if not, its not a good node
"""
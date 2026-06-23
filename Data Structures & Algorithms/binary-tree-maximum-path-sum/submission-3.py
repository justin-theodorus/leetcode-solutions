# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # global max sum
        res = float("-inf")

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            # not taking left or right if negative
            leftDown = max(dfs(node.left), 0)
            rightDown = max(dfs(node.right), 0)

            # update global
            res = max(res, node.val + leftDown + rightDown)

            # returns max value for current node and one subtree to be reused
            return node.val + max(leftDown, rightDown)
        
        dfs(root)
        return res



"""
dfs traverse through each node
at each node, can either take, or not take

path type:

root.val only
root.val + maxPathSum(root.left)
root.val + maxPathSum(root.right)
maxPathSum(root.left)
maxPathSum(root.right)
maxPathSum(root.left) + root.val + maxPathSum(root.right)

"""
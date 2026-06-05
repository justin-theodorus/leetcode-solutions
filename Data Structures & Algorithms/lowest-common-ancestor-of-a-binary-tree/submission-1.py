# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right

"""
    - p and q in left subtree
    - p and q in right subtree
    - p and q in left and righ subtree (or vice versa)

LCA is the node where p is in its left subtree and q is in its right subtree (or vice versa)


if p and q in left subtree -> lowestCommonAncestor(root.left, p, q)
else if p and q in right subtree -> lowestCommonAncestor(root.right, p, q)
else -> return root
"""
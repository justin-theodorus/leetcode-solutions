# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node, target):
            if not node:
                return False 
            elif node.val == target.val:
                return True
            return find(node.left, target) or find(node.right, target)
        
        find_left = find(root.left, p) and find(root.left, q)
        if find_left:
            return self.lowestCommonAncestor(root.left,p,q)

        find_right = find(root.right, p) and find(root.right, q)
        if find_right:
            return self.lowestCommonAncestor(root.right,p,q)
        return root

"""
    - p and q in left subtree
    - p and q in right subtree
    - p and q in left and righ subtree (or vice versa)

LCA is the node where p is in its left subtree and q is in its right subtree (or vice versa)


if p and q in left subtree -> lowestCommonAncestor(root.left, p, q)
else if p and q in right subtree -> lowestCommonAncestor(root.right, p, q)
else -> return root
"""
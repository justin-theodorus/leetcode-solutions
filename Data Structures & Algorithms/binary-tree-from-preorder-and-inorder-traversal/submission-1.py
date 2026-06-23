# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = 0
        inIdx = 0
        def dfs(limit):
            """
            Build the left subtree up until inorder reaches limit
            Limit is an upper bound
            Preorder = node creation
            Inorder = separation between left and right subtree
            """
            nonlocal preIdx, inIdx

            if preIdx >= len(preorder):
                # done building all nodes
                return None
            
            if inorder[inIdx] == limit:
                # reach the end of the left subtree
                inIdx += 1
                return None
            
            curr = preorder[preIdx] # first element is always root/parent
            preIdx += 1
            root = TreeNode(curr)
            root.left = dfs(root.val) # build left subtree until inorder reaches root value
            root.right = dfs(limit)

            return root
        
        return dfs(float("inf"))




"""
preorder = parent -> left -> right
inorder = left -> parent -> right
"""
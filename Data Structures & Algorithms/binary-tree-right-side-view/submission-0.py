# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        ans = []

        while q:
            rightmost = 1000
            for i in range(len(q)):
                node = q.popleft()
                rightmost = node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(rightmost)
        return ans

"""
BFS
append the rightmost in the queue at each level

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = deque([p])
        q_queue = deque([q])

        while p_queue and q_queue:
            for i in range(len(p_queue)):
                node_p = p_queue.popleft()
                node_q = q_queue.popleft()

                if not node_q and not node_p:
                    continue

                if not node_q or not node_p or node_p.val != node_q.val:
                    return False
                
                p_queue.append(node_p.left)
                p_queue.append(node_p.right)
                q_queue.append(node_q.left)
                q_queue.append(node_q.right)
        return False if p_queue or q_queue else True
                
            